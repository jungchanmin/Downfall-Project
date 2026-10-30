---
id: MECH_Check_System
title: Downfall Check / Resolution System
type: mechanic
authority: CURRENT
status: APPROVED
version: 1.0.0

parent:
  - SYS_Design_Pillars

references:
  - MECH_NPC_Stats_System
  - MECH_Combat_System

summary: >
  Downfall 전역에서 사용되는 판정의 요청, 기본 Roll,
  판정값 Source, Modifier 집계, Requirement 비교,
  성공/실패 및 Margin 반환 규칙을 정의하는 공통 Resolution System.

tags:
  - mechanic
  - check
  - resolution
  - dice
  - difficulty

keywords:
  - 판정
  - 1d12
  - 요구치
  - 성공
  - 실패
  - Margin
  - Modifier
  - 난이도

last_updated: 2026-10-30
---

# Downfall Check / Resolution System

## 1. Purpose

본 문서는 Downfall 전역에서 공통으로 사용하는 판정 시스템을 정의한다.

Check System은 Combat 전용 시스템이 아니다.

다음과 같은 다양한 Gameplay System이 동일한 Check System을 사용할 수 있다.

- Combat
- Exploration
- Event
- Dialogue
- Care
- Craft
- NPC Behavior
- Quirk / Emotion Resistance
- 기타 능력 또는 상태 기반 판정

본 시스템의 목적은:

> 서로 다른 게임 시스템이 동일한 방식으로 불확실한 행동 결과를 판정할 수 있는 공통 Resolution Contract를 제공하는 것

이다.

---

# 2. Core Resolution

Downfall의 기본 판정은 다음 구조를 사용한다.

```text id="ck01"
1d12
+
Check Source Value
+
Modifiers
>=
Requirement
```

조건을 충족하면 성공한다.

조건을 충족하지 못하면 실패한다.

정식 주사위 표기는:

```text id="ck02"
1d12
```

를 사용한다.

`12d`는 현행 공식 표기로 사용하지 않는다.

---

# 3. Terminology

본 문서에서는 다음 용어를 사용한다.

### Roll

기본 주사위 결과.

```text id="ck03"
1d12
```

---

### Check Source

판정의 기본 능력 또는 상태값.

예:

```text id="ck04"
Combat
Exploration
Dialogue
Sanity
```

---

### Modifier

판정 상황에 따라 추가되는 보정값.

예:

```text id="ck05"
Equipment
Condition
Fatigue
Emotion
Quirk
Environment
Skill
Relationship
```

---

### Requirement

판정 성공을 위해 최종값이 도달해야 하는 목표값.

---

### Final Value

개념적으로:

```text id="ck06"
Final Value
=
Roll
+
Check Source Value
+
Modifier Total
```

---

### Margin

최종 판정값과 Requirement의 차이.

```text id="ck07"
Margin
=
Final Value - Requirement
```

---

# 4. Success and Failure

판정 결과는 기본적으로 다음과 같이 처리한다.

```text id="ck08"
Final Value >= Requirement
→ Success

Final Value < Requirement
→ Failure
```

성공과 실패는 모든 Check가 제공하는 기본 결과다.

---

# 5. Margin

Check System은 단순 성공/실패뿐 아니라 Margin을 반환한다.

예:

```text id="ck09"
Final Value = 16
Requirement = 13

Margin = +3
```

또는:

```text id="ck10"
Final Value = 9
Requirement = 12

Margin = -3
```

Margin은 판정 결과의 정도를 표현한다.

다른 시스템은 이를 이용해 추가적인 결과 단계를 정의할 수 있다.

예:

```text id="ck11"
Success
Great Success
Partial Success
Severe Failure
```

그러나 이러한 결과 단계의 의미와 Threshold를 Check Core가 전역적으로 강제하지 않는다.

---

# 6. Check Request

다른 시스템은 Check System에 판정을 요청한다.

개념적인 Check Request는 다음 정보를 가질 수 있다.

```text id="ck12"
Actor
Check Source
Requirement
Modifiers
Context
```

실제 코드 구조와 Field 이름은 Technical Specification에서 정의한다.

---

# 7. Check Result

Check System은 판정 후 결과 Context를 반환한다.

개념적으로:

```text id="ck13"
Roll
Source Value
Modifiers
Modifier Total
Final Value
Requirement
Success
Margin
```

을 포함할 수 있다.

---

# 8. Check Source

Check Source는 판정에 사용되는 기본값이다.

