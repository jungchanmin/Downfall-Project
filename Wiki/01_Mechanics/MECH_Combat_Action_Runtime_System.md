---
id: MECH_Combat_Action_Runtime_System
title: Downfall Combat Action Runtime System
type: mechanic
authority: CURRENT
status: APPROVED
version: 1.0.0

parent:
  - MECH_Combat_Action_System

references:
  - MECH_Combat_System
  - MECH_Monster_AI
  - MECH_Encounter_Resolution_System
  - MECH_Combat_Status_Effect_System
  - DATA_Monster_Action_Catalog

summary: >
  Combat Action의 전투 중 Runtime State, Round 기반 Cooldown,
  Prepared Action, Telegraph 연계, Fizzle, 사용 이력 및 Runtime Cleanup을 정의한다.

tags:
  - mechanic
  - combat
  - action
  - runtime

keywords:
  - Action Runtime
  - Cooldown
  - Prepared Action
  - Telegraph
  - Fizzle
  - Last Used Round
  - Activation

last_updated: 2026-10-28
---

# Downfall Combat Action Runtime System

## 1. Purpose

본 문서는 Combat Action Definition과 전투 중 Runtime State를 분리하고,
Cooldown, Prepared Action, Telegraph 연계, Fizzle, Action History와 Runtime Cleanup의 공통 계약을 정의한다.

개별 Action의 Damage, Check Requirement, Positioning 규칙, AI Profile 수치와 Telegraph 문장은 확정하지 않는다.

---

# 2. Ownership

본 시스템이 소유하는 영역:

```text
Action Runtime State
Cooldown Lifecycle
Last Used Round
Usage Count
Prepared Action Runtime / Prepared Target
Prepared Requirement Revalidation
Fizzle
Runtime Action Lock
Cooldown Fallback
Combat End Cleanup
Combat Log Event Boundary
```

본 시스템이 소유하지 않는 영역:

```text
Action Definition / Action Effect
Damage Formula / Check Formula
Monster AI Weight / AI Profile
Position Rules / Status Definition
Encounter Resolution
R18-specific Rules
Save Schema
```

---

# 3. Definition vs Runtime

Action Definition은 Action ID, Role, Tier, Threat, Requirements, Cooldown Value,
Telegraph Metadata, Prepared Trigger Metadata와 Effects 같은 정적 정보를 제공할 수 있다.

Runtime은 Cooldown Remaining, Last Used Round, Usage Count, Prepared State,
Prepared Target과 Temporary Lock 같은 전투 중 상태다.

Definition에 현재 Cooldown이나 Prepared 상태를 저장하지 않는다.
개별 정의와 값은 Action Definition / Data Owner가 소유한다.

---

# 4. Cooldown — Round Contract

Director 승인: `Cooldown Unit = Round`.

Cooldown N은 Action 사용 이후 **N개의 완전한 Round 동안** 해당 Action을 다시 사용할 수 없음을 의미한다.

```text
Cooldown = 1
Round 3: Action 사용
Round 4: 사용 불가
Round 5: 사용 가능

Cooldown = 2
Round 3: Action 사용
Round 4: 사용 불가
Round 5: 사용 불가
Round 6: 사용 가능
```

---

# 5. Cooldown Tick / Ready Condition

사용 직후 Cooldown을 등록하고, 이후 완전한 Round가 경과할 때마다 1씩 감소한다.
사용한 Round의 남은 부분은 차단해야 하는 완전한 Round로 계산하지 않는다.

```text
Cooldown Remaining == 0 → Cooldown 관점에서 사용 가능
Cooldown Remaining > 0  → 사용 불가
```

Tick 이벤트 이름과 구현 순서는 TECH_SPEC가 정한다.
어떤 구현도 위 CD1 / CD2 예시와 N개의 완전 Round 차단 의미를 바꿀 수 없다.

---

# 6. Cooldown vs AI Weight

```text
Cooldown = 사용 가능 여부
AI Weight = 사용 가능한 Action 중 선택 선호도
```

Cooldown이 종료됐다고 AI가 해당 Action을 반드시 선택하지 않는다.
Runtime은 Cooldown 상태와 Eligibility 결과를 제공하며 Monster AI는 선택을 담당한다.

---

# 7. Last Used Round / Usage History

각 Runtime Action은 필요할 경우 `last_used_round` 개념을 가질 수 있다.
Cooldown Fallback, 행동 이력 추적, 디버깅과 플레이어 패턴 분석을 지원한다.

