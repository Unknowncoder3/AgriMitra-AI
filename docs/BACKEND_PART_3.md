# Part 3 — Backend foundation

## First milestone
FastAPI modular-monolith foundation, PostgreSQL/PostGIS and Redis services, SQLAlchemy persistence, Alembic migration environment, JWT/password authentication, farmer-owned farm records and soil sample/result endpoints.

## Implemented endpoints
- GET /health and /ready
- POST /api/v1/auth/register and /login
- GET /api/v1/users/me
- GET/POST /api/v1/farms
- GET/PATCH/DELETE /api/v1/farms/{farm_id}
- POST /api/v1/soil/samples
- GET /api/v1/soil/farms/{farm_id}/history

## Security baseline
Passwords use Argon2 via pwdlib. Access tokens are expiring JWTs. Farm and soil endpoints filter by authenticated ownership. Secrets and database credentials come from environment variables; CORS origins are configurable.

OTP delivery, refresh-token rotation, account recovery, role administration, upload scanning and production rate limits are not implemented in this increment. Do not expose this initial backend publicly until those controls are added.

## Local development
1. Copy backend/.env.example to backend/.env.
2. Start services from the repository root: docker compose up -d db redis.
3. Create a Python virtual environment in backend and install requirements.txt.
4. Run uvicorn app.main:app --reload --port 8000 from backend.
5. Open http://localhost:8000/docs.

Alembic initial migration is included as 0001_initial. Run alembic upgrade head from backend after setting DATABASE_URL. SQLite is available for test runs; PostgreSQL is the intended persistent database.

## Limitations
PostGIS is provisioned but spatial columns and indexes arrive with the field/location migration. Redis is provisioned but caching and queues are not wired. Frontend still uses local storage; API client/auth integration follows after local API verification. File storage, disease screening, marketplace transactions, weather, assistant and expert workflows remain future work.