Check System은 특정 NPC Stat만 사용하도록 제한하지 않는다.

판정 Source는 개념적으로 다음 계열을 가질 수 있다.

```text id="ck14"
Ability
State
Derived Value
```

---

# 9. Ability Check

NPC의 Ability Stat을 사용하는 가장 일반적인 판정.

현재 Ability 예:

```text id="ck15"
Combat
Exploration
Dialogue
Care
Craft
Technique
Charm
Intelligence
```

예:

```text id="ck16"
Exploration Check

1d12
+ Exploration
+ Modifiers
>= Requirement
```

---

# 10. State Check

일부 상황에서는 Ability가 아니라 NPC의 현재 상태값 자체를 판정 Source로 사용할 수 있다.

예:

```text id="ck17"
Sanity Resistance
Mental Resistance
```

기존 Event에는 정신력 등을 직접 사용하는 판정이 존재한다.

따라서 Check System은 State 기반 판정을 지원할 수 있어야 한다.

다만 아무 State나 임의로 판정 Source로 사용할 수 있다는 의미는 아니다.

각 Source의 사용 가능 여부는 해당 Stat / System Owner가 정의한다.

---

# 11. Derived Check Source

필요한 경우 하나 이상의 데이터를 기반으로 계산된 Derived Value를 Check Source로 사용할 수 있다.

예:

```text id="ck18"
Escape Resistance
Command Resistance
Special Monster Resistance
```

정확한 계산식은 해당 System Owner가 소유한다.

Check System은 계산된 값만 받아 사용한다.

---

## 11.1 Composite Check Source

하나의 행동이 둘 이상의 Source를 동시에 요구하는 경우 Composite Check를 사용할 수 있다.
기본 Composite Source Value는 필요한 Source 값의 **동일 가중치 평균을 내림**한 값이다.

```text
Composite Source Value = Floor(Average(required Source Values))
```

예를 들어 Combat = 7, Technique = 4이면 평균 5.5를 내림하여 Source Value는 5다.
이 값으로 일반 Check를 수행한다: `1d12 + Composite Source Value + Modifiers >= Requirement`.
어떤 Action / Event가 Composite를 요구하는지는 Consumer Owner가 결정한다.
Weighted Composite는 승인된 Core 기본 규칙이 아니며 후속 확장 검토 대상이다.
Composite는 Source 계산이며 Equipment, Fatigue, Status, Environment 등의 Modifier와 구분한다.
최종 Modifier 합계는 기존대로 `Clamp(sum, -3, +3)`를 적용한다.

---

# 12. Modifier Model

Modifier는 Check Source 외의 상황적 영향을 표현한다.

대표적인 Modifier Source:

```text id="ck19"
Condition
Fatigue
Equipment
Skill
Emotion
Quirk
Relationship
Environment
Combat Condition
Temporary Effect
```

Check System은 Modifier의 의미를 직접 정의하지 않는다.

---

# 13. Modifier Ownership

각 System은 자신의 Modifier 값을 정의한다.

예:

```text id="ck20"
NPC State
→ Fatigue Modifier

Item
→ Equipment Modifier

Emotion System
→ Emotion Modifier

Quirk System
→ Quirk Modifier
```

Check System은 전달받은 Modifier를 합산하고 최종 합계를 -3 이상 +3 이하로 제한한 뒤 적용한다.
개별 Modifier의 출처와 원래 값은 추적할 수 있으나 최종 제한은 합계에 적용한다.

---

# 14. Modifier Source Tracking

Modifier는 가능하면 값뿐 아니라 출처를 함께 유지한다.

예:

```text id="ck21"
+2  Skill: Veteran Scout
+1  Equipment: Binoculars
-1  Fatigue
```

이를 통해:

- UI 설명
- Debugging
- Automated Test
- Balance Review

가 가능해진다.

---

# 15. Modifier Transparency

판정 결과는 가능하면 플레이어가 이해할 수 있어야 한다.

예:

```text id="ck22"
Roll        8
Exploration +5
Equipment  +1
Fatigue    -1
----------------
Final      13
Requirement 12

Success
```

실제 UI 표현 방식은 Presentation Layer가 소유한다.

Check System은 이러한 설명에 필요한 데이터를 제공한다.

---

# 16. Integer-Based Resolution

Core Check 값은 기본적으로 정수 기반으로 처리하는 것을 원칙으로 한다.

즉:

```text id="ck23"
Roll
Source
Modifier
Requirement
Margin
```

