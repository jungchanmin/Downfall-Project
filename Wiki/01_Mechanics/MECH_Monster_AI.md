---
id: MECH_Monster_AI
title: "핵심 시스템 사양서 — 괴물 행동 결정 (AI) 시스템"
type: mechanic
status: wip
version: 1.0.0
summary: >
  괴물의 턴 행동 선택 로직. 괴물 전용 게이지 3종(분노·흥분·위압)이 전투 진행에 따라 누적되어
  행동 분포(기본기/고유기/R18 전조/방어 빈도)를 동적으로 변화시킨다. R18 ON=흥분, OFF=위압으로
  배타 적용. 분노 우선 에스컬레이션. 괴물 스타일 프로파일(신중형/호전형 등) 선호율로 개체 차별화.
  정의/참조 분리 — 개체는 ai_profile 참조만.
tags:
  - mechanic
  - system
  - monster
  - ai
  - combat
keywords:
  - 괴물 AI, 행동 결정, 분노 게이지, 흥분 게이지, 위압 게이지, 행동 분포,
    스타일 프로파일, 신중형, 호전형, 기본 세트, 선호율, 에스컬레이션
depends_on:
  - SYS_Manifest
  - MECH_Combat_System
  - MECH_Skill_Catalog
  - MECH_R18_Skill_Catalog
  - MECH_Status_Effect_DB
  - MONSTER_DB
last_updated: 2026-06-09
---

# 🧠 DOWNFALL 괴물 행동 결정 (AI) 시스템 (v1.0)

> 괴물이 매 턴 *어떤 기술을 고르는가*. 게이지가 행동 분포를 동적으로 바꿔, 정적 반복("약기술 2~3개")을 해소.
> 정의/참조 분리: 게이지·행동 규칙은 본 문서, 기술 정의는 카탈로그, 개체는 `ai_profile` 참조만.

---

## SECTION 0 — 설계 원칙

1. **게이지는 괴물 전용**: 분노·흥분·위압은 괴물에게만 누적. 생존자 게이지 아님.
2. **대처 방식이 게이지를 민다**: 생존자의 공세/방어 대처가 괴물 행동 분포를 결정 → "플레이어가 전투 장르를 선택".
3. **3계층 기술**: 기본 세트(무제약·약함) / 고유 약기술(개성) / 시그니처(강함·제약). 게이지가 비율을 가중.
4. **분노 우선 에스컬레이션**: 분노가 일정 이상이면 흥분/위압을 누르고 공세 우선(단방향 폭주).
5. **R18 배타**: R18 모듈 ON=흥분 / OFF=위압. 한 괴물이 흥분·위압을 동시에 갖지 않음.

---

## SECTION 1 — 게이지 3종

| 게이지 | 트리거 (생존자 대처) | 효과 (괴물 행동) | 특성 | 적용 |
|---|---|---|---|---|
| **분노(Rage)** | 공세적 대처(강공·약공·격파 시도) | 고유·공격 기술 빈도↑ | 누적·지속 | 공통 |
| **흥분(Arousal)** | 방어적 대처(유혹·회피·물러섬·탐색) | R18 전조기술 빈도↑ + 굴복 페이즈 '받아줌' | 누적·지속 | R18 ON |
| **위압(Intimidation)** | 방어적 대처(동일) | 괴물 방어·경계 빈도↑ (투우장 — 기세에 신중) | 단기·소모(방어 기술 시 감소) | R18 OFF |

### 1-1. 핵심 관계
```
방어적 대처 → 흥분(R18 ON) / 위압(R18 OFF)   ┐
공세적 대처 → 분노                            ┘ 일관된 대립 틀

분노 우선: 분노 ≥ 임계 → 흥분/위압을 누르고 분노 기반 공세 우선.
          (특수기술·특성으로 분노 강제 감소 시에만 역전 — 예외)
          → "처음엔 신중하다가 전투가 치열해지면 결국 폭주"(단방향 에스컬레이션).

흥분/위압 배타: R18 모듈 유무로 갈림 → 한 괴물이 동시 보유 불가(충돌 원천 소멸).
```

### 1-2. 굴복 페이즈 진입 (흥분 연동)
```
생존자가 굴복 커맨드를 골라도, 괴물의 흥분이 충분해야 괴물이 '받아줘' 페이즈 전환 성립.
→ 생존자 일방으로 굴복 페이즈를 열 수 없음. 괴물 흥분 상태가 전제.
(Combat SECTION 11-1 분노/흥분 진입 게이트와 연동 — 본 문서가 괴물 측 산출.)
```

---

## SECTION 2 — 행동 분포 결정

