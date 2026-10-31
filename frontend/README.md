# Frontend — AgriMitra AI

## Run locally
```bash
npm install
npm run dev
```

## Current scope (Part 2)
- Responsive dashboard and navigation
- Light/dark theme toggle
- Farm profile creation
- Soil sample record entry
- Crop image case intake UI (metadata only; no upload/inference)
- Regional crop guide filters
- Local farming task calendar
- Produce listing drafts
- Expense and harvest revenue records
- Weather integration placeholder
- Assistant conversation UI placeholder

## Local prototype storage
The frontend persists sample records in browser local storage under `agrimitra.frontend.v1`. Clearing browser storage removes these records. No user account, remote API or cloud sync exists yet.

## Production integration still required
Authentication, backend persistence, private file uploads, weather provider, validated ML inference, agronomic knowledge retrieval, buyer discovery, orders, payments, notifications and expert review.

## Build check
Run `npm run build` before committing frontend changes.