은 정수를 기본값으로 한다.

기존 설계에 존재했던:

```text id="ck24"
+0.5
+1.5
```

같은 Modifier는 현행 Core Contract의 기본 형식으로 사용하지 않는다.

향후 반드시 필요하다고 판단되면 별도 검토한다.

---

# 17. Difficulty

판정은 Requirement 숫자 외에도 사람이 이해하기 쉬운 Difficulty Tier를 사용할 수 있다.

기본 Difficulty Tier는 다음 방향을 유지한다.

```text id="ck25"
Very Easy
Easy
Normal
Hard
Very Hard
Impossible
```

한국어:

```text id="ck26"
매우 쉬움
쉬움
보통
어려움
매우 어려움
불가능
```

---

# 18. Difficulty Design Target

Difficulty Tier는 단순한 이름이 아니라 목표 성공률을 표현하는 Design Contract다.

현재 목표 범위:

| 난이도 | 목표 성공률 |
|---|---:|
| 매우 쉬움 | 약 85~90% |
| 쉬움 | 약 70~85% |
| 보통 | 약 50~60% |
| 어려움 | 약 35~45% |
| 매우 어려움 | 약 15~30% |
| 불가능 | 약 5~10% 이하 |

이 성공률은 평균적인 상황을 기준으로 한 목표 범위다.
목표 범위는 설계적 의미이며 아래 승인된 구체 Requirement 대응이 우선한다.

---

# 19. Difficulty Requirement Table

승인된 Tier별 Requirement와 Source Value 5, Modifier 0 기준 기본 성공률은 다음과 같다.

| Difficulty | 한국어 | Requirement | 기본 성공률 |
|---|---|---:|---:|
| Very Easy | 매우 쉬움 | 7 | 91.7% |
| Easy | 쉬움 | 9 | 75.0% |
| Normal | 보통 | 11 | 58.3% |
| Hard | 어려움 | 13 | 41.7% |
| Very Hard | 매우 어려움 | 15 | 25.0% |
| Impossible | 불가능 | 17 | 8.3% |

## 19.1 Fate Override

불확실한 상황에서 Check 수행이 결정된 경우에만, 기본 Check의 수학적 성공 확률이
정확히 0% 또는 100%이면 별도 `1d100` Fate Override Roll을 수행한다.

| 기본 성공 확률 | 1d100 = 1–2 | 1d100 = 3–100 | 최종 성공 확률 |
|---|---|---|---:|
| 100% | Success를 Failure로 반전 | Success 유지 | 98% |
| 0% | Failure를 Success로 반전 | Failure 유지 | 2% |

기본 확률이 0% 초과 100% 미만이면 Fate Override를 추가로 굴리지 않는다.
이는 Natural Roll에 따른 Critical이 아닌 Check Resolution의 별도 단계다.
Narrative certainty, System-guaranteed result 또는 의미 있는 불확실성이 없는 경우에는
Consumer가 Check Request 자체를 생략할 수 있다. RNG Provider / C# 구현은 TECH_SPEC 소유이며
Multiplayer에서는 기존과 같이 Host가 결과의 권위를 가진다.

---

# 20. Static Check

가장 기본적인 Check는 고정 Requirement를 사용하는 판정이다.

예:

```text id="ck31"
1d12
+ Exploration
+ Modifiers
>= Requirement 14
```

이를 Static Check라고 부를 수 있다.

정확한 코드 명칭은 Technical Specification에서 확정한다.

---

# 21. Opposed Check

두 대상이 서로 경쟁하는 상황에서는 Opposed Check가 필요할 수 있다.

대표적 예:

```text id="ck32"
Stealth vs Exploration
Grab vs Escape
Persuasion vs Resistance
```

Opposed Check의 필요성은 인정한다.

다만 정확한 공식은 아직 확정하지 않는다.

현재 상태:

```text id="ck33"
SUPPORTED CONCEPT
FORMULA UNDEFINED
```

---

# 22. Critical Rule

현재 Core Check는 Natural Critical을 사용하지 않는다.
Natural Roll 기반 자동 성공 / 자동 실패도 정의하지 않는다.

예:

```text id="ck34"
Natural 1
Natural 12
```

에 Natural Critical이나 자동 성공 / 실패를 부여하지 않는다.
Fate Override는 Natural 1 / 12와 무관한 별도 Resolution 단계이며 Critical이 아니다.

---

# 23. Great Success / Great Failure

기존 문서에는 다음과 같은 Legacy 규칙이 존재했다.