```
매 턴 괴물 행동 = 카테고리별 가중치 추첨:
  base_weight(기본 세트)  : 항상 일정 (무제약 기본기 — 흐름 메우기)
  + rage 비례 (고유·공격 기술 가중)
  + arousal 비례 (R18 전조기술 가중)        [R18 ON]
  + intimidation 비례 (방어·경계 가중)       [R18 OFF]
  × ai_profile 선호율 (SECTION 3)
선택된 카테고리에서 사용 가능 기술 1개 추첨(쿨타임·게이트·자세 제약 통과분 중).
```

> 시그니처/준-강기술은 *조건·쿨타임* 충족 시에만 후보군 진입(휘둘림 방지 — Combat 3계층).

---

## SECTION 3 — 괴물 스타일 프로파일 (선호율 프리셋)

> 같은 기본 세트·게이지를 공유해도 *선호율*이 달라 다른 적이 된다. 개체는 `ai_profile`로 참조.

| 프로파일 | 성향 | 선호 가중 | 분노 상승 | 예시 개체 |
|---|---|---|---|---|
| `AI_Cautious` | 신중형 | 방어·경계·견제↑ | 느림 | 자경단원(말단) |
| `AI_Aggressive` | 호전형 | 공격·고유기↑ | 빠름 | 악마조직원(예정) |
| `AI_Predator` | 포식형 | 추격·고립 표적↑ | 중간 | 짐승·포식 네임드 |
| `AI_Fanatic` | 광신형 | R18 전조·정신기↑ | 중간 | 광신도 |
| `AI_Opportunist` | 기회형 | 무방비·약체 노림↑ | 중간 | 약탈자 |

```yaml
# 프로파일 정의 예:
AI_Cautious:
  category_pref: { basic: 1.2, defensive: 1.5, unique: 0.8, signature: 0.7 }
  rage_gain_mult: 0.7        # 분노 천천히 — 좀처럼 폭주 안 함
AI_Aggressive:
  category_pref: { basic: 0.8, defensive: 0.5, unique: 1.4, signature: 1.2 }
  rage_gain_mult: 1.3        # 분노 빠름 — 금세 흉포
```

> 자경단(신중)과 악마조직원(호전)의 호전성 차이 = 프로파일 + 분노 상승률로 구현.

---

## SECTION 4 — 기본 세트 연동

```
괴물 기본 세트(형태별 공유·무제약·약함) = MECH_Skill_Catalog 정의.
인간형 기본 세트 4종: 맨손 타격 / 위협·조롱 / 경계(방어·피해 감소) / 거리 벌리기(회피성).
  - 무장 해제돼도 사용 가능(맨몸) → 완전 무력화 방지(답답함 차단), 강한 무기 기술은 잠김(약점 유효).
  - 괴물 방어 = 피해 무효 아님. 피해 감소 + 다음 행동/게이지 영향 + 경계 태세.
3계층 비중(목표 감각): 기본 30% / 고유 50% / 시그니처 20% (게이지·프로파일로 변동).
```

---

## SECTION 5 — 구현 데이터 구조

```yaml
MonsterAIState:               # 전투 중 괴물 인스턴스
  rage: int
  arousal: int | null         # R18 ON
  intimidation: int | null    # R18 OFF
  profile: AI_*               # ai_profile 참조

on_survivor_action(monster, action):
    if action.is_offensive: monster.rage += w * profile.rage_gain_mult
    elif action.is_defensive:
        if monster.r18_on: monster.arousal += w
        else: monster.intimidation += w   # 단기 — 매 턴 자연 감소 + 방어 기술 시 감소

choose_action(monster):
    if monster.rage >= RAGE_PRIORITY: bias = offensive
    else: bias = gauge_weighted(monster)
    weights = base + gauge_bias(monster) * profile.category_pref
    cat = weighted_pick(weights)
    return pick_usable_skill(cat)   # 쿨타임·게이트·자세 통과분 중
```

---

## SECTION 6 — 버전 관리

- **문서 위치**: `01_Mechanics/MECH_Monster_AI.md`
- **커밋 메시지**: `feat(mechanic): monster AI — gauge-driven action distribution (rage/arousal/intimidation), style profiles`
- **Wiki_Index.md 갱신 필요 여부**: **필요 (YES)**

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.0.0 | 2026-06-09 | 최초. 게이지 3종(분노·흥분·위압, R18 배타·분노 우선) / 행동 분포 가중치 / 스타일 프로파일 5종(신중·호전·포식·광신·기회) / 기본 세트 연동(3계층 비중) / 굴복 진입 흥분 연동 / 구현 의사코드. |

**갱신 기준**: 게이지 임계·상승률·프로파일 가중치 밸런스 테스트 후 확정. 신규 프로파일 추가 시 등록.
