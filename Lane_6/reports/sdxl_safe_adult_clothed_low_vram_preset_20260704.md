# Lane 6 Report: SDXL Safe Adult Clothed Low-VRAM Preset

Created: 2026-07-04T16:05:30Z

## Outcome

Lane 6 created a Main Flow-traceable SDXL candidate preset, proved local ComfyUI is blocked, and filed a Lane 4 runtime request for live candidate generation or exact runtime/model blocker evidence.

## Main Flow Trace

- Canonical Main Flow: `C:\Comfy_UI\Implementation\workflows\ui\WAVE42_MAIN_FLOW_20260702.json`
- SHA256: `eee910f1d00a6858abc67a27ea783c43c8ad876fd60f6b26865bced39bc647c0`
- Main Flow was read/hash-referenced only; Lane 6 did not edit it.

## Primary Artifacts

- AI_Front prompt template: `C:\Comfy_UI_Lora\AI_Front\prompts\self_hosted_generation_preset_suggest_v1.md`
- Preset: `C:\Comfy_UI\Implementation\presets\generation_preset_lab\wave42_sdxl_safe_adult_clothed_low_vram_v1.json`
- Evidence: `C:\Comfy_UI\Implementation\evidence\generation_preset_lab\wave42_sdxl_safe_adult_clothed_low_vram_v1_evidence_20260704_160530.json`
- Manifest: `C:\Comfy_UI\Implementation\manifests\generation_preset_lab\wave42_sdxl_safe_adult_clothed_low_vram_v1_manifest_20260704_160530.json`
- Lane 4 runtime request: `C:\Comfy_UI_Lora\5_sessions\Main\shared_state\ec2_requests\20260704_160530_Lane_6_sdxl_safe_adult_clothed_low_vram_candidate.json`

## Proof And Blocker

- Local self-hosted `qwen2.5:14b` drafted the preset through `http://127.0.0.1:11434/v1/chat/completions`.
- No OpenAI, Grok, Anthropic, or other cloud LLM provider was used.
- Local ComfyUI `127.0.0.1:8188` refused TCP and `/prompt` connections.
- No candidate media was claimed.

## Validation

- Preset, request, evidence, and manifest parse as JSON.
- Evidence passes `C:\Comfy_UI_Lora\5_sessions\Main\schemas\evidence_record.schema.json`.
- Evidence artifact SHA256 values match current files.
