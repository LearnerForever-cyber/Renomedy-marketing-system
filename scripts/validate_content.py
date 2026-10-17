#!/usr/bin/env python3
"""Schema and safety-gate validator for Renomedy content records.

This tool checks record structure and workflow guardrails. It is not a medical,
legal, privacy, or brand review, and a passing result never grants publish approval.
"""
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

SCHEMA_PATH = Path(__file__).resolve().parents[1] / "content" / "content-schema.json"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_record(data: Any, schema: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    validator = Draft202012Validator(schema)
    for issue in sorted(validator.iter_errors(data), key=lambda err: list(map(str, err.absolute_path))):
        location = ".".join(str(part) for part in issue.absolute_path) or "record"
        errors.append(f"Schema error at {location}: {issue.message}")

    if not isinstance(data, dict):
        return errors, warnings

    if data.get("asks_for_public_health_details", False):
        errors.append("Do not ask for personal health details in public.")

    status = data.get("status")
    if status in {"approved", "published", "measured"} and not data.get("human_approved", False):
        errors.append(f"Status '{status}' requires human_approved=true.")
    if status == "published" and not data.get("published_url"):
        errors.append("Published records must include published_url.")

    if not data.get("human_approved", False):
        warnings.append("Human approval is pending; do not publish.")

    claims = data.get("claims", [])
    if isinstance(claims, list):
        for i, claim in enumerate(claims, start=1):
            if not isinstance(claim, dict):
                continue
            if not claim.get("verified", False):
                warnings.append(f"Claim {i} is not verified.")
            if claim.get("review_required", False):
                warnings.append(f"Claim {i} requires qualified human review.")
            if not claim.get("source_url"):
                warnings.append(f"Claim {i} has no source URL.")

    return errors, warnings


def collect_paths(arguments: list[str]) -> list[Path]:
    paths: list[Path] = []
    for argument in arguments:
        path = Path(argument)
        if path.is_dir():
            paths.extend(sorted(item for item in path.rglob("*.json") if item.name != "content-schema.json"))
        else:
            paths.append(path)
    return paths


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python scripts/validate_content.py path/to/post.json [more.json ...] | content/")
        return 2

    try:
        schema = load_json(SCHEMA_PATH)
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        print(f"ERROR: Content schema is invalid: {exc}")
        return 2

    paths = collect_paths(sys.argv[1:])
    if not paths:
        print("ERROR: No content JSON records found.")
        return 2

    total_errors = 0
    for path in paths:
        try:
            data = load_json(path)
        except Exception as exc:
            print(f"ERROR: {path}: Could not read valid JSON: {exc}")
            total_errors += 1
            continue

        errors, warnings = validate_record(data, schema)
        print(f"Checking {path}")
        for item in errors:
            print(f"ERROR: {item}")
        for item in warnings:
            print(f"WARNING: {item}")
        if errors:
            total_errors += len(errors)
        else:
            print("Structure and hard guardrails passed. This is not a medical/legal review or publishing approval.")

    return 1 if total_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
