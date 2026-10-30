---
id: MECH_Monster_AI
title: Downfall Monster Combat AI System
type: mechanic
authority: CURRENT
status: APPROVED
version: 2.0.0

parent:
  - MECH_Combat_System

references:
  - MECH_Encounter_Resolution_System
  - MECH_Combat_Action_System
  - MECH_Combat_Status_Effect_System
  - DATA_Monster_Action_Catalog
  - DATA_Combat_Status_Effect_Catalog
  - MONSTER_DB

summary: >
  Hostile Encounter에서 Monster가 사용 가능한 Combat Action을 Context와 AI Profile,
  Action 특성 및 Weighted Random을 통해 선택하는 공통 계약을 정의한다.

tags:
  - mechanic
  - monster
  - ai
  - combat

keywords:
  - Monster AI
  - Action Selection
  - Eligibility
  - AI Profile
  - Weighted Random
  - Telegraph
  - Cooldown
  - Prepared Action

last_updated: 2026-10-28
---

# Downfall Monster Combat AI System

## 1. Purpose

본 문서는 Hostile Encounter 안에서 Monster가 현재 사용 가능한 Combat Action 중 하나를
상황, AI Profile, Action 특성과 약간의 불확실성에 따라 선택하는 공통 AI 계약을 정의한다.

Monster AI는 선택을 담당한다. Encounter Resolution, Negotiation, Action Effect,
Check 공식, Damage 공식과 Optional Module의 세부 규칙을 직접 소유하지 않는다.

---

# 2. Ownership

Monster AI owns:

```text
Combat Action candidate selection
Action eligibility 결과 소비
Context evaluation
AI Profile preference
Target preference
Action weight evaluation
Weighted random selection
Prepared Action priority
Simple / Advanced AI extension boundary
Monster-specific AI State extension boundary
```

Monster AI does not own:

```text
Encounter State / Stance / Intent / Escalation
Negotiation / Dialogue / Faction / Relationship
Combat Action Definition / Action Effect
Damage Formula / Check Formula / Status Definition
Cooldown Runtime state / Prepared Action Runtime state
Positioning rules
R18-specific Gauge / Action / Transition
Save Schema
```

---

# 3. Encounter Boundary

Monster Combat AI는 Encounter State를 결정하지 않는다.
Encounter Resolution System이 제공하는 Context를 소비한다.

```text
Encounter = Hostile → Monster Combat AI may act
Encounter = NonHostile → normal Combat Action AI inactive
Encounter = Transition → Encounter Response Logic 영역
Encounter = Resolved → Monster Combat AI inactive
```

Opening에서의 반응도 Encounter의 책임 경계에 속한다. 일반 Combat Action Selection은 Hostile에서만 활성화된다.
Monster AI는 Gold 비용, Fame, Faction Reputation, Negotiation Requirement 또는 De-escalation을 계산하지 않는다.

---

# 4. Intent and Player Actions

Legacy v1.0의 `공격적 대처 / 방어적 대처` 분류를 현행 Encounter Intent로 사용하지 않는다.

```text
Defense Action ≠ Non-Hostile Intent
```

AI가 플레이어 입력을 공격적 / 방어적으로 재분류하여 Encounter 방향을 결정하지 않는다.
필요한 전투 Context는 Combat / Encounter / Action Result가 구조화하여 제공한다.
Hostile / Non-Hostile Intent와 Escalation은 Encounter Owner가 관리한다.

---

# 5. Core Selection Pipeline

```text
Monster Activation
↓
Encounter Hostile Context 확인
↓
Prepared Action 확인
↓
Available Action IDs 수집
↓
Eligibility Filter
↓
Target Candidates
↓
Context Evaluation
↓
AI Profile Modifier
↓
Action Weight 계산
↓
Weighted Random Selection
↓
Selected Action
↓
Combat / Action Resolver
```

Prepared Action이 있다면 일반 후보 추첨 전에 우선 처리한다.
정확한 함수명과 API는 TECH_SPEC가 정의한다.
정상 Eligibility 이후 사용 가능한 후보가 없다면 `MECH_Combat_Action_Runtime_System`의
Cooldown-only Fallback을 사용할 수 있다. 일반 후보와 Cooldown-only 후보가 모두 없는 경우는 미정이다.