Usage Count와 Temporary Lock도 Runtime State다. 정확한 필드명은 TECH_SPEC가 정한다.

---

# 8. Runtime and Combat Log

```text
Action Runtime → authoritative runtime state
Combat Log → 기록 / UI / 디버깅 / 재현 보조
```

Last Used Round, Cooldown과 Prepared State는 Runtime이 소유한다.
Combat Log는 동일 사건을 기록할 수 있으나 Gameplay State의 Source of Truth가 아니다.

---

# 9. No Available Action Fallback

정상 Eligibility 이후 사용 가능한 Action Candidate가 하나도 없으면 Fallback을 수행할 수 있다.

```text
Available Action Candidates = 0
```

모든 공격 Action이 Cooldown이라는 이유만으로 즉시 Override하지 않는다.
이 규칙의 목적은 Monster Activation의 교착을 방지하면서 Cooldown 패턴을 유지하는 것이다.

---

# 10. Cooldown-only Candidate

Fallback 후보는 Cooldown만 아니었다면 현재 실행 가능한 Action으로 제한한다.

예를 들어 Target, Position, Required Status, Required Equipment, Encounter State와
다른 Runtime Lock 조건이 모두 유효하고 `Cooldown active`만 유일한 실패 이유여야 한다.

Strong / Signature Action도 이 조건을 충족할 때만 후보가 될 수 있다.
예를 들어 Death Roll이 Cooldown 중이고 Target에 ST_Bound가 없다면 Override 대상이 아니다.
Fallback은 Action Requirement나 Prepared 조건을 무시하지 않는다.

---

# 11. Cooldown Override Selection

Cooldown-only Candidate가 하나 이상이면 가장 오래전에 사용된 Action을 우선 복구한다.

```text
oldest last_used_round
↓
해당 Action의 Cooldown = 0
↓
후보군 복귀
↓
일반 AI Selection 재수행 가능
```

Never-used Action은 기본적으로 가능한 가장 오래된 이력으로 취급해 우선 복구 후보가 될 수 있다.
동률의 정확한 Tie-break는 TECH_SPEC에서 정한다.

일반 후보도 Cooldown-only 후보도 없는 경우의 최종 처리는 `UNDEFINED REQUIREMENT`다.
정의되지 않은 대체 행동이나 조건 무시를 임의로 만들지 않는다.

---

# 12. Prepared Action Creation

Prepared Action은 단순한 Action 선택 시점이 아니라,
**선행 Action Resolution 성공과 Prepared Trigger 조건 충족 이후** 생성한다.

```text
Grab 성공
↓
ST_Bound 적용
↓
Death Roll Trigger 만족
↓
Telegraph 발생
↓
Prepared Action 생성
```

Grab 실패 시 Prepared Action을 생성하지 않는다. 이 흐름은 개념 예시이며 개별 Action Definition을 승인하지 않는다.

---

# 13. Telegraph / Prepared Relationship

Director 승인 기본 규칙:

```text
One Telegraph ↔ One Prepared Action
```

하나의 Telegraph는 기본적으로 하나의 특정 Prepared Action을 뜻한다.
같은 Telegraph에서 파훼법이 다른 강기술을 무작위 선택하는 구조를 기본 패턴으로 사용하지 않는다.

Telegraph는 Gameplay Information이다. 위험 행동 준비를 인지하고, 경험을 통해 패턴을 배우며,
파훼 여부와 Risk / Reward를 판단할 수 있게 한다.

---

# 14. Telegraph Presentation

Director 승인: 최소형 Telegraph를 기본으로 한다. Core의 요구는 `Telegraph must be perceivable`이다.
정확한 파훼법을 텍스트나 정답 UI로 직접 설명할 필요는 없다.

Narration, Short Combat Log, Animation, Sound, Visual Cue 등을 사용할 수 있다.
구체 Presentation과 문장은 해당 Owner가 소유한다.

---

# 15. Prepared Capacity / Priority

Simple Monster AI 기준 기본값은 `Max Prepared Action = 1`이다.
한 Monster가 동시에 여러 Prepared Strong Action을 쌓지 않는다.
Advanced AI 예외는 명시적 Extension으로만 허용하며 상세는 후속 검토한다.

```text
Monster Activation
↓
Prepared Action exists?
├─ YES → Prepared evaluation
└─ NO → Normal Action Selection
```

