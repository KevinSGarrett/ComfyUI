# Lane 3 Model And LoRA Compatibility Table

Created: 2026-07-04T15:50:47Z
Lane: Lane_3
Scope: local model/LoRA inventory, compatibility classification, hash evidence, and runtime-visibility handoff.

## Summary

| Area | Finding |
| --- | --- |
| Civitai targeted search manifest | 368 candidate records, 249 tagged `sdxl`, 119 tagged `flux`; no search errors; download URLs omitted for secret safety. |
| Civitai install manifest | 19 installed LoRAs, 19 downloaded/verified, 0 failed. |
| Local LoRA files hashed | 22 total: 19 Civitai LoRAs plus 3 pre-existing Wave42 SDXL LoRAs. |
| Hash result | 19/19 Civitai LoRAs matched their expected SHA256; 3 pre-existing Wave42 LoRAs now have recorded SHA256 values but no prior expected hash. |
| Runtime visibility | Not proven in live ComfyUI during this lane pass; Lane 4 request created for `/object_info` and model-path visibility checks. |
| Checkpoints/control/video/audio | `C:\Comfy_UI\models` has taxonomy folders for Flux, SDXL, LTX/AnimateDiff/Hunyuan/Wan video families, but no model files were found there. `C:\Comfy_UI_Lora\models` contains empty family folders only. |
| LLM local route | Ollama is installed and `http://127.0.0.1:11434/v1` is reachable; `qwen2.5:14b` completed a smoke request. |

## Compatibility Rules

| Rule | Status | Notes |
| --- | --- | --- |
| Keep SDXL LoRAs on SDXL checkpoints/workflows only. | Required | SDXL LoRAs live under `Runtime_Data\models\loras\...\sdxl\...`. |
| Keep Flux LoRAs on Flux checkpoints/workflows only. | Required | Flux LoRAs live under `Runtime_Data\models\loras\...\flux\...`. |
| Pony candidates from search manifest are not installed. | Preserved | Search manifest includes Pony candidates, but the install pass intentionally excluded Pony because local proven checkpoints are SDXL/Flux oriented. |
| Treat empty video/audio taxonomy folders as planned structure, not available runtime assets. | Required | No LTXV, Wan, Hunyuan, AnimateDiff, audio, ControlNet, IPAdapter, VAE, checkpoint, or upscaler binaries were found in those folders. |
| External LLM APIs are fallback-only. | Required | Local Ollama route works for a basic request; EC2 route must be Lane 4 controlled if needed. |

## SDXL LoRAs

