#!/usr/bin/env python3
"""Generate Wiki_Index.md from Wiki document frontmatter.

Usage:
  python tools/wiki/build_index.py
  python tools/wiki/build_index.py --check
  python tools/wiki/build_index.py --verbose

Documents under Wiki/Garbage and explicitly tracked migration backlog files are not
canonical Wiki entries. They are skipped with warnings until reviewed.
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)

WIKI_ROOT = Path("Wiki")
INDEX_PATH = WIKI_ROOT / "00_System" / "Wiki_Index.md"
REQUIRED_FIELDS = ["id", "title", "type", "status", "summary"]
KNOWN_TYPES = {
    "system", "template", "mechanic", "lore_world", "lore_char",
    "lore_faction", "event", "planning", "log",
}
STATUS_ICONS = {
    "complete": "✅",
    "wip": "🟡",
    "draft": "⚪",
    "deprecated": "🗑️",
}
ARCHIVE_DIRS = {"Garbage"}
LEGACY_UNINDEXED = {
    "Wiki/00_System/Planning/02_Event_QA_Protocol.md",
    "Wiki/00_System/Planning/03_Downfall_PRD.md",
    "Wiki/00_System/Planning/04_Solo_Dev_AI_Tools_Tutorial.md",
    "Wiki/00_Templates/EVT_NotificationTest.md",
    "Wiki/02_World/World_Concept.md",
    "Wiki/03_Entities/Entities.md",
    "Wiki/PROJECT_STATE.md",
}


def extract_frontmatter(path: Path):
    try:
        text = path.read_text(encoding="utf-8").lstrip()
    except Exception as exc:
        return None, f"read-error: {exc}"
    if not text.startswith("---"):
        return None, "no-frontmatter"
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, "malformed-frontmatter (no closing ---)"
    try:
        meta = yaml.safe_load(parts[1])
    except yaml.YAMLError as exc:
        return None, f"yaml-parse-error: {exc}"
    if not isinstance(meta, dict):
        return None, "frontmatter-not-dict"
    return meta, None


def validate(meta: dict) -> list[str]:
    warnings: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in meta or meta[field] in (None, ""):
            warnings.append(f"missing required field: '{field}'")
    if "type" in meta and meta["type"] not in KNOWN_TYPES:
        warnings.append(f"unknown type: '{meta['type']}' (allowed: {sorted(KNOWN_TYPES)})")
    if "status" in meta and meta["status"] not in STATUS_ICONS:
        warnings.append(f"unknown status: '{meta['status']}' (allowed: {list(STATUS_ICONS)})")
    return warnings


def is_archive(path: Path, wiki_root: Path) -> bool:
    parts = path.relative_to(wiki_root).parts
    return bool(parts) and parts[0] in ARCHIVE_DIRS


def collect_entries(wiki_root: Path):
    entries, errors, migration_warnings = [], [], []
    index_abs = INDEX_PATH.resolve()

    for md in sorted(wiki_root.rglob("*.md")):
        if md.resolve() == index_abs or is_archive(md, wiki_root):
            continue

        repo_rel = md.as_posix()
        if repo_rel in LEGACY_UNINDEXED:
            migration_warnings.append(md)
            continue

        meta, error = extract_frontmatter(md)
        if error:
            errors.append((md, error))
            continue

        validation = validate(meta)
        if validation:
            errors.append((md, "; ".join(validation)))
            meta["_broken"] = True
        entries.append((md, meta))

    return entries, errors, migration_warnings


def render(entries, wiki_root: Path) -> str:
    by_folder: dict[str, list] = {}
    for path, meta in entries:
        folder = str(path.parent.relative_to(wiki_root)) or "."
        by_folder.setdefault(folder, []).append((path, meta))

    lines = [
        "# 🗂️ Downfall Wiki Master Index",
        "",
        f"*Auto-generated on {dt.datetime.now().isoformat(timespec='seconds')}*  ",
        f"*Total entries: {len(entries)}*  ",
        "*⚠️ DO NOT EDIT BY HAND — modify each file's frontmatter, then re-run build_index.py.*",
        "",
        "---",
        "",
    ]

    for folder in sorted(by_folder):
        lines.extend([f"## 📁 `{folder}/`", ""])
        for path, meta in sorted(by_folder[folder], key=lambda item: item[0].name):
            icon = STATUS_ICONS.get(meta.get("status", ""), "❓")
            broken = " ⚠️" if meta.get("_broken") else ""
            lines.append(f"### {icon} `{path.name}`{broken}")
            lines.append(f"- **Title:** {meta.get('title', '(untitled)')}")
            lines.append(f"- **ID:** `{meta.get('id', '(no-id)')}` | **Type:** `{meta.get('type', '?')}`")

            summary = (meta.get("summary") or "").strip()
            if summary:
                lines.append(f"- **Summary:** {summary}")

            keywords = meta.get("keywords") or []
            if keywords:
                value = ", ".join(str(item) for item in keywords) if isinstance(keywords, list) else str(keywords)
                lines.append(f"- **Keywords:** {value}")

            dependencies = meta.get("depends_on") or []
            if dependencies:
                value = ", ".join(f"`{item}`" for item in dependencies) if isinstance(dependencies, list) else f"`{dependencies}`"
                lines.append(f"- **Depends on:** {value}")

            emits = meta.get("emits") or []
            if emits:
                value = ", ".join(f"`{item}`" for item in emits) if isinstance(emits, list) else f"`{emits}`"
                lines.append(f"- **Emits:** {value}")
            lines.append("")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Wiki_Index.md from frontmatter.")
    parser.add_argument("--check", action="store_true", help="Validate only; do not write the index.")
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("--root", type=Path, default=WIKI_ROOT)
    args = parser.parse_args()

    if not args.root.exists():
        print(f"ERROR: wiki root '{args.root}' not found.", file=sys.stderr)
        return 2

    entries, errors, migration_warnings = collect_entries(args.root)

    for path in migration_warnings:
        print(
            f"WARNING: {path}: pending frontmatter migration; see docs/WIKI_MIGRATION_BACKLOG.md",
            file=sys.stderr,
        )

    if args.verbose or errors:
        print(f"Scanned {len(entries)} indexed files in {args.root}/.")
    if errors:
        print(f"\n⚠️  {len(errors)} file(s) have frontmatter issues:\n", file=sys.stderr)
        for path, error in errors:
            print(f"  - {path}: {error}", file=sys.stderr)
        print("", file=sys.stderr)

    if args.check:
        return 1 if errors else 0

    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(render(entries, args.root), encoding="utf-8")
    print(
        f"✅ Wrote {INDEX_PATH} ({len(entries)} entries, {len(errors)} flagged, "
        f"{len(migration_warnings)} migration-pending)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