---

# 6. Available Action Source

Monster AI는 Action을 직접 정의하지 않는다.
Monster Definition 또는 Runtime Participant가 제공하는 Action ID references를 입력으로 받는다.

Action Definition은 `DATA_Monster_Action_Catalog` 및 해당 Action Owner가 소유한다.
AI는 동일 Action의 효과를 복제하지 않는다.
현재 Data Catalog가 `CURRENT_CANDIDATE / REVIEW`인 점과 개별 데이터의 승인 여부는 별도로 확인한다.

---

# 7. Eligibility Filtering

사용할 수 없는 Action은 평가 전에 제외한다.
Eligibility 입력은 다음을 포함할 수 있다.

```text
Action Requirements
Cooldown
Target Availability
Position / Range
Required Status
Required Equipment
Encounter State
Prepared State
Usage Limit
Other Runtime Locks
```

AI는 조건의 의미나 계산을 재구현하지 않는다. 각 Owner가 제공하는 eligibility 결과를 소비한다.
Target Candidates 역시 각 Action과 관련 Owner가 제공하는 유효 범위에서 평가한다.

---

# 8. Cooldown

Director 승인 방향:

```text
Cooldown Unit = Round
```

Action별 Cooldown은 차등 적용할 수 있다. 반복 행동을 억제하고 Monster 패턴을 형성하며,
플레이어가 재사용 시점을 추론하고 Strong / Signature Action에 대응할 수 있게 한다.

AI가 Cooldown 값을 직접 감소시키지 않는다. `MECH_Combat_Action_Runtime_System`이 Cooldown Remaining을 관리하고,
AI는 Cooldown active → candidate 제외라는 eligibility 결과만 소비한다.

```text
Cooldown = 사용 가능 여부
AI Weight = 사용 가능한 Action 중 선택 선호도
```

Cooldown이 끝났다고 Action을 반드시 선택하지 않는다.
Action별 수치와 구체 Tick 이벤트 / 구현 순서는 후속 TECH_SPEC에서 확정한다.
Cooldown의 Round 기준과 완전한 Round 차단 의미는 Action Runtime Contract를 따른다.

---

# 9. Role / Tier / Threat

Legacy 약기술 / 강기술의 플레이 경험은 보존하되 개념을 분리한다.

```text
Role = Action 기능
Tier = Action의 희소성 / 특수성
Threat = 플레이어 대응이 요구되는 위험 수준
```

예: `Role: Attack / Tier: Signature / Threat: Strong`.
정확한 필드 Schema는 Combat Action 후속 Data 검토에서 확정한다.
Monster AI Contract는 이 구분을 소비할 수 있다는 것만 정의한다.

---

# 10. Weak Action

일반적인 전투 흐름을 유지하는 행동이다.
낮은 위협, 짧거나 없는 Cooldown, Telegraph 불필요 가능성과
기본 Attack / Control / Movement는 특성 후보다.

모든 Basic Action이 반드시 Weak이라는 규칙을 만들지 않는다.

---

# 11. Strong Action

플레이어가 인지하고 대응할 가치가 있는 고위험 행동이다.
Telegraph, Requirement, Cooldown, Prepared Action을 사용할 수 있지만
모든 Strong Action이 동일한 구조를 사용해야 하는 것은 아니다.

---

# 12. Telegraph

Strong Action은 Telegraph를 사용할 수 있으며, Telegraph는 플레이어가 대응 가능한 정보여야 한다.
반드시 독립된 빈 준비 턴을 뜻하지 않는다. 선행 Action 성공 자체가 Telegraph를 생성할 수 있다.

```text
Grab 성공 → ST_Bound + Death Roll Telegraph
```

플레이어가 위험한 Action의 준비, 파훼할 Requirement와 다음 Round의 위험을 추론할 수 있게 한다.
Presentation 구현은 별도 Owner가 담당한다. 위 예시는 신규 Action ID나 개별 효과 승인에 해당하지 않는다.

---

# 13. Prepared Action

