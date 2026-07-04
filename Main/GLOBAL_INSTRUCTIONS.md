# Global Instructions

## Scope

This is a Codex Desktop operating system for the Wave42 ComfyUI hyperrealism project. It has six builder lanes plus Lane 7 integration/history:

- `Lane_1`: Main Flow architecture and workflow graph wiring.
- `Lane_2`: Spatial, pose, mask, contact, and soft-body control design.
- `Lane_3`: Model, LoRA, Civitai, asset, and compatibility management.
- `Lane_4`: EC2 runtime, deployment, sync, and live ComfyUI validation.
- `Lane_5`: QA, evidence ingestion, tracker promotion, and audit.
- `Lane_6`: Generation presets, candidate media, tuning, and comparison.
- `Lane_7`: Cross-lane integration, end-to-end release history, usage-limit resume packets, storage-pressure reporting, and dashboard documentation.

All lanes share the same project roots:

- `C:\Comfy_UI`
- `C:\Comfy_UI_Lora`
- `C:\Comfy_UI_Lora\5_sessions`

## Source Of Truth

Use local files and current live state as source of truth. Do not rely on old chat history when files can be inspected.

Each session must start by reading:

1. `C:\Comfy_UI_Lora\5_sessions\Main\GLOBAL_INSTRUCTIONS.md`
2. `C:\Comfy_UI_Lora\5_sessions\Main\LANE_BOUNDARIES.md`
3. `C:\Comfy_UI_Lora\5_sessions\Main\EC2_LEASE_PROTOCOL.md`
4. `C:\Comfy_UI_Lora\5_sessions\Main\SELF_HOSTED_LLM_POLICY.md` if touching AI/LLM or AI front-end work.
5. `C:\Comfy_UI_Lora\5_sessions\Main\STRICT_AUTONOMOUS_QA_PROTOCOL.md`
6. Its own `Lane_X\LANE_INSTRUCTIONS.md`
7. Any relevant current tracker, manifest, workflow, or evidence file it will use.

## Non-Negotiable Rules

- Do not print, log, commit, upload, or package secret values from `.env`, AWS credentials, GitHub tokens, Civitai tokens, SSH keys, presigned URLs, or provider keys.
- Do not stage or commit model files, generated media, credentials, EC2 mirrors, raw downloads, or local cache files.
- Do not download Civitai/model binaries to local project roots. `C:\Comfy_UI_Lora\downloads\models` CSVs are read-only local metadata sources; model downloads must run on EC2 through Lane 4 after Lane 3 produces a storage-gated manifest.
- Do not claim completion from plans, packets, placeholder media, untested graph connectivity, or nonblank outputs.
- Do not promote tracker rows unless direct evidence proves the row requirement.
- Do not keep a row blocked merely because it was blocked before if current direct evidence proves it.
- Do not bypass legal, credential, provider, paid-access, account-owner, or rights-holder constraints.
- Preserve real blockers honestly. Remove only false blockers and paperwork-only blockers.
- Every generated artifact, runtime result, model test, preset, or promotion must be evidence-backed.
- Every lane must maintain continuous history and status reporting as defined in `STRICT_AUTONOMOUS_QA_PROTOCOL.md`.
- Any hand, finger, contact, pose, mask, body-interaction, candidate media, or hand-adjacent claim must include strict hand review or an explicit `not_visually_reviewed` / `manual_review_required` limitation.
- Follow `USAGE_BUDGET_POLICY.md`. When usage is low, use standard speed, reduce no-op polling, avoid blanket `xhigh`, prefer deterministic scripts for mechanical work, and wake only owner lanes with concrete next actions.

## AI/LLM Provider Policy

For `C:\Comfy_UI_Lora\AI_LLM_Intelligence_Plan`, `C:\Comfy_UI_Lora\AI_Front`, and any related automation/UI intelligence, use a self-hosted LLM route by default. Prefer local computer hosting when feasible and EC2-hosted LLM runtime when GPU/server capacity is required.

External providers such as OpenAI, Grok, Anthropic, or other paid/cloud APIs are fallback routes only. Do not make them the default architecture, do not require their credentials for normal operation, and do not send project prompts, media metadata, private files, or tracker content to an external provider without an explicit approved reason and secret-safe evidence.