```text id="ck36"
DC +5
→ Great Success

DC -5
→ Great Failure
```

이 숫자는 현행 규칙으로 확정하지 않는다.

대신 Check System은 `Margin`을 제공한다.

Consumer System은 필요에 따라 자체 Threshold를 정의할 수 있다.

예:

```text id="ck37"
Exploration:
Margin >= X
→ Great Success

Combat:
Margin >= Y
→ Bonus Effect
```

---

# 24. Consumer-Owned Outcome

Check System은 성공 이후 어떤 Gameplay 결과가 발생하는지 결정하지 않는다.

예:

```text id="ck38"
Exploration Success
```

이후:

```text id="ck39"
Item 발견
Clue 획득
Monster 정보 공개
```

등을 결정하는 것은 Exploration / Event System이다.

마찬가지로 Combat 판정 성공 후 Damage를 계산하는 것은 Combat System이다.

---

# 25. Combat Integration

Combat은 Check System을 Consumer로 사용한다.

개념:

```text id="ck40"
Combat Action
↓
Check Request
↓
Check Result
↓
Combat Effect Resolution
```

Combat System은 Dice Formula를 직접 소유하지 않는다.

---

# 26. Event Integration

Event는 판정이 필요한 Choice 또는 Scene에서 Check Request를 생성할 수 있다.

개념:

```text id="ck41"
Event Choice
↓
Check
↓
Result
↓
Event Branch
```

Event는 Check Result를 이용해:

- Success
- Failure
- Great Success
- Special Branch

등을 결정할 수 있다.

---

# 27. Exploration Integration

Exploration에서 Check는:

- 위험 발견
- 탐색
- 구조
- 자원 발견
- 특수 보상

등의 결과에 사용될 수 있다.

Exploration System은 판정 결과에 따라 실제 Reward를 결정한다.

---

# 28. NPC Behavior Integration

NPC Behavior System 역시 필요에 따라 Check를 사용할 수 있다.

예:

```text id="ck42"
Command Resistance
Fear Resistance
Special Behavior Trigger
```

그러나 모든 NPC 행동을 반드시 Dice Check로 해결해야 하는 것은 아니다.

Behavior System은 Utility / Rule / Threshold 기반 결정을 사용할 수 있다.

---

# 29. Check Is Not Decision AI

다음 개념은 구분한다.

```text id="ck43"
Check
≠
AI Decision
```

Check는 불확실한 결과를 판정하는 Resolution Tool이다.

AI가 무엇을 선택할지 결정하는 것은 NPC / Monster Behavior System이 소유한다.

---

# 30. Check Is Not Event Logic

Check System은:

```text id="ck44"
어떤 판정을 해야 하는가?
왜 판정하는가?
성공하면 무엇이 발생하는가?
```

를 결정하지 않는다.

Consumer가 Check Request를 만들고 결과를 해석한다.

Check System은 Resolution만 수행한다.

---

# 31. Legacy d6 Success Pool

기존 Combat v0.3.x에는 다음 판정 구조가 있었다.

```text id="ck45"
관련 능력치만큼 d6
4+ = 성공
성공 수 >= 요구 성공 수
```

이 구조는 현행 판정 시스템의 정본이 아니다.

분류:

```text id="ck46"
LEGACY CHECK MODEL
```

Combat 또는 다른 시스템에서 신규 구현 기준으로 사용하지 않는다.

---

# 32. Legacy DC System

기존 NPC Stats 및 Event 문서에는:

```text id="ck47"
stat
dc
modifier
```

구조가 존재한다.

예:

```yaml id="ck48"
check:
  stat: Search
  dc: 12
```

이 데이터는 현재 즉시 폐기하지 않는다.

기존 Event 콘텐츠 Migration을 위한 Legacy Data로 유지한다.

---

# 33. Legacy Modifier Expressions

기존 문서에 다음 표현이 존재할 수 있다.

```text id="ck49"
+2 Dice
-1 Dice
DC +2
Modifier -1.5
```

이들은 모두 과거 Check System에 종속된 표현이다.

현재 Core Contract로 직접 해석하지 않는다.

관련 Owner 문서를 Migration할 때 현행 Modifier 형태로 변환한다.

---

# 34. Migration Principle

기존 모든 Event / Skill / Quirk / Status 데이터를 한 번에 변경하지 않는다.

Progressive Migration을 사용한다.

절차:

