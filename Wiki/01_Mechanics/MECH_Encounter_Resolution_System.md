---
id: MECH_Encounter_Resolution_System
title: Downfall Encounter Resolution System
type: mechanic
authority: CURRENT
status: APPROVED
version: 1.0.0

parent:
  - SYS_Design_Pillars

references:
  - MECH_Combat_System
  - MECH_Check_System
  - MECH_Resource_System
  - MECH_Combat_Action_System
  - MONSTER_DB

summary: >
  Downfall의 Encounter 상태, 갈등 스탠스, 적대도 누적,
  해결 경로 가용성, 적대/비적대 전환 및 Encounter 종료 결과를 정의한다.

tags:
  - mechanic
  - encounter
  - conflict
  - resolution

keywords:
  - Encounter
  - Conflict Stance
  - Hostile
  - NonHostile
  - Escalation
  - Negotiation
  - Alternative Resolution
  - Special Resolution

last_updated: 2026-10-27
---

# Downfall Encounter Resolution System

## 1. Purpose

본 문서는 Encounter가 현재 어떤 갈등 상태이며, 플레이어가 어떤 해결 방향을 취하고 있고,
적대가 얼마나 누적되었으며, 어떤 해결 경로가 아직 가능한지를 관리하는 상위 Core Contract다.

Monster Combat AI, Dialogue·Faction·Relationship 공식, Resource 비용, R18 세부 규칙,
Telegraph / Cooldown / Prepared Action Runtime 구현은 직접 소유하지 않는다.

---

# 2. Encounter Definition

Encounter는:

> 하나 이상의 참가자가 상호작용하며 Combat, Negotiation, Escape, Trade,
> Special Resolution 등 하나 이상의 해결 경로를 가질 수 있는 갈등 단위

다.

```text
Encounter
├─ Combat 가능
├─ Negotiation 가능
├─ Escape 가능
├─ Trade / Bribe 가능
└─ Special Resolution 가능
```

Encounter와 Combat은 동일 개념이 아니다.
위 경로가 모든 Encounter에 제공된다는 의미도 아니다.

---

# 3. Encounter / Combat Boundary

Encounter는 Combat보다 상위 Context를 제공한다.

```text
Encounter
↓
현재 Resolution Mode / Conflict State
↓
Hostile이면 Combat 활성 가능
↓
Combat Result
↓
Encounter Resolution로 반환 가능
```

Combat System은 Encounter 전체 상태를 소유하지 않는다.
Encounter System도 Combat Action Resolution을 소유하지 않는다.

기존 Combat 문서의 `Combat Encounter`는 Combat 내부의 Lifecycle Context를 뜻한다.
이를 본 문서의 상위 Encounter와 동일한 상태 객체나 전체 해결 범위로 간주하지 않는다.

---

# 4. Encounter State

Core Contract는 최소 다음 상태 의미를 지원한다.

```text
Opening
Hostile
NonHostile
Transition
Resolved
```

정확한 enum 이름은 TECH_SPEC에서 결정할 수 있으나 의미는 유지한다.

---

# 5. Opening

Encounter 시작 직후 상태다.
플레이어가 아직 명확한 해결 방향을 선택하지 않았을 수 있다.

Attack, Dialogue, Trade, Threaten, Withdraw, Special Interaction 등의 선택이 가능할 수 있다.
실제 선택지는 개별 Encounter Definition과 Consumer가 결정한다.

---

# 6. Hostile

명시적인 적대 행동이 발생했거나 Combat이 활성화된 상태다.
Combat System과 Monster Combat AI가 활성화될 수 있다.

Hostile이 Negotiation의 영구 불가를 의미하지 않는다.
일부 Encounter는 Hostile에서도 De-escalation을 시도할 수 있다.

---

# 7. NonHostile

Dialogue, Negotiation, Trade 등 비적대 해결 시도가 진행되는 상태다.
이미 성공적으로 해결됐다는 의미가 아니다.

