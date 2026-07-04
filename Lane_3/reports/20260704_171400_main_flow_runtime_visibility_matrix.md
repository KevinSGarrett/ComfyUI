# Main Flow Runtime Visibility Update (171400)

- Workflow SHA256: `5C67A23D1F70A6E7A5687E99E58F73EA475A172B4736F32D192AB3929BC35EC9`  
- Workflow refs: `38`
- Family split: `Flux=17`, `SDXL=10`, `LLM=1`, `Other=10`
- Runtime-present: `29`
- Missing (hard blockers): `3`

## Resolved source aliases

- `bbox/hand_yolov8n.pt` → `/home/ubuntu/ComfyUI/models/ultralytics/bbox/hand_yolov8n.pt`
- `C:\Comfy_UI_Lora\downloads\Hands\Better hands flux v1.0.safetensors` → `C:\Comfy_UI\Runtime_Data\models\loras\wave42\flux\hands\flux_hands_Better_hands_flux_v1_0.safetensors`
- `C:\Comfy_UI_Lora\downloads\Hands\Detailed_Hands-000001.safetensors` → `C:\Comfy_UI\Runtime_Data\models\loras\wave42\flux\hands\flux_hands_Detailed_Hands-000001.safetensors`
- `C:\Comfy_UI_Lora\downloads\Hands\feminine_hands.safetensors` → `C:\Comfy_UI\Runtime_Data\models\loras\wave42\flux\hands\flux_hands_feminine_hands.safetensors`
- `C:\Comfy_UI_Lora\downloads\Hands\Hand v2.safetensors` → `C:\Comfy_UI\Runtime_Data\models\loras\wave42\flux\hands\flux_hands_Hand_v2.safetensors`
- `C:\Comfy_UI_Lora\downloads\Hands\Hands.safetensors` → `C:\Comfy_UI\Runtime_Data\models\loras\wave42\sdxl\jewelry_accessories\sdxl_jewelry_accessories_Hands.safetensors`

## Remaining hard blockers (not present in checked local runtime roots)

- `/home/ubuntu/ComfyUI/models/ultralytics/bbox/hand_yolov8n.pt`
- `dw-ll_ucoco_384_bs5.torchscript.pt`
- `sam_vit_b_01ec64.pth`

## Next owner action

Lane 4 should validate and install/map these 3 blocker paths under EC2/runtime expectations and return an 38-ref runtime visibility matrix with concrete hit names.
