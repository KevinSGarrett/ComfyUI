# Lane 3 Current Main Flow Auxiliary Reference Addendum - 2026-07-04 16:30:52 UTC

## Scope

After Lane 3 reconciled Lane 1's 26 requested Main Flow model references, an xhigh sanity check parsed the current canonical workflow directly:

`C:\Comfy_UI\Implementation\workflows\ui\WAVE42_MAIN_FLOW_20260702.json`

Current workflow SHA256 during this addendum:

`5C67A23D1F70A6E7A5687E99E58F73EA475A172B4736F32D192AB3929BC35EC9`

The workflow currently contains 38 unique model-like strings. All 26 Lane 1 requested refs are still present in the workflow and already resolved locally. The remaining 12 strings break down as follows.

## Active Additional References

| Reference | Node / context | Local status | Next action |
| --- | --- | --- | --- |
| `bbox/hand_yolov8n.pt` | Node 973 `UltralyticsDetectorProvider`, title `Strict Hand YOLO Detector` | missing in checked local roots | Lane 4 should verify runtime availability or restore from EC2 path `/home/ubuntu/ComfyUI/models/ultralytics/bbox/hand_yolov8n.pt`; workflow metadata gives SHA256 `f3f23b865741cc8373a76dfac31a71ffd71356a480ca43266f294815b608e174`. |
| `sam_vit_b_01ec64.pth` | Node 975 `SAMLoader`, title `Strict Hand SAM Loader` | missing in checked local roots | Lane 4 should verify runtime availability or identify sanctioned source/install path. |
| `dw-ll_ucoco_384_bs5.torchscript.pt` | Nodes 978 and 1040 `DWPreprocessor`, titles `Strict Hand DWPose Control` and `Strict Body Contact DWPose Control` | missing in checked local roots | Lane 4 should verify runtime availability or identify sanctioned source/install path. |
| `wave42/sdxl/pose_camera/sdxl_adult_male_Double_Kiss_POV.safetensors` | Node 411 `Lora Loader Stack (rgthree)` | present under `C:\Comfy_UI\Runtime_Data\models\loras\wave42\sdxl\pose_camera` | Include in Lane 4 LoRA catalog visibility check. |
| `wave42/sdxl/skin_imperfections/sdxl_hair_heavily_freckled_SDXL_NSFW.safetensors` | Node 411 `Lora Loader Stack (rgthree)` | present under `C:\Comfy_UI\Runtime_Data\models\loras\wave42\sdxl\skin_imperfections` | Include in Lane 4 LoRA catalog visibility check. |
| `wave42/sdxl/skin_texture/sdxl_skin_texture_Wet_Makeup__Runny_Mascara-000006.safetensors` | Nodes 411, 505, 686, 742 `Lora Loader Stack (rgthree)` | present under `C:\Comfy_UI\Runtime_Data\models\loras\wave42\sdxl\skin_texture` | Include in Lane 4 LoRA catalog visibility check. |

## Metadata-Only Strings

The remaining strings were found in registry/evidence metadata, not active widget values requiring direct loader catalog visibility:

- `/home/ubuntu/ComfyUI/models/ultralytics/bbox/hand_yolov8n.pt`
- `C:\Comfy_UI_Lora\downloads\Hands\Better hands flux v1.0.safetensors`
- `C:\Comfy_UI_Lora\downloads\Hands\Detailed_Hands-000001.safetensors`
- `C:\Comfy_UI_Lora\downloads\Hands\feminine_hands.safetensors`
- `C:\Comfy_UI_Lora\downloads\Hands\Hand v2.safetensors`
- `C:\Comfy_UI_Lora\downloads\Hands\Hands.safetensors`

`Hands.safetensors` matches the already-resolved Main Flow relative reference `wave42/sdxl/jewelry_accessories/sdxl_jewelry_accessories_Hands.safetensors` by SHA256 `2B280402901408C3F5E2B02E9F197FEB500796A4B93E57E638BA8454755BE10C`.

## Conclusion

No new checkpoint, Flux, VAE, ControlNet, upscale, text-encoder, or Wave42 LoRA local-placement blocker remains from this addendum. The current concrete blockers are three active auxiliary detection/preprocessor assets used by strict hand/body-contact nodes. Lane 4 runtime visibility/load verification is still required.
