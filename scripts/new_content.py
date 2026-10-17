#!/usr/bin/env python3
"""Create a safe, schema-aligned starter record for a Renomedy content idea."""
import argparse
import json
import re
from pathlib import Path

FORMATS = {"carousel", "reel", "story", "founder_post"}
PILLARS = {"clarity", "continuity", "coordination", "trust", "build_in_public"}


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug[:60].strip("-") or "content-idea"


def create_record(title: str, format_name: str, pillar: str, audience: str,
                  takeaway: str, cta: str) -> dict:
    if format_name not in FORMATS:
        raise ValueError(f"format must be one of: {', '.join(sorted(FORMATS))}")
    if pillar not in PILLARS:
        raise ValueError(f"pillar must be one of: {', '.join(sorted(PILLARS))}")
    if not title.strip() or not takeaway.strip() or not cta.strip():
        raise ValueError("title, takeaway, and CTA must not be empty")

    return {
        "id": slugify(title),
        "status": "idea",
        "format": format_name,
        "pillar": pillar,
        "working_title": title.strip(),
        "audience_hypothesis": audience.strip(),
        "takeaway": takeaway.strip(),
        "cta": cta.strip(),
        "claims": [],
        "product_features_mentioned": [],
        "asks_for_public_health_details": False,
        "human_approved": False
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--title", required=True, help="Working title for the post")
    parser.add_argument("--format", dest="format_name", choices=sorted(FORMATS), required=True)
    parser.add_argument("--pillar", choices=sorted(PILLARS), required=True)
    parser.add_argument("--audience", default="", help="Audience hypothesis, not a verified segment")
    parser.add_argument("--takeaway", required=True)
    parser.add_argument("--cta", required=True)
    parser.add_argument("--output-dir", default="content/drafts")
    args = parser.parse_args()

    try:
        record = create_record(args.title, args.format_name, args.pillar,
                               args.audience, args.takeaway, args.cta)
    except ValueError as exc:
        parser.error(str(exc))

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{record['id']}.json"
    if output_path.exists():
        print(f"ERROR: {output_path} already exists; choose a different title or output directory.")
        return 1

    output_path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Created {output_path}")
    print("Status is 'idea'; human approval is false. This record is not ready to publish.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
