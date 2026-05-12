#!/usr/bin/env python3
"""
build_index.py — Auto-generate Wiki_Index.md from frontmatter of wiki files.

Usage:
  python tools/wiki/build_index.py            # build index, write file
  python tools/wiki/build_index.py --check    # lint-only mode (CI 검증용, 파일 안 씀)
  python tools/wiki/build_index.py --verbose  # 상세 로그

Requirements:
  pip install pyyaml

Frontmatter spec (필수 필드: id, title, type, status, summary):
---
id: LORE_CHAR_Gavin
title: 가빈 잭슨 캐릭터 로어 바이블
type: character_lore        # template | mechanic | lore_world | lore_char | event | system
status: complete            # draft | wip | complete | deprecated
summary: 한두 문장 요약.
tags: [character, survivor]
keywords: [가빈, Gavin]
depends_on: [Bot_Universal_Template]
emits: [Flag_Memory_Gavin_X]
last_updated: 2026-05-12
---
"""

from __future__ import annotations
import sys
import argparse
import datetime as dt
from pathlib import Path

try:
    import yaml  # PyYAML
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

# ───────────── Configuration ─────────────
WIKI_ROOT = Path("Wiki")
INDEX_PATH = WIKI_ROOT / "00_System" / "Wiki_Index.md"
REQUIRED_FIELDS = ["id", "title", "type", "status", "summary"]
KNOWN_TYPES = {
    "system", "template", "mechanic",
    "lore_world", "lore_char", "lore_faction",
    "event", "planning", "log",
}
STATUS_ICONS = {
    "complete":   "✅",
    "wip":        "🟡",
    "draft":      "⚪",
    "deprecated": "🗑️",
}

# ───────────── Frontmatter extraction ─────────────
def extract_frontmatter(path: Path):
    """Return (meta_dict, error_str). meta_dict is None on error."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        return None, f"read-error: {e}"

    if not text.lstrip().startswith("---"):
        return None, "no-frontmatter"

    # Remove leading whitespace before first '---'
    text = text.lstrip()
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, "malformed-frontmatter (no closing ---)"

    try:
        meta = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        return None, f"yaml-parse-error: {e}"

    if not isinstance(meta, dict):
        return None, "frontmatter-not-dict"

    return meta, None


def validate(meta: dict) -> list[str]:
    """Return list of validation warnings (empty if OK)."""
    warnings = []
    for f in REQUIRED_FIELDS:
        if f not in meta or meta[f] in (None, ""):
            warnings.append(f"missing required field: '{f}'")
    if "type" in meta and meta["type"] not in KNOWN_TYPES:
        warnings.append(f"unknown type: '{meta['type']}' (allowed: {sorted(KNOWN_TYPES)})")
    if "status" in meta and meta["status"] not in STATUS_ICONS:
        warnings.append(f"unknown status: '{meta['status']}' (allowed: {list(STATUS_ICONS)})")
    return warnings


# ───────────── Collection ─────────────
def collect_entries(wiki_root: Path):
    entries, errors = [], []
    index_abs = INDEX_PATH.resolve()

    for md in sorted(wiki_root.rglob("*.md")):
        # Skip the index itself
        if md.resolve() == index_abs:
            continue

        meta, err = extract_frontmatter(md)
        if err:
            errors.append((md, err))
            continue

        warnings = validate(meta)
        if warnings:
            errors.append((md, "; ".join(warnings)))
            # Still include in index but mark as broken
            meta["_broken"] = True

        entries.append((md, meta))
    return entries, errors


# ───────────── Rendering ─────────────
def render(entries, wiki_root: Path) -> str:
    by_folder: dict[str, list] = {}
    for path, meta in entries:
        folder = str(path.parent.relative_to(wiki_root)) or "."
        by_folder.setdefault(folder, []).append((path, meta))

    now = dt.datetime.now().isoformat(timespec="seconds")
    lines = [
        "# 🗂️ Downfall Wiki Master Index",
        "",
        f"*Auto-generated on {now}*  ",
        f"*Total entries: {len(entries)}*  ",
        "*⚠️ DO NOT EDIT BY HAND — modify each file's frontmatter, then re-run build_index.py.*",
        "",
        "---",
        "",
    ]

    for folder in sorted(by_folder.keys()):
        lines.append(f"## 📁 `{folder}/`")
        lines.append("")
        for path, meta in sorted(by_folder[folder], key=lambda x: x[0].name):
            icon = STATUS_ICONS.get(meta.get("status", ""), "❓")
            broken = " ⚠️" if meta.get("_broken") else ""
            title = meta.get("title", "(untitled)")
            mid = meta.get("id", "(no-id)")
            summary = (meta.get("summary") or "").strip()
            deps = meta.get("depends_on") or []
            emits = meta.get("emits") or []
            type_ = meta.get("type", "?")
            keywords = meta.get("keywords") or []

            lines.append(f"### {icon} `{path.name}`{broken}")
            lines.append(f"- **Title:** {title}")
            lines.append(f"- **ID:** `{mid}` | **Type:** `{type_}`")
            if summary:
                lines.append(f"- **Summary:** {summary}")
            if keywords:
                kw_str = ", ".join(str(k) for k in keywords) if isinstance(keywords, list) else str(keywords)
                lines.append(f"- **Keywords:** {kw_str}")
            if deps:
                deps_str = ", ".join(f"`{d}`" for d in deps) if isinstance(deps, list) else f"`{deps}`"
                lines.append(f"- **Depends on:** {deps_str}")
            if emits:
                emits_str = ", ".join(f"`{e}`" for e in emits) if isinstance(emits, list) else f"`{emits}`"
                lines.append(f"- **Emits:** {emits_str}")
            lines.append("")
        lines.append("")

    return "\n".join(lines)


# ───────────── Main ─────────────
def main():
    parser = argparse.ArgumentParser(description="Build Wiki_Index.md from frontmatter.")
    parser.add_argument("--check", action="store_true",
                        help="lint mode: only report issues, do not write index. Exits non-zero on errors.")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="verbose output.")
    parser.add_argument("--root", type=Path, default=WIKI_ROOT,
                        help=f"wiki root path (default: {WIKI_ROOT})")
    args = parser.parse_args()

    wiki_root = args.root
    if not wiki_root.exists():
        print(f"ERROR: wiki root '{wiki_root}' not found.", file=sys.stderr)
        sys.exit(2)

    entries, errors = collect_entries(wiki_root)

    if args.verbose or errors:
        print(f"Scanned {len(entries)} files in {wiki_root}/.")
    if errors:
        print(f"\n⚠️  {len(errors)} file(s) have frontmatter issues:\n", file=sys.stderr)
        for path, err in errors:
            print(f"  - {path}: {err}", file=sys.stderr)
        print("", file=sys.stderr)

    if args.check:
        sys.exit(1 if errors else 0)

    # Write index
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    output = render(entries, wiki_root)
    INDEX_PATH.write_text(output, encoding="utf-8")
    print(f"✅ Wrote {INDEX_PATH} ({len(entries)} entries, {len(errors)} flagged).")

    # Lint-style exit code (always 0 unless --check)
    sys.exit(0)


if __name__ == "__main__":
    main()