협상 실패나 배신 행동으로 Hostile로 전환될 수 있다.

---

# 8. Transition

Resolution 방향 전환을 시도하는 상태다.

```text
Hostile → NonHostile Attempt
NonHostile → Hostile
```

Transition은 즉시 성공을 의미하지 않는다.
전환 가능 여부, Escalation, 비용, Check와 외부 조건을 평가한 뒤 다음 상태가 결정된다.

---

# 9. Resolved

Encounter 종료 상태다. 가능한 Resolution Type의 예는 다음과 같다.

```text
Enemy Defeated
Escape
Enemy Withdrawal
Negotiated Resolution
Trade / Bribe Resolution
Objective Completed
Special Resolution
Defeat
```

정확한 Schema는 TECH_SPEC 또는 후속 Data 설계가 구체화한다.
Combat의 기존 Resolution Path를 중복 정의하거나 결과를 다시 계산하지 않는다.
필요하면 CombatResult를 Encounter Result로 변환한다.

---

# 10. Conflict Stance / Intent

Encounter는 플레이어의 현재 해결 방향을 표현할 수 있어야 한다.

```text
Hostile Intent
Non-Hostile Intent
Undecided
```

Legacy의 공격적 행동 / 방어적 행동을 이 Core 의미로 사용하지 않는다.
전투 중 방어 Action과 비적대 해결 의도는 서로 다르다.
정확한 Runtime 필드명은 TECH_SPEC에서 정의한다.

---

# 11. Hostile Intent

공격, 제압, 강제적 피해, 명백한 전투 행동 등 갈등을 적대적으로 해결하려는 방향이다.

Hostile Encounter 안에서 Defense / Evade는 Hostile Conflict 내부 행동일 수 있다.

```text
Defense Action ≠ Non-Hostile Intent
```

---

# 12. Non-Hostile Intent

대화, 협상, 거래, 회유, 항복 제안, 관계·명성 활용 등 직접적인 적대 전투 외 해결 방향이다.

Dialogue, Faction Reputation, Fame, Gold, Item, Check, Special Character 등의
구체적인 성공 조건은 각 Owner가 제공한다. Encounter가 직접 계산하지 않는다.

---

# 13. Escalation

현재 Hostile 여부와 별개로, 지금까지 갈등이 얼마나 심각하게 악화됐는지를 나타낸다.

```text
Escalation ≠ Monster Emotion ≠ Monster Rage
```

Escalation은 Encounter 전체의 갈등 역사다.
초기 해결 경로 선택, 전환 비용, 협상 가용성, 배신의 후속 효과와
심각한 교전 이후 해결 경로 폐쇄를 위한 상위 Context다.

---

# 14. Escalation Inputs

다음 사건이 Escalation 입력이 될 수 있다.

```text
Hostile Action Attempt
Actual Damage
Severe Damage
Strong / Signature Action
Participant Injury
Participant Death
Betrayal Attack
Repeated Hostile Intent
```

Weapon Lowered, Surrender Offer, Ceasefire, Return Hostage,
Compensation, Medical Assistance 등은 De-escalation 입력이 될 수 있다.

이번 Core Contract는 행동별 증감 수치를 정의하지 않는다.

---

# 15. Escalation Representation

내부 표현은 Numeric Value 또는 Low / Medium / High / Critical 같은 단계일 수 있다.
정확한 Scale과 Threshold는 확정하지 않는다.

확정되는 계약은 Escalation이 누적되고 Resolution Path에 영향을 줄 수 있다는 것이다.

---

# 16. Late Stance Change Penalty

플레이어는 Encounter 초기에 해결 스탠스를 선택하는 것이 유리해야 한다.
Hostile 행동을 지속하다 불리해진 뒤 비적대 해결로 전환하려 하면
De-escalation Cost가 증가할 수 있다.

가능한 패널티는 다음과 같다.

```text
Higher Check Requirement
Additional Gold
Faction Reputation Requirement
Fame Requirement
Item / Resource Concession
Surrender Condition
Weapon Surrender
Special NPC Requirement
Resolution Path Closure
```