Telegraph 이후 다음 Round 등에 실행 예정인 Strong Action은 개념적으로 Prepared Action 상태를 사용할 수 있다.

```text
Prepared Action: Death Roll 예시
Target: 대상
Required Status: ST_Bound
```

Action ID, Target과 Requirement의 정확한 Runtime Schema는 본 문서에서 확정하지 않는다.
Prepared Action Runtime 상태는 AI가 아닌 `MECH_Combat_Action_Runtime_System`이 소유한다.

---

# 14. Prepared Action Priority and Revalidation

Prepared Action이 있으면 일반 Weighted Selection보다 우선 평가한다.
일반 후보와 같은 가중치 추첨에 다시 넣지 않는 방향을 기본으로 한다.

```text
Monster Activation
↓
Prepared Action exists?
├─ no → normal Action selection
└─ yes → Requirement revalidation
```

실행 전 Requirement를 다시 검사한다. 예를 들어 다음 Round에 Target의 ST_Bound가 여전히 유효한지 확인한다.
실제 Requirement 의미와 평가 결과는 해당 Owner가 제공한다.

---

# 15. Prepared Action Execution / Fizzle

Requirement가 유지되면 Prepared Action을 실행한다.
Damage, Check와 Effect Resolution은 Combat / Action System이 수행한다.

Requirement가 파훼되면:

```text
Prepared Action Fizzle
+
Monster Activation Consumed
```

Monster는 즉시 다른 Action을 대신 선택하지 않는다.
Telegraph 발견 → 위험 조건 파악 → 공격 욕심과 파훼 사이의 선택 → 정확한 파훼 → 괴물 행동 손실은
플레이어에게 유리한 대응 기회를 제공하는 Risk / Reward 구조다.

---

# 16. Fizzle and Cooldown

Fizzle 시 기본값은 Full Cooldown이다. 승인된 Action-specific override를 허용할 수 있다.
등록 및 상세 경계는 `MECH_Combat_Action_Runtime_System`이 소유한다.

---

# 17. Action Weight

일반 선택에서 각 후보는 Context에 따라 Weight를 가질 수 있다.
개념적으로 다음 입력이 기여할 수 있다.

```text
Base Action Weight
AI Profile Preference
Target Context
Self Context
Encounter Combat Context
Optional Action-specific Modifier
```

이는 입력 관계의 개념 설명이다. 정확한 산식, 연산 방식, Clamp와 수치는 Core Contract에서 확정하지 않는다.

---

# 18. Weighted Random

AI는 항상 최고 Weight Action만 선택하지 않는다.
충분히 선호되는 행동은 더 자주 선택하되 완전히 결정적이지 않게 한다.

```text
Bite       40
Grab       30
TailSwipe  20
Backstep   10
```

위 숫자는 개념 예시이며 밸런스 값이 아니다. 실제 수치는 Data / Balance Layer가 정의한다.
Weighted Random은 반복 패턴을 줄이면서 Monster의 학습 가능한 성향과 결과의 불확실성을 유지한다.
Random Source의 실제 구현은 TECH_SPEC에서 정의한다.

---

# 19. AI Profile

기존 `ai_profile` 개념을 유지한다. Monster Definition은 Profile ID를 참조할 수 있다.

```text
ai_profile: AI_Predator
```

Profile은 행동 평가 성향을 제공하며 Action Definition을 소유하지 않는다.

---

# 20. Legacy Profile Migration

다음 기존 ID는 Migration 후보로 보존한다.

```text
AI_Cautious
AI_Aggressive
AI_Predator
AI_Fanatic
AI_Opportunist
```

기존 `rage_gain_mult`, R18 Action Preference, 세 Gauge 전용 Weight를 현행 Profile 규칙으로 자동 승인하지 않는다.
실제 Profile Data Migration은 별도 후속 작업이다. 기존 ID를 이번 작업에서 변경하지 않는다.

---

# 21. Profile Preference

Profile은 다음 Preference를 표현할 수 있다.

```text
Action Role preference
Threat preference
Target preference
Low HP behavior
Distance preference
Status exploitation
Signature tendency
Defensive tendency
Movement tendency
```

