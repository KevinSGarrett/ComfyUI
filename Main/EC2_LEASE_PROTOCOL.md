# EC2 Lease Protocol

The project has one shared EC2 instance:

- Instance id: `i-0560bf8d143f93bb1`
- Normal idle state: stopped
- Expected runtime owner: `Lane_4`

## Rule

Only one lane may hold the EC2 lease. Only the active lease owner may start or stop EC2. By policy, only `Lane_4` should acquire the lease for live runtime work. Other lanes submit requests.

## Lease File

Canonical live lease:

`C:\Comfy_UI_Lora\5_sessions\Main\shared_state\ec2_lease.json`

Template:

`C:\Comfy_UI_Lora\5_sessions\Main\shared_state\ec2_lease.template.json`

Use:

```powershell
C:\Comfy_UI_Lora\5_sessions\Main\scripts\ec2_lease.ps1 -Action status
C:\Comfy_UI_Lora\5_sessions\Main\scripts\ec2_lease.ps1 -Action acquire -Lane Lane_4 -Purpose "live ComfyUI endpoint validation" -LeaseMinutes 90
C:\Comfy_UI_Lora\5_sessions\Main\scripts\ec2_lease.ps1 -Action heartbeat -Lane Lane_4
C:\Comfy_UI_Lora\5_sessions\Main\scripts\ec2_lease.ps1 -Action release -Lane Lane_4
```

## Requesting Runtime Work

Non-runtime lanes create request files under:

`C:\Comfy_UI_Lora\5_sessions\Main\shared_state\ec2_requests`

Request fields:

- `requesting_lane`
- `purpose`
- `needed_by`
- `required_files`
- `commands_or_endpoints`
- `expected_outputs`
- `max_runtime_minutes`
- `stop_after_completion`

## Required Live Window Steps

Lane 4 must:

1. Confirm no active lease exists.
2. Acquire lease.
3. Check AWS auth without printing credentials.
4. Check active local stop/reboot loops.
5. Check current EC2 state.
6. Start EC2 only if live runtime is necessary.
7. Batch all endpoint, model, generation, and sync work tightly.
8. Collect evidence and hashes.
9. Stop EC2 as soon as work is done, blocked, or paused.
10. Verify stopped state and no public IP.
11. Release lease.

If AWS auth fails, EC2 is unreachable, ComfyUI is down, or credentials expire, record the exact blocker and do not claim live validation is complete.

