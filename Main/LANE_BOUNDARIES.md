# Lane Boundaries

These are hard write boundaries for concurrent Codex Desktop sessions. A lane may read broadly, but writes are limited to its owned paths unless the shared claim protocol is used.

## Main Flow Convergence Rule

The whole system is organized around the canonical Main Flow:

`C:\Comfy_UI\Implementation\workflows\ui\WAVE42_MAIN_FLOW_20260702.json`

Lane work may cover the broader system, but it must keep producing Main Flow-facing outputs: workflow repairs, asset/model/runtime visibility evidence, Lane 1 wiring requests, Lane 4 runtime requests, Lane 5 tracker/evidence decisions, or Lane 6 presets/candidates that can be traced back to the Main Flow. Side documents and inventories are intermediate work, not final lane completion, when a Main Flow-facing next action remains.

## Strict QA And History Rule

All lanes must follow:

`C:\Comfy_UI_Lora\5_sessions\Main\STRICT_AUTONOMOUS_QA_PROTOCOL.md`

This includes continuous lane journals, frequent status reports, issue/blocker records, QA/test evidence, and strict hand review for every hand/contact/candidate/media-related claim. These records belong in each lane's owned `history`, `reports`, `issues`, and `hand_reviews` subfolders under its worktree and shared session mirror when practical.

## Lane 1: Main Flow Architecture

Mission: repair, wire, validate, and preserve the canonical Main Flow workflow graph.

Owned write areas:

- `C:\Comfy_UI\Implementation\workflows`
- `C:\Comfy_UI\Implementation\workflow_backups`
- `C:\Comfy_UI\Implementation\evidence\workflow_validation`
- `C:\Comfy_UI_Lora\5_sessions\Lane_1`

May modify only with backup first:

- `C:\Comfy_UI\Implementation\workflows\ui\WAVE42_MAIN_FLOW_20260702.json`

Forbidden without request/claim:

- Tracker CSV status columns.
- EC2 start/stop.
- Model downloads or deletion.
- Generated media cleanup.

Minimum outcome: a graph change, graph validation, or exact blocker with workflow/evidence references.

## Lane 2: Spatial, Pose, Mask, Contact, Soft-Body Controls

Mission: design and validate the explicit spatial truth layer: pose, masks, depth, contact-pair graphs, collision checks, and localized deformation controls.

Owned write areas:

- `C:\Comfy_UI\Implementation\evidence\spatial_validation`
- `C:\Comfy_UI\Implementation\evidence\mask_validation`
- `C:\Comfy_UI\Implementation\evidence\contact_physics`
- `C:\Comfy_UI\Layout_Images`
- `C:\Comfy_UI\Input_References`
- `C:\Comfy_UI_Lora\5_sessions\Lane_2`

Forbidden without request/claim:

- Direct Main Flow edits.
- Tracker promotions.
- EC2 start/stop.
- Model deletion.

Minimum outcome: mask/pose/contact evidence, a Lane 1 wiring request, or exact blocker.

## Lane 3: Models, LoRAs, Civitai, Assets

Mission: verify, acquire, classify, hash, deploy-readiness-check, and compatibility-test model assets.

For `C:\Comfy_UI_Lora\downloads\models`, Lane 3 may parse CSV metadata locally and create dry EC2 ingest manifests, target folder taxonomy, model-card drafts, storage projections, and Lane 4 download requests. Lane 3 must not download the listed model binaries locally.

Owned write areas:

- `C:\Comfy_UI\Implementation\manifests\civitai_model_acquisition`
- `C:\Comfy_UI\Implementation\evidence\model_asset_validation`
- `C:\Comfy_UI\Implementation\evidence\model_tests`
- `C:\Comfy_UI\Implementation\evidence\llm_runtime`
- `C:\Comfy_UI\Runtime_Data\models`
- `C:\Comfy_UI_Lora\models`
- `C:\Comfy_UI_Lora\AI_LLM_Intelligence_Plan`
- `C:\Comfy_UI_Lora\Model_Organize`
- `C:\Comfy_UI_Lora\Organizaion_Model`
- `C:\Comfy_UI_Lora\5_sessions\Lane_3`

Forbidden without request/claim:

- Workflow edits.
- Tracker promotions.
- EC2 start/stop.
- Broad Civitai mirroring.
- Local Civitai/model binary downloads from the CSV inventory.
- Committing model binaries.

Minimum outcome: model existence/load/visibility evidence, model-test evidence, a clean blocker, or a compatibility table update.

LLM note: Lane 3 owns self-hosted LLM model selection, local model inventory, compatibility, quantization, endpoint requirements, and evidence that an LLM model can load locally or on EC2. External LLM APIs are fallback only.

## Lane 4: EC2 Runtime, Deployment, Sync

Mission: own all live EC2 runtime windows, deployment, sync, ComfyUI endpoint validation, and cost-control state.

Lane 4 also owns EC2-only Civitai/model download execution when requested by Lane 3. It must follow `EC2_MODEL_INGESTION_POLICY.md`, acquire the EC2 lease, verify storage before and after each batch, use `CIVITAI_TOKEN` without logging it, and produce per-batch download/hash/catalog evidence before stopping EC2 and releasing the lease.

Owned write areas:

