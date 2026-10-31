# AgriMitra AI — ML and Data Architecture

## 1. Model portfolio

| Capability | Initial baseline | Candidate advanced model | Output |
|---|---|---|---|
| Disease screening | Transfer-learning image classifier | EfficientNet / MobileNet family | Suspected class, confidence, uncertainty |
| Soil interpretation | Agronomy rules and thresholds from trusted references | Validated tabular classifier/ranker | Parameter interpretation and recommendations |
| Crop suitability | Transparent rule-based scoring | Random Forest / XGBoost ranking | Ranked crop candidates and explanation |
| Yield estimation | Historical average / linear baseline | Gradient boosting / temporal models | Yield range and uncertainty |
| Price forecasting | Seasonal naive baseline | XGBoost / Prophet / LSTM if justified | Price forecast and error range |
| Assistant | Curated retrieval and templates | LLM + RAG | Grounded answer with citations |

Do not train a complex model before a reliable baseline and suitable labelled data exist.

## 2. Common ML lifecycle

1. Dataset registration and license/consent review.
2. Data validation, schema checks and duplicate detection.
3. Label quality review by qualified domain experts.
4. Preprocessing and feature engineering with versioned code.
5. Split by farm/location/time where appropriate to reduce leakage.
6. Train baseline and candidate models.
7. Evaluate on held-out, geographically relevant data.
8. Review failure modes and subgroup performance.
9. Register model artifact, metrics, training data version and limitations.
10. Deploy behind a versioned inference interface.
11. Monitor latency, drift, confidence distribution and expert disagreement.
12. Retrain only after data quality and validation gates pass.

## 3. Disease image screening

- Input: farmer-submitted crop image plus crop, location, plant stage and symptom context.
- Preprocessing: decode safely, validate dimensions/format, remove metadata where appropriate, resize and normalize.
- Training: transfer learning; augment for realistic lighting, background and orientation variation.
- Evaluation: per-class precision/recall/F1, confusion matrix, calibration, out-of-distribution testing and field-image holdout.
- Output: top candidate classes, calibrated confidence where possible, model version and uncertainty state.
- Fallback: unknown/low-confidence response and expert review.

PlantVillage and PlantDoc can be starting benchmarks, not proof of real-world performance. Collect consented, expert-labelled West Bengal field images across varieties, growth stages, lighting and devices. Separate train/test by source/farm where possible to avoid near-duplicate leakage.

## 4. Soil intelligence

Use laboratory or validated field measurements as ground truth. Store parameter, numeric value, unit, method, lab/source, sample date and location. Interpret through versioned agronomy rules grounded in authoritative local guidance. If OCR is added to parse reports, extracted values remain pending until user/expert confirmation. A photograph must never be represented as a direct NPK or pH measurement.

## 5. Crop suitability and economics

First implement an explainable multi-factor score using:
- crop/season compatibility,
- soil parameter suitability,
- water/irrigation availability,
- weather and sowing window,
- regional cultivation guidance,
- crop history and risk,
- sourced market demand/price information.

Return ranked options, factor-level explanation, missing inputs, source timestamps and assumptions. Keep agronomic suitability separate from financial attractiveness. Cost/yield/price estimates should show ranges and uncertainty, not guaranteed profit.

## 6. Yield and price models

- Establish seasonal-naive and historical-average baselines.
- Track data by crop, variety, location, season, unit and timestamp.
- Use temporal validation; do not randomly mix future observations into training.
- Report MAE/RMSE or suitable metrics, prediction intervals and performance by district/season.
- Do not publish a forecast when data coverage or validation is insufficient.

## 7. Assistant and RAG

- Ingest only approved, licensed, dated agricultural documents.
- Store publisher, source URL, publication date, version, region and crop tags.
- Chunk documents with source metadata; retrieve by language, crop, location and topic.
- Generate answers from retrieved evidence; show source citations.
- If evidence is missing or conflicting, say so and escalate to an expert.
- Keep user-private farm context separate from shared public knowledge.
- Evaluate retrieval relevance, citation correctness, language quality and unsafe advice refusal.

## 8. Model service contract

A model prediction record should include:
- model_name and model_version,
- input_reference and preprocessing_version,
- prediction and alternatives,
- confidence/calibration metadata,
- uncertainty/out-of-distribution flag,
- created_at and inference latency,
- evaluation dataset/version reference.

The application service owns authorization and persistence. The model inference component does not independently decide user permissions.

## 9. Data governance

For every dataset, create a data card: source, license, permitted use, geography, date range, label definitions, collection method, consent, preprocessing, known bias and retention policy. Never commit private farmer images, identity documents, API secrets or restricted datasets to Git. Use controlled storage and access logs.
