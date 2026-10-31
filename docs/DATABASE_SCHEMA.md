# AgriMitra AI — Logical Database Schema

**Database:** PostgreSQL; enable PostGIS for geospatial fields.  
**Conventions:** UUID primary keys, UTC timestamps, explicit units, foreign keys, indexes, soft-delete only where justified.

This is the logical schema for implementation in Part 3. Exact columns and constraints will be finalized alongside SQLAlchemy models and Alembic migrations.

## 1. Identity and access

### users
- id UUID PK
- full_name, phone_e164 UNIQUE, email UNIQUE NULL
- password_hash NULL (only if password login is enabled)
- preferred_language, account_status
- phone_verified_at, created_at, updated_at

### roles / user_roles
- roles: id, code UNIQUE (farmer, buyer, expert, supplier, admin)
- user_roles: user_id FK, role_id FK, composite unique

### user_profiles
- user_id PK/FK, avatar_object_key, district, block, village
- consent_preferences JSONB, created_at, updated_at

## 2. Farms and fields

### farms
- id UUID PK, owner_user_id FK users
- name, district, block, village, address_text
- location GEOGRAPHY(Point, 4326), total_area, area_unit
- verification_status, created_at, updated_at

### farm_fields
- id UUID PK, farm_id FK farms
- name, area, area_unit, boundary GEOGRAPHY(Polygon, 4326) NULL
- soil_texture, irrigation_type, water_source, notes

### farm_members (later)
- farm_id FK, user_id FK, permission_level, created_at
- unique(farm_id, user_id)

## 3. Soil

### soil_samples
- id UUID PK, farm_field_id FK farm_fields
- collected_at, sample_depth, source_type (lab/manual)
- lab_name NULL, report_object_key NULL, notes
- created_by FK users, created_at

### soil_test_results
- id UUID PK, soil_sample_id FK soil_samples
- parameter_code, numeric_value, unit, method NULL
- result_status, unique(soil_sample_id, parameter_code)

### soil_recommendations
- id UUID PK, soil_sample_id FK
- recommendation_type, content JSONB, source_reference
- ruleset_version, created_at, reviewed_by NULL

Store the actual value, unit, method and provenance. Do not infer laboratory nutrient values from leaf/soil photographs.

## 4. Crop catalogue and crop cycles

### crops
- id UUID PK, common_name, scientific_name NULL
- category, crop_family NULL, active

### crop_varieties
- id UUID PK, crop_id FK, variety_name, maturity_days NULL
- source_reference, active

### crop_cycles
- id UUID PK, farm_field_id FK, crop_id FK, variety_id FK NULL
- season, sowing_date NULL, expected_harvest_date NULL
- actual_harvest_date NULL, status, notes

### crop_recommendations
- id UUID PK, farm_field_id FK, generated_at
- input_snapshot JSONB, recommendation_version
- status, expires_at NULL

### crop_recommendation_items
- id UUID PK, recommendation_id FK, crop_id FK
- rank, suitability_score NULL, score_explanation JSONB
- estimated_cost_min NULL, estimated_cost_max NULL
- estimated_yield_min NULL, estimated_yield_max NULL
- assumptions JSONB, source_references JSONB

## 5. Disease cases and model predictions

### disease_cases
- id UUID PK, crop_cycle_id FK NULL, farm_field_id FK NULL
- submitted_by FK users, crop_id FK NULL
- symptoms_text NULL, plant_stage NULL, location_snapshot JSONB
- status, expert_review_status, created_at

### disease_images
- id UUID PK, disease_case_id FK
- object_key, mime_type, file_size, checksum, captured_at NULL
- upload_status, consent_to_model_training BOOLEAN DEFAULT FALSE

### disease_predictions
- id UUID PK, disease_case_id FK
- model_name, model_version, predicted_class
- confidence, alternatives JSONB, inference_metadata JSONB
- out_of_distribution BOOLEAN, created_at

### expert_reviews
- id UUID PK, disease_case_id FK, expert_user_id FK users
- assessment, recommended_next_step, references JSONB
- reviewed_at, review_status

