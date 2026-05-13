#!/usr/bin/env python3
"""
lint_event.py — Gate A automated linting for Downfall v2 event files.

Runs 7 lint rules against EVT_* files:
  1. lint_family_required       — event_meta.family 필드 필수 + F1~F5 검증 [ERROR]
  2. lint_resolution_mode       — Track A/B 에 맞는 resolution.mode 검증 [ERROR]
  3. lint_check_modifier        — stat_check 모드의 check 필드 완전성 [ERROR/WARN]
  4. lint_particle_slot         — 한국어 조사 슬롯 누락 검출 [WARN]
  5. lint_banned_words          — 금지어(코즈믹 호러, 기괴한 등) 검출 [WARN]
  6. lint_emits_completeness    — flags_emit ↔ frontmatter.emits 일치성 [WARN/INFO]
  7. lint_trigger_negation      — trigger 에 not 절 존재 [WARN]

Usage:
  python lint_event.py path/to/event.md
  python lint_event.py Wiki/05_Events/
  python lint_event.py --check Wiki/05_Events/         # exit 1 on ERROR
  python lint_event.py --strict --check Wiki/05_Events/ # exit 1 on WARN too
  python lint_event.py --rule particle_slot path/to/event.md  # 특정 린트만 실행

Requirements: pip install pyyaml
"""

from __future__ import annotations
import argparse
import re
import sys
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Callable

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


# ═══════════════════════════════════════════════════════
# Constants
# ═══════════════════════════════════════════════════════

VALID_FAMILIES = {
    "F1_Resource", "F2_Atmosphere", "F3_Internal",
    "F4_Encounter", "F5_Cosmic",
}

BANNED_WORDS = [
    "코즈믹 호러", "코즈믹호러",
    "기괴한", "기괴함", "기괴하게", "기괴해",
    "초자연적인", "초자연적",
    "광기",
    "환각",
    # "무서운" 은 인물 대사 안에서는 정당할 수 있으므로 제외 (false positive 빈도 높음)
]


class Severity(Enum):
    ERROR = "ERROR"
    WARNING = "WARN"
    INFO = "INFO"


@dataclass
class LintIssue:
    severity: Severity
    rule: str
    message: str
    location: str = ""


# ═══════════════════════════════════════════════════════
# Parsing
# ═══════════════════════════════════════════════════════

def parse_event_file(path: Path) -> tuple[dict, dict, str]:
    """
    Return (frontmatter, body, narrative_text).
    Frontmatter and body are dicts. narrative_text is all extracted free text.
    Raises ValueError on parse failure.
    """
    text = path.read_text(encoding="utf-8")
    if not text.lstrip().startswith("---"):
        raise ValueError("missing frontmatter")

    text = text.lstrip()
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("malformed frontmatter (no closing ---)")

    frontmatter = yaml.safe_load(parts[1]) or {}
    body = yaml.safe_load(parts[2]) or {}

    # Collect all narrative text recursively (text/narration/label/notes/outcome_text)
    NARRATIVE_KEYS = {"text", "narration", "label", "notes", "outcome_text"}
    narrative_parts: list[str] = []

    def collect(obj: Any):
        if isinstance(obj, str):
            return
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in NARRATIVE_KEYS and isinstance(v, str):
                    narrative_parts.append(v)
                collect(v)
        elif isinstance(obj, list):
            for item in obj:
                collect(item)

    collect(body)
    return frontmatter, body, "\n".join(narrative_parts)


# ═══════════════════════════════════════════════════════
# Lint Rules
# ═══════════════════════════════════════════════════════

def lint_family_required(fm: dict, body: dict, narr: str) -> list[LintIssue]:
    issues = []
    meta = body.get("event_meta", {}) or {}
    family = meta.get("family")
    if not family:
        issues.append(LintIssue(
            Severity.ERROR, "family_required",
            "event_meta.family 필드가 없습니다. F1~F5 중 하나로 지정 필요.",
            "event_meta.family",
        ))
    elif family not in VALID_FAMILIES:
        issues.append(LintIssue(
            Severity.ERROR, "family_required",
            f"family '{family}' 는 유효하지 않습니다. 허용: {sorted(VALID_FAMILIES)}",
            "event_meta.family",
        ))
    return issues


