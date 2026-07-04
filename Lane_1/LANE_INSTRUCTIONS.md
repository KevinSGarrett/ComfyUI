# Lane 1: Main Flow Architecture

Mission: repair, wire, validate, and preserve the canonical Main Flow workflow graph.

Read first:

- `C:\Comfy_UI_Lora\5_sessions\Main\GLOBAL_INSTRUCTIONS.md`
- `C:\Comfy_UI_Lora\5_sessions\Main\LANE_BOUNDARIES.md`
- `C:\Comfy_UI_Lora\5_sessions\Main\EC2_LEASE_PROTOCOL.md`
- `C:\Comfy_UI\Implementation\workflows\ui\WAVE42_MAIN_FLOW_20260702.json`

Owned work:

- Main Flow graph inspection and mutation.
- Workflow JSON validation.
- Node/link/group verification.
- Backup creation before graph edits.
- Lane 2 integration requests for pose/mask/contact lanes.
- Lane 5 evidence handoff for QA and tracker mapping.

Do not:

- Start or stop EC2.
- Promote tracker rows.
- Download or delete models.
- Call unconnected prompt notes production-wired behavior.

Minimum acceptable outcome:

- A validated workflow change with backup and evidence, or
- A wiring request to Lane 2/Lane 3/Lane 4 with exact missing dependency, or
- A concrete blocker with file paths and next action.