- `C:\Comfy_UI\Implementation\deployment`
- `C:\Comfy_UI\Implementation\sync_bundles`
- `C:\Comfy_UI\Implementation\evidence\runtime`
- `C:\Comfy_UI\Implementation\evidence\ec2`
- `C:\Comfy_UI\EC2_Mirror`
- `C:\Comfy_UI\_ec2sd`
- `C:\Comfy_UI_Lora\5_sessions\Main\shared_state\ec2_requests`
- `C:\Comfy_UI_Lora\5_sessions\Lane_4`

Exclusive authority:

- Acquire/release the EC2 lease.
- Start EC2.
- Stop EC2.
- Run deployment or live ComfyUI endpoint checks.
- Run EC2-only Civitai/model download batches requested by Lane 3.

Forbidden:

- Stopping EC2 while another active lease owner exists.
- Printing credentials or tokens.
- Terminating unrelated processes.
- Runtime claims without endpoint/output evidence.

Minimum outcome: live validation evidence, stopped-cost state proof, or exact AWS/runtime blocker.

## Lane 5: QA, Evidence, Tracker Promotion

Mission: enforce strict QA, evidence ingestion, tracker promotion, rolling promotion-quality audit, and honest re-blocking.

For EC2 model ingestion, Lane 5 audits model-card completeness, download/hash/catalog evidence, storage reports, scan/license fields, and direct tracker impact. CSV metadata alone proves planning only, not downloaded readiness.

Owned write areas:

- `C:\Comfy_UI\Implementation\evidence`
- `C:\Comfy_UI\Implementation\trackers`
- `C:\Comfy_UI\Implementation\manifests`
- `C:\Comfy_UI\Implementation\docs`
- `C:\Comfy_UI\Items`
- `C:\Comfy_UI_Lora\5_sessions\Lane_5`

Forbidden without request/claim:

- Main Flow edits.
- EC2 start/stop.
- Model downloads.
- Generated media deletion.

Minimum outcome: QA verdicts, evidence-to-tracker mapping, audited promotions, re-blocks, or exact blocker.

## Lane 6: Candidate Generation, Presets, Tuning

Mission: produce, compare, score, tune, and preserve image/video/audio generation candidates and settings presets.

Lane 6 may consume the model catalog only after Lane 3/Lane 4/Lane 5 evidence distinguishes planned, downloaded, hash-verified, catalog-visible, load-tested, and generation-tested states.

Owned write areas:

- `C:\Comfy_UI\Generated_Outputs`
- `C:\Comfy_UI\outputs`
- `C:\Comfy_UI\Implementation\presets`
- `C:\Comfy_UI\Implementation\settings`
- `C:\Comfy_UI\Implementation\evidence\generation_preset_lab`
- `C:\Comfy_UI\Implementation\manifests\generation_preset_lab`
- `C:\Comfy_UI_Lora\AI_Front`
- `C:\Comfy_UI_Lora\5_sessions\Lane_6`

Forbidden without request/claim:

- Tracker promotions.
- Main Flow edits.
- EC2 start/stop.
- Model downloads beyond a Lane 3 request.

Minimum outcome: candidate outputs with QA/provenance, named presets, comparison evidence, or exact blocker.

LLM note: Lane 6 may integrate AI front-end behavior and prompt/preset assistance only through the self-hosted LLM contract unless a documented fallback is approved.

## Lane 7: Integration, Release History, Operations Watch

Mission: keep the end-to-end picture coherent across all lanes: continuous history, release readiness, usage-limit resume packets, storage-pressure reports, dashboard summaries, and cross-lane issue tracking.

For EC2 model ingestion, Lane 7 tracks the dashboard, usage-limit resume packet, storage risk, and owner-lane next actions only. It must not download, delete, retag, or claim readiness for models.

Owned write areas:

- `C:\Comfy_UI\Implementation\docs`
- `C:\Comfy_UI\Implementation\manifests\integration_status`
- `C:\Comfy_UI\Implementation\evidence\integration_review`
- `C:\Comfy_UI_Lora\5_sessions\Main\reports`
- `C:\Comfy_UI_Lora\5_sessions\Main\shared_state\resume_packets`
- `C:\Comfy_UI_Lora\5_sessions\Main\shared_state\storage_reports`
- `C:\Comfy_UI_Lora\5_sessions\Lane_7`

Forbidden without request/claim:

- Direct Main Flow edits.
- Tracker promotions or re-blocks.
- EC2 start/stop.
- Model downloads or deletion.
- Generated media deletion.
- Broad EC2 mirror cleanup apply runs.

Minimum outcome: an end-to-end status dashboard, cross-lane issue/resume packet, storage pressure report, release-readiness rollup, or exact blocker routed to the owning lane.

Lane 7 may recommend cleanup, runtime, tracker, workflow, model, or candidate actions, but the owning lane must execute them.

## Shared Claim Rule

If a lane needs to write outside its owned area, it must create a claim file in:

`C:\Comfy_UI_Lora\5_sessions\Main\shared_state\claims`

Claim filename format:

`YYYYMMDD_HHMMSS_Lane_X_short-purpose.json`

Claim fields:

- `lane_id`
- `target_path`
- `purpose`
- `expires_at_utc`
- `risk`
- `expected_outputs`

Claims do not grant EC2 authority. EC2 authority is only through the EC2 lease protocol.
