# AgriMitra AI 🌱

AI-powered agricultural intelligence and farmer marketplace, starting with West Bengal.

## Product scope
- Farm and field management
- Soil-test record keeping and interpretation
- Crop disease screening with expert escalation
- Crop suitability and profitability decision support
- Weather-aware farming calendar
- Bengali-first agricultural assistant
- Farmer-to-buyer marketplace
- Farm economics and government-service discovery

## Repository layout
- `frontend/` — React + Vite responsive web application / PWA foundation
- `backend/` — FastAPI application foundation (Part 3)
- `ml/` — model training and inference pipelines (Part 4)
- `ai_assistant/` — retrieval and knowledge workflows
- `docs/` — architecture, database, API and ML documentation
- `infrastructure/` — container and deployment configuration

## Development plan
1. Architecture and engineering blueprint — documented in `docs/`.
2. Frontend — responsive farmer workspace and local prototype workflows.
3. Backend and database — FastAPI, PostgreSQL/PostGIS, auth and APIs.
4. AI/ML — validated disease, soil, crop, yield and price intelligence.
5. Integration and launch — tests, deployment and West Bengal pilot.

## Frontend quick start
```bash
cd frontend
npm install
npm run dev
```
Open the Vite URL printed in the terminal (normally `http://localhost:5173`).

## Frontend prototype notice
Part 2 uses browser local storage for farm profiles, soil entries, calendar tasks, marketplace drafts and financial records. These are local prototype records, not cloud-synced production data.

Disease case submission currently stores case metadata and a filename only; it does not upload an image or run a model. Crop guides are general information, not personalized recommendations. Weather, live buyer discovery, payments and AI answers are not connected. The interface must not be used to make real treatment or investment decisions.

## Engineering principles
- Do not commit secrets, private farmer images or restricted datasets.
- Do not fabricate live weather, mandi prices, disease predictions or model confidence.
- Keep AI outputs explainable, versioned and appropriately uncertain.
- Use trusted local agronomy sources and expert review for high-impact advice.
- Add dependencies only when their feature is being implemented.
