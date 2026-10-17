#!/usr/bin/env python3
"""Small guardrail validator for Renomedy Instagram content JSON."""
import json
import sys
from pathlib import Path

REQUIRED = ["id", "status", "format", "pillar", "working_title", "takeaway", "cta"]
ALLOWED_FORMATS = {"carousel", "reel", "story", "founder_post"}
ALLOWED_PILLARS = {"clarity", "continuity", "coordination", "trust", "build_in_public"}

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_content.py path/to/post.json")
        return 2
    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERROR: Could not read valid JSON: {exc}")
        return 2

    errors, warnings = [], []
    for field in REQUIRED:
        if not data.get(field):
            errors.append(f"Missing required field: {field}")
    if data.get("format") and data["format"] not in ALLOWED_FORMATS:
        errors.append(f"Unknown format: {data['format']}")
    if data.get("pillar") and data["pillar"] not in ALLOWED_PILLARS:
        errors.append(f"Unknown pillar: {data['pillar']}")
    if data.get("asks_for_public_health_details", False):
        errors.append("Do not ask for personal health details in public.")
    if not data.get("human_approved", False):
        warnings.append("Human approval is pending; do not publish.")
    for i, claim in enumerate(data.get("claims", []), start=1):
        if not claim.get("verified", False):
            warnings.append(f"Claim {i} is not verified.")
        if claim.get("review_required", False):
            warnings.append(f"Claim {i} requires qualified human review.")
        if not claim.get("source_url"):
            warnings.append(f"Claim {i} has no source URL.")

    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARNING: {item}")
    if errors:
        return 1
    print("Structure looks valid. This is not a medical/legal review or publishing approval.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
