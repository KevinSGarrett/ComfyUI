# Lane 2: Spatial, Pose, Mask, Contact, Soft-Body Controls

Mission: build the explicit spatial truth layer for pose, masks, depth, contact-pair graphs, collision checks, and localized deformation controls.

Read first:

- `C:\Comfy_UI_Lora\5_sessions\Main\GLOBAL_INSTRUCTIONS.md`
- `C:\Comfy_UI_Lora\5_sessions\Main\LANE_BOUNDARIES.md`
- Current workflow and mask/contact evidence under `C:\Comfy_UI\Implementation\evidence`

Owned work:

- Per-character masks.
- Per-hand masks.
- Contact-zone masks.
- Depth/normal/occlusion evidence.
- Contact-pair definitions.
- Collision and deformation QA inputs.
- Requests to Lane 1 for graph wiring.

Do not:

- Edit the Main Flow directly without a claim.
- Start or stop EC2.
- Promote tracker rows.
- Delete models or generated evidence.

Minimum acceptable outcome:

- Mask/pose/contact evidence, or
- A reusable contact-control artifact, or
- A precise Lane 1 wiring request, or
- A concrete blocker with exact missing model/tool/reference.

