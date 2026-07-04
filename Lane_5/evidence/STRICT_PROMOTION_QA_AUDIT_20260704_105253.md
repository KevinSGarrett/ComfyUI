# Strict Promotion QA Audit 20260704_105253

- Generated UTC: `2026-07-04T15:54:48Z`
- Baseline tracker: `C:\Comfy_UI\Implementation\trackers\wave42_working_tracker_20260701_131029.csv`
- Latest audited tracker: `C:\Comfy_UI\Implementation\trackers\wave42_working_tracker_20260702_202657.csv`
- Corrected tracker snapshot: `C:\Comfy_UI\Implementation\trackers\wave42_working_tracker_20260704_105253.csv`
- Promoted since baseline: `557`
- Re-blocked overpromotions: `30`
- Preserved scoped/manual rows: `5`
- Counts before: `{'Verified Complete': 12112, 'Blocked - Model Asset': 717, 'Blocked - External API': 58}`
- Counts after: `{'Verified Complete': 12082, 'Blocked - Model Asset': 744, 'Blocked - External API': 61}`

## Verdict

The prior rolling audit was too permissive for rows whose only existing artifacts were readiness packets, resume kits, or handoff material. Under the Lane 5 direct-evidence rule, those artifacts are advisory and cannot prove completion. This pass re-blocks only the rows with no direct/intervention evidence path and preserves rows with scoped local artifacts or direct runtime/intervention evidence.

The July 4 EC2 side-push crop/inpaint runtime bundles are accepted as candidate evidence only. They prove mechanical runtime, generated nonblank artifacts, endpoint/object_info capture, and model/control visibility, but their own `strict_visual_verdict` is `manual_review_required` and no exact blocked tracker row ID is present.

## Re-blocked Rows

- `ART-0679` -> `Blocked - Model Asset`: Activate/verify artifact: WAVE26_TO_WAVE27_HANDOFF_MAP.md
- `ART-0706` -> `Blocked - Model Asset`: Activate/verify artifact: WAVE27_TO_WAVE28_HANDOFF_MAP.md
- `ART-0826` -> `Blocked - External API`: Activate/verify artifact: WAVE29_TO_WAVE30_HANDOFF_MAP.md
- `ART-0843` -> `Blocked - Model Asset`: Activate/verify artifact: WAVE25_TO_WAVE26_HANDOFF_MAP.md
- `ART-2367` -> `Blocked - Model Asset`: Configure runtime from config artifact: router_bindings_wave26.json
- `ART-2368` -> `Blocked - Model Asset`: Configure runtime from config artifact: wave27_handoff_manifest.json
- `ART-2397` -> `Blocked - Model Asset`: Configure runtime from config artifact: lora_stack_presets.json
- `ART-2412` -> `Blocked - Model Asset`: Configure runtime from config artifact: router_bindings_wave27.json
- `ART-2413` -> `Blocked - Model Asset`: Configure runtime from config artifact: wave28_handoff_manifest.json
- `ART-2636` -> `Blocked - Model Asset`: Configure runtime from config artifact: router_bindings_wave25.json
- `ART-2645` -> `Blocked - Model Asset`: Configure runtime from config artifact: wave26_handoff_manifest.json
- `CHECK-0029` -> `Blocked - Model Asset`: Confirm the intended workflow lane.
- `CHECK-0030` -> `Blocked - Model Asset`: Review model source/usage notes.
- `CHECK-0124` -> `Blocked - Model Asset`: AV sync manifest declares no binary audio/video/model assets in package.
- `CHECK-0212` -> `Blocked - Model Asset`: Object contacts/handoffs align with visual action and foley/SFX cues.
- `ENTRY-0004` -> `Blocked - Model Asset`: Review primary entrypoint: 01_MANUALS/WAVE_42_OPERATOR_PRODUCTION_RUNBOOK.md
- `ENTRY-0006` -> `Blocked - Model Asset`: Review primary entrypoint: 01_MANUALS/WAVE_42_REVIEWER_ACCEPTANCE_GUIDE.md
- `IMPL-00079` -> `Blocked - Model Asset`: Wave 09 - Install or configure wave components: SDXL ControlNet Pose/Depth/Structure Pipeline
- `IMPL-00290` -> `Blocked - External API`: Wave 39 - Import or bind wave workflows/templates: Sound Effects, Foley, Ambience, and Music Generation
- `IMPL-00297` -> `Blocked - External API`: Wave 40 - Import or bind wave workflows/templates: Audio-Video Synchronization, Lip Sync, and Timeline Mixing
- `IMPL-00323` -> `Blocked - Model Asset`: Smoke test custom node pack ControlNet Auxiliary Preprocessors
- `SETUP-0146` -> `Blocked - Model Asset`: Define incident stop conditions
- `WAVE-0182` -> `Blocked - Model Asset`: Complete Wave 20 objective: FLUX Identity, Reference & Edit Control Layer
- `WAVE-0193` -> `Blocked - Model Asset`: Complete Wave 21 objective: SDXL Specialty Support Pass for FLUX Outputs
- `WAVE-0205` -> `Blocked - Model Asset`: Complete Wave 22 objective: Cross-Engine Control Maps & Structural Conditioning
- `WAVE-0230` -> `Blocked - Model Asset`: Complete Wave 24 objective: Multi-Engine Image QA, Comparison & Scoring
- `WAVE-0288` -> `Blocked - Model Asset`: Complete Wave 29 objective: Video Engine Router, Motion QA & Engine Comparison
- `WAVE-0408` -> `Blocked - Model Asset`: Prove Wave 38 acceptance: Speech can be generated from prompt/script inputs.
- `WFLOW-00227` -> `Blocked - Model Asset`: Import and runtime-test workflow/API template: LTX2_KEYFRAME_VIDEO_API_TEMPLATE.json
- `WFLOW-00229` -> `Blocked - Model Asset`: Import and runtime-test workflow/API template: LTX2_T2V_FAST_API_TEMPLATE.json