```text id="ck50"
Legacy Data 발견
↓
현재 Owner 확인
↓
관련 문서 Audit
↓
현행 Check Contract에 맞게 변환
↓
승인
```

---

# 35. Legacy Event Migration

기존 Event의:

```yaml id="ck51"
mode: stat_check
check:
  stat: 정신력
  dc: 13
  modifiers:
```

같은 구조는 내용 자산 자체를 버리지 않는다.

향후 현행 Schema로 Migration한다.

예시 개념:

```yaml id="ck52"
check:
  source:
    type: state
    id: Sanity
  difficulty: Hard
```

또는:

```yaml id="ck53"
check:
  source:
    type: state
    id: Sanity
  requirement: 14
```

정확한 Event Schema는 Event System이 소유한다.

---

# 36. Determinism and Testing

동일한 입력과 필요한 모든 Roll 결과(적용 시 Fate Override Roll 포함)가 주어지면 Check 계산 결과는 동일해야 한다.

따라서 Check Core Logic은 가능한 한:

```text id="ck54"
Pure / Deterministic Resolution
```

형태로 구현하는 것을 권장한다.

Random Roll 생성과 Resolution 계산을 분리하면 테스트가 쉬워진다.

예:

```text id="ck55"
Dice Provider
↓
Roll Value

Check Resolver
↓
Result
```

구체적인 Architecture는 Technical Specification에서 결정한다.

---

# 37. Multiplayer Boundary

향후 Host-Authoritative Multiplayer 환경에서는 최종 Check 결과의 권위는 Host가 가져야 한다.

Client가 독립적으로 Roll을 확정해서는 안 된다.

개념적으로:

```text id="ck56"
Client Action Request
↓
Host Check Resolution
↓
Authoritative Result
```

정확한 Networking 구현은 Multiplayer Technical Specification이 소유한다.

---

# 38. Save Boundary

일반적인 Check 자체는 영구 State가 아니다.

따라서 모든 Roll 결과를 Save해야 하는 것은 아니다.

필요한 경우:

- Event History
- Combat Log
- Replay
- Achievement

등이 Check Result를 기록할 수 있다.

Save 정책은 해당 Owner가 정의한다.

---

# 39. Ownership Summary

Check System owns:

```text id="ck57"
1d12 Base Roll
Check Request
Check Source
Modifier Aggregation
Requirement Comparison
Success / Failure
Margin
Check Result
Difficulty Tier Semantics
Difficulty Requirement Mapping
Composite Source Calculation
Fate Override Resolution
```

Check System does not own:

```text id="ck58"
NPC Stat Definition
Modifier Source Values
Combat Damage
Event Branch
Reward
Skill Effect
Quirk Effect
Emotion Effect
AI Decision
Consumer-owned Critical Outcome
```

---

# 40. Current Undefined Requirements

다음은 의도적으로 미확정 상태로 둔다.

```text id="ck59"
Universal Great Success Threshold
Universal Great Failure Threshold
Opposed Check Formula
Fractional Modifier Support
Weighted Composite
```

이 항목은 별도 Balance / Feature Review 후 확정한다.

---

# 41. Stability Rule

다음 변경은 일반적으로 Check Core 변경을 요구하지 않는다.

- 신규 Skill
- 신규 Event
- 신규 Monster
- 신규 Quirk
- Modifier 값 변경
- Combat Damage 변경
- Reward 변경

다음 변경은 Check Core 재검토가 필요하다.

- 기본 Dice 변경
- 성공 비교 공식 변경
- Check Source 구조 변경
- Modifier Aggregation 방식 변경
- Margin 제거
- Difficulty 의미 변경

---

# 42. Migration Notes

현재 프로젝트에서 다음 판정 세대가 혼재한다.

```text id="ck60"
Legacy DC
Legacy d6 Success Pool
Legacy Dice Modifier
Current 1d12 Resolution
```

현행 기준은:

```text id="ck61"
1d12
+
Check Source
+
Integer Modifiers
>=
Requirement
```

이다.

과거 판정 방식은 Reference / Migration Source로만 사용한다.

---

# 43. Final Principle

Check System의 목적은:

> 각 Feature가 자신만의 주사위 규칙을 만드는 것

을 방지하는 것이다.

모든 Gameplay System은 동일한 Resolution Contract를 공유하고,

각 System은:

> 무엇을 판정할 것인가

와:

> 판정 결과로 무엇이 발생하는가

만 소유한다.

Check System은 그 사이의 불확실한 결과를 일관되게 해결한다.