Prepared Action을 일반 Weighted Random 후보군에 다시 넣지 않는다.
다음 유효 Activation은 Prepared Action Execute 또는 Fizzle로 소비된다.
Prepared를 유지하면서 다른 일반 Action을 선택하지 않는다.

---

# 16. Prepared Target Lock

Prepared Action은 기본적으로 Target Lock을 가진다.
다음 Activation에서 다른 참가자를 임의로 Target으로 바꾸지 않는다.

Target이 Escape, Death, Removal, Untargetable, Invalid State 등으로 유효하지 않으면 Fizzle한다.
새 Target을 즉시 찾지 않는다.

---

# 17. Prepared Requirement Revalidation

Prepared Action 실행 직전에 모든 필수 Requirement를 다시 검사한다.
예를 들어 Death Roll이 Target의 ST_Bound를 요구한다면 다음 Activation에 해당 조건이 여전히 유효한지 확인한다.

Target, Status, Position, Equipment, 실행 가능 상태와 다른 조건의 판단은 각 Requirement Owner가 제공한다.
필수 Requirement가 유효하면 Action을 실행하고 실제 Damage, Check, Status, Position은 Combat / Action Resolver가 처리한다.

---

# 18. Eligibility vs Penalty

모든 불리한 상태가 Prepared Action을 취소하지 않는다.

```text
Eligibility = false → Fizzle
Action remains eligible but penalized → Execute with penalty
```

개념 예시로 Action 자체가 불가능한 경우와 불이익을 받아도 실행 가능한 경우를 구분한다.
Stun / Stagger의 실제 효과나 밸런스를 여기서 확정하지 않는다.
AI와 Runtime은 특정 Status 이름을 하드코딩하지 않고 Owner의 Eligibility 결과를 소비한다.

---

# 19. Fizzle

Required Target이 무효이거나, 필수 Status / Position / Equipment가 사라지거나,
Monster가 실행할 수 없거나 다른 필수 조건이 깨져 Eligibility가 실패하면 Fizzle한다.

```text
Prepared Action Fizzle
+
Monster Activation Consumed
```

Monster는 같은 Activation에 다른 Action을 선택하지 않는다.
Telegraph 파훼로 Monster 행동을 잃게 하여 플레이어에게 Free Advantage Window를 제공한다.

---

# 20. Fizzle Cooldown

Director 승인 기본값: `Default Fizzle Cooldown = Full Cooldown`.
Prepared Strong Action이 Fizzle해도 정상적인 전체 Cooldown을 등록한다.
이는 파훼 보상을 강화하고 즉시 재준비를 막으며 패턴 학습을 지원한다.

Action-specific override는 허용할 수 있다. 구체 Override Data는 Action Definition / Data Layer가 소유한다.

```text
Prepared Fizzle 확정
↓
기본 Full Cooldown 등록 (승인된 Action-specific override가 있으면 적용)
↓
Activation consumed
```

---

# 21. Normal Execution Cooldown

정상적으로 Action Resolution이 완료된 후 해당 Action의 Cooldown을 등록한다.
Action Definition에서 제공한 정상 Cooldown을 적용한다.

정확한 이벤트 순서는 TECH_SPEC에서 정의하되 사용한 Action이 동일 Activation에서 다시 사용 가능해지지 않게 한다.
Cooldown 값 자체가 없는 Action의 개별 데이터는 이 문서에서 새로 정하지 않는다.

---

# 22. Prepared Transition Lock

Prepared Action Pending 동안 플레이어가 자발적으로 Hostile → NonHostile 전환,
De-escalation 또는 Negotiation을 시작할 수 없다.

Prepared Action은 먼저 Execute 또는 Fizzle되어야 하며 그 후에 De-escalation Attempt가 가능하다.
Runtime은 Prepared 존재 여부를 Encounter에 제공하고 Encounter Owner가 전환 경계를 조정한다.

---

# 23. Forced Encounter End Exception

Player-initiated Transition Lock은 Monster Death, Encounter Forced End,
Scripted Interruption, Environment Collapse 또는 External Resolution에 따른 강제 종료까지 막지 않는다.

```text
Player-initiated transition = locked while Prepared Pending
Forced encounter termination = may override
```

정확한 외부 종료 규칙은 Encounter Owner가 소유한다.

---

# 24. Combat End Cleanup

Combat 종료 후 전투 전용 Action Runtime은 기본적으로 폐기한다.

```text
Cooldown Remaining
Prepared Action / Prepared Target
Temporary Lock
Combat Usage Count if combat-scoped
```

