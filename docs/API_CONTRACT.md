# AgriMitra AI — API Contract

**Base path:** /api/v1  
**Style:** REST + JSON; multipart/form-data for file uploads.  
**Identifiers:** UUID.  
**Time:** ISO 8601 timestamps with timezone; persist UTC.

## 1. API conventions

Success:
```json
{
  "success": true,
  "data": {},
  "meta": { "request_id": "uuid" }
}
```

Error:
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Please check the submitted fields",
    "details": []
  },
  "meta": { "request_id": "uuid" }
}
```

Use appropriate HTTP status codes: 200/201/204, 400, 401, 403, 404, 409, 413, 422, 429 and 5xx. Paginate collection endpoints. Validate all input with Pydantic. Never expose internal stack traces.

## 2. Authentication and profile

| Method | Path | Purpose |
|---|---|---|
| POST | /auth/register | Create account |
| POST | /auth/login | Start authenticated session |
| POST | /auth/verify-otp | Verify phone challenge |
| POST | /auth/refresh | Rotate session token |
| POST | /auth/logout | Revoke session |
| GET | /users/me | Current profile |
| PATCH | /users/me | Update allowed profile fields |

Production OTP delivery requires a selected provider, rate limits, expiry, abuse controls and privacy review.

## 3. Farms and fields

| Method | Path | Purpose |
|---|---|---|
| GET/POST | /farms | List/create current user's farms |
| GET/PATCH/DELETE | /farms/{farm_id} | Read/update/archive owned farm |
| GET/POST | /farms/{farm_id}/fields | List/create fields |
| PATCH/DELETE | /fields/{field_id} | Update/archive owned field |
| GET | /farms/{farm_id}/summary | Farm dashboard data |

Coordinates and boundaries must be validated. All queries enforce ownership or explicit membership permissions.

## 4. Soil

| Method | Path | Purpose |
|---|---|---|
| POST | /soil/samples | Create sample metadata |
| POST | /soil/samples/{sample_id}/report | Upload lab report |
| POST | /soil/samples/{sample_id}/results | Save measured results |
| GET | /soil/samples/{sample_id} | Retrieve sample and results |
| POST | /soil/samples/{sample_id}/interpret | Generate interpretation |
| GET | /soil/fields/{field_id}/history | View soil history |

Measured values require units and source provenance. Report OCR, if added, must be reviewed before values become confirmed test results.

## 5. Crops and planning

| Method | Path | Purpose |
|---|---|---|
| GET | /crops | Crop catalogue and filters |
| GET | /crops/{crop_id} | Crop profile |
| POST | /crop-cycles | Record planting cycle |
| GET/PATCH | /crop-cycles/{cycle_id} | Read/update cycle |
| POST | /crop-recommendations | Rank suitable crops for a field |
| GET | /crop-recommendations/{id} | Read recommendation and assumptions |

Recommendations should disclose missing inputs, rules/model version and data freshness.

## 6. Disease screening

| Method | Path | Purpose |
|---|---|---|
| POST | /disease/cases | Create case and upload metadata |
| POST | /disease/cases/{case_id}/images | Upload image |
| POST | /disease/cases/{case_id}/screen | Queue screening |
| GET | /disease/cases/{case_id} | Read case, prediction and status |
| POST | /disease/cases/{case_id}/request-review | Request expert review |
| POST | /expert/cases/{case_id}/review | Submit authorized expert review |

Image upload uses private storage, strict size/type validation and asynchronous inference when required. The API should return a case ID and processing status rather than block for long inference.

## 7. Weather and calendar

| Method | Path | Purpose |
|---|---|---|
| GET | /weather/farms/{farm_id}/current | Current conditions |
| GET | /weather/farms/{farm_id}/forecast | Forecast |
| GET/POST | /calendar/tasks | List/create tasks |
| PATCH | /calendar/tasks/{task_id} | Update/complete task |
| GET | /calendar/farms/{farm_id} | Farm calendar |

Every weather response includes provider and observation/issue timestamps.

## 8. Marketplace, offers and orders

| Method | Path | Purpose |
|---|---|---|
| GET/POST | /marketplace/listings | Search/create listings |
| GET/PATCH | /marketplace/listings/{id} | Read/update own listing |
| POST | /marketplace/listings/{id}/offers | Submit offer |
| GET | /marketplace/offers | View authorized offers |
| POST | /marketplace/offers/{id}/accept | Accept offer |
| POST | /marketplace/offers/{id}/reject | Reject offer |
| POST | /orders | Create order from accepted offer |
| GET | /orders | List buyer/seller orders |
| GET | /orders/{id} | Read authorized order |
| POST | /payments/webhook/{provider} | Verify provider event |

Commercial state transitions must be server-authorized and transactional. Webhooks must be signature-verified and idempotent.

## 9. Finance and assistant

| Method | Path | Purpose |
|---|---|---|
| GET/POST | /finance/expenses | List/create expenses |
| GET/POST | /finance/harvests | List/create harvest records |
| GET | /finance/farms/{farm_id}/summary | Cost and revenue summary |
| POST | /assistant/chat | Submit user message |
| GET | /assistant/sessions | List own sessions |
| GET | /assistant/sessions/{id} | Read own session |

Assistant responses should include citations/references, language, safety flags and a clear uncertainty statement where appropriate.

## 10. API engineering requirements

- Enforce authentication, roles and resource ownership at the service boundary.
- Add request IDs and structured error responses.
- Use idempotency keys for order/payment operations.
- Rate-limit authentication, uploads, assistant and expensive inference endpoints.
- Restrict CORS to known frontend origins in production.
- Version breaking API changes.
- Publish OpenAPI documentation from FastAPI.
- Add contract tests for critical endpoints.