def lint_resolution_mode(fm: dict, body: dict, narr: str) -> list[LintIssue]:
    issues = []
    meta = body.get("event_meta", {}) or {}
    track = meta.get("track")

    if track == "A":
        res = body.get("resolution", {}) or {}
        mode = res.get("mode")
        if not mode:
            issues.append(LintIssue(
                Severity.ERROR, "resolution_mode",
                "Track A 인데 resolution.mode 가 없습니다.",
                "resolution.mode",
            ))
        elif mode not in {"deterministic", "stat_check"}:
            issues.append(LintIssue(
                Severity.ERROR, "resolution_mode",
                f"Track A 의 mode '{mode}' 는 deterministic|stat_check 중 하나여야 합니다.",
                "resolution.mode",
            ))
    elif track == "B":
        choices = body.get("choices", []) or []
        if len(choices) < 2:
            issues.append(LintIssue(
                Severity.ERROR, "resolution_mode",
                f"Track B 는 2~3 개의 선택지가 필요합니다 (현재: {len(choices)}).",
                "choices",
            ))
        if len(choices) > 3:
            issues.append(LintIssue(
                Severity.WARNING, "resolution_mode",
                f"Track B 선택지가 {len(choices)}개 — 4개 이상은 분기 폭발의 위험.",
                "choices",
            ))
        for i, ch in enumerate(choices):
            ch_id = ch.get("id", f"choice[{i}]")
            res = ch.get("resolution", {}) or {}
            mode = res.get("mode")
            if not mode:
                issues.append(LintIssue(
                    Severity.ERROR, "resolution_mode",
                    f"choice '{ch_id}' 에 resolution.mode 가 없습니다.",
                    f"choices.{ch_id}.resolution.mode",
                ))
            elif mode not in {"deterministic", "stat_check"}:
                issues.append(LintIssue(
                    Severity.ERROR, "resolution_mode",
                    f"choice '{ch_id}' 의 mode '{mode}' 가 유효하지 않습니다.",
                    f"choices.{ch_id}.resolution.mode",
                ))
    elif track is None:
        issues.append(LintIssue(
            Severity.ERROR, "resolution_mode",
            "event_meta.track 이 없습니다. 'A' 또는 'B' 로 지정 필요.",
            "event_meta.track",
        ))
    return issues


def lint_check_modifier(fm: dict, body: dict, narr: str) -> list[LintIssue]:
    issues = []

    def check(res: dict, path: str):
        if res.get("mode") != "stat_check":
            return
        chk = res.get("check", {}) or {}
        if not chk.get("stat"):
            issues.append(LintIssue(
                Severity.ERROR, "check_modifier",
                f"{path}: stat_check 인데 check.stat 가 없습니다.",
                f"{path}.check.stat",
            ))
        if chk.get("dc") is None:
            issues.append(LintIssue(
                Severity.ERROR, "check_modifier",
                f"{path}: stat_check 인데 check.dc 가 없습니다.",
                f"{path}.check.dc",
            ))
        mods = chk.get("modifiers", []) or []
        if not mods:
            issues.append(LintIssue(
                Severity.WARNING, "check_modifier",
                f"{path}: stat_check 의 modifiers 가 비어 있습니다. "
                "캐릭터 상태(기벽·스트레스·플래그)가 결과에 영향을 주지 못함.",
                f"{path}.check.modifiers",
            ))

    meta = body.get("event_meta", {}) or {}
    track = meta.get("track")

    if track == "A":
        check(body.get("resolution", {}) or {}, "resolution")
    elif track == "B":
        for i, ch in enumerate(body.get("choices", []) or []):
            ch_id = ch.get("id", f"choice[{i}]")
            check(ch.get("resolution", {}) or {}, f"choices.{ch_id}.resolution")

    return issues


