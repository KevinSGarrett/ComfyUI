# Main Shared Directory

This is the global instruction and coordination directory for all six Codex Desktop lanes.

Important files:

- `GLOBAL_INSTRUCTIONS.md`: shared operating rules.
- `LANE_BOUNDARIES.md`: hard write boundaries and ownership.
- `EC2_LEASE_PROTOCOL.md`: live EC2 coordination rules.
- `SELF_HOSTED_LLM_POLICY.md`: local/EC2 LLM-first policy for AI intelligence and front-end AI features.
- `CLEANUP_POLICY.md`: safe cleanup allowlist and protected paths.
- `GIT_WORKTREE_SETUP.md`: local Git/worktree plan.
- `schemas\evidence_record.schema.json`: canonical evidence schema.
- `shared_state\lane_registry.json`: machine-readable lane map.
- `scripts\ec2_lease.ps1`: acquire, heartbeat, release, and inspect the EC2 lease.
- `scripts\aws_live_window.ps1`: wrapper for lease-gated AWS live-window operations.
- `scripts\safe_cleanup.ps1`: dry-run-first cleanup helper.
- `scripts\verify_session_system.ps1`: validates the coordination setup.

Live state files are intentionally ignored by Git. The canonical live state location is this shared directory, not any individual lane worktree.
