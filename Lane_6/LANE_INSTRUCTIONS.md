# Lane 6: Candidate Generation, Presets, Tuning

Mission: generate, compare, tune, score, and preserve image/video/audio candidates and reusable settings presets.

Read first:

- `C:\Comfy_UI_Lora\5_sessions\Main\GLOBAL_INSTRUCTIONS.md`
- `C:\Comfy_UI_Lora\5_sessions\Main\LANE_BOUNDARIES.md`
- `C:\Comfy_UI_Lora\5_sessions\Main\SELF_HOSTED_LLM_POLICY.md`
- `C:\Comfy_UI_Lora\5_sessions\Main\schemas\evidence_record.schema.json`
- Current presets/settings under `C:\Comfy_UI\Implementation\presets` and `C:\Comfy_UI\Implementation\settings`

Owned work:

- Candidate generation plans.
- Local or requested runtime generation batches.
- Preset and settings records.
- AI front-end integration plans that use the self-hosted LLM contract.
- Output QA scoring.
- Comparison tables.
- Handoffs to Lane 5 for tracker promotion.

Do not:

- Start or stop EC2.
- Promote tracker rows directly.
- Edit the Main Flow directly.
- Download models without a Lane 3 request or documented local availability check.
- Treat placeholder/provisional media as final.

Minimum acceptable outcome:

- Real candidate outputs with provenance and QA, or
- A named preset backed by output evidence, or
- A comparison showing improved/failing settings, or
- A precise runtime/model/preset blocker.

LLM rule: AI front-end features should call the self-hosted endpoint contract first. OpenAI/Grok/etc. should remain optional fallbacks, not required runtime dependencies.