정확한 필드와 값은 Data Layer가 소유한다.

---

# 22. Target Evaluation

AI는 Action 선택과 함께 Target 후보를 평가할 수 있다.
Target HP, Status, Position, Isolation, Vulnerability와 Threat는 Context 예시다.

AI는 HP 공식, Status 효과, Position 규칙이나 Threat 계산을 소유하지 않는다.
해당 Owner가 제공하는 Context를 소비한다.

---

# 23. ST_Exposed / ST_Bound Integration

승인된 방향의 `ST_Exposed`는 Vulnerability Marker다.
Profile 또는 Action은 Target이 해당 Marker를 가졌는지 보고 Target / Action Weight에 영향을 줄 수 있다.
구체 Weight는 정하지 않는다.

Target의 `ST_Bound`는 특정 Action Requirement를 충족할 수 있다.
Death Roll을 예로 들면 AI는 Requirement 결과를 소비하며 Status 의미를 복제하지 않는다.
Status Data Catalog는 현재 REVIEW이므로 개별 효과를 현행 밸런스로 자동 승인하지 않는다.

---

# 24. Distance / Positioning

AI는 melee available, ranged preferred, target out of range, movement required 같은 Context를 사용할 수 있다.
Positioning 규칙 자체는 AI가 소유하지 않는다.

Positioning Owner와 공통 Contract는 `MECH_Combat_Positioning_System`이다.
정확한 Monster Position Data와 개별 Preference는 후속 작업이다.

---

# 25. Simple AI

대부분의 일반 Monster는 단순 AI를 사용한다.

```text
Eligibility Filter
+
Profile Weight
+
Small Context Modifiers
+
Weighted Random
```

일반 Monster에 복잡한 장기 전략 탐색을 기본 적용하지 않는다.

---

# 26. Advanced AI

Named / High Intelligence / Ruin Monster는 Advanced AI Extension을 사용할 수 있다.
Phase, Action Sequence, Combo, Target Priority, Reaction, Scripted Tactical Rule,
Conditional Plan을 추가할 수 있으며 Core Simple AI를 깨뜨리지 않고 확장한다.

Advanced AI는 어떤 Action을 언제 선택할지 결정한다.
Action이 무엇을 하는지는 Action System이 소유한다.

---

# 27. Monster-specific AI State

특정 Monster 또는 Profile은 Rage, Alertness, Hunger, Aggression, Special Phase State를 가질 수 있다.
이를 모든 Monster가 반드시 가져야 하는 Core Gauge로 만들지 않는다.

Legacy Rage는 Optional / Monster-specific AI State 후보로 재분류한다.
기존의 공통 필수 Gauge, 구체 수치와 상승 공식은 현행 승인하지 않는다.

Legacy Intimidation도 공통 Core Gauge에서 제거한다.
Profile-specific State, Encounter Context response 또는 Special Monster State 후보로 후속 재설계할 수 있다.
현행 Core Runtime State로 승인하지 않는다.

---

# 28. Core / Optional AI Boundary

Arousal과 R18 Submission / Skill 의존은 Core Monster AI에서 제거한다.

```text
Optional R18 AI Extension
↓ depends on
Core Monster AI
```

Core AI는 Arousal, Submission Gauge, R18 Skill, R18 Transition을 필수 Runtime State로 알지 않는다.
Optional Module은 추가 Action Candidate, Weight Modifier, Target Preference,
Optional Prepared Action을 AI 평가에 확장할 수 있다.

Core가 Modifier의 R18 의미를 이해할 필요는 없다. 정확한 Extension API는 TECH_SPEC에서 정의한다.

---

# 29. Monster Definition Boundary

`MONSTER_DB` 또는 향후 Monster Data는 Monster ID, Action IDs, AI Profile ID와
선택적인 Advanced AI Extension ID / Monster-specific AI State Definition을 참조할 수 있다.

본 문서는 개별 Monster 데이터를 복제하지 않는다. `MONSTER_DB`는 현재 REFERENCE다.

---

# 30. Action Runtime Boundary

AI가 소비하지만 직접 소유하지 않는 정보:

