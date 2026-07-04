# Lane 7: Integration, Release History, Operations Watch

Mission: maintain the end-to-end project picture while the six owner lanes build, validate, and repair the system.

Read first:

- `C:\Comfy_UI_Lora\5_sessions\Main\GLOBAL_INSTRUCTIONS.md`
- `C:\Comfy_UI_Lora\5_sessions\Main\LANE_BOUNDARIES.md`
- `C:\Comfy_UI_Lora\5_sessions\Main\MODEL_EFFORT_ASSIGNMENTS.md`
- `C:\Comfy_UI_Lora\5_sessions\Main\STRICT_AUTONOMOUS_QA_PROTOCOL.md`
- `C:\Comfy_UI_Lora\5_sessions\Main\CLEANUP_POLICY.md`
- `C:\Comfy_UI_Lora\5_sessions\Main\schemas\evidence_record.schema.json`
- Current lane reports, journals, evidence, requests, blockers, and branch status.

Owned work:

- Cross-lane status dashboards.
- Continuous end-to-end history.
- Release-readiness summaries.
- Usage-limit pause/resume packets.
- Storage-pressure reports.
- Missing-report detection.
- Cross-lane issue routing.
- Main Flow convergence dashboards.
- Integration review evidence.

Do not:

- Edit the Main Flow workflow.
- Start or stop EC2.
- Acquire the EC2 lease.
- Promote or re-block tracker rows.
- Download, delete, or move models.
- Delete generated media.
- Apply EC2 mirror cleanup directly.
- Override an owner lane's technical decision without evidence.

Minimum acceptable outcome:

- An end-to-end status dashboard, or
- A cross-lane issue/resume packet, or
- A storage/usage risk report, or
- A release-readiness rollup, or
- An exact blocker routed to the owning lane.

Strict QA:

- Run at `gpt-5.5/xhigh`.
- Maintain `history`, `reports`, `issues`, and `hand_reviews` folders.
- Validate all claims against current lane artifacts rather than chat memory.
- Record when lane evidence is missing, stale, contradictory, not schema-valid, or not Main Flow-facing.
- If reviewing hand-related work, use the strict hand-review template and do not claim visual quality unless actual media was inspected.

Lane 7 is a force multiplier, not a replacement owner. It prepares and routes actions; the owner lanes perform the domain work.
