#!/usr/bin/env python3
"""
test_lint_event.py — Self-contained test cases for the Gate A linter.

각 테스트는 *인라인 이벤트 픽스처* 를 임시 파일로 쓴 뒤 린트를 돌려, 기대 결과와 일치하는지 검증.
"""

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lint_event import lint_file, Severity, ALL_LINTS


# ═══════════════════════════════════════════════════════
# Fixtures
# ═══════════════════════════════════════════════════════

VALID_TRACK_A_DETERMINISTIC = """\
---
id: EVT_A001_test
title: 정상 Track A 결정론 이벤트
type: event
status: complete
summary: 테스트용 정상 이벤트.
tags: [event, track_a]
keywords: [테스트]
emits: [Flag_Memory_Test_Saw]
last_updated: 2026-05-12
---

event_meta:
  id: EVT_A001_test
  track: A
  family: F2_Atmosphere
  phase: 밤
  location: Loc_지하실
  weight: 1.0

trigger:
  all:
    - phase: 밤
    - location: Loc_지하실
    - not: { flag: Flag_Cleansed }

narration: |
  {actor}{이/가} 지하실로 들어선다. 공기가 무겁다.
  {actor}{은/는} 침묵 속에서 발걸음을 옮긴다.

resolution:
  mode: deterministic
  effects:
    stat_delta:
      "{actor}.스트레스": 1
    flags_emit:
      - Flag_Memory_Test_Saw

shirley_jackson_axes:
  primary: 공간의_악의
  notes: 지하실의 의인화
"""

VALID_TRACK_A_STAT_CHECK = """\
---
id: EVT_A002_test
title: 정상 Track A stat_check 이벤트
type: event
status: complete
summary: 테스트용.
emits: [Flag_Memory_Found, Flag_Memory_Missed]
last_updated: 2026-05-12
---

event_meta:
  id: EVT_A002_test
  track: A
  family: F4_Encounter
  phase: 점심

trigger:
  all:
    - phase: 점심
    - not: { trait: { actor: "Gavin", trait: "초자연_무감각" } }

narration: |
  {actor}{이/가} 책상 위 장부를 들여다본다.

resolution:
  mode: stat_check
  check:
    actor: "{actor}"
    stat: 지능
    dc: 12
    modifiers:
      - condition: { trait: { actor: "{actor}", trait: "통제강박" } }
        bonus: 2
  on_success:
    text: "{actor}{은/는} 결산이 틀렸음을 알아차린다."
    effects:
      flags_emit: [Flag_Memory_Found]
  on_fail:
    text: "{actor}{은/는} 무엇인가 어긋났다는 느낌만 안고 떠난다."
    effects:
      flags_emit: [Flag_Memory_Missed]
"""

VALID_TRACK_B = """\
---
id: EVT_B001_test
title: 정상 Track B 이벤트
type: event
status: complete
summary: 테스트용.
emits: [Flag_Memory_TookMedkit, Flag_Trauma_Betrayed]
last_updated: 2026-05-12
---

event_meta:
  id: EVT_B001_test
  track: B
  family: F4_Encounter
  phase: 점심
  location: Loc_폐가

trigger:
  all:
    - phase: 점심
    - location: Loc_폐가
    - not: { flag: Flag_PolarHouseCleared }

narration: |
  썩은 나무 문 너머로 무언가가 맥박 친다.

choices:
  - id: ch1
    label: "{actor}{이/가} 렌치를 휘둘러 물자를 뺏는다"
    resolution:
      mode: stat_check
      check:
        actor: "{actor}"
        stat: 전투
        dc: 12
        modifiers:
          - condition: { stat: { actor: "{actor}", 체력: { gte: 50 } } }
            bonus: 1
      on_success:
        text: "{actor}{이/가} 구급상자를 낚아챈다."
        effects:
          flags_emit: [Flag_Memory_TookMedkit]
      on_fail:
        text: "타격이 미끄러진다."
        effects: {}

  - id: ch2
    label: "{ally}{을/를} 미끼로 삼는다"
    resolution:
      mode: deterministic
      outcome_text: "{actor}{이/가} {ally}{을/를} 떠민다."
      effects:
        flags_emit: [Flag_Trauma_Betrayed]
"""