정확한 수치와 조합은 개별 Encounter / Dialogue / Faction / Resource Owner가 정의한다.
Core는 이러한 패널티를 지원하는 구조만 소유한다.

---

# 17. Cost Before Hard Lock

스탠스 변경은 가능하지만 늦을수록 비싸지는 구조를 기본 철학으로 우선한다.

다만 Participant Death, Critical Betrayal, Narrative No-Return Condition 등
특정 사건 이후 경로가 완전히 닫힐 수 있으며 개별 Encounter가 이를 선언할 수 있다.
모든 Encounter에 동일한 Hard Lock을 강제하지 않는다.

---

# 18. Recent Intent History

Runtime은 최근 플레이어 행동의 해결 의도를 짧게 추적할 수 있다.

```text
Recent Intent History: [Hostile, Hostile, NonHostile]
```

일관된 방향 판단, 갑작스러운 전환 패널티, Betrayal 판단과 Negotiation Context 제공이 목적이다.
저장 개수와 Runtime Schema는 TECH_SPEC가 정한다.
장기 NPC Memory System과 동일한 기능으로 만들지 않는다.

---

# 19. Betrayal

NonHostile Interaction 도중 적대 행동을 시작하면 Betrayal Context Flag가 발생할 수 있다.

Escalation 급증, 향후 Negotiation 불리, Faction / Relationship 영향 후보와
Special Event Trigger로 사용될 수 있다.
실제 Reputation 수치 변경은 해당 Owner가 처리한다.

---

# 20. Hostile → NonHostile Transition

Dialogue나 Negotiation을 선택해도 즉시 Combat이 종료되지 않는다.
Prepared Action Pending 동안에는 플레이어가 자발적인 De-escalation / Negotiation 전환을 시작할 수 없다.
Prepared Action이 Execute 또는 Fizzle된 후 시도할 수 있다. 강제 Encounter 종료는 이 Lock을 우회할 수 있다.
Prepared 상태와 Lock의 공통 계약은 `MECH_Combat_Action_Runtime_System`을 따른다.

```text
Player requests de-escalation
↓
Encounter validates Resolution Path
↓
Escalation / History Context 제공
↓
Dialogue / Faction / Resource / Check Owner 평가
↓
Success → NonHostile 또는 Resolved
Failure → Hostile 유지
```

---

# 21. NonHostile → Hostile Transition

비적대 상태에서 공격을 선언하면 Hostile 전환이 가능하다.
Betrayal Context, Escalation, Previous Negotiation State를 기록할 수 있다.

Combat 시작 자체는 Combat System이 담당한다.

---

# 22. Resolution Capabilities

모든 Encounter / Monster가 동일한 해결 경로를 제공한다고 가정하지 않는다.
개별 Encounter 또는 관련 Entity Definition이 지원 가능한 Capability를 선언할 수 있다.

```text
Combat
Escape
Negotiation
Trade
Bribe
Intimidation
Surrender
Special
```

Optional Module은 추가 Capability를 확장할 수 있다.
정확한 Data Schema는 후속 Data Contract가 정의한다.

---

# 23. Capability Examples

인간형 적대 세력은 Combat / Negotiation / Trade / Bribe / Withdrawal을,
본능형 괴물은 Combat / Escape / Special을 제공할 수 있다.

이는 개념 설명이며 특정 Monster의 현행 설정이나 모든 인간형의 협상 가능성을 승인하지 않는다.

---

# 24. Consumer Ownership

Faction Reputation, Fame, Gold, Dialogue Ability, Check Result, Relationship, Item은 각 Owner가 제공한다.
Encounter는 Resolution Requirement Evaluation Request와 결과 조정만 담당한다.

---

# 25. Resource Boundary

Gold나 다른 Resource가 Negotiation 비용이 될 수 있으나 Encounter가 Resource State를 직접 변경하지 않는다.