def lint_particle_slot(fm: dict, body: dict, narr: str) -> list[LintIssue]:
    """
    Direct particle attachment to a variable like {actor}이 → should be {actor}{이/가}.
    Heuristic: {varname} followed immediately by a particle char, then whitespace/punct.
    """
    issues = []
    # 다음과 같은 패턴을 찾는다: {varname}<조사>(공백|구두점) — slot form 인 {actor}{이/가} 는 매칭하지 않음
    # 우선순위 보존을 위해 긴 조사부터 (이여, 으로) 먼저 시도
    pattern = re.compile(
        r"\{([a-zA-Z_가-힣][\w가-힣]*)\}"  # {varname}
        r"(이여|으로|이|가|을|를|은|는|와|과|아|야|로|여)"  # particle
        r"(?=[\s.,!?…\"'·\)\]\}]|$)"  # followed by whitespace, punct, or EOL
    )

    for match in pattern.finditer(narr):
        var, particle = match.group(1), match.group(2)
        start = max(0, match.start() - 15)
        end = min(len(narr), match.end() + 15)
        ctx = narr[start:end].replace("\n", " ").strip()
        issues.append(LintIssue(
            Severity.WARNING, "particle_slot",
            f"직접 조사 표기: '{{{var}}}{particle}' → '{{{var}}}{{{particle}/...}}' 형식 권장. "
            f"context: ...{ctx}...",
        ))
    return issues


def lint_banned_words(fm: dict, body: dict, narr: str) -> list[LintIssue]:
    issues = []
    for word in BANNED_WORDS:
        idx = 0
        while True:
            pos = narr.find(word, idx)
            if pos < 0:
                break
            start = max(0, pos - 15)
            end = min(len(narr), pos + len(word) + 15)
            ctx = narr[start:end].replace("\n", " ").strip()
            issues.append(LintIssue(
                Severity.WARNING, "banned_words",
                f"금지어 '{word}' 발견. 물리적 현상·생리적 반응으로 대체할 것. "
                f"context: ...{ctx}...",
            ))
            idx = pos + len(word)
    return issues


def lint_emits_completeness(fm: dict, body: dict, narr: str) -> list[LintIssue]:
    issues = []

    # 1) Find all flags actually emitted (in flags_emit lists)
    emitted: set[str] = set()
    def find_emit_lists(obj: Any, in_trigger: bool = False):
        # trigger 안의 flag 는 emit 가 아니라 *조건* 임 — 구분
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == "trigger":
                    find_emit_lists(v, in_trigger=True)
                elif k == "flags_emit" and isinstance(v, list) and not in_trigger:
                    for f in v:
                        if isinstance(f, str):
                            emitted.add(f)
                else:
                    find_emit_lists(v, in_trigger)
        elif isinstance(obj, list):
            for item in obj:
                find_emit_lists(item, in_trigger)

    find_emit_lists(body)

    # 2) Declared in frontmatter
    declared = set(fm.get("emits", []) or [])

    # 3) Missing: emitted in body but not in frontmatter
    missing = emitted - declared
    for f in sorted(missing):
        issues.append(LintIssue(
            Severity.WARNING, "emits_completeness",
            f"플래그 '{f}' 가 body 의 flags_emit 에는 있으나 frontmatter.emits 에 없음. "
            "프론트매터에 추가하면 Wiki 검색에서 잡힙니다.",
            "emits",
        ))

    # 4) Orphan: declared but never emitted
    orphan = declared - emitted
    for f in sorted(orphan):
        issues.append(LintIssue(
            Severity.INFO, "emits_completeness",
            f"플래그 '{f}' 가 frontmatter.emits 에는 있으나 body 어디서도 발행되지 않음.",
            "emits",
        ))

    return issues


def lint_trigger_negation(fm: dict, body: dict, narr: str) -> list[LintIssue]:
    """trigger 에 not 절이 하나도 없으면 경고 (부적절한 맥락 차단 미명시)."""
    issues = []
    trigger = body.get("trigger")
    if not trigger:
        return issues  # trigger 없음은 다른 린트가 잡음

    def has_not(obj: Any) -> bool:
        if isinstance(obj, dict):
            if "not" in obj:
                return True
            for v in obj.values():
                if has_not(v):
                    return True
        elif isinstance(obj, list):
            for item in obj:
                if has_not(item):
                    return True
        return False

    if not has_not(trigger):
        issues.append(LintIssue(
            Severity.WARNING, "trigger_negation",
            "trigger 에 not 절이 없습니다. 부적절한 맥락(예: 식량 풍부 시 식량 부족 "
            "이벤트 발현)을 명시적으로 차단하지 않으면 어색한 발현 가능.",
            "trigger",
        ))
    return issues