# ── INVALID FIXTURES ──

MISSING_FAMILY = """\
---
id: EVT_X001
title: Family 없음
type: event
status: draft
summary: 테스트
last_updated: 2026-05-12
---

event_meta:
  id: EVT_X001
  track: A
  phase: 밤

trigger:
  all:
    - not: { flag: X }

resolution:
  mode: deterministic
  effects: {}
"""

INVALID_FAMILY = """\
---
id: EVT_X002
title: Family 잘못됨
type: event
status: draft
summary: 테스트
last_updated: 2026-05-12
---

event_meta:
  id: EVT_X002
  track: A
  family: F99_Nonsense
  phase: 밤

trigger:
  all:
    - not: { flag: X }

resolution:
  mode: deterministic
  effects: {}
"""

MISSING_RESOLUTION_MODE = """\
---
id: EVT_X003
title: Mode 누락
type: event
status: draft
summary: 테스트
last_updated: 2026-05-12
---

event_meta:
  id: EVT_X003
  track: A
  family: F1_Resource
  phase: 아침

trigger:
  all:
    - not: { flag: X }

resolution:
  effects: {}
"""

STAT_CHECK_EMPTY_MODIFIERS = """\
---
id: EVT_X004
title: modifiers 빈 배열
type: event
status: draft
summary: 테스트
emits: []
last_updated: 2026-05-12
---

event_meta:
  id: EVT_X004
  track: A
  family: F4_Encounter
  phase: 점심

trigger:
  all:
    - not: { flag: X }

resolution:
  mode: stat_check
  check:
    actor: "{actor}"
    stat: 지능
    dc: 10
    modifiers: []
  on_success: { text: "..." }
  on_fail:    { text: "..." }
"""

DIRECT_PARTICLE_ATTACHMENT = """\
---
id: EVT_X005
title: 조사 직접 표기
type: event
status: draft
summary: 테스트
emits: []
last_updated: 2026-05-12
---

event_meta:
  id: EVT_X005
  track: A
  family: F2_Atmosphere
  phase: 밤

trigger:
  all:
    - not: { flag: X }

narration: |
  {actor}이 들어왔다.
  {actor}는 침묵했다.
  {ally}을 보았다.

resolution:
  mode: deterministic
  effects: {}
"""

BANNED_WORDS_IN_BODY = """\
---
id: EVT_X006
title: 금지어 사용
type: event
status: draft
summary: 테스트
emits: []
last_updated: 2026-05-12
---

event_meta:
  id: EVT_X006
  track: A
  family: F5_Cosmic
  phase: 밤

trigger:
  all:
    - not: { flag: X }

narration: |
  {actor}{이/가} 기괴한 광경을 목격한다.
  코즈믹 호러가 그를 사로잡았다.
  광기가 차오른다.

resolution:
  mode: deterministic
  effects: {}
"""

EMITS_MISMATCH = """\
---
id: EVT_X007
title: emits 불일치
type: event
status: draft
summary: 테스트
emits: [Flag_Memory_DeclaredOnly]
last_updated: 2026-05-12
---

event_meta:
  id: EVT_X007
  track: A
  family: F1_Resource
  phase: 아침

trigger:
  all:
    - not: { flag: X }

resolution:
  mode: deterministic
  effects:
    flags_emit:
      - Flag_Memory_UndeclaredInFrontmatter
"""

NO_TRIGGER_NEGATION = """\
---
id: EVT_X008
title: not 절 없음
type: event
status: draft
summary: 테스트
emits: []
last_updated: 2026-05-12
---

event_meta:
  id: EVT_X008
  track: A
  family: F1_Resource
  phase: 아침

trigger:
  all:
    - phase: 아침
    - resource: { food: { lt: 5 } }

resolution:
  mode: deterministic
  effects: {}
"""


# ═══════════════════════════════════════════════════════
# Test runner
# ═══════════════════════════════════════════════════════

