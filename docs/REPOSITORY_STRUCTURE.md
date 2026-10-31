# AgriMitra AI — Target Repository Structure

This is the target structure. Build it incrementally; do not create empty directories or install every planned dependency before its feature phase.

```text
AgriMitra-AI/
├── frontend/
│   ├── public/
│   └── src/
│       ├── assets/
│       ├── components/
│       │   ├── common/
│       │   ├── layout/
│       │   ├── dashboard/
│       │   └── forms/
│       ├── pages/
│       │   ├── auth/
│       │   ├── dashboard/
│       │   ├── farms/
│       │   ├── soil/
│       │   ├── crops/
│       │   ├── disease/
│       │   ├── weather/
│       │   ├── calendar/
│       │   ├── marketplace/
│       │   ├── finance/
│       │   ├── experts/
│       │   └── assistant/
│       ├── hooks/
│       ├── context/
│       ├── services/
│       ├── routes/
│       ├── utils/
│       └── styles/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── core/
│   │   ├── api/v1/endpoints/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── repositories/
│   │   ├── services/
│   │   ├── integrations/
│   │   ├── workers/
│   │   └── utils/
│   ├── migrations/
│   ├── tests/
│   └── requirements.txt
│
├── ml/
│   ├── datasets/
│   ├── notebooks/
│   ├── preprocessing/
│   ├── training/
│   │   ├── disease_detection/
│   │   ├── soil_intelligence/
│   │   ├── crop_recommendation/
│   │   ├── yield_prediction/
│   │   └── price_forecasting/
│   ├── evaluation/
│   ├── inference/
│   ├── artifacts/
│   └── model_registry/
│
├── ai_assistant/
│   ├── rag/
│   ├── embeddings/
│   ├── knowledge_base/
│   ├── prompts/
│   └── evaluation/
│
├── docs/
│   ├── SYSTEM_ARCHITECTURE.md
│   ├── DATABASE_SCHEMA.md
│   ├── API_CONTRACT.md
│   ├── ML_AND_DATA_ARCHITECTURE.md
│   └── REPOSITORY_STRUCTURE.md
│
├── infrastructure/
│   ├── docker/
│   ├── nginx/
│   ├── monitoring/
│   └── deployment/
├── scripts/
├── .github/workflows/
├── .env.example
├── .gitignore
├── docker-compose.yml
└── README.md
```

## Folder ownership

- frontend: UI, client-side routing, forms, state and API client.
- backend: authorization, domain logic, persistence and external adapters.
- ml: offline training, evaluation and online inference components.
- ai_assistant: retrieval, prompts, source management and assistant evaluation.
- docs: architecture decisions, data cards, API and operational guides.
- infrastructure: local containers, deployment, reverse proxy and monitoring.
- scripts: repeatable setup, data validation and maintenance utilities.

## Engineering conventions

- Keep secrets and private data out of Git.
- Use feature branches and small commits.
- Add tests beside each domain.
- Use migrations for schema changes.
- Keep API and ML contracts versioned.
- Prefer reusable components and typed/validated interfaces.
- Add dependencies only when the corresponding feature is being implemented.
