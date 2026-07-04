# Lane 6 Report: AI Front Self-Hosted LLM Contract Proof

Created: 2026-07-04T15:51:33Z

## Outcome

Lane 6 proved the AI_Front self-hosted OpenAI-compatible LLM route for local planning calls and created a named text-planning provider preset.

## Primary Artifacts

- Contract: `C:\Comfy_UI_Lora\AI_Front\provider_contracts\self_hosted_openai_compatible_contract_v1.json`
- Probe report: `C:\Comfy_UI_Lora\AI_Front\provider_contracts\self_hosted_llm_probe_20260704_155133.md`
- Preset: `C:\Comfy_UI\Implementation\presets\ai_front\wave42_ai_front_self_hosted_llm_qwen14b_text_planning_v1.json`
- Evidence: `C:\Comfy_UI\Implementation\evidence\generation_preset_lab\wave42_ai_front_self_hosted_llm_qwen14b_text_planning_v1_evidence_20260704_155133.json`
- Manifest: `C:\Comfy_UI\Implementation\manifests\generation_preset_lab\wave42_ai_front_self_hosted_llm_qwen14b_text_planning_v1_manifest_20260704_155133.json`

## Proof

- `GET http://127.0.0.1:11434/v1/models` passed.
- Local models returned: `llava:13b`, `qwen2.5:14b`, `qwen2.5:32b`.
- `POST http://127.0.0.1:11434/v1/chat/completions` passed for `qwen2.5:14b`.
- `qwen2.5:14b` latency: `14894 ms`.
- Response proved `provider=self_hosted` and `cloud_required=false`.
- Secondary `llava:13b` chat probe also passed.

## Boundary

No OpenAI, Grok, Anthropic, or other external provider was used. No tracker row was promoted. No EC2 start/stop action was performed.

Local ComfyUI `127.0.0.1:8188` was unreachable, so no local candidate media generation was claimed.

## Validation

- JSON parse passed for contract, preset, evidence, and manifest.
- Evidence passed `C:\Comfy_UI_Lora\5_sessions\Main\schemas\evidence_record.schema.json`.
- Evidence artifact SHA256 values match current files.