```text
Encounter Resolution Attempt
↓
Resource Requirement
↓
Resource System validation
↓
Spend
↓
Result returned
```

---

# 26. Check Boundary

Negotiation / Intimidation / De-escalation에 Check가 필요하면 `MECH_Check_System`을 사용한다.
Encounter는 Dice 공식이나 Requirement Table을 복제하지 않는다.

Escalation이 Requirement나 Modifier에 영향을 줄 수 있지만
구체 수치, Modifier 값과 Requirement 계산은 후속 Balance / Data Owner가 정의한다.

---

# 27. Faction / Relationship Boundary

Faction Reputation이나 Relationship이 해결 조건이 될 수 있다.
Encounter는 Reputation Threshold나 Relationship Calculation을 소유하지 않는다.
해당 Owner에게 질의하고 결과만 소비한다.

---

# 28. Monster AI Boundary

Monster Combat AI는 Encounter Stance를 결정하지 않고 Encounter Context를 읽는다.

```text
Encounter = Hostile → Monster Combat AI active 가능
Encounter = NonHostile → normal Combat Action AI inactive
Encounter = Transition → Encounter Response Logic 사용 가능
```

Monster AI는 Negotiation 가격, Fame Requirement, Gold Cost를 계산하지 않는다.
전투 Action 선택과 Encounter 해결 방향 조정을 분리한다.

---

# 29. Encounter Response Logic

Transition에서 상대는 Accept / Reject / Counteroffer / Threaten / Withdraw / Attack으로 반응할 수 있다.
이는 Monster Combat Action AI와 다른 책임이다.
정확한 Response AI / Dialogue AI 설계는 본 문서 범위 밖이다.

---

# 30. Combat Resolution Integration

Combat이 Enemy Defeated / Escape / Enemy Withdrawal / Objective Completed /
Special Resolution / Defeat 결과를 반환하면 Encounter는 최종 해결 결과로 변환할 수 있다.

Combat 결과를 다시 판정하거나 중복 계산하지 않는다.

---

# 31. Core / Optional R18 Boundary

```text
Optional R18 Encounter Extension
↓ depends on
Encounter Resolution System
```

Core에서 Optional R18로 의존하는 반대 방향은 금지한다.
Optional Module은 Alternative Resolution 확장으로 Seduction, Submission Transition,
R18 Alternative Combat Phase 등을 제공할 수 있다.

Core는 Arousal, R18 Gauge, Submission 세부 규칙이나 R18 Action을 필수로 알지 않는다.
Optional Gauge와 데이터는 Module이 소유하며 Core Encounter나 Core Monster AI의 필수 Runtime State에 넣지 않는다.

---

# 32. Encounter Runtime Context

개념적으로 Runtime은 다음 정보를 가질 수 있다.

```text
Encounter State
Current Intent / Stance
Escalation
Recent Intent History
Available Resolution Paths
Context Flags
Participants
```

정확한 C# Schema는 TECH_SPEC에서 정의한다.

---

# 33. Definition vs Runtime

Definition은 Encounter ID, Allowed Resolution Capabilities, Special Conditions,
Participant Rules 같은 정적 정보를 가진다.

Runtime은 Current State, Escalation, Recent Intent History, Current Resolution Attempt,
Closed Resolution Paths, Context Flags 같은 현재 상태다.

둘을 분리하며 Save Schema는 별도 Owner가 소유한다.

---

# 34. Resolution Result

종료 결과는 개념적으로 다음 Context를 반환할 수 있다.

```text
Resolution Type
Participants
Resolution Path Used
Escalation Final State
Consumed Resources
Relationship / Faction Result Requests
Combat Result Reference
Flags
Special Consequences
```

정확한 Schema는 TECH_SPEC가 정의한다.
결과 요청을 포함한다고 해서 해당 Owner의 State를 Encounter가 직접 수정하지 않는다.

---

# 35. Follow-up Combat Decisions