def run_test(label: str, fixture: str, expectations: dict) -> bool:
    """
    expectations: {
      rule_name: { 'count': N, 'min_severity': Severity, ... }
    }
    또는 expectations = {} 면 *모든 린트가 통과* 해야 한다.
    """
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", delete=False, encoding="utf-8"
    ) as f:
        f.write(fixture)
        fpath = Path(f.name)

    try:
        issues = lint_file(fpath)
        by_rule: dict[str, list] = {}
        for i in issues:
            by_rule.setdefault(i.rule, []).append(i)

        ok = True
        problems = []

        if not expectations:
            # Expect clean
            if issues:
                ok = False
                problems.append(f"   기대: 깨끗함 / 실제: {len(issues)}개 issue")
                for i in issues:
                    problems.append(f"     - [{i.rule}] {i.message[:80]}")
        else:
            # 각 기대 규칙이 발동되었는지 확인
            for rule, expect in expectations.items():
                actual_count = len(by_rule.get(rule, []))
                expected_count = expect.get("count", "at_least_1")
                if expected_count == "at_least_1":
                    if actual_count < 1:
                        ok = False
                        problems.append(
                            f"   기대: [{rule}] ≥1개 발동 / 실제: {actual_count}개"
                        )
                elif actual_count != expected_count:
                    ok = False
                    problems.append(
                        f"   기대: [{rule}] {expected_count}개 / 실제: {actual_count}개"
                    )

            # 기대 외의 규칙이 발동되었는지도 체크 (선택)
            expected_rules = set(expectations.keys())
            for rule, rule_issues in by_rule.items():
                if rule not in expected_rules:
                    # 다른 린트가 *과잉* 발동된 경우
                    # 다만 이건 strict 모드일 때만 fail 시키자
                    pass

        mark = "✅" if ok else "❌"
        print(f"{mark} {label}")
        for p in problems:
            print(p)
        return ok
    finally:
        fpath.unlink()


def main():
    print("=" * 60)
    print("Gate A 린트 테스트")
    print("=" * 60)
    print()

    results = []

    # Valid fixtures — 깨끗해야 함
    print("── 정상 케이스 (issues 없어야 함) ──")
    results.append(run_test("Track A deterministic 정상", VALID_TRACK_A_DETERMINISTIC, {}))
    results.append(run_test("Track A stat_check 정상", VALID_TRACK_A_STAT_CHECK, {}))
    results.append(run_test("Track B 정상", VALID_TRACK_B, {}))
    print()

    # Invalid fixtures — 각각의 린트가 잡아야 함
    print("── 비정상 케이스 (각 린트가 잡아야 함) ──")
    results.append(run_test(
        "family 누락",
        MISSING_FAMILY,
        {"family_required": {"count": "at_least_1"}},
    ))
    results.append(run_test(
        "family 잘못된 값",
        INVALID_FAMILY,
        {"family_required": {"count": "at_least_1"}},
    ))
    results.append(run_test(
        "resolution_mode 누락",
        MISSING_RESOLUTION_MODE,
        {"resolution_mode": {"count": "at_least_1"}},
    ))
    results.append(run_test(
        "stat_check 의 modifiers 빈 배열",
        STAT_CHECK_EMPTY_MODIFIERS,
        {"check_modifier": {"count": "at_least_1"}},
    ))
    results.append(run_test(
        "직접 조사 표기 ({actor}이 등)",
        DIRECT_PARTICLE_ATTACHMENT,
        {"particle_slot": {"count": "at_least_1"}},
    ))
    results.append(run_test(
        "금지어 사용 (기괴한·코즈믹·광기)",
        BANNED_WORDS_IN_BODY,
        {"banned_words": {"count": "at_least_1"}},
    ))
    results.append(run_test(
        "emits 프론트매터 ↔ body 불일치",
        EMITS_MISMATCH,
        {"emits_completeness": {"count": "at_least_1"}},
    ))
    results.append(run_test(
        "trigger 에 not 절 없음",
        NO_TRIGGER_NEGATION,
        {"trigger_negation": {"count": "at_least_1"}},
    ))
    print()

    # Summary
    print("=" * 60)
    passed = sum(results)
    total = len(results)
    print(f"총 {total} 케이스 / {passed} 통과 / {total - passed} 실패")
    print("=" * 60)
    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    main()
