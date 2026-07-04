# Main Shared Directory

This is the global instruction and coordination directory for the six builder Codex Desktop lanes plus Lane 7 integration/history.

Important files:

- `GLOBAL_INSTRUCTIONS.md`: shared operating rules.
- `LANE_BOUNDARIES.md`: hard write boundaries and ownership.
- `MODEL_EFFORT_ASSIGNMENTS.md`: intended Codex Desktop model/effort for each lane.
- `EC2_LEASE_PROTOCOL.md`: live EC2 coordination rules.
- `SELF_HOSTED_LLM_POLICY.md`: local/EC2 LLM-first policy for AI intelligence and front-end AI features.
- `EC2_MODEL_INGESTION_POLICY.md`: EC2-only Civitai/model ingest rules, storage gates, model-card/report requirements.
- `USAGE_BUDGET_POLICY.md`: budget-aware polling, standard-speed, model, and effort rules.
- `CLEANUP_POLICY.md`: safe cleanup allowlist and protected paths.
- `GIT_WORKTREE_SETUP.md`: local Git/worktree plan.
- `schemas\evidence_record.schema.json`: canonical evidence schema.
- `shared_state\lane_registry.json`: machine-readable lane map.
- `scripts\ec2_lease.ps1`: acquire, heartbeat, release, and inspect the EC2 lease.
- `scripts\aws_live_window.ps1`: wrapper for lease-gated AWS live-window operations.
- `scripts\safe_cleanup.ps1`: dry-run-first cleanup helper.
- `scripts\verify_session_system.ps1`: validates the coordination setup.
- `templates\model_card.template.md`: required model-card shape for every downloaded model.
- `templates\model_download_report.template.md`: required EC2 batch download report shape.

Live state files are intentionally ignored by Git. The canonical live state location is this shared directory, not any individual lane worktree.
