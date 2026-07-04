# Lane 3: Models, LoRAs, Civitai, Assets

Mission: verify, acquire, classify, hash, and compatibility-test model assets without contaminating incompatible workflows.

Read first:

- `C:\Comfy_UI_Lora\5_sessions\Main\GLOBAL_INSTRUCTIONS.md`
- `C:\Comfy_UI_Lora\5_sessions\Main\LANE_BOUNDARIES.md`
- `C:\Comfy_UI_Lora\5_sessions\Main\SELF_HOSTED_LLM_POLICY.md`
- `C:\Comfy_UI\Implementation\manifests\civitai_model_acquisition`
- `C:\Comfy_UI\Runtime_Data\models`

Owned work:

- Model inventory.
- Civitai acquisition metadata.
- SHA256 verification.
- Runtime visibility requests to Lane 4.
- Compatibility classification: SDXL, Flux, LTXV, Wan, audio, ControlNet, IPAdapter, VAE, LoRA, checkpoint, upscaler.
- Self-hosted LLM model inventory and load-test requirements for `AI_LLM_Intelligence_Plan`.
- Quarantine recommendations for incompatible assets.

Do not:

- Broadly mirror Civitai.
- Print Civitai or GitHub tokens.
- Mix SDXL and Flux LoRAs/checkpoints.
- Start or stop EC2.
- Promote tracker rows directly.
- Commit model binaries.

Minimum acceptable outcome:

- A model wiring/visibility table, or
- New targeted asset evidence, or
- A model test result, or
- A precise blocker such as missing token, access denial, incompatible family, failed hash, failed visibility, or failed load.

LLM rule: default to a local or EC2-hosted model. External LLM APIs are fallback-only and must not become the normal dependency.
