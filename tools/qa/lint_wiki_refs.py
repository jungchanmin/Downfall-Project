#!/usr/bin/env python3
"""Validate Downfall Wiki frontmatter IDs and cross-document references.

The default mode blocks structural errors while reporting legacy reference debt as
warnings. Use --strict to make unresolved dependencies and event filename/ID
mismatches fail CI.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[2]
WIKI_ROOT = ROOT / "Wiki"
INDEX_PATH = WIKI_ROOT / "00_System" / "Wiki_Index.md"
EVENT_FILE_RE = re.compile(r"^(EVT_[A-Z]\d{3})_")
EVENT_ID_RE = re.compile(r"^(EVT_[A-Z]\d{3})_")


def extract_frontmatter(path: Path) -> tuple[dict | None, str | None]:
    try:
        text = path.read_text(encoding="utf-8").lstrip()
    except Exception as exc:
        return None, f"read error: {exc}"
    if not text.startswith("---"):
        return None, "missing frontmatter"
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, "unclosed frontmatter"
    try:
        meta = yaml.safe_load(parts[1])
    except yaml.YAMLError as exc:
        return None, f"YAML parse error: {exc}"
    if not isinstance(meta, dict):
        return None, "frontmatter must be a mapping"
    return meta, None


def as_list(value: object) -> list[str]:
    if value in (None, ""):
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def scan() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    records: list[tuple[Path, dict]] = []
    ids: dict[str, list[Path]] = defaultdict(list)

    for path in sorted(WIKI_ROOT.rglob("*.md")):
        if path.resolve() == INDEX_PATH.resolve():
            continue
        meta, error = extract_frontmatter(path)
        rel = path.relative_to(ROOT).as_posix()
        if error:
            errors.append(f"{rel}: {error}")
            continue
        assert meta is not None
        doc_id = str(meta.get("id", "")).strip()
        if not doc_id:
            errors.append(f"{rel}: missing id")
            continue
        ids[doc_id].append(path)
        records.append((path, meta))

    for doc_id, paths in sorted(ids.items()):
        if len(paths) > 1:
            joined = ", ".join(p.relative_to(ROOT).as_posix() for p in paths)
            errors.append(f"duplicate id {doc_id}: {joined}")

    known_ids = set(ids)
    for path, meta in records:
        rel = path.relative_to(ROOT).as_posix()
        doc_id = str(meta["id"]).strip()

        for dependency in as_list(meta.get("depends_on")):
            if dependency not in known_ids:
                warnings.append(f"{rel}: unresolved depends_on '{dependency}'")

        if path.name.startswith("EVT_"):
            file_match = EVENT_FILE_RE.match(path.stem)
            id_match = EVENT_ID_RE.match(doc_id)
            if file_match and id_match and file_match.group(1) != id_match.group(1):
                warnings.append(
                    f"{rel}: filename prefix {file_match.group(1)} != id prefix {id_match.group(1)}"
                )

        for key in ("depends_on", "emits", "tags", "keywords"):
            value = meta.get(key)
            if value is not None and not isinstance(value, (list, str)):
                warnings.append(f"{rel}: {key} should be a list or string")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint Wiki IDs and references.")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors.")
    args = parser.parse_args()

    if not WIKI_ROOT.exists():
        print(f"ERROR: Wiki root not found: {WIKI_ROOT}", file=sys.stderr)
        return 2

    errors, warnings = scan()
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    print(f"Wiki reference lint: {len(errors)} error(s), {len(warnings)} warning(s).")
    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
