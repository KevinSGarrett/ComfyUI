# Wave42 Six-Lane Codex Desktop Control Root

This directory coordinates six separate Codex Desktop sessions working on the same ComfyUI/Wave42 system.

Canonical paths:

- Session root: `C:\Comfy_UI_Lora\5_sessions`
- Shared instructions: `C:\Comfy_UI_Lora\5_sessions\Main`
- Project root: `C:\Comfy_UI`
- LoRA/model planning root: `C:\Comfy_UI_Lora`
- Worktree root: `C:\Comfy_UI_Lora\5_session_worktrees`
- GitHub repo target: `KevinSGarrett/ComfyUI`

Start here:

1. Read `Main\GLOBAL_INSTRUCTIONS.md`.
2. Read `Main\LANE_BOUNDARIES.md`.
3. Read `Main\SELF_HOSTED_LLM_POLICY.md` before touching `AI_LLM_Intelligence_Plan` or `AI_Front`.
4. Read the assigned lane file, for example `Lane_1\LANE_INSTRUCTIONS.md`.
5. Load environment variables from `Main\env\codex_lane_env.template.ps1` or copy it to a local untracked lane env file.
6. Use `Main\scripts\ec2_lease.ps1` before any EC2 live-window work.
7. Write evidence using `Main\schemas\evidence_record.schema.json`.

The six-lane split is intentional. Do not collapse lane ownership just because another lane is idle. If a lane needs work owned by another lane, it writes a request under its lane `requests` folder or under `Main\shared_state\ec2_requests` for runtime work.