| Provenance | Category | Model | Base/family | Size bytes | SHA256 status | Runtime relative path |
| --- | --- | --- | --- | ---: | --- | --- |
| Civitai install | mature_age | Mature Female | SDXL 1.0 | 170540788 | match `A31129F52E53761B7888D138F803D2D69640A9AB380A31EA21CCEFA906737E3C` | `civitai_wave42/sdxl/mature_age/Mature_Female__v342953__MatureFemaleSDXL-LoCon.safetensors` |
| Civitai install | curvy_hourglass_body | Hourglass Body Shape SD1.5/SDXL/PONY/FLUX | SDXL 1.0 | 57444860 | match `1F2CD36C9C0ED5FBF0834556EF9A066FEAE81DC8B3893D381429A96AB497FE5B` | `civitai_wave42/sdxl/curvy_hourglass_body/Hourglass_Body_Shape_SD1.5_SDXL_PONY_FLUX_olaz__v911708__hourglassv2_SDXL.safetensors` |
| Civitai install | curvy_body_shape | Curvy body - SDXL | SDXL 1.0 | 405038036 | match `B72DBBA89076442D25A8DA9894830D1538B0C9BA22F957F068418A3A419AADB3` | `civitai_wave42/sdxl/curvy_body_shape/Curvy_body_-_SDXL__v1449869__b8174d41-8ba7-4318-bc14-53ee7e353d91.TA_trained.safetensors` |
| Civitai install | body_slider | bodyslider sdxl | SDXL 1.0 | 228463140 | match `5CAB974A9956CA95192CD8BEB9BBF262F3862D244A402DB6FC5EEF4339C77F70` | `civitai_wave42/sdxl/body_slider/bodyslider_sdxl__v2515273__bodyslider_sdxl.safetensors` |
| Civitai install | bbw_large_butt_thighs | Chubby BBW - XL | SDXL 1.0 | 532093668 | match `439AAD7DAFD316E9F1AE1F9554AB15146E0587C161AEA1F7ED30D7803183B9C7` | `civitai_wave42/sdxl/bbw_large_butt_thighs/Chubby_BBW_-_XL__v704816__Chubby_BBW_-_XL.safetensors` |
| Civitai install | skin_imperfections | Skin Realism SDXL | SDXL 1.0 | 23401064 | match `9C80E90E7DECC4DF7C4730B3CF19EA78BBACAD8BEEA04295124A8066EEA49976` | `civitai_wave42/sdxl/skin_imperfections/Skin_Realism_Acne_Skin_Details_Imperfections_SDX__v280914__imperfect.safetensors` |
| Civitai install | skin_texture_realism | Realistic Skin Texture style XL | SDXL 1.0 | 456490292 | match `BC0F5B9D2479AF0D82BEF4E7A7E97253E16E3EFAC8BC3612D3E985A5018C4BAD` | `civitai_wave42/sdxl/skin_texture_realism/Realistic_Skin_Texture_style_Detailed_Skin_XL_SD__v647890__skin_texture_style.safetensors` |
| Civitai install | lip_expression | Joschek's Lip Biting | SDXL 1.0 | 228465700 | match `A5049114C72961E9A93F3B1A419A2CEA281D5E654556AA614B111785349EAA30` | `civitai_wave42/sdxl/lip_expression/Joschek_s_Lip_Biting__v384729__biting_own_lip-000008.safetensors` |
| Civitai install | hoop_earrings | oversize hoop earrings SDXL | SDXL 1.0 | 228455468 | match `4CCBD1B8E83D3FEADE360F29495B5862E0984FEC0E2EAF784676F17BD2E53960` | `civitai_wave42/sdxl/hoop_earrings/oversize_hoop_earrings_SDXL__v2951537__oversize_hoop_earrings_SDXL_epoch_16.safetensors` |
| Civitai install | pov_camera | Point of view cinematic style XL | SDXL 1.0 | 456484996 | match `3F723CB66EC7DF10DE4CFB2F0CC5DDB2464DF13846B4AE816757D692EB2A7893` | `civitai_wave42/sdxl/pov_camera/Point_of_view_pov_fps_cinematic_subjective_camer__v712243__point_of_view_style_v3.safetensors` |
| Local Wave42 existing | pose_camera | sdxl_adult_male_Double_Kiss_POV | SDXL-compatible path | 228454548 | recorded `81DFDDB3246862A1353222A96B128AC0FE9E6113483563DBFF7283A08487D6CD` | `wave42/sdxl/pose_camera/sdxl_adult_male_Double_Kiss_POV.safetensors` |
| Local Wave42 existing | skin_imperfections | sdxl_hair_heavily_freckled_SDXL_NSFW | SDXL-compatible path | 228458596 | recorded `344FD9735F04CCBDAAFD2D0F7C2AB4CF8BD7F39CDF07675A9D71A47396471E3A` | `wave42/sdxl/skin_imperfections/sdxl_hair_heavily_freckled_SDXL_NSFW.safetensors` |
| Local Wave42 existing | skin_texture | sdxl_skin_texture_Wet_Makeup__Runny_Mascara-000006 | SDXL-compatible path | 228459156 | recorded `3234F2819F7DFC73E14C88EB3633E1D9BF671D22D4D269648C4BEBF453E3F198` | `wave42/sdxl/skin_texture/sdxl_skin_texture_Wet_Makeup__Runny_Mascara-000006.safetensors` |

## Flux LoRAs

