# Lane 6 Report: AI Front Self-Hosted Provider Trace Schemas

Created: 2026-07-04T16:08:42Z

## Outcome

Lane 6 materialized auditable AI_Front schemas for self-hosted LLM provider requests and decision traces. The examples are tied to the canonical Main Flow and the `wave42_sdxl_safe_adult_clothed_low_vram_v1` preset.

## Artifacts

- Request schema: `C:\Comfy_UI_Lora\AI_Front\schemas\self_hosted_llm_provider_request.schema.json`
- Decision trace schema: `C:\Comfy_UI_Lora\AI_Front\schemas\self_hosted_llm_decision_trace.schema.json`
- Request example: `C:\Comfy_UI_Lora\AI_Front\examples\provider_requests\wave42_sdxl_safe_adult_clothed_low_vram_request_20260704_160530.json`
- Decision trace example: `C:\Comfy_UI_Lora\AI_Front\examples\decision_traces\wave42_sdxl_safe_adult_clothed_low_vram_trace_20260704_160842.json`
- Evidence: `C:\Comfy_UI\Implementation\evidence\generation_preset_lab\wave42_ai_front_self_hosted_provider_trace_schema_evidence_20260704_160842.json`
- Manifest: `C:\Comfy_UI\Implementation\manifests\generation_preset_lab\wave42_ai_front_self_hosted_provider_trace_schema_manifest_20260704_160842.json`

## Main Flow Trace

- Canonical Main Flow: `C:\Comfy_UI\Implementation\workflows\ui\WAVE42_MAIN_FLOW_20260702.json`
- SHA256: `eee910f1d00a6858abc67a27ea783c43c8ad876fd60f6b26865bced39bc647c0`
- Main Flow was not edited.

## Validation

- Request example validates against request schema.
- Decision trace example validates against decision trace schema.
- Evidence validates against `C:\Comfy_UI_Lora\5_sessions\Main\schemas\evidence_record.schema.json`.
- Evidence artifact SHA256 values match current files.

## Boundary

This proves local LLM provenance structure only. It does not prove candidate media quality, live ComfyUI runtime, model load visibility, or tracker promotion readiness.