Cooldown을 다음 Encounter까지 유지하지 않는다.
Boss Phase 전환이나 동일 Combat 내부의 연속 Phase에서 Combat이 종료되지 않았다면 Runtime을 유지할 수 있다.
정확한 Combat / Encounter 경계는 Combat Owner가 제공한다.

---

# 25. Combat Log Events

Combat Log는 다음 사건을 기록할 수 있다.

```text
Action Used / Action Result
Cooldown Started / Cooldown Overridden
Telegraph Triggered / Prepared Action Created
Prepared Requirement Failed / Prepared Action Fizzled / Prepared Action Executed
```

로그는 플레이어 전투 기록, QA, 재현, AI 결정 조사와 밸런스 분석에 활용할 수 있다.
필요하면 AI Debug Log와 분리한다. Logging Schema는 TECH_SPEC가 정의한다.
로그는 Runtime State의 권위 있는 원본이 아니다.

---

# 26. Runtime State Concept

Action Runtime이 가질 수 있는 개념:

```text
Action ID
Cooldown Remaining
Last Used Round
Usage Count
Temporary Lock
```

Monster / Participant 단위 Prepared Runtime이 가질 수 있는 개념:

```text
Prepared Action ID
Prepared Target
Prepared Trigger Source
Prepared Created Round
```

이는 Data Contract의 개념이며 정확한 C# Schema는 TECH_SPEC가 정의한다.

---

# 27. Monster AI / Action Runtime Boundary

Action Runtime은 Eligibility / Cooldown / Prepared 데이터를 제공하고 Monster AI는 Action을 선택한다.

AI는 `Prepared Action present?`, `Action available?`, `Cooldown active?`를 소비한다.
Cooldown을 직접 감소시키거나 Prepared Runtime을 직접 생성 / 삭제하지 않는다.
Cooldown과 Prepared Action을 Monster AI State에 중복 저장하지 않는다.

---

# 28. Position / Status / Encounter Boundary

Prepared Requirement나 Eligibility는 Distance / Position과 Status를 참조할 수 있다.
Positioning 규칙은 본 시스템이 소유하지 않는다. Positioning Owner는 `MECH_Combat_Positioning_System`이다.

예를 들어 Target의 ST_Bound 유효성은 Status / Requirement Owner가 제공한다.
Status 의미, Duration, Removal을 Runtime에서 재정의하지 않는다.

Prepared Action은 Hostile Combat Context에서 사용된다.
Encounter State / Intent / Escalation은 `MECH_Encounter_Resolution_System`이 소유한다.

---

# 29. Save / Multiplayer / Optional Boundary

Action Runtime의 Save 방식은 Save System이 소유한다. Encounter 중 Save를 지원한다면 필요한 Cooldown / Prepared State를 직렬화할 수 있다.
본 Contract는 Save Schema를 정의하지 않는다.

향후 Multiplayer에서 Action Runtime State는 Host Authoritative다.
Client는 Cooldown Override, Prepared Creation 또는 Prepared Fizzle을 최종 확정하지 않는다.
정확한 Sync 방식은 TECH_SPEC가 소유한다.

Core Runtime은 R18 전용 규칙이나 문서에 의존하지 않는다. Optional Module은 Core 계약을 사용할 수 있다.

---

# 30. Stability Rule

다음은 일반적으로 Core Contract 수정이 필요하지 않다.

- Action별 Cooldown 값 조정
- Telegraph 문장 변경
- 특정 Strong Action 추가
- Prepared Requirement 변경
- Action-specific Fizzle Cooldown override

다음은 Core Contract 검토가 필요하다.

- Cooldown 의미 또는 단위 변경
- Prepared Action 우선 처리 변경
- Fizzle 시 Activation 소비 변경
- Prepared Target Lock 제거
- Telegraph ↔ Prepared 1:1 기본 규칙 변경
- Prepared Transition Lock 또는 Runtime Ownership 변경

---

# 31. Open Items / Documentation Impact

정확한 Runtime Schema, Action별 Cooldown 값, Fallback Tie-break와
Advanced multiple-prepared 예외는 후속 작업이다.

---

# 32. Final Principle

Action Runtime System의 목적은 개별 Action의 효과나 AI 선택을 소유하는 것이 아니다.

> 전투 중 Action 상태를 일관되게 관리하고, 플레이어가 Telegraph에 대응한 결과와
> Cooldown·Prepared Action의 약속을 신뢰할 수 있도록 하는 것

이다.
