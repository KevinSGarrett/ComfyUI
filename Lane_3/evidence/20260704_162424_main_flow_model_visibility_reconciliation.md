# Lane 3 Main Flow Model Visibility Reconciliation - 2026-07-04 16:24:24 UTC

## Scope

Lane 3 consumed Lane 1's Main Flow model visibility request and reconciled the 26 referenced assets against the canonical Main Flow workflow and local model roots.

- Canonical workflow: `C:\Comfy_UI\Implementation\workflows\ui\WAVE42_MAIN_FLOW_20260702.json`
- Workflow SHA256 at reconciliation: `273158B6B84CEFC67A706AC1C4656D90CFBEBF04F0890A9230DD526475D5B96D`
- Lane 1 request: `C:\Comfy_UI_Lora\5_sessions\Lane_1\requests\lane1_to_lane3_main_flow_model_visibility_20260704_105550.json`
- Lane 1 request SHA256: `9F02B716544FE40612A010906C6DEF297951939DDDC41A51E258E3FAFB0F748A`
- Checked model roots: `C:\Comfy_UI\models`, `C:\Comfy_UI\Runtime_Data\models`, `C:\Comfy_UI_Lora\models`

## Result

All 26 of 26 Main Flow references are now present by exact expected name under `C:\Comfy_UI\Runtime_Data\models`.

This proves local file placement and hash identity for the reconciled Main Flow references. It does not prove that the running ComfyUI process has refreshed its model catalog or can load each asset in a workflow execution. Lane 4 runtime visibility verification is still required.

## Compatibility Table

