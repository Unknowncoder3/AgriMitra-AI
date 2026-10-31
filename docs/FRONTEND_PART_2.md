# Part 2 — Frontend implementation notes

## UX principles
- Mobile-first responsive layout; navigation collapses into a drawer on small screens.
- Clear empty states and explicit prototype/data-source labels.
- No fabricated live weather, market prices, disease predictions or AI answers.
- Accessible labels, button names, keyboard-friendly controls and form validation.
- Bengali/English localization is planned; the current interface is primarily English.

## Implemented browser workflows
- Farm profiles: create and review basic farm records.
- Soil: record measured values and sample provenance.
- Disease: create a local case record with crop, symptom notes and selected filename; image bytes are not uploaded or persisted.
- Crop guide: filter a small static regional planning guide. It is not a recommendation model.
- Calendar: create and complete local reminders.
- Marketplace: create local produce listing drafts; drafts are not visible to buyers.
- Finance: record expenses and harvest revenue and calculate a local arithmetic summary.
- Weather and assistant: interface placeholders only.

## State and integration boundary
The `AppDataContext` is a temporary browser persistence adapter. In Part 3, replace its persistence actions with API services while keeping UI components independent of storage details. Do not treat local storage as authentication or a secure store.

## Acceptance checklist
- [ ] `npm install` completes
- [ ] `npm run build` completes
- [ ] Navigation works on desktop and mobile
- [ ] Forms validate required fields
- [ ] Local records survive page refresh
- [ ] Theme selection works
- [ ] Empty, populated and narrow-screen states are checked
- [ ] No screen implies that an unconnected AI/external service is live
