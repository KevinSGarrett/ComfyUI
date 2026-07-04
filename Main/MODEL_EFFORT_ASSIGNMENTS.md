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

If a lane was initially created with the app default settings, immediately send a follow-up prompt with the model and effort above before allowing substantive work to continue.

Do not downgrade a lane unless the user explicitly authorizes it.

