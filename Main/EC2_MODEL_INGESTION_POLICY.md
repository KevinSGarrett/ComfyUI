# EC2 Model Ingestion Policy

## Purpose

`C:\Comfy_UI_Lora\downloads\models` contains the curated Civitai CSV inventory for models that may be added to the ComfyUI EC2 runtime.

This is not permission for a broad local mirror. Local work against those CSVs is read-only metadata analysis. Actual model downloads must run on EC2 or another explicitly approved remote storage target with enough capacity.

## Source Inventory

Observed on 2026-07-04:

| File | Data rows | Size MB | Role |
| --- | ---: | ---: | --- |
| `PENDING_flux1_sdxl_TOP500_curated.csv` | 500 | 3.21 | Immediate curated ingest candidate set. |
| `model_index_full_capture.csv` | 5530 | 0.98 | Model-level index. |
| `model_details_full_capture.csv` | 5530 | 9.45 | Model details, licensing, descriptions, tags, suggested weights. |
| `model_versions_full_capture.csv` | 11220 | 6.10 | Version metadata, base model, trained words, version status. |
| `model_files_full_capture.csv` | 11688 | 6.38 | File metadata, sizes, hashes, scan results, download URLs. |
| `model_images_full_capture.csv` | 200766 | 538.21 | Image/prompt/reference metadata. Do not copy images locally as part of ingest. |
| `model_match_manifest.csv` | 106823 | 29.55 | Taxonomy/model matching provenance. |
| `model_payload_leaf_rows.csv` | 4000443 | 691.90 | Expanded payload details for metadata mining only. |
| `model_payload_path_catalog.csv` | 176827 | 10.50 | JSON path catalog for payload mining. |
| `WAVE15_FILLED_MASTER_NSFW_MODEL_TAXONOMY.csv` | 2188 | 5.31 | Taxonomy and integration fields. |
| `fill_review_report.csv` | 2188 | 0.38 | Fill status/review summary. |

## Hard Boundaries

- Do not download model binaries, images, archives, or raw Civitai payload mirrors to local `C:\Comfy_UI`, `C:\Comfy_UI_Lora`, or lane worktrees.
- Do not commit model binaries, generated media, raw downloads, credential files, token-bearing URLs, or raw API responses that contain secrets.
- Do not print, log, commit, or include `CIVITAI_TOKEN` or tokenized Civitai URLs in reports, model cards, SSM output, shell history, or evidence.
- Do not start a broad ingest from all 5530 models until Lane 3 has produced a storage-ranked manifest and Lane 4 has proven EC2 free space and rollback/stop behavior.
- Do not continue EC2 downloads if projected free space after the batch would fall below 150 GB or 15 percent of the attached volume, whichever is stricter.
- Stop and report before any batch that cannot be proven to fit inside the EC2 storage budget.

## Lane Ownership

Lane 3 owns:

- Parsing the local CSVs read-only.
- Deduplicating model/version/file rows.
- Selecting phased ingest batches.
- Defining the EC2 target folder taxonomy.
- Creating a model-card draft for every model selected for download.
- Creating Lane 4 model-ingest requests with expected sizes, URLs redacted, hash expectations, and storage projections.
- Keeping Civitai and self-hosted LLM model selection separate.

Lane 4 owns:

- Acquiring the EC2 lease for any live download/sync window.
- Verifying EC2 disk state before, during, and after each batch.
- Running EC2-only Civitai downloads through a secret-safe method.
- Verifying downloaded file sizes, hashes, ComfyUI model-folder placement, and `/object_info` visibility where applicable.
- Stopping EC2 and releasing the lease after each bounded window.
- Writing download evidence and a batch report.

Lane 5 owns:

- Auditing model-card completeness, evidence schema compliance, direct proof of downloaded files, hash checks, scan status, license/usage fields, and tracker impact.
- Rejecting claims based only on CSV metadata or planned downloads.

Lane 6 owns:

- Consuming the resulting model catalog for presets and AI_Front model selection only after Lane 5 accepts evidence or records the precise limitation.

Lane 7 owns:

- Tracking the end-to-end ingest dashboard, storage pressure, usage-limit resume packets, and owner-lane next actions.
- It must not download, delete, or retag models.

## Required Phases