# ═══════════════════════════════════════════════════════
# Orchestration
# ═══════════════════════════════════════════════════════

ALL_LINTS: dict[str, Callable] = {
    "family_required":      lint_family_required,
    "resolution_mode":      lint_resolution_mode,
    "check_modifier":       lint_check_modifier,
    "particle_slot":        lint_particle_slot,
    "banned_words":         lint_banned_words,
    "emits_completeness":   lint_emits_completeness,
    "trigger_negation":     lint_trigger_negation,
}


def lint_file(path: Path, enabled_rules: set[str] | None = None) -> list[LintIssue]:
    try:
        fm, body, narr = parse_event_file(path)
    except Exception as e:
        return [LintIssue(Severity.ERROR, "parse", f"파싱 실패: {e}")]

    issues = []
    for name, fn in ALL_LINTS.items():
        if enabled_rules is None or name in enabled_rules:
            issues.extend(fn(fm, body, narr))
    return issues


# ═══════════════════════════════════════════════════════
# Output formatting
# ═══════════════════════════════════════════════════════

ICON = {Severity.ERROR: "❌", Severity.WARNING: "⚠️ ", Severity.INFO: "ℹ️ "}

def format_file_result(path: Path, issues: list[LintIssue]) -> str:
    if not issues:
        return f"✅ {path} — clean"
    lines = [f"📄 {path}"]
    for sev in [Severity.ERROR, Severity.WARNING, Severity.INFO]:
        for i in issues:
            if i.severity != sev:
                continue
            lines.append(f"   {ICON[sev]} [{i.rule}] {i.message}")
    return "\n".join(lines)


# ═══════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════

def main():
    p = argparse.ArgumentParser(description="Gate A lint for Downfall events")
    p.add_argument("paths", nargs="+", type=Path,
                   help="event files or directories")
    p.add_argument("--check", action="store_true",
                   help="exit non-zero if any ERROR found (CI mode)")
    p.add_argument("--strict", action="store_true",
                   help="under --check, WARN also fails")
    p.add_argument("--rule", action="append",
                   help="run only specific rule (can repeat)")
    p.add_argument("--quiet", action="store_true",
                   help="suppress clean files in output")
    args = p.parse_args()

    if args.rule:
        unknown = set(args.rule) - set(ALL_LINTS.keys())
        if unknown:
            print(f"ERROR: unknown rule(s): {unknown}", file=sys.stderr)
            print(f"Available: {sorted(ALL_LINTS.keys())}", file=sys.stderr)
            sys.exit(2)
        enabled = set(args.rule)
    else:
        enabled = None

    # Collect files
    files: list[Path] = []
    for path in args.paths:
        if path.is_dir():
            files.extend(sorted(path.rglob("EVT_*.md")))
        elif path.is_file():
            files.append(path)
        else:
            print(f"WARN: '{path}' not found", file=sys.stderr)

    if not files:
        print("No event files found.", file=sys.stderr)
        sys.exit(1)

    # Run lints
    total_errors = 0
    total_warns = 0
    total_infos = 0
    for f in files:
        issues = lint_file(f, enabled)
        if issues or not args.quiet:
            print(format_file_result(f, issues))
        for i in issues:
            if i.severity == Severity.ERROR:   total_errors += 1
            elif i.severity == Severity.WARNING: total_warns += 1
            else: total_infos += 1

    # Summary
    print()
    print("─" * 50)
    print(f"Scanned: {len(files)} file(s)")
    print(f"Errors:  {total_errors}")
    print(f"Warns:   {total_warns}")
    print(f"Infos:   {total_infos}")

    if args.check:
        if total_errors > 0 or (args.strict and total_warns > 0):
            sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
