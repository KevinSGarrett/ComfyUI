# Model And Effort Assignments

These are the intended Codex Desktop model and reasoning effort settings for the six Wave42 lanes.

Use the strongest model for lanes where mistakes can corrupt shared architecture, QA status, runtime state, or evidence claims.

| Lane | Mission | Model | Reasoning effort |
| --- | --- | --- | --- |
| Lane_1 | Main Flow architecture and workflow graph wiring | `gpt-5.5` | `xhigh` |
| Lane_2 | Spatial, pose, mask, contact, depth, and soft-body controls | `gpt-5.5` | `xhigh` |
| Lane_3 | Models, LoRAs, Civitai assets, and self-hosted LLM route | `gpt-5.5` | `high` |
| Lane_4 | EC2 runtime, deployment, sync, live validation, and cost control | `gpt-5.5` | `high` |
| Lane_5 | QA, evidence ingestion, tracker promotion, and re-blocking | `gpt-5.5` | `xhigh` |
| Lane_6 | Candidate generation, presets, tuning, and AI_Front self-hosted LLM integration | `gpt-5.5` | `high` |

## Dynamic Adjustment Policy

The table above is the baseline. The supervisor must watch lane progress and adjust model/effort when the work changes shape.

Escalate to `xhigh` when a lane is doing any of the following:

- editing or validating `C:\Comfy_UI\Implementation\workflows\ui\WAVE42_MAIN_FLOW_20260702.json`
- deciding whether evidence justifies a tracker promotion or re-block
- opening, extending, or closing an EC2 live runtime window
- resolving cross-lane conflicts, shared claims, or contradictory evidence
- making model/runtime visibility decisions that affect Main Flow readiness
- making a safety, content, privacy, credential, or cost-control decision

Keep the baseline `high` setting when a lane is doing bounded inventory, formatting, manifest writing, or non-destructive evidence packaging.

Do not downgrade below the baseline table unless the user explicitly authorizes it. If a lane was initially created with the app default settings, immediately send a follow-up prompt with the model and effort above before allowing substantive work to continue.

## Current Supervisor Defaults

- Lane_1, Lane_2, and Lane_5 should normally stay at `xhigh`.
- Lane_3, Lane_4, and Lane_6 normally run at `high`, but the supervisor should temporarily prompt them at `xhigh` for Main Flow model-visibility adjudication, EC2 live-window decisions, runtime evidence conflicts, or candidate/media QA decisions.
- The supervisor should record any intentional temporary escalation in a lane report or coordination summary.
