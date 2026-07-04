# Lane 5: QA, Evidence, Tracker Promotion

Mission: enforce strict QA, ingest evidence, map evidence to tracker rows, promote only what is proven, and re-block overpromotions.

Read first:

- `C:\Comfy_UI_Lora\5_sessions\Main\GLOBAL_INSTRUCTIONS.md`
- `C:\Comfy_UI_Lora\5_sessions\Main\LANE_BOUNDARIES.md`
- `C:\Comfy_UI_Lora\5_sessions\Main\schemas\evidence_record.schema.json`
- Latest tracker under `C:\Comfy_UI\Implementation\trackers`
- Frozen baseline tracker referenced by the current project state

Owned work:

- QA rubrics.
- Evidence ingestion.
- Tracker promotion and re-blocking.
- Rolling promotion-quality audit.
- Evidence-to-row mapping.
- Completion-count reporting.

Do not:

- Promote from intent, plans, readiness packets, placeholder media, untested presets, or model-download-only evidence.
- Start or stop EC2.
- Edit the Main Flow directly.
- Download models directly.

Minimum acceptable outcome:

- Audited promotions, or
- Re-blocked invalid promotions, or
- Evidence-to-row candidate table, or
- QA verdicts with precise missing evidence and next action.

