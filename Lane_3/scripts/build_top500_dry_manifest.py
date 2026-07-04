#!/usr/bin/env python3
"""Build a local-only dry EC2 ingest manifest from the curated Civitai Top500 CSV.

This script never downloads model files and intentionally omits Civitai download URLs.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_SOURCE = Path(r"C:\Comfy_UI_Lora\downloads\models\PENDING_flux1_sdxl_TOP500_curated.csv")
DEFAULT_OUT_ROOT = Path(r"C:\Comfy_UI_Lora\5_session_worktrees\Lane_3")
LANE_ID = "Lane_3"
SAFETY_BLOCK_TERMS = {
    "nudify",
    "undress",
    "undressing",
    "deepfake",
    "nonconsensual",
    "non-consensual",
    "loli",
    "shota",
    "underage",
    "teen",
    "minor",
    "schoolgirl",
    "child",
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def slug(value: str, fallback: str = "uncategorized") -> str:
    value = (value or "").strip().lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_")
    return value or fallback


def as_bool(value: str) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes"}


def as_float(value: str, default: float = 0.0) -> float:
    try:
        return float(str(value).strip())
    except Exception:
        return default


def as_int(value: str, default: int = 0) -> int:
    try:
        return int(float(str(value).strip()))
    except Exception:
        return default


def classify_family(base_model: str) -> tuple[str, str]:
    bm = (base_model or "").strip().lower()
    if bm.startswith("sdxl"):
        return "sdxl", "eligible_main_flow_family"
    if bm.startswith("flux.1"):
        return "flux", "eligible_main_flow_family"
    if bm.startswith("zimage"):
        return "z_image", "eligible_main_flow_family"
    if bm.startswith("flux.2"):
        return "flux2_pending_runtime", "quarantine_pending_runtime_family"
    if bm.startswith("wan"):
        return "wan_video", "quarantine_video_family"
    if bm.startswith("sd 1.5"):
        return "sd15", "quarantine_legacy_family"
    if bm.startswith("pony"):
        return "pony", "quarantine_non_main_flow_family"
    if bm.startswith("illustrious"):
        return "illustrious", "quarantine_non_main_flow_family"
    if bm.startswith("chroma"):
        return "chroma", "quarantine_non_main_flow_family"
    if bm.startswith("qwen"):
        return "qwen_image", "quarantine_pending_runtime_family"
    if bm.startswith("hidream"):
        return "hidream", "quarantine_pending_runtime_family"
    return slug(base_model, "unknown"), "quarantine_unknown_family"


def first_category(row: dict[str, str]) -> str:
    raw = row.get("categories_original", "")
    parts = [p.strip() for p in raw.split(",") if p.strip()]
    return slug(parts[0] if parts else "", "uncategorized")


def reject_reasons(row: dict[str, str], family_status: str) -> list[str]:
    reasons: list[str] = []
    if as_bool(row.get("minor", "")):
        reasons.append("minor_flag_true")
    if as_bool(row.get("poi", "")):
        reasons.append("poi_flag_true")
    if row.get("availability") != "Public" or row.get("primary_version_availability") != "Public":
        reasons.append("not_public")
    if row.get("primary_file_virusScanResult") != "Success":
        reasons.append("virus_scan_not_success")
    if row.get("primary_file_pickleScanResult") != "Success":
        reasons.append("pickle_scan_not_success")
    if row.get("primary_file_format") != "SafeTensor":
        reasons.append("not_safetensor")
    if family_status != "eligible_main_flow_family":
        reasons.append(family_status)
    if not row.get("primary_file_id"):
        reasons.append("missing_file_id")
    if not row.get("primary_file_name"):
        reasons.append("missing_filename")
    if as_float(row.get("size_mb_original"), 0.0) <= 0:
        reasons.append("missing_size")
    safety_text = " ".join(
        str(row.get(k, ""))
        for k in (
            "name",
            "description_plain",
            "primary_version_name",
            "primary_version_description_plain",
            "primary_version_trainedWords",
            "tags",
            "categories_original",
        )
    ).lower()
    for term in sorted(SAFETY_BLOCK_TERMS):
        if term in safety_text:
            reasons.append(f"safety_block_term_{slug(term)}")
            break
    return reasons


def target_relative_path(row: dict[str, str], family: str) -> str:
    model_type = slug(row.get("type", "model"), "model")
    category = first_category(row)
    filename = row.get("primary_file_name", "").strip()
    if model_type in {"lora", "locon", "dora"}:
        return f"loras/{family}/{category}/{filename}"
    return f"{model_type}/{family}/{category}/{filename}"


def safe_entry(row: dict[str, str], family: str, family_status: str) -> dict[str, Any]:
    size_mb = as_float(row.get("size_mb_original"), 0.0)
    trained_words = row.get("primary_version_trainedWords", "")
    tags = row.get("tags", "")
    return {
        "rank": as_int(row.get("rank")),
        "civitai_model_id": row.get("model_id"),
        "civitai_version_id": row.get("primary_version_id"),
        "civitai_file_id": row.get("primary_file_id"),
        "name": row.get("name"),
        "creator": row.get("creator_username"),
        "model_type": row.get("type"),
        "base_model": row.get("primary_version_baseModel"),
        "compatibility_family": family,
        "family_status": family_status,
        "version_name": row.get("primary_version_name"),
        "filename": row.get("primary_file_name"),
        "size_mb": round(size_mb, 3),
        "size_bytes_estimate": int(round(size_mb * 1024 * 1024)),
        "file_format": row.get("primary_file_format"),
        "hashes": {
            "sha256": row.get("primary_file_hash_SHA256"),
            "auto_v2": row.get("primary_file_hash_AutoV2"),
            "blake3": row.get("primary_file_hash_BLAKE3"),
            "crc32": row.get("primary_file_hash_CRC32"),
        },
        "scan": {
            "virus": row.get("primary_file_virusScanResult"),
            "pickle": row.get("primary_file_pickleScanResult"),
            "scanned_at": row.get("primary_file_scannedAt"),
        },
        "safety": {
            "nsfw": row.get("nsfw"),
            "nsfw_level": row.get("nsfwLevel"),
            "version_nsfw_level": row.get("primary_version_nsfwLevel"),
            "poi": row.get("poi"),
            "minor": row.get("minor"),
            "sfw_only": row.get("sfwOnly"),
        },
        "licensing": {
            "allow_no_credit": row.get("allowNoCredit"),
            "allow_commercial_use": row.get("allowCommercialUse"),
            "allow_derivatives": row.get("allowDerivatives"),
            "allow_different_license": row.get("allowDifferentLicense"),
        },
        "taxonomy": {
            "categories": row.get("categories_original"),
            "tags": tags,
        },
        "prompt_use": {
            "trained_words": trained_words,
        },
        "civitai_url": row.get("civitai_url"),
        "download_url_redacted": True,
        "target_relative_path": target_relative_path(row, family),
        "planned_status": "dry_manifest_only_not_downloaded",
    }


def card_text(batch_id: str, entry: dict[str, Any], report_path: str) -> str:
    hashes = entry["hashes"]
    scan = entry["scan"]
    licensing = entry["licensing"]
    safety = entry["safety"]
    prompt_use = entry["prompt_use"]
    trained_words = prompt_use.get("trained_words") or "n/a"
    return f"""# Model Card: {entry['name']}

