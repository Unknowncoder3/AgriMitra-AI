# AgriMitra AI Backend

FastAPI modular monolith. See `../docs/BACKEND_PART_3.md` for scope and runbook.

## Local run
1. Copy `.env.example` to `.env` and set a strong `SECRET_KEY`.
2. From repository root run `docker compose up -d db redis`.
3. `cd backend && python -m venv .venv && source .venv/bin/activate`.
4. `pip install -r requirements.txt`.
5. Run `uvicorn app.main:app --reload --port 8000`.

The API defaults to SQLite if DATABASE_URL is not set, for a quick local smoke test. PostgreSQL/PostGIS is the intended persistent database. Open `/docs` for interactive API documentation.
