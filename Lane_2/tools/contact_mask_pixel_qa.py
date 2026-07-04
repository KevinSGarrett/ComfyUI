#!/usr/bin/env python3
"""Pixel-level QA for Wave42 strict body-contact mask assets.

This is a local, read-only analysis tool for Lane 2. It does not execute
ComfyUI and does not make visual-quality claims from masks alone.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image, ImageFilter


DEFAULT_WORKFLOW = Path(r"C:\Comfy_UI\Implementation\workflows\ui\WAVE42_MAIN_FLOW_20260702.json")
DEFAULT_SLOT_ROOT = Path(r"C:\Comfy_UI\Input_References\main_flow\body_contact_slots")
DEFAULT_OUTPUT_ROOT = Path(r"C:\Comfy_UI_Lora\5_session_worktrees\Lane_2\Lane_2\contact_mask_pixel_qa")

MASKS = {
    "character_a_body": "character_a_body_mask.png",
    "character_a_receiver_breast": "character_a_receiver_breast_mask.png",
    "character_a_receiver_butt": "character_a_receiver_butt_mask.png",
    "character_a_left_hand": "character_a_left_hand_mask.png",
    "character_a_right_hand": "character_a_right_hand_mask.png",
    "character_b_left_hand": "character_b_left_hand_mask.png",
    "character_b_right_hand": "character_b_right_hand_mask.png",
    "character_b_actor_hand": "character_b_actor_hand_mask.png",
    "character_b_body": "character_b_body_mask.png",
    "hand_contact": "hand_contact_mask.png",
    "contact_zone": "contact_zone_mask.png",
    "occlusion_order": "interaction_occlusion_order_mask.png",
    "pressure": "soft_body_pressure_map.png",
    "indentation": "soft_body_indentation_mask.png",
    "contact_shadow": "contact_shadow_mask.png",
}

IMAGES = {
    "body_contact_base": "body_contact_base_input.png",
    "contact_pose_reference": "contact_pose_reference.png",
    "depth_reference": "soft_body_contact_depth_reference.png",
    "normal_reference": "soft_body_normal_reference.png",
}

EDGE_DEFINITIONS = [
    {
        "edge_id": "fallback_actor_hand_to_receiver_butt",
        "actor_mask": "character_b_actor_hand",
        "receiver_mask": "character_a_receiver_butt",
        "status_rule": "fallback_actor_hand_only",
    },
    {
        "edge_id": "fallback_actor_hand_to_receiver_breast",
        "actor_mask": "character_b_actor_hand",
        "receiver_mask": "character_a_receiver_breast",
        "status_rule": "fallback_actor_hand_only",
    },
    {
        "edge_id": "B.left_to_A.left_breast_side_push",
        "actor_mask": "character_b_left_hand",
        "receiver_mask": "character_a_receiver_breast",
        "status_rule": "per_hand_split_required",
    },
    {
        "edge_id": "B.right_to_A.right_breast_side_push",
        "actor_mask": "character_b_right_hand",
        "receiver_mask": "character_a_receiver_breast",
        "status_rule": "per_hand_split_required",
    },
    {
        "edge_id": "B.left_to_A.left_butt_squeeze",
        "actor_mask": "character_b_left_hand",
        "receiver_mask": "character_a_receiver_butt",
        "status_rule": "per_hand_split_required",
    },
    {
        "edge_id": "B.right_to_A.right_butt_squeeze",
        "actor_mask": "character_b_right_hand",
        "receiver_mask": "character_a_receiver_butt",
        "status_rule": "per_hand_split_required",
    },
]


def sha256_path(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def load_gray(path: Path) -> np.ndarray:
    return np.array(Image.open(path).convert("L"))


def load_rgb(path: Path) -> np.ndarray:
    return np.array(Image.open(path).convert("RGB"))


def bbox(mask: np.ndarray) -> list[int] | None:
    ys, xs = np.where(mask)
    if len(xs) == 0:
        return None
    return [int(xs.min()), int(ys.min()), int(xs.max() + 1), int(ys.max() + 1)]


def centroid(mask: np.ndarray) -> list[float] | None:
    ys, xs = np.where(mask)
    if len(xs) == 0:
        return None
    return [round(float(xs.mean()), 3), round(float(ys.mean()), 3)]


def connected_components(mask: np.ndarray, min_area: int = 8) -> list[dict[str, Any]]:
    visited = np.zeros(mask.shape, dtype=bool)
    components: list[dict[str, Any]] = []
    height, width = mask.shape
    ys, xs = np.where(mask)
    for start_y, start_x in zip(ys.tolist(), xs.tolist()):
        if visited[start_y, start_x]:
            continue
        q: deque[tuple[int, int]] = deque([(start_y, start_x)])
        visited[start_y, start_x] = True
        pixels: list[tuple[int, int]] = []
        while q:
            y, x = q.popleft()
            pixels.append((y, x))
            for ny in (y - 1, y, y + 1):
                for nx in (x - 1, x, x + 1):
                    if ny == y and nx == x:
                        continue
                    if 0 <= ny < height and 0 <= nx < width and mask[ny, nx] and not visited[ny, nx]:
                        visited[ny, nx] = True
                        q.append((ny, nx))
        if len(pixels) >= min_area:
            comp_mask = np.zeros(mask.shape, dtype=bool)
            for py, px in pixels:
                comp_mask[py, px] = True
            components.append(
                {
                    "area": int(len(pixels)),
                    "bbox": bbox(comp_mask),
                    "centroid": centroid(comp_mask),
                }
            )
    components.sort(key=lambda c: c["area"], reverse=True)
    return components


def dilate(mask: np.ndarray, radius: int) -> np.ndarray:
    if radius <= 0:
        return mask
    image = Image.fromarray((mask.astype(np.uint8) * 255), mode="L")
    return np.array(image.filter(ImageFilter.MaxFilter(radius * 2 + 1))) > 0


def ratio(numerator: int, denominator: int) -> float | None:
    if denominator == 0:
        return None
    return round(numerator / denominator, 8)


def mask_metrics(path: Path, gray: np.ndarray) -> dict[str, Any]:
    mask = gray > 0
    pixel_count = int(mask.size)
    area = int(mask.sum())
    components = connected_components(mask)
    return {
        "path": str(path),
        "exists": path.exists(),
        "size_bytes": path.stat().st_size,
        "sha256": sha256_path(path),
        "width": int(gray.shape[1]),
        "height": int(gray.shape[0]),
        "nonzero_pixels": area,
        "pixel_count": pixel_count,
        "nonzero_ratio": ratio(area, pixel_count),
        "luma_min": int(gray.min()),
        "luma_max": int(gray.max()),
        "bbox": bbox(mask),
        "centroid": centroid(mask),
        "connected_component_count": len(components),
        "largest_components": components[:8],
    }


def image_metrics(path: Path, rgb: np.ndarray) -> dict[str, Any]:
    gray = np.array(Image.fromarray(rgb).convert("L"))
    pixel_count = int(gray.size)
    nonzero = int((gray > 0).sum())
    return {
        "path": str(path),
        "exists": path.exists(),
        "size_bytes": path.stat().st_size,
        "sha256": sha256_path(path),
        "width": int(rgb.shape[1]),
        "height": int(rgb.shape[0]),
        "mode": "RGB",
        "luma_min": int(gray.min()),
        "luma_max": int(gray.max()),
        "luma_mean": round(float(gray.mean()), 6),
        "luma_std": round(float(gray.std()), 6),
        "nonzero_pixels": nonzero,
        "pixel_count": pixel_count,
        "nonzero_ratio": ratio(nonzero, pixel_count),
    }


def mean_luma_in(gray: np.ndarray, mask: np.ndarray) -> float | None:
    if not mask.any():
        return None
    return round(float(gray[mask].mean()), 6)


def edge_metrics(edge: dict[str, Any], masks: dict[str, np.ndarray], depth: np.ndarray) -> dict[str, Any]:
    actor = masks[edge["actor_mask"]]
    receiver = masks[edge["receiver_mask"]]
    contact = masks["contact_zone"]
    pressure = masks["pressure"]
    indentation = masks["indentation"]
    shadow = masks["contact_shadow"]
    occlusion = masks["occlusion_order"]
    body = masks["character_a_body"]

    actor_area = int(actor.sum())
    receiver_area = int(receiver.sum())
    contact_area = int(contact.sum())
    pressure_area = int(pressure.sum())
    indentation_area = int(indentation.sum())
    union_for_contact = dilate(actor | receiver | shadow, 6)

    actor_contact = int((actor & contact).sum())
    receiver_contact = int((receiver & contact).sum())
    contact_contained = int((contact & union_for_contact).sum())
    pressure_in_receiver = int((pressure & body & receiver).sum())
    indentation_in_receiver = int((indentation & body & receiver).sum())
    occlusion_on_actor = int((occlusion & actor).sum())

    if actor_area == 0:
        verdict = "blocked"
        reason = "actor mask is zero/off"
    elif contact_area == 0 or receiver_area == 0:
        verdict = "blocked"
        reason = "contact or receiver mask is zero/off"
    elif ratio(actor_contact, actor_area) is not None and ratio(actor_contact, actor_area) >= 0.06:
        verdict = "provisional_pass_for_mask_geometry"
        reason = "actor hand has required overlap with contact zone; runtime visual/depth interpretation still unproven"
    else:
        verdict = "fail"
        reason = "actor hand/contact overlap is below threshold"

    return {
        "edge_id": edge["edge_id"],
        "actor_mask": edge["actor_mask"],
        "receiver_mask": edge["receiver_mask"],
        "status_rule": edge["status_rule"],
        "verdict": verdict,
        "reason": reason,
        "areas": {
            "actor": actor_area,
            "receiver": receiver_area,
            "contact_zone": contact_area,
            "pressure": pressure_area,
            "indentation": indentation_area,
        },
        "ratios": {
            "actor_contact_overlap_over_actor": ratio(actor_contact, actor_area),
            "actor_contact_overlap_over_contact": ratio(actor_contact, contact_area),
            "receiver_contact_overlap_over_contact": ratio(receiver_contact, contact_area),
            "contact_zone_contained_by_dilated_actor_receiver_shadow": ratio(contact_contained, contact_area),
            "pressure_inside_character_a_body_and_receiver": ratio(pressure_in_receiver, pressure_area),
            "indentation_inside_character_a_body_and_receiver": ratio(indentation_in_receiver, indentation_area),
            "occlusion_overlap_over_actor": ratio(occlusion_on_actor, actor_area),
        },
        "depth_luma": {
            "actor_mean": mean_luma_in(depth, actor),
            "receiver_mean": mean_luma_in(depth, receiver),
            "contact_mean": mean_luma_in(depth, contact),
            "pressure_mean": mean_luma_in(depth, pressure),
            "note": "Depth luma convention is not interpreted as absolute foreground/background without runtime model context.",
        },
    }


def audit(workflow_path: Path, slot_root: Path, run_id: str) -> dict[str, Any]:
    masks_gray: dict[str, np.ndarray] = {}
    masks_bool: dict[str, np.ndarray] = {}
    mask_records: dict[str, Any] = {}
    for key, name in MASKS.items():
        path = slot_root / name
        gray = load_gray(path)
        masks_gray[key] = gray
        masks_bool[key] = gray > 0
        mask_records[key] = mask_metrics(path, gray)

    image_records: dict[str, Any] = {}
    for key, name in IMAGES.items():
        path = slot_root / name
        image_records[key] = image_metrics(path, load_rgb(path))

    depth = masks_gray.get("depth_reference")
    if depth is None:
        depth = load_gray(slot_root / IMAGES["depth_reference"])

    edges = [edge_metrics(edge, masks_bool, depth) for edge in EDGE_DEFINITIONS]

    hand_mask = masks_bool["character_b_actor_hand"]
    hand_components = connected_components(hand_mask, min_area=8)
    per_hand_split_feasibility = {
        "combined_actor_hand_component_count": len(hand_components),
        "combined_actor_hand_components": hand_components,
        "can_truthfully_split_into_left_right_from_current_mask_only": False,
        "reason": "The active combined actor-hand mask has no reliable Character A/B left/right labels; zero/off per-hand placeholders avoid inventing geometry.",
    }

    blockers: list[dict[str, str]] = []
    if any(mask_records[key]["nonzero_pixels"] == 0 for key in ("character_b_left_hand", "character_b_right_hand", "character_a_left_hand", "character_a_right_hand")):
        blockers.append(
            {
                "category": "per_hand_split_masks",
                "description": "Nodes 1051-1054 resolve to files but the masks are zero/off placeholders.",
                "next_action": "Provide same-scene nonzero left/right hand split masks before accepting per-hand contact-pair QA.",
            }
        )
    if mask_records["character_b_body"]["nonzero_pixels"] == 0:
        blockers.append(
            {
                "category": "actor_body_segmentation",
                "description": "character_b_body_mask.png remains zero/off and cannot support full actor-body collision QA.",
                "next_action": "Provide a trustworthy same-scene actor body segmentation source when full actor-body collision QA is required.",
            }
        )

    provisional_pass_edges = [e["edge_id"] for e in edges if e["verdict"] == "provisional_pass_for_mask_geometry"]
    blocked_edges = [e["edge_id"] for e in edges if e["verdict"] == "blocked"]

    return {
        "schema_version": "1.0",
        "artifact_id": f"lane2_contact_mask_pixel_qa_{run_id}",
        "lane_id": "Lane_2",
        "created_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "workflow": {
            "path": str(workflow_path),
            "sha256": sha256_path(workflow_path),
        },
        "slot_root": str(slot_root),
        "summary": {
            "mask_count": len(mask_records),
            "image_reference_count": len(image_records),
            "contact_edges_checked": len(edges),
            "provisional_pass_edges": provisional_pass_edges,
            "blocked_edges": blocked_edges,
            "zero_mask_ids": [key for key, value in mask_records.items() if value["nonzero_pixels"] == 0],
        },
        "mask_records": mask_records,
        "image_records": image_records,
        "per_hand_split_feasibility": per_hand_split_feasibility,
        "contact_edge_metrics": edges,
        "collision_and_deformation_checks": {
            "fallback_actor_hand_overlap_threshold": "actor_contact_overlap_over_actor >= 0.06",
            "contact_zone_containment_target": ">= 0.92 inside dilated(actor_hand, receiver_surface, contact_shadow)",
            "pressure_indent_receiver_target": ">= 0.97 inside character_a_body and selected receiver surface",
            "runtime_visual_required": True,
        },
        "blockers": blockers,
        "limitations": [
            "This is a local mask/depth pixel QA pass only.",
            "No live ComfyUI execution was performed.",
            "No final generated output or hand anatomy was visually accepted.",
            "Depth luma is summarized but not interpreted as absolute foreground/background without runtime context.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workflow", type=Path, default=DEFAULT_WORKFLOW)
    parser.add_argument("--slot-root", type=Path, default=DEFAULT_SLOT_ROOT)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--run-id", default=datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S"))
    args = parser.parse_args()

    artifact = audit(args.workflow, args.slot_root, args.run_id)
    output_dir = args.output_root / args.run_id
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"lane2_contact_mask_pixel_qa_{args.run_id}.json"
    with output_path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(artifact, f, indent=2)
        f.write("\n")

    print(json.dumps({"output_path": str(output_path), "summary": artifact["summary"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