## Identity

- Model card id: {batch_id}_model_{entry['civitai_model_id']}_version_{entry['civitai_version_id']}
- Civitai model id: {entry['civitai_model_id']}
- Civitai version id: {entry['civitai_version_id']}
- Civitai file id: {entry['civitai_file_id']}
- Civitai URL: {entry['civitai_url']}
- Creator: {entry['creator']}
- Source CSV rows: PENDING_flux1_sdxl_TOP500_curated.csv rank {entry['rank']}
- Created/updated: {datetime.now(timezone.utc).isoformat()}

## Classification

- Model type: {entry['model_type']}
- Base model: {entry['base_model']}
- Compatibility family: {entry['compatibility_family']}
- Intended ComfyUI folder: /home/ubuntu/ComfyUI/models/{entry['target_relative_path']}
- Intended Main Flow or preset use: planned curated LoRA/preset candidate; not yet runtime-visible
- Taxonomy rows: {entry['taxonomy']['categories']}
- Priority tier: batch0_dry_rank_{entry['rank']}

## File

- Filename: {entry['filename']}
- Size KB:
- Size MB: {entry['size_mb']}
- Expected hashes: SHA256={hashes.get('sha256')}; AutoV2={hashes.get('auto_v2')}; BLAKE3={hashes.get('blake3')}; CRC32={hashes.get('crc32')}
- Verified hashes: not downloaded
- Pickle scan result: {scan.get('pickle')}
- Virus scan result: {scan.get('virus')}
- Scanned at: {scan.get('scanned_at')}
- Download status: planned_dry_manifest_only
- EC2 target path: /home/ubuntu/ComfyUI/models/{entry['target_relative_path']}
- Local binary present: no

## Prompt Use