| Reference | Family | Loader / role | Status | Primary path | SHA256 |
| --- | --- | --- | --- | --- | --- |
| `RealESRGAN_x4plus.pth` | Upscale model | `UpscaleModelLoader` | present | `C:\Comfy_UI\Runtime_Data\models\upscale_models\RealESRGAN_x4plus.pth` | `4FA0D38905F75AC06EB49A7951B426670021BE3018265FD191D2125DF9D682F1` |
| `RealVisXL_V5.0_fp16.safetensors` | SDXL checkpoint | `CheckpointLoaderSimple` | present | `C:\Comfy_UI\Runtime_Data\models\checkpoints\RealVisXL_V5.0_fp16.safetensors` | `6A35A7855770AE9820A3C931D4964C3817B6D9E3C6F9C4DABB5B3A94E5643B80` |
| `ae.safetensors` | Flux VAE | `VAELoader` | present | `C:\Comfy_UI\Runtime_Data\models\vae\ae.safetensors` | `AFC8E28272CD15DB3919BACDB6918CE9C1ED22E96CB12C4D5ED0FBA823529E38` |
| `controlnet-canny-sdxl-1.0-small.safetensors` | SDXL ControlNet | `ControlNetLoader` | present | `C:\Comfy_UI\Runtime_Data\models\controlnet\controlnet-canny-sdxl-1.0-small.safetensors` | `97B75CE51FAE5CFC4D5EA98445292D482D911B241B9A82FD8260DBAA2269031A` |
| `controlnet-depth-sdxl-1.0-small.fp16.safetensors` | SDXL ControlNet | `ControlNetLoader` | present | `C:\Comfy_UI\Runtime_Data\models\controlnet\controlnet-depth-sdxl-1.0-small.fp16.safetensors` | `6F23C58FD632F52238A7B35EBDC02F9F596FD13DBAA121F9B37B9F4689C2B1E9` |
| `controlnet-openpose-sdxl-1.0.safetensors` | SDXL ControlNet | `ControlNetLoader` | present | `C:\Comfy_UI\Runtime_Data\models\controlnet\controlnet-openpose-sdxl-1.0.safetensors` | `B8524E557A7DF60D081F5D4A0EB109967D107DF217943BF88C2D99B9EBCC06C5` |
| `flux1-dev-fp8.safetensors` | Flux checkpoint | `CheckpointLoaderSimple` | present | `C:\Comfy_UI\Runtime_Data\models\checkpoints\flux1-dev-fp8.safetensors` | `8E91B68084B53A7FC44ED2A3756D821E355AC1A7B6FE29BE760C1DB532F3D88A` |
| `flux1-schnell-fp8.safetensors` | Flux checkpoint | `CheckpointLoaderSimple` | present | `C:\Comfy_UI\Runtime_Data\models\checkpoints\flux1-schnell-fp8.safetensors` | `EAD426278B49030E9DA5DF862994F25CE94AB2EE4DF38B556DDDDB3DB093BF72` |
| `qwen_3_4b.safetensors` | Text encoder | `CLIPLoader` | present | `C:\Comfy_UI\Runtime_Data\models\text_encoders\qwen_3_4b.safetensors` | `6C671498573AC2F7A5501502CCCE8D2B08EA6CA2F661C458E708F36B36EDFC5A` |
| `z_image_turbo_bf16.safetensors` | Z-Image diffusion model | `UNETLoader` | present | `C:\Comfy_UI\Runtime_Data\models\diffusion_models\z_image_turbo_bf16.safetensors` | `2407613050B809FFDFF18A4AC99AF83EA6B95443ECEBDF80E064A79C825574A6` |
| `wave42/flux/fluids/flux_fluids_Dirty_Sweat_Movie.safetensors` | Flux LoRA | `LoraLoader` / rgthree LoRA stack | present | `C:\Comfy_UI\Runtime_Data\models\loras\wave42\flux\fluids\flux_fluids_Dirty_Sweat_Movie.safetensors` | `613B1FFBAD683049521F9CC6295D622EA83BC43DCDC45F044AA6AC948FC5E606` |
| `wave42/flux/fluids/flux_fluids_flux_sweat_v2.safetensors` | Flux LoRA | `LoraLoader` / rgthree LoRA stack | present | `C:\Comfy_UI\Runtime_Data\models\loras\wave42\flux\fluids\flux_fluids_flux_sweat_v2.safetensors` | `41617D0983F0D465AE74FED3F76A83577C785EF98505D4071FBD08928F2C96CB` |
| `wave42/flux/fluids/flux_fluids_mascara-tears-v2.safetensors` | Flux LoRA | `LoraLoader` / rgthree LoRA stack | present | `C:\Comfy_UI\Runtime_Data\models\loras\wave42\flux\fluids\flux_fluids_mascara-tears-v2.safetensors` | `7BEFC2B2A0E5EC32A0231EC744EC38BDF73FC995877934F699FDE04F432F29C7` |
| `wave42/flux/fluids/flux_fluids_Oily_skin_style_v1.safetensors` | Flux LoRA | `LoraLoader` / rgthree LoRA stack | present | `C:\Comfy_UI\Runtime_Data\models\loras\wave42\flux\fluids\flux_fluids_Oily_skin_style_v1.safetensors` | `859AAD5F4E0B99A0447FB4EF7E35CE594791730C4386B3EEC92632B8EE20F7DB` |
| `wave42/flux/fluids/flux_fluids_SWEATY.safetensors` | Flux LoRA | `LoraLoader` / rgthree LoRA stack | present | `C:\Comfy_UI\Runtime_Data\models\loras\wave42\flux\fluids\flux_fluids_SWEATY.safetensors` | `AA8911EE3C42BE0E373E2AC529591E9C15BCA045A81F740ED7AE4E747255C4CF` |
| `wave42/flux/fluids/flux_fluids_Sweaty_1.safetensors` | Flux LoRA | `LoraLoader` / rgthree LoRA stack | present | `C:\Comfy_UI\Runtime_Data\models\loras\wave42\flux\fluids\flux_fluids_Sweaty_1.safetensors` | `CE2A841015D3B251ECAB3B108948E796C59F5B7FC092E940F1F6B5FDDAC8BF0E` |
| `wave42/flux/hands/flux_hands_Better_hands_flux_v1_0.safetensors` | Flux LoRA | `LoraLoader` / rgthree LoRA stack | present | `C:\Comfy_UI\Runtime_Data\models\loras\wave42\flux\hands\flux_hands_Better_hands_flux_v1_0.safetensors` | `7A4760CD8C95F700A9D2BD107C93631A87E3F24127EE0973CC110E619CC786C9` |
| `wave42/flux/hands/flux_hands_Detailed_Hands-000001.safetensors` | Flux LoRA | `LoraLoader` / rgthree LoRA stack | present | `C:\Comfy_UI\Runtime_Data\models\loras\wave42\flux\hands\flux_hands_Detailed_Hands-000001.safetensors` | `DB03488D97D57FC4024322BA799DBF4EF3C894DFEEB2560D1FBED994F842A335` |
| `wave42/flux/hands/flux_hands_feminine_hands.safetensors` | Flux LoRA | `LoraLoader` / rgthree LoRA stack | present | `C:\Comfy_UI\Runtime_Data\models\loras\wave42\flux\hands\flux_hands_feminine_hands.safetensors` | `1B886A1C45CDB6F896ACACB387A973DD39D035576891C34B6A1F1DE19E6ED54C` |
| `wave42/flux/hands/flux_hands_Hand_v2.safetensors` | Flux LoRA | `LoraLoader` / rgthree LoRA stack | present | `C:\Comfy_UI\Runtime_Data\models\loras\wave42\flux\hands\flux_hands_Hand_v2.safetensors` | `82B169C9500DA411FBCCAA40538F34F44290A525B9A2710431E91229D281F96E` |
| `wave42/flux/skin/flux_skin_Bombshell_Flux_V3.safetensors` | Flux LoRA | `LoraLoader` / rgthree LoRA stack | present | `C:\Comfy_UI\Runtime_Data\models\loras\wave42\flux\skin\flux_skin_Bombshell_Flux_V3.safetensors` | `E4C1A7EB7E89415198AFF67D52735964FCA0A29025CC6B6CB9C4EEA507832FD1` |
| `wave42/flux/skin/flux_skin_FC-Bandeau.safetensors` | Flux LoRA | `LoraLoader` / rgthree LoRA stack | present | `C:\Comfy_UI\Runtime_Data\models\loras\wave42\flux\skin\flux_skin_FC-Bandeau.safetensors` | `766B3DFB3F665D49522C7E94B0A58AB94A7763DD65199C8EA51066EE82DAAF43` |
| `wave42/flux/skin/flux_skin_OiledSkin_FluxDev.safetensors` | Flux LoRA | `LoraLoader` / rgthree LoRA stack | present | `C:\Comfy_UI\Runtime_Data\models\loras\wave42\flux\skin\flux_skin_OiledSkin_FluxDev.safetensors` | `4A0C0F8E8C45587AA12EAD2E785C1F21DF452D933A51793EC7E3E4E3D6EB1C03` |
| `wave42/flux/style/flux_style_Hair_Style_Wet_Hair-Weak.safetensors` | Flux LoRA | `LoraLoader` / rgthree LoRA stack | present | `C:\Comfy_UI\Runtime_Data\models\loras\wave42\flux\style\flux_style_Hair_Style_Wet_Hair-Weak.safetensors` | `2D0C893944C97021C1B6A6E16AC17A6B2477811F883A2E0B56ADE41522D3951D` |
| `wave42/sdxl/fluids/sdxl_fluids_Sweaty_Realism_4-000006.safetensors` | SDXL LoRA | `LoraLoader` / rgthree LoRA stack | present | `C:\Comfy_UI\Runtime_Data\models\loras\wave42\sdxl\fluids\sdxl_fluids_Sweaty_Realism_4-000006.safetensors` | `FEB1A58BFCC24AC7A37FA50599F063EECB8ED2484B88A67E8F9F1FE8F52D1FA4` |
| `wave42/sdxl/jewelry_accessories/sdxl_jewelry_accessories_Hands.safetensors` | SDXL LoRA | `LoraLoader` / rgthree LoRA stack | present | `C:\Comfy_UI\Runtime_Data\models\loras\wave42\sdxl\jewelry_accessories\sdxl_jewelry_accessories_Hands.safetensors` | `2B280402901408C3F5E2B02E9F197FEB500796A4B93E57E638BA8454755BE10C` |

## Lane 4 Runtime Request

Lane 4 should verify that live ComfyUI exposes these names in `/object_info` or equivalent node dropdown data, then run the smallest safe load/catalog smoke check needed to prove runtime visibility. No local-file blocker remains from Lane 3's current reconciliation.
