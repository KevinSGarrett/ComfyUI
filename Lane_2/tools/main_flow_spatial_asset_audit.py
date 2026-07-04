#!/usr/bin/env python3
"""Audit Main Flow LoadImage/LoadImageMask spatial assets for Lane 2.

The script is intentionally read-only for the workflow and input assets. It
writes a JSON audit artifact with dimensions, hashes, and mask occupancy for
Main Flow-facing spatial/control references.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from PIL import Image, ImageStat


DEFAULT_WORKFLOW = Path(r"C:\Comfy_UI\Implementation\workflows\ui\WAVE42_MAIN_FLOW_20260702.json")
DEFAULT_INPUT_ROOT = Path(r"C:\Comfy_UI\Input_References")
DEFAULT_OUTPUT_ROOT = Path(r"C:\Comfy_UI_Lora\5_session_worktrees\Lane_2\Lane_2\main_flow_spatial_asset_audit")

SPATIAL_TYPES = {
    "LoadImage",
    "LoadImageMask",
    "SolidMask",
    "MaskComposite",
    "MaskToImage",
    "ControlNetLoader",
    "ControlNetApplyAdvanced",
    "IPAdapterUnifiedLoader",
    "IPAdapter",
}

BODY_CONTACT_NODE_IDS = set(range(999, 1018)) | set(range(1051, 1063)) | set(range(1067, 1071))
EDGE_QA_NODE_IDS = set(range(1075, 1094))
STRICT_HAND_NODE_IDS = set(range(972, 986))
ACTIVE_REFERENCE_NODE_IDS = {80, 81, 111, 121}
PER_HAND_NODE_IDS = {1051, 1052, 1053, 1054}
DEPTH_NORMAL_OCCLUSION_NODE_IDS = {1001, 1013, 1014, 1015, 1016, 1017}


def sha256_path(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def classify_path(relative_path: str) -> str:
    normalized = relative_path.replace("\\", "/")
    if "/body_contact_slots/" in f"/{normalized}":
        return "body_contact_slots"
    if "/multi_character_slots/" in f"/{normalized}":
        return "multi_character_slots"
    if "/multi_character_interaction_slots/" in f"/{normalized}":
        return "multi_character_interaction_slots"
    if "/body_part_reference_slots/" in f"/{normalized}":
        return "body_part_reference_slots"
    if "/category_reference_slots/" in f"/{normalized}":
        return "category_reference_slots"
    if normalized.endswith("strict_hand_detail_input.png"):
        return "strict_hand_reference"
    return "other_input_reference"


def node_group(node_id: int) -> str:
    if node_id in BODY_CONTACT_NODE_IDS:
        return "strict_body_contact"
    if node_id in EDGE_QA_NODE_IDS:
        return "strict_body_contact_edge_qa"
    if node_id in STRICT_HAND_NODE_IDS:
        return "strict_hand"
    if node_id in ACTIVE_REFERENCE_NODE_IDS:
        return "active_reference_route"
    return "reference_or_support"


def resolve_input_path(input_root: Path, widget_value: Any) -> Path | None:
    if not isinstance(widget_value, str) or not widget_value:
        return None
    candidate = Path(widget_value)
    if candidate.is_absolute():
        return candidate
    return input_root / candidate


def image_metrics(path: Path, is_mask: bool) -> dict[str, Any]:
    with Image.open(path) as img:
        record: dict[str, Any] = {
            "width": img.width,
            "height": img.height,
            "mode": img.mode,
            "format": img.format,
        }
        gray = img.convert("L")
        stat = ImageStat.Stat(gray)
        extrema = gray.getextrema()
        histogram = gray.histogram()
        pixel_count = gray.width * gray.height
        zero_count = histogram[0] if histogram else 0
        nonzero_count = pixel_count - zero_count
        record.update(
            {
                "luma_min": int(extrema[0]),
                "luma_max": int(extrema[1]),
                "luma_mean": float(stat.mean[0]),
                "nonzero_pixels": int(nonzero_count),
                "pixel_count": int(pixel_count),
                "nonzero_ratio": round(nonzero_count / pixel_count, 8) if pixel_count else 0.0,
            }
        )
        if is_mask:
            record["mask_state"] = "nonzero" if nonzero_count > 0 else "zero"
        else:
            record["image_state"] = "nonzero_luma" if nonzero_count > 0 else "zero_luma"
        return record


def load_nodes(workflow_path: Path) -> list[dict[str, Any]]:
    with workflow_path.open("r", encoding="utf-8") as f:
        workflow = json.load(f)
    nodes = workflow.get("nodes", [])
    if not isinstance(nodes, list):
        raise ValueError("Workflow JSON does not contain a list at key 'nodes'.")
    return nodes


def audit(workflow_path: Path, input_root: Path, output_root: Path, run_id: str) -> dict[str, Any]:
    nodes = load_nodes(workflow_path)
    workflow_hash = sha256_path(workflow_path)
    artifact_records: list[dict[str, Any]] = []
    controlnet_requirements: list[dict[str, Any]] = []
    mask_composites: list[dict[str, Any]] = []
    previews: list[dict[str, Any]] = []

    for node in nodes:
        node_id = int(node.get("id"))
        node_type = str(node.get("type") or node.get("class_type") or "")
        title = str(node.get("title") or "")
        widgets = node.get("widgets_values") or []
        if node_type not in SPATIAL_TYPES and "Mask" not in node_type and "ControlNet" not in node_type:
            continue

        base = {
            "node_id": node_id,
            "node_type": node_type,
            "title": title,
            "group": node_group(node_id),
            "widgets": widgets,
        }

        if node_type in {"LoadImage", "LoadImageMask"}:
            relative = widgets[0] if widgets else None
            resolved = resolve_input_path(input_root, relative)
            is_mask = node_type == "LoadImageMask"
            record = {
                **base,
                "relative_path": relative,
                "resolved_path": str(resolved) if resolved else None,
                "asset_group": classify_path(relative) if isinstance(relative, str) else "unknown",
                "exists": bool(resolved and resolved.exists()),
                "is_mask": is_mask,
            }
            if resolved and resolved.exists():
                record["size_bytes"] = resolved.stat().st_size
                record["sha256"] = sha256_path(resolved)
                try:
                    record["image_metrics"] = image_metrics(resolved, is_mask=is_mask)
                except Exception as exc:  # pragma: no cover - evidence should record bad assets too.
                    record["image_error"] = f"{type(exc).__name__}: {exc}"
            artifact_records.append(record)
        elif node_type == "ControlNetLoader":
            controlnet_requirements.append(
                {
                    **base,
                    "model_name": widgets[0] if widgets else None,
                    "visibility_status": "not_validated_by_lane_2",
                    "next_owner": "Lane_3_or_Lane_4",
                }
            )
        elif node_type == "MaskComposite":
            mask_composites.append(base)
        elif node_type == "MaskToImage":
            previews.append(base)

    load_image_count = sum(1 for r in artifact_records if r["node_type"] == "LoadImage")
    load_mask_count = sum(1 for r in artifact_records if r["node_type"] == "LoadImageMask")
    missing_assets = [r for r in artifact_records if not r.get("exists")]
    zero_masks = [
        r
        for r in artifact_records
        if r.get("is_mask") and (r.get("image_metrics") or {}).get("mask_state") == "zero"
    ]
    per_hand_masks = [r for r in artifact_records if r["node_id"] in PER_HAND_NODE_IDS]
    body_contact_inputs = [
        r for r in artifact_records if r["group"] == "strict_body_contact" and r["node_type"] in {"LoadImage", "LoadImageMask"}
    ]
    depth_normal_occlusion = [r for r in artifact_records if r["node_id"] in DEPTH_NORMAL_OCCLUSION_NODE_IDS]

    actionable_findings: list[dict[str, str]] = []
    for record in missing_assets:
        actionable_findings.append(
            {
                "severity": "blocked",
                "node_id": str(record["node_id"]),
                "finding": f"Missing input asset: {record.get('relative_path')}",
                "next_action": "Lane 1 should rewire the node or request/provide the missing input asset.",
            }
        )
    for record in zero_masks:
        if record["group"] == "strict_body_contact":
            next_action = "Lane 1 should choose graph semantics or request/provide a trustworthy nonzero mask source."
        else:
            next_action = "Lane 2 should determine whether this zero mask is intentional placeholder or an asset blocker."
        actionable_findings.append(
            {
                "severity": "blocked" if record["group"] == "strict_body_contact" else "provisional",
                "node_id": str(record["node_id"]),
                "finding": f"Zero-valued mask: {record.get('relative_path')}",
                "next_action": next_action,
            }
        )

    return {
        "schema_version": "1.0",
        "artifact_id": f"lane2_main_flow_spatial_asset_audit_{run_id}",
        "lane_id": "Lane_2",
        "created_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "workflow": {
            "path": str(workflow_path),
            "sha256": workflow_hash,
            "node_count": len(nodes),
        },
        "input_root": str(input_root),
        "summary": {
            "spatial_asset_nodes": len(artifact_records),
            "load_image_nodes": load_image_count,
            "load_image_mask_nodes": load_mask_count,
            "missing_assets": len(missing_assets),
            "zero_masks": len(zero_masks),
            "per_hand_masks_checked": len(per_hand_masks),
            "body_contact_input_nodes_checked": len(body_contact_inputs),
            "controlnet_requirements": len(controlnet_requirements),
            "mask_composites": len(mask_composites),
            "mask_previews": len(previews),
        },
        "actionable_findings": actionable_findings,
        "per_hand_masks": per_hand_masks,
        "body_contact_inputs": body_contact_inputs,
        "depth_normal_occlusion_requirements": depth_normal_occlusion,
        "all_load_image_assets": artifact_records,
        "controlnet_requirements": controlnet_requirements,
        "mask_composites": mask_composites,
        "mask_previews": previews,
        "limitations": [
            "This audit validates local workflow references and image/mask metadata only.",
            "It does not perform live ComfyUI runtime execution.",
            "It does not visually approve generated hands, contact, collision, or deformation quality.",
            "ControlNet model file visibility is listed as a requirement but not validated by Lane 2.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workflow", type=Path, default=DEFAULT_WORKFLOW)
    parser.add_argument("--input-root", type=Path, default=DEFAULT_INPUT_ROOT)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--run-id", default=datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S"))
    args = parser.parse_args()

    output_dir = args.output_root / args.run_id
    output_dir.mkdir(parents=True, exist_ok=True)
    artifact = audit(args.workflow, args.input_root, output_dir, args.run_id)
    output_path = output_dir / f"lane2_main_flow_spatial_asset_audit_{args.run_id}.json"
    with output_path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(artifact, f, indent=2)
        f.write("\n")

    print(json.dumps({"output_path": str(output_path), "summary": artifact["summary"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