1. Inventory phase:
   - Read CSV headers/counts and build a deduplicated model/version/file manifest.
   - Group by base model family, model type, size, scan status, license/commercial fields, tags, and taxonomy row.
   - Estimate total byte size for the selected batch before any download.

2. Planning phase:
   - Prefer `PENDING_flux1_sdxl_TOP500_curated.csv` for the first batch.
   - Sort by Main Flow relevance, required runtime families, safety/scan status, file size, and taxonomy priority.
   - Produce a batch manifest and one model card draft per model before Lane 4 downloads.

3. EC2 preflight phase:
   - Lane 4 verifies the EC2 instance state, attached volume capacity, free space, ComfyUI model roots, active downloads, and lease state.
   - Lane 4 cleans stale EC2 mirror snapshots first if local storage pressure blocks safe coordination.
   - Lane 4 must record projected EC2 free space after the batch.

4. Download phase:
   - Downloads run on EC2 only.
   - Use `CIVITAI_TOKEN` without echoing it or persisting it in command logs.
   - Download to a staging directory first, then atomically move into the organized ComfyUI model folder after size/hash verification.
   - Maintain a resumable manifest with per-file status.

5. Verification phase:
   - Verify expected file size and available hashes from Civitai metadata.
   - Record Civitai scan fields from the CSV.
   - Verify ComfyUI-visible folder placement and, when a live window is already justified, `/object_info` catalog visibility.
   - Do not claim generation compatibility until a generation/load test has evidence.

6. Reporting phase:
   - Update the per-model model card.
   - Update the batch download report.
   - Produce Lane 5-ready evidence that distinguishes `downloaded`, `hash_verified`, `catalog_visible`, `load_tested`, and `generation_tested`.

## EC2 Target Organization

Lane 3 should choose the exact taxonomy before the first batch. Default target roots:

- `/home/ubuntu/ComfyUI/models/checkpoints/<family>/`
- `/home/ubuntu/ComfyUI/models/loras/<family>/<source-or-taxonomy>/`
- `/home/ubuntu/ComfyUI/models/controlnet/<family>/`
- `/home/ubuntu/ComfyUI/models/vae/<family>/`
- `/home/ubuntu/ComfyUI/models/clip/<family>/`
- `/home/ubuntu/ComfyUI/models/unet/<family>/`
- `/home/ubuntu/ComfyUI/models/upscale_models/<family>/`
- `/home/ubuntu/ComfyUI/models/embeddings/<family>/`

Every file must keep a stable source identity:

- `civitai_model_id`
- `civitai_version_id`
- `civitai_file_id`
- `downloaded_filename`
- `target_relative_path`
- `sha256` or best available hash

## Model Card Minimum Fields

Use `Main\templates\model_card.template.md`.

Each downloaded model must have a model card that includes:

- Model name, Civitai URL, model/version/file IDs.
- Base model and compatibility family.
- Model type and ComfyUI destination.
- File size, filename, hashes, scan status, and download date.
- Creator, tags, trained words, suggested weight/range, and trigger notes.
- License/commercial/derivative/no-credit fields exactly as captured.
- Safety flags: NSFW level, POI/minor flags if present, availability, and any rejection notes.
- Taxonomy matches and intended Main Flow/preset use.
- Evidence links: download report row, hash verification, `/object_info` visibility, generation/load tests if present.
- Current QA status and remaining blockers.

## Batch Report Minimum Fields

Use `Main\templates\model_download_report.template.md`.

Each batch report must include:

- Batch id and lane ids.
- EC2 instance id and volume/free-space preflight.
- Selected CSV source files and row filters.
- Planned total bytes, downloaded bytes, skipped bytes, failed bytes.
- Per-model status table.
- Exact target root layout.
- Stop/resume instructions.
- Evidence paths and hashes.
- Storage after-state.
- Explicit list of models not downloaded and why.

## First Safe Next Step

Before any model download:

1. Lane 3 builds `top500` batch 0 as a dry manifest from `PENDING_flux1_sdxl_TOP500_curated.csv`.
2. Lane 3 creates model-card drafts for that batch from the CSV metadata.
3. Lane 4 finishes current local storage cleanup and verifies EC2 free space.
4. Lane 4 designs a token-safe EC2 download runner and dry-runs it with no token output.
5. Lane 5 audits the manifest/card/report schema before the first live download batch.
