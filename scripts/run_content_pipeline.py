#!/usr/bin/env python3
"""Run the approval-first content pipeline: draft -> AI review -> asset generation.

Requires RENOMEDY_LLM_API_KEY and RENOMEDY_LLM_MODEL. Does not publish or approve content.
"""
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(command):
    print("+", " ".join(str(x) for x in command), flush=True)
    result = subprocess.run(command, cwd=ROOT)
    if result.returncode:
        raise RuntimeError(f"Pipeline stage failed with exit code {result.returncode}: {command[1]}")
    

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("brief", help="Path to a content brief JSON record")
    parser.add_argument("--assets-root", default="content/assets")
    parser.add_argument("--drafts-root", default="content/drafts")
    parser.add_argument("--reviewed-root", default="content/reviewed")
    args = parser.parse_args()

    if not os.getenv("RENOMEDY_LLM_API_KEY") or not os.getenv("RENOMEDY_LLM_MODEL"):
        print("ERROR: Set RENOMEDY_LLM_API_KEY and RENOMEDY_LLM_MODEL. No API call was made.", file=sys.stderr)
        return 2
    try:
        brief_path = Path(args.brief)
        brief = json.loads(brief_path.read_text(encoding="utf-8"))
        base_id = str(brief.get("id", "content"))
        # Match generate_draft.py's stable slug logic without importing CLI behavior.
        import re
        slug = re.sub(r"[^a-z0-9]+", "-", (base_id + "-ai-draft").lower()).strip("-")[:60].strip("-") or "content-draft"
        draft_path = Path(args.drafts_root) / f"{slug}.json"
        reviewed_id = re.sub(r"[^a-z0-9]+", "-", (slug + "-reviewed").lower()).strip("-")[:50]
        reviewed_path = Path(args.reviewed_root) / f"{reviewed_id}.json"

        run([sys.executable, "scripts/generate_draft.py", str(brief_path), "--output-dir", args.drafts_root])
        run([sys.executable, "scripts/review_draft.py", str(draft_path), "--output-dir", args.reviewed_root])

        if not reviewed_path.exists():
            raise RuntimeError(f"Review stage did not create expected record: {reviewed_path}")
        reviewed = json.loads(reviewed_path.read_text(encoding="utf-8"))
        if reviewed.get("status") != "awaiting_human_approval":
            print(json.dumps({
                "status": reviewed.get("status"),
                "review_record": str(reviewed_path),
                "assets_generated": False,
                "next_step": "Resolve review findings, regenerate, and review again."
            }, indent=2))
            return 1

        run([sys.executable, "scripts/generate_assets.py", str(reviewed_path), "--output-root", args.assets_root])
        asset_dir = Path(args.assets_root) / re.sub(r"[^a-z0-9]+", "-", str(reviewed.get("id", "content")).lower()).strip("-")[:64]
        manifest_path = asset_dir / "asset-manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        result = {
            "status": "awaiting_human_approval",
            "review_record": str(reviewed_path),
            "asset_manifest": str(manifest_path),
            "asset_count": len(manifest.get("assets", [])),
            "assets_status": manifest.get("status"),
            "human_approved": False,
            "published": False
        }
        print(json.dumps(result, indent=2))
        if manifest.get("status") == "assets_generated_video_incomplete":
            print("NEXT: supply and verify the finished MP4 before the package can be considered complete.")
        else:
            print("NEXT: human must inspect the assets, approve the package, then publish manually.")
        return 0
    except (OSError, json.JSONDecodeError, RuntimeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