다음은 Director가 승인한 전투 설계 방향이다.
Encounter가 Runtime을 직접 소유하지 않으며 공통 Runtime 계약은 `MECH_Combat_Action_Runtime_System`을 따른다.

- Strong Action은 Telegraph를 사용할 수 있다.
- Telegraph는 반드시 독립된 빈 준비 턴을 소비하지 않는다. 선행 Action 성공이 동시에 Telegraph를 생성할 수 있다.
- Cooldown Unit은 Round다.
- 전조 후 다음 Round 실행 예정 상태는 Prepared Action 개념으로 관리하는 것을 권장한다.
- Prepared Action 실행 전에 Requirement를 다시 검사한다.
- Requirement가 깨지면 Prepared Action Fizzle이 발생하고 Monster Activation이 소비된다.

개념 예:

```text
Grab 성공 → ST_Bound → Death Roll Telegraph
↓
다음 Round: Bound Requirement 재검사
├─ 유효 → Death Roll
└─ 무효 → Prepared Action Fizzle + Monster Activation Consumed
```

이 예시는 기존 Action의 ID, Definition이나 밸런스를 수정하지 않는다.
Fizzle Cooldown은 기본적으로 Full이며 승인된 Action-specific override를 허용할 수 있다.
Action별 Cooldown 수치, Runtime 필드명, 구체 Tick 이벤트와 정확한 Schema는 후속 Data / TECH_SPEC가 소유한다.

---

# 36. Ownership Summary

MECH_Encounter_Resolution_System owns:

```text
Encounter concept / lifecycle / State
Conflict Stance / Intent
Escalation
Recent Intent History concept
Resolution Capabilities
Resolution Path Availability
Hostile ↔ NonHostile Transition
Late Stance Change Penalty concept
Betrayal context
Alternative Resolution coordination
Encounter Resolution Result boundary
Core / Optional Resolution boundary
```

Does not own:

```text
Combat Action Resolution
Monster Combat Action Selection / AI Weight
Dialogue formula
Faction Reputation / Relationship formula
Resource balance
Check formula
Damage formula
Position rules
R18-specific rules
Telegraph / Cooldown / Prepared Action Runtime
Save Schema
```

---

# 37. Stability Rule

다음 변경은 일반적으로 Core Contract 수정이 필요하지 않다.

- 신규 Encounter 추가
- 특정 Encounter의 Gold 비용 변경
- Negotiation Requirement 조정
- 특정 Monster의 Resolution Capability 변경
- Faction Requirement 변경
- 새로운 Special Resolution 추가

다음 변경은 Core Contract 검토가 필요하다.

- Encounter / Combat 관계 변경
- Stance / Intent 의미 변경
- Escalation 역할 변경
- Resolution Capability 구조 변경
- Hostile ↔ NonHostile Transition 모델 변경
- Optional Module 의존 방향 변경

---

# 38. Existing Document / Follow-up Boundaries

기존 Combat / AI / Monster / Resource 문서는 이번 작업에서 수정하지 않는다.
기존 Combat Encounter 표현은 상위 Encounter와의 경계를 후속 정리해야 한다.
Legacy 공격·방어 대처와 Monster Gauge를 Encounter Intent나 Escalation의 정본으로 사용하지 않는다.

구체 Escalation Scale / Threshold, Negotiation Balance, Encounter Response Logic은 후속 Owner 작업이다.
Encounter Resolution, Monster AI와 Action Runtime 공통 계약에 이어 Positioning을 검토한다.
이 흐름은 기존 전체 Audit Queue를 대체하지 않으며 Director가 우선순위를 조정할 수 있다.

---

# 39. Final Principle

Encounter Resolution System은 모든 해결 공식을 직접 계산하는 중앙 시스템이 아니다.

목적은:

> 현재 갈등 상태와 해결 의도, 누적된 적대 역사와 가능한 해결 경로를 유지하고,
> 각 Owner의 평가와 결과를 조정하여 Encounter를 일관되게 해결하는 것

이다.