- Trained words: {trained_words}
- Suggested weight min:
- Suggested weight max:
- Suggested weight text:
- Trigger notes: from CSV trained words only; requires Lane 5 audit before use
- Stacking notes:
- Negative interactions:

## Licensing And Safety

- Availability: Public
- NSFW: {safety.get('nsfw')}
- NSFW level: {safety.get('nsfw_level')}
- POI: {safety.get('poi')}
- Minor flag: {safety.get('minor')}
- Allow commercial use: {licensing.get('allow_commercial_use')}
- Allow derivatives: {licensing.get('allow_derivatives')}
- Allow different licenses: {licensing.get('allow_different_license')}
- Allow no credit: {licensing.get('allow_no_credit')}
- License notes: captured from CSV only
- Rejection or caution notes: adult/NSFW metadata requires downstream safety/QA review

## Evidence

- Batch manifest: {batch_id}.dry_manifest.json
- Download report row: {report_path}
- Hash verification: pending EC2 download/hash verification
- ComfyUI catalog visibility: pending Lane 4
- Load test: pending Lane 4/Lane 5
- Generation test: pending Lane 6/Lane 5
- QA audit: pending Lane 5

## Status

- Ingest status: planned
- Current blockers: no download/hash/catalog/load/generation evidence yet
- Next owner lane: Lane_5 audit before Lane_4 launch; Lane_4 for EC2-only download if approved
- Last updated: {datetime.now(timezone.utc).isoformat()}
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--out-root", type=Path, default=DEFAULT_OUT_ROOT)
    parser.add_argument("--batch-size", type=int, default=20)
    parser.add_argument("--max-gib", type=float, default=10.0)
    parser.add_argument("--timestamp", default=datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S"))
    args = parser.parse_args()

    source = args.source
    out_root = args.out_root
    batch_id = f"{args.timestamp}_top500_batch0_dry"
    manifest_dir = out_root / "Implementation" / "manifests" / "civitai_model_acquisition" / batch_id
    card_dir = manifest_dir / "model_cards"
    evidence_dir = out_root / "Lane_3" / "evidence"
    for d in (manifest_dir, card_dir, evidence_dir):
        d.mkdir(parents=True, exist_ok=True)

    with source.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    selected: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    family_counts: dict[str, int] = {}
    type_counts: dict[str, int] = {}
    planned_bytes = 0
    max_bytes = int(args.max_gib * 1024 * 1024 * 1024)

    for row in sorted(rows, key=lambda r: as_int(r.get("rank"))):
        family, family_status = classify_family(row.get("primary_version_baseModel", ""))
        family_counts[family] = family_counts.get(family, 0) + 1
        type_counts[row.get("type", "unknown")] = type_counts.get(row.get("type", "unknown"), 0) + 1
        reasons = reject_reasons(row, family_status)
        entry = safe_entry(row, family, family_status)
        if reasons:
            skipped.append({"rank": entry["rank"], "model_id": entry["civitai_model_id"], "name": entry["name"], "family": family, "reasons": reasons[:4]})
            continue
        next_bytes = planned_bytes + entry["size_bytes_estimate"]
        if len(selected) >= args.batch_size:
            skipped.append({"rank": entry["rank"], "model_id": entry["civitai_model_id"], "name": entry["name"], "family": family, "reasons": ["batch_count_cap"]})
            continue
        if next_bytes > max_bytes:
            skipped.append({"rank": entry["rank"], "model_id": entry["civitai_model_id"], "name": entry["name"], "family": family, "reasons": ["batch_size_cap"]})
            continue
        selected.append(entry)
        planned_bytes = next_bytes

    manifest_path = manifest_dir / f"{batch_id}.dry_manifest.json"
    report_path = manifest_dir / f"{batch_id}.dry_download_report.md"
    summary_path = manifest_dir / f"{batch_id}.inventory_summary.json"
    evidence_path = evidence_dir / f"{batch_id}_evidence.json"

    card_paths = []
    for entry in selected:
        card_name = f"rank{entry['rank']:04d}_model{entry['civitai_model_id']}_version{entry['civitai_version_id']}.md"
        card_path = card_dir / card_name
        card_path.write_text(card_text(batch_id, entry, str(report_path)), encoding="utf-8")
        entry["model_card_path"] = str(card_path)
        card_paths.append(str(card_path))

    manifest = {
        "schema_version": "1.0",
        "batch_id": batch_id,
        "lane_id": LANE_ID,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_csv": str(source),
        "source_csv_sha256": sha256_file(source),
        "mode": "dry_manifest_only_no_download",
        "selection_policy": {
            "source": "PENDING_flux1_sdxl_TOP500_curated.csv",
            "sort": "rank ascending",
            "eligible_families": ["sdxl", "flux", "z_image"],
            "required_scan": "virus=Success and pickle=Success",
            "required_availability": "Public",
            "excluded_flags": ["minor=True", "poi=True"],
            "safety_block_terms": sorted(SAFETY_BLOCK_TERMS),
            "batch_size_cap": args.batch_size,
            "planned_size_cap_gib": args.max_gib,
        },
        "storage_projection": {
            "planned_file_count": len(selected),
            "planned_total_bytes": planned_bytes,
            "planned_total_gib": round(planned_bytes / (1024 ** 3), 3),
            "ec2_stop_threshold": "Do not start download if projected free space after batch is below 150 GB or 15 percent, whichever is stricter.",
            "ec2_free_space_verified": False,
        },
        "secret_handling": {
            "download_urls_redacted": True,
            "token_variable_name": "CIVITAI_TOKEN",
            "token_value_present": False,
            "token_printed_or_persisted": False,
        },
        "target_roots": {
            "lora": "/home/ubuntu/ComfyUI/models/loras/<family>/<category>/",
        },
        "entries": selected,
        "skipped_preview": skipped[:100],
        "not_a_launch_request": True,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    summary = {
        "source_csv": str(source),
        "source_csv_sha256": manifest["source_csv_sha256"],
        "row_count": len(rows),
        "family_counts": dict(sorted(family_counts.items())),
        "type_counts": dict(sorted(type_counts.items())),
        "selected_count": len(selected),
        "selected_total_gib": manifest["storage_projection"]["planned_total_gib"],
        "selected_family_counts": dict(sorted({e["compatibility_family"]: sum(1 for x in selected if x["compatibility_family"] == e["compatibility_family"]) for e in selected}.items())),
        "skipped_preview_count": len(skipped[:100]),
        "download_urls_redacted": True,
    }
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    rows_md = "\n".join(
        f"| {e['rank']} | {e['civitai_model_id']} | {e['civitai_version_id']} | {e['civitai_file_id']} | {e['name']} | {e['model_type']} | {e['compatibility_family']} | {e['size_mb']} | `{e['target_relative_path']}` | planned | pending | pending | {Path(e['model_card_path']).name} | dry manifest only |"
        for e in selected
    )
    family_rows = "\n".join(
        f"| {family} | lora/locon/dora | `/home/ubuntu/ComfyUI/models/loras/{family}/<category>/` |"
        for family in sorted({e["compatibility_family"] for e in selected})
    )
    report = f"""# Model Download Report: {batch_id}

## Summary

- Batch id: {batch_id}
- Created at: {datetime.now(timezone.utc).isoformat()}
- Owner lanes: Lane_3 planning, Lane_4 EC2 download if later approved, Lane_5 audit
- EC2 instance id: i-0560bf8d143f93bb1
- Source CSV files: {source}
- Row filters: rank ascending; public; SafeTensor; scan success; minor=false; poi=false; family in SDXL/Flux.1/ZImage
- Planned model count: {len(selected)}
- Planned file count: {len(selected)}
- Planned bytes: {planned_bytes}
- Downloaded bytes: 0
- Skipped bytes: 0
- Failed bytes: 0

## Storage Gate

- EC2 volume total: pending Lane 4 preflight
- EC2 free before: pending Lane 4 preflight
- Projected free after: pending Lane 4 preflight
- EC2 free after: not applicable
- Gate result: dry_manifest_only_not_approved_for_download
- Stop threshold: 150 GB free or 15 percent free, whichever is stricter
- Cleanup performed before batch: none by Lane 3

## Secret Handling

- Token source: `C:\\Comfy_UI\\.env` variable name only
- Token printed/logged: no
- Token stored in report/evidence: no
- Token-bearing URLs persisted: no
- Secret-safe method: Lane 4 must inject token at runtime without echoing or persisting it

## Target Layout

| Family | Model type | Target root |
| --- | --- | --- |
{family_rows}

## Per-Model Status

| Rank | Model id | Version id | File id | Name | Type | Family | Size MB | Target path | Status | Hash result | Catalog visible | Card path | Blocker |
| ---: | --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- | --- |
{rows_md}

## Failures And Skips

| Model id | Version id | File id | Reason | Next action |
| --- | --- | --- | --- | --- |
| batch-level | n/a | n/a | no EC2 preflight, no Lane 5 audit, no download approval | Lane 5 audits manifest/cards before Lane 4 launch |

## Evidence

- Download manifest: {manifest_path}
- Hash report: pending EC2 verification
- ComfyUI visibility report: pending Lane 4
- Lane 5 QA report: pending
- EC2 lease record: pending if launched later
- EC2 stopped-state proof: pending if launched later

## Resume Instructions

- Resume command: Lane 4 only after Lane 5 audit and EC2 storage preflight
- Manifest path: {manifest_path}
- Safe retry rules: verify size/hash per file, keep token out of logs, stop on storage threshold
- Stop conditions: projected free space below threshold, failed auth, failed scan/hash, unexpected file type, user/lane stop
"""
    report_path.write_text(report, encoding="utf-8")

    evidence = {
        "schema_version": "1.0",
        "evidence_id": f"lane3-{batch_id}",
        "lane_id": LANE_ID,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "claim": {
            "summary": f"Lane 3 parsed the curated Top500 CSV locally and produced a dry EC2 ingest batch with {len(selected)} planned model-card drafts, no downloads, and redacted download URLs.",
            "status": "provisional",
            "requirement_ids": ["Lane_3.CivitaiTop500DryManifest", "EC2_MODEL_INGESTION_POLICY.InventoryPhase"],
        },
        "inputs": {
            "workflow_path": r"C:\Comfy_UI\Implementation\workflows\ui\WAVE42_MAIN_FLOW_20260702.json",
            "source_csv": str(source),
            "source_csv_sha256": manifest["source_csv_sha256"],
            "settings": manifest["selection_policy"],
        },
        "runtime": {
            "ec2_state_before": "not_checked_by_lane_3",
            "ec2_state_after": "not_changed_by_lane_3",
            "endpoints_checked": [],
            "aws_auth_status": "not_used",
        },
        "models": [
            {
                "name": e["name"],
                "family": e["compatibility_family"],
                "path": f"/home/ubuntu/ComfyUI/models/{e['target_relative_path']}",
                "sha256": e["hashes"].get("sha256") or "",
                "role": "planned_civitai_ingest_candidate",
                "visibility_evidence": "csv_metadata_only_not_downloaded",
                "load_result": "not_downloaded_not_loaded",
            }
            for e in selected
        ],
        "artifacts": [
            {"path": str(manifest_path), "type": "dry_manifest", "description": "No download URLs or token values."},
            {"path": str(report_path), "type": "dry_download_report", "description": "Batch report template filled for planned state."},
            {"path": str(summary_path), "type": "inventory_summary", "description": "Top500 family/type counts and selected batch summary."},
            {"path": str(card_dir), "type": "model_card_directory", "description": f"{len(selected)} model-card drafts."},
        ],
        "qa": {
            "verdict": "provisional",
            "checks": [
                {"name": "local_csv_only", "result": "pass", "notes": "Read local CSV only; no model download commands issued."},
                {"name": "download_urls_redacted", "result": "pass", "notes": "Manifest/report/cards omit primary_version_downloadUrl and primary_file_downloadUrl values."},
                {"name": "scan_filter", "result": "pass", "notes": "Selected entries require virus and pickle scan Success in CSV metadata."},
                {"name": "runtime_visibility", "result": "not_applicable", "notes": "Dry manifest only; no ComfyUI runtime visibility claim."},
                {"name": "lane5_audit", "result": "provisional", "notes": "Lane 5 audit required before any Lane 4 EC2 launch request."},
            ],
            "failure_reasons": ["CSV metadata does not prove downloaded, hash-verified, catalog-visible, load-tested, or generation-tested status."],
        },
        "tracker_mapping": {
            "proves_rows": ["Top500 curated CSV can be parsed into a bounded dry EC2 ingest manifest with model-card drafts."],
            "does_not_prove_rows": ["Any model is downloaded, hash-verified, catalog-visible, load-tested, generation-tested, or safe for tracker promotion."],
            "promotion_decision": "needs_more_evidence",
        },
        "blockers": [
            {
                "category": "dry_manifest_only",
                "description": "No EC2 storage preflight, Lane 5 audit, or download/hash/catalog evidence exists for this batch.",
                "next_action": "Lane 5 should audit this dry manifest and model cards; Lane 4 should only run EC2 downloads after audit plus storage preflight.",
            }
        ],
    }
    evidence_path.write_text(json.dumps(evidence, indent=2, ensure_ascii=False), encoding="utf-8")

    print(json.dumps({
        "batch_id": batch_id,
        "selected_count": len(selected),
        "planned_total_gib": manifest["storage_projection"]["planned_total_gib"],
        "manifest": str(manifest_path),
        "report": str(report_path),
        "summary": str(summary_path),
        "evidence": str(evidence_path),
        "model_cards": len(card_paths),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