| Provenance | Category | Model | Base/family | Size bytes | SHA256 status | Runtime relative path |
| --- | --- | --- | --- | ---: | --- | --- |
| Civitai install | mature_age | Mature Women Flux | Flux.1 D | 19299784 | match `1072C4A093BDB1231369608695CA366B803D6C06C0F345CAAA107B754A9BD63C` | `civitai_wave42/flux/mature_age/Mature_Women_Flux__v1746681__Mature_Women_Flux.safetensors` |
| Civitai install | curvy_hourglass_body | Hourglass Body Shape SD1.5/SDXL/PONY/FLUX | Flux.1 D | 153293920 | match `9830F79604EBC49C85965202529DC9399B1B1022FEC3895EF0BD0329C81E0F1C` | `civitai_wave42/flux/curvy_hourglass_body/Hourglass_Body_Shape_SD1.5_SDXL_PONY_FLUX_olaz__v932199__hourglassv2_flux.safetensors` |
| Civitai install | skin_pores_realism | Realistic Skin Texture style Flux | Flux.1 D | 343805479 | match `6A597F63C07E0C1AD022400F0F611ABB377FA258C06676F34276FD33ABAED721` | `civitai_wave42/flux/skin_pores_realism/Realistic_Skin_Texture_style_Detailed_Skin_XL_SD__v804746__detailed_skin_pore_style_v2.safetensors` |
| Civitai install | long_curly_hair | Long hair LoRA - Flux / Z-image | Flux.1 D | 19259304 | match `A7025C1C655229D64C728173A33A3CA0158FD5329920005B06CFE50A36C3E3AC` | `civitai_wave42/flux/long_curly_hair/Long_hair_LoRA_-_Flux_Z-image__v753327__Longhair2.safetensors` |
| Civitai install | big_lips | big lips | Flux.1 D | 19281432 | match `71BDAD4A4AF2C54804FFCAE7D14328A887288FB06D7FA97C6C0F81E1FB6A6205` | `civitai_wave42/flux/big_lips/big_lips__v1699453__lips2.safetensors` |
| Civitai install | lip_expression | Joschek's Lip Biting for Flux | Flux.1 D | 153284592 | match `146D945DC793ADD98501162BCDEE9B8BECE8DE78473D44229BB56E860575290B` | `civitai_wave42/flux/lip_expression/Joschek_s_Lip_Biting_for_Flux__v2091427__lip_bitiing_flux.safetensors` |
| Civitai install | hoop_earrings | Hoop earrings | Flux.1 D | 19258624 | match `66B48048B3062D14FE05013062DEE92DEE94E96CA9C3A3AF1CF1248005EDDD32` | `civitai_wave42/flux/hoop_earrings/Hoop_earrings__v1448114__Hoop_earrings.safetensors` |
| Civitai install | pov_camera | Point of view cinematic style Flux | Flux.1 D | 306498944 | match `B9CC7164038EDB18A65272BE6F21C2E234F55B1C6702EAE65B086F8E22163373` | `civitai_wave42/flux/pov_camera/Point_of_view_pov_fps_cinematic_subjective_camer__v1407640__pov_style_v1.safetensors` |
| Civitai install | saggy_breasts | saggy breasts proof of concept | Flux.1 D | 836874584 | match `C59B19887FFC6804943A24E746E93683C9FF7368EA68AC2AA2D842EF84624E94` | `civitai_wave42/flux/saggy_breasts/saggy_breasts_proof_of_concept__v888864__saggy_breasts-save-560-20-0.safetensors` |

## LLM Route Evidence

| Item | Current evidence |
| --- | --- |
| Local engine | Ollama installed at `C:\Users\kevin\AppData\Local\Programs\Ollama\ollama.exe`. |
| Local endpoint | `http://127.0.0.1:11434/v1/models` returned in 341 ms. |
| Installed local LLMs | `llava:13b` manifest `0D0EB4D7F485D7D0A21FD9B0C1D5B04DA481D2150A097E81B64ACB59758FDEF6`; `qwen2.5:14b` manifest `7CDF5A0187D5C58CC5D369B255592F7841D1C4696D45A8C8A9489440385B22F6`; `qwen2.5:32b` manifest `9F13BA1299AFEA09D9A956FC6A85BECC99115A6D596FAE201A5487A03BDC4368`. |
| Smoke inference | `qwen2.5:14b` via `/v1/chat/completions` returned `WAVE42_LOCAL_OK`, finish `stop`, 49 total tokens, 16146 ms elapsed. |
| Plan gap | Existing AI plan names Qwen3-Coder / Qwen3.x as target primary models, but those are not installed locally. Use current local Qwen2.5 models as the immediate self-hosted route and ask Lane 4 to validate EC2-hosted Qwen3-Coder-class capacity if required. |

## Runtime Request

Lane 4 runtime visibility request:

Canonical live request:

`C:\Comfy_UI_Lora\5_sessions\Main\shared_state\ec2_requests\20260704_155047_Lane_3_model_lora_llm_visibility.json`

Committed Lane 3 copy:

`C:\Comfy_UI_Lora\5_session_worktrees\Lane_3\Lane_3\requests\20260704_155047_Lane_3_model_lora_llm_visibility.json`