## Preserved Scoped Manual Rows

- `CHECK-0214` remains `Verified Complete`: Scoped local dialogue-intent metadata exists: voice profiles plus speech request manifest record voice profile, emotion, tone, and pacing. Does not prove rendered speech quality.
- `CHECK-0217` remains `Verified Complete`: Direct returned-candidate audio QA CSV records exists=True, non_silent=True, not_clipped=True, sha256_matches=True, and peak_norm below 1.0 for all listed audio assets.
- `SETUP-0107` remains `Verified Complete`: Direct voice profile registry and per-character assignment artifacts cover each dialogue character with selected voice_profile_id values. Does not prove rendered speech.
- `WAVE-0175` remains `Verified Complete`: Scoped FLUX LoRA/reference compatibility registry deliverable exists with compatibility rules and downstream bindings. Registry rows still note needs_local_asset, so model files/load remain separate blockers.
- `WAVE-0403` remains `Verified Complete`: Scoped TTS adapter registry deliverable exists and is downstream-usable by local speech routing artifacts. External/provider TTS execution and production voice quality remain separate blockers.

## Outputs

- Audit CSV: `C:\Comfy_UI\Implementation\evidence\promotion_quality_audit\strict_promotion_quality_audit_20260704_105253.csv`
- Reblock CSV: `C:\Comfy_UI\Implementation\evidence\promotion_quality_audit\strict_promotion_reblocks_20260704_105253.csv`
- Evidence-to-row candidate CSV: `C:\Comfy_UI\Implementation\evidence\promotion_quality_audit\evidence_to_row_candidates_20260704_105253.csv`
- Schema evidence record: `C:\Comfy_UI\Implementation\evidence\promotion_quality_audit\lane5_strict_promotion_audit_evidence_20260704_105253.json`
- Manifest: `C:\Comfy_UI\Implementation\manifests\promotion_quality_audit\strict_promotion_quality_audit_20260704_105253.json`
