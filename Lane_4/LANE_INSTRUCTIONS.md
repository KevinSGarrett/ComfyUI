# Lane 4: EC2 Runtime, Deployment, Sync

Mission: own live runtime windows, EC2 state, ComfyUI endpoint validation, deployment, sync, and cost-control proof.

Read first:

- `C:\Comfy_UI_Lora\5_sessions\Main\GLOBAL_INSTRUCTIONS.md`
- `C:\Comfy_UI_Lora\5_sessions\Main\LANE_BOUNDARIES.md`
- `C:\Comfy_UI_Lora\5_sessions\Main\EC2_LEASE_PROTOCOL.md`

Owned work:

- EC2 lease.
- AWS auth/state checks.
- Start/stop EC2 when justified.
- ComfyUI `/system_stats`, `/object_info`, and `/queue` checks.
- Self-hosted LLM endpoint hosting/checks when the LLM runs on EC2.
- Deployment and sync bundles.
- Runtime evidence collection.
- Cost-state verification after live work.

Do not:

- Leave EC2 running after active live work finishes or blocks.
- Stop EC2 without owning the lease.
- Terminate unrelated user/AWS/Codex processes.
- Print credentials, tokens, or secret-bearing URLs.

Minimum acceptable outcome:

- Live runtime validation evidence, or
- Stopped-state cost evidence, or
- A precise AWS/SSM/SSH/ComfyUI blocker with exact next command/action.

LLM rule: if hosting an LLM on EC2, use the same lease, cost-control, tunnel/security, endpoint evidence, and stop-state proof as ComfyUI runtime work.