Keep model output and expert assessment separate. Never overwrite a prediction with an expert conclusion.

## 6. Weather, calendar and notifications

### weather_observations
- id UUID PK, farm_id FK NULL, location GEOGRAPHY(Point,4326)
- provider, observed_at, temperature_c, humidity_pct
- rainfall_mm, wind_speed_mps, raw_payload JSONB

### weather_forecasts
- id UUID PK, farm_id FK NULL, provider
- issued_at, forecast_for, temperature_min_c, temperature_max_c
- rainfall_probability_pct, rainfall_mm NULL, humidity_pct NULL
- raw_payload JSONB

### farm_tasks
- id UUID PK, farm_id FK, farm_field_id FK NULL
- crop_cycle_id FK NULL, task_type, title, due_at
- status, source_type (user/recommendation), completed_at NULL

### notifications
- id UUID PK, user_id FK, channel, title, body
- status, scheduled_at NULL, sent_at NULL, metadata JSONB

## 7. Marketplace and commerce

### buyer_profiles
- user_id PK/FK users, organization_name NULL
- buyer_type, verification_status, preferred_commodities JSONB

### produce_listings
- id UUID PK, seller_user_id FK users, farm_id FK NULL
- crop_id FK, variety_id FK NULL, title, description
- quantity, quantity_unit, grade NULL, asking_price, currency
- available_from, available_until NULL, location GEOGRAPHY(Point,4326)
- status, created_at, updated_at

### listing_images
- id UUID PK, listing_id FK, object_key, display_order

### offers
- id UUID PK, listing_id FK, buyer_user_id FK users
- offered_quantity, offered_price, currency, message NULL
- status, expires_at NULL, created_at

### orders / order_items
- orders: id, buyer_user_id, seller_user_id, status, total_amount, currency, delivery_details JSONB, created_at
- order_items: id, order_id FK, listing_id FK, quantity, unit_price, subtotal

### payments
- id UUID PK, order_id FK, provider, provider_reference UNIQUE
- amount, currency, status, verified_at NULL, raw_event_reference NULL

Never trust client-submitted payment success. Verify signed provider callbacks and use idempotency keys.

## 8. Farm economics

### farm_expenses
- id UUID PK, farm_id FK, crop_cycle_id FK NULL
- category, amount, currency, expense_date, description NULL

### harvest_records
- id UUID PK, crop_cycle_id FK
- harvested_at, quantity, quantity_unit, quality_grade NULL
- recorded_by FK users

### farm_sales
- id UUID PK, harvest_record_id FK NULL, order_id FK NULL
- quantity, unit_price, total_amount, currency, sold_at

## 9. Assistant, knowledge and platform operations

- assistant_sessions: id, user_id FK, language, context_scope, created_at
- assistant_messages: id, session_id FK, role, content, citations JSONB, created_at
- knowledge_documents: id, title, publisher, source_url, license, version, published_at, ingested_at, status
- knowledge_chunks: id, document_id FK, chunk_text, embedding/vector, metadata JSONB
- model_versions: id, model_name, version, artifact_uri, metrics JSONB, training_data_version, status
- audit_logs: id, actor_user_id NULL, action, resource_type, resource_id, request_id, created_at
- integration_sync_logs: id, provider, dataset, status, fetched_at, source_timestamp NULL, error_summary NULL

## 10. Database engineering rules

- Use UUID identifiers and UTC timestamps.
- Add indexes for foreign keys, status/date filters, phone/email lookup and marketplace search.
- Add GiST indexes for PostGIS geometry/geography columns.
- Use CHECK constraints for positive area, quantity, price and valid percentages.
- Use explicit units in column names or unit columns; never mix acres/hectares or kg/quintals silently.
- Use transactions for offers, order creation, inventory/quantity reservation and payment state transitions.
- Use audit logs for privileged actions and important commercial state changes.
- Avoid storing raw identity documents or unnecessary personal data.
- Use migrations for every schema change; do not manually alter production tables.