```text
Cooldown Remaining
Prepared Action
Usage Count
Temporary Lock
Current Target
Action Availability
```

Cooldown과 Prepared Action의 Runtime Owner는 `MECH_Combat_Action_Runtime_System`이다.
정확한 Runtime Schema와 API는 후속 TECH_SPEC에서 확정한다.
AI State에 Cooldown / Prepared Action을 중복 저장하지 않는다.

---

# 31. Runtime AI State

AI Runtime 자체는 다음을 필요로 할 수 있다.

```text
Profile Reference
Evaluation Context
Last Selected Action optional
Advanced AI State optional
Monster-specific AI State optional
```

정확한 Schema는 TECH_SPEC에서 정의한다.

---

# 32. Repetition Control

반복 억제의 1차 수단은 Action별 Cooldown이다.
`recent_action_penalty` 같은 추가 AI Weight Modifier는 후속 Data Layer에서 사용할 수 있으나
Core의 필수 규칙으로 만들지 않는다.

---

# 33. Player Learnability

Monster AI가 완전히 랜덤해서는 안 된다. 플레이어는 다음을 학습할 수 있어야 한다.

- Monster가 선호하는 Role과 가진 Strong Action
- 방금 사용한 기술의 Cooldown 여부
- Telegraph가 예고하는 Strong Action
- 파훼해야 하는 Requirement

AI Profile, Cooldown, Telegraph는 이러한 정보성을 강화한다.

---

# 34. Combat Result Boundary

AI는 `Selected Action`을 반환한다.
Combat / Action Resolver가 Check, Damage, Status, Position, Resource와 Result를 처리한다.
AI는 Combat 결과를 직접 적용하지 않는다.

---

# 35. Save / Multiplayer Boundary

AI Runtime의 Save Schema는 Save System이 소유한다. Encounter 중 Save를 지원한다면 필요한 AI State를 직렬화할 수 있다.

향후 Multiplayer의 Monster Action Selection과 Weighted Random 결과는 Host Authoritative다.
Client가 최종 Monster Action을 결정하지 않는다. 정확한 Network Sync Schema는 TECH_SPEC에서 정의한다.

---

# 36. Legacy v1.0 Audit / Migration

Audit Result: `REFACTOR`.

Preserve:

```text
AI Profile
Weighted Action Selection
Action Availability Filtering
Monster 행동 성향 차별화
Player-learnable tendencies
```

Redefine:

```text
Skill → Combat Action
Skill Category → Action Role / Tier / Threat
Rage → optional monster-specific AI state candidate
Intimidation → optional / profile-specific concept candidate
Basic / Unique / Signature fixed ratios → Profile / Data Weight
```

Remove from Core:

```text
Arousal
R18 Submission dependency
R18 Skill dependency
mandatory three-gauge architecture
Legacy offensive / defensive encounter interpretation
```

v1.0의 Gauge 계산, 비율, Profile Weight는 Legacy 자료이며 현행 밸런스로 자동 승인하지 않는다.
기존 v1.0 원문은 Git 기록에 보존한다. Legacy Consumer와 Data의 변경은 별도 Migration 작업이다.

---

# 37. Stability Rule

다음은 일반적으로 Core Contract 수정이 필요하지 않다.

- 신규 AI Profile, Profile Weight 또는 특정 Monster Profile 변경
- Action Weight, Action Cooldown 값 변경 또는 신규 Monster Action 추가
- 특정 Monster Advanced Rule 추가

다음은 Core Contract 검토가 필요하다.

- AI Selection Pipeline 변경
- Monster AI와 Encounter 책임 경계 변경
- Prepared Action 우선 처리 구조 변경
- Simple / Advanced AI 경계 변경
- Optional Module 의존 방향 변경
- Action Ownership 변경

---

# 38. Final Principle

Monster AI의 목적은 모든 전투 효과와 갈등 규칙을 한곳에서 결정하는 것이 아니다.

> Hostile 전투 Context에서 유효한 Action을 상황과 Monster의 성향에 따라 선택하고,
> 플레이어가 경향을 배우면서도 결과에 불확실성이 남도록 하는 것

이다.