See `SELF_HOSTED_LLM_POLICY.md`.

## EC2 Model Ingestion Policy

For model ingestion from `C:\Comfy_UI_Lora\downloads\models`, follow:

`C:\Comfy_UI_Lora\5_sessions\Main\EC2_MODEL_INGESTION_POLICY.md`

Lane 3 may parse the CSV files locally, create dry manifests, organize target taxonomy, and draft model cards. Lane 4 is the only lane that may run Civitai downloads, and those downloads must happen on EC2 or another explicitly approved remote target with enough storage. Lane 5 must audit evidence before any tracker or readiness claim. Lane 7 must track storage and usage-limit risk.

The token variable name is `CIVITAI_TOKEN`, stored in `C:\Comfy_UI\.env`. Never print its value, commit it, include it in a URL, or persist it in SSM output, reports, model cards, manifests, or evidence.

## Usage Budget Policy

When usage is low or the user requests budget control, follow:

`C:\Comfy_UI_Lora\5_sessions\Main\USAGE_BUDGET_POLICY.md`

Autonomy still matters, but it must be budget-aware. Continuous mode means lanes keep resumable goals and owner-lane readiness, not that every lane should burn high-speed or high-effort reasoning on every heartbeat.

## Safety Boundary

All human subjects in generated or validated project media must be clearly adult. Do not generate, validate, request, or preserve minors, ambiguous-age subjects, coercive scenarios, non-consensual scenarios, or sexualized age ambiguity. Any lane that encounters ambiguous or unsafe source material must reject it and record the rejection.

## EC2 Cost Control

EC2 is expensive and must remain stopped unless a live runtime window is actively needed. Only `Lane_4` may start or stop EC2 directly, and only after acquiring the shared EC2 lease.

Other lanes must submit EC2 requests instead of starting or stopping the instance themselves. They may inspect read-only AWS state if credentials are valid and doing so does not alter runtime state.

## Evidence Standard

Evidence must be specific enough for another lane to reproduce or reject the claim.

Use `Main\schemas\evidence_record.schema.json` and include:

- output or artifact path
- SHA256 where applicable
- timestamp
- lane id
- source inputs
- workflow or script path
- model/checkpoint/LoRA/control assets and compatibility family
- prompt/settings where applicable
- runtime endpoint evidence where applicable
- QA verdict and failure reasons
- tracker rows proven and not proven

## Main Flow Convergence Standard

All lane work must converge back to the canonical ComfyUI Main Flow unless the lane is explicitly producing governance, QA, or cost-control evidence.

The canonical Main Flow workflow is:

`C:\Comfy_UI\Implementation\workflows\ui\WAVE42_MAIN_FLOW_20260702.json`

Every lane output should answer at least one of these questions:

- Does this make the Main Flow graph more correctly wired?
- Does this prove that a Main Flow asset, model, node, control, preset, or runtime dependency is present and visible?
- Does this produce a concrete Lane 1 request to wire or repair the Main Flow?
- Does this produce a concrete Lane 4 request to validate Main Flow runtime behavior?
- Does this produce Lane 5 evidence that can honestly promote, preserve, or re-block Main Flow-related tracker rows?
- Does this produce Lane 6 presets or candidates that are traceable to the Main Flow and its self-hosted LLM/provider contract?

Side artifacts are useful only when they strengthen Main Flow readiness, runtime validation, candidate generation, or QA. Do not let a lane stop at a plan, inventory, or standalone architecture note when a Main Flow-facing next action remains available.

## Coordination Standard

Before writing outside its owned lane directory, a lane must confirm the path is allowed by `LANE_BOUNDARIES.md`.

For shared files that more than one lane may touch, create a claim file under:

`C:\Comfy_UI_Lora\5_sessions\Main\shared_state\claims`

The claim must include lane id, file path, purpose, timestamp, and expiry. Do not overwrite another active claim.

## GitHub And Git

The configured GitHub target is `KevinSGarrett/ComfyUI`. Tokens must stay in environment variables or secret stores only. Never put a token in a remote URL, command output, commit, evidence file, or generated report.

This coordination layer is Git-ready, with hooks under `.githooks`. The hooks block obvious secrets, model files, generated media, and live state.
