# Lane 7 Storage Pressure Report - 2026-07-04T19:35:00Z

## Snapshot

- `C:` free: `164.391 GB`
- `C:` total: `951.646 GB`
- Free percent: `17.27%`
- EC2 lease: free (`owner_lane: null`, `purpose: null`)
- `C:\Comfy_UI\EC2_Mirror\20260628_211600` absent
- `C:\Comfy_UI\_ec2sd\20260701_125027` absent

## Risk

- Risk remains `watch`; no immediate new storage crisis.

## Policy constraints (lane owner applies only)

- No cleanup apply by Lane 7.
- Dry-run only before any cleanup if later requested.
- Do not remove protected roots (`models`, `workflows`, `trackers`, `evidence`, generated media, credentials).

## Ownership routing

- Keep cleanup and EC2-cost ownership with Lane 4 per constraints.
- Continue to route any storage cleanup request to owner lanes with evidence-backed command log.
