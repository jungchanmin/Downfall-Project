---
id: MECH_Combat_Status_Effect_System
title: Downfall Combat Status Effect System
type: mechanic
authority: CURRENT
status: APPROVED
version: 1.0.0

parent:
  - MECH_Combat_System

references:
  - MECH_Combat_Action_System
  - MECH_Check_System
  - MECH_NPC_Stats_System
  - MECH_Status_Effect_DB

summary: >
  Downfall 전투에서 사용되는 Combat Status Effect의 정의,
  적용, 유지, 중첩, 해제, 만료 및 다른 시스템과의 연결 경계를 정의한다.

tags:
  - mechanic
  - combat
  - status_effect
  - condition

keywords:
  - 전투 상태효과
  - Combat Status Effect
  - 적용
  - 해제
  - 지속
  - 중첩
  - 만료
  - Status ID

last_updated: 2026-10-27
---

# Downfall Combat Status Effect System

## 1. Purpose

본 문서는 Combat Status Effect의 공통 Lifecycle과 시스템 경계를 정의한다.

전투 상태효과가 무엇이며, 어떤 방식으로 적용되고, 얼마나 유지되고,
어떻게 중첩되고 제거되며, 다른 시스템과 어떤 책임 경계를 가지는지 정의한다.

개별 상태효과 목록과 수치는 본 문서가 소유하지 않는다.
기존 Status Data의 전체 Migration이나 밸런스 변경은 이번 계약의 범위가 아니다.

---

# 2. Terminology

Downfall에서는 다음 두 개념을 반드시 구분한다.

```text
NPC Stats의 상태이상
= Abnormality Susceptibility

Combat Status Effect
= 전투 중 적용되는 일시적 또는 조건부 상태
```

한국어 문서에서는 Combat 관련 효과를 기본적으로 `전투 상태효과`라고 표기한다.
NPC의 상태이상 Stat과 동일한 용어로 혼용하지 않는다.

---

# 3. Combat Status Effect Definition

Combat Status Effect는:

> Combat Participant에게 적용되어 전투 중 행동, 판정, 피해, 이동, 선택지,
> 정보, Targeting 또는 기타 Combat Resolution에 영향을 주는 Runtime Effect

를 의미한다.

Bound, Bleed, Stun, Pain, Fear, Stealth는 기존 Legacy Asset의 예시다.
이 예시의 개별 수치나 동작을 본 문서에서 현행 규칙으로 승인하지 않는다.

---

# 4. Action / Status Relationship

Action은 Status Effect를 직접 정의하지 않는다.

```text
Combat Action
↓
Status Effect ID 요청
↓
Combat Status Effect System
↓
적용 가능 여부 확인
↓
Runtime Status 적용
```

예를 들어 `SK_Bite`는 `ST_Bound` 적용을 요청한다.
Action은 ID만 참조하며 실제 Definition은 별도 Status Data Catalog가 소유한다.

---

# 5. Single Source Principle

모든 Combat Status Effect Definition은 하나의 Authoritative Data Source에서만 정의한다.
Action, Monster, Skill, Event 문서에서 동일한 효과를 복제하지 않는다.

Status Catalog에 `ST_Bleed`가 정의되어 있다면 Action은 다음처럼 ID만 참조한다.

```text
apply_status:
  ST_Bleed
```

이는 참조 개념이며 Runtime Schema를 확정하는 예시가 아니다.

---

# 6. Status ID

모든 Combat Status Effect는 고유 ID를 가진다.
기존 `ST_*` ID 체계를 보존한다.

예: `ST_Bound`, `ST_Bleed`, `ST_Stun`, `ST_Pain`.

이번 작업에서 기존 ID를 Rename하지 않는다.

---

# 7. Definition vs Runtime State

Status Effect Definition은 정적 데이터다.

```text
ID
Name
Allowed Target
Duration Model
Stack Rule
Clear Condition
Effect Definition
```

Runtime Instance는 실제 전투 중 상태다.

```text
Remaining Duration
Current Stack Count
Source Entity
Applied Round
Temporary Parameters
```

Definition에 Runtime 값을 저장하지 않는다.

---

# 8. Duration Model

Core Contract는 다음 지속 모델의 존재와 의미를 지원한다.

| 모델 | 의미 |
|---|---|
| Timed | 지정된 시간 단위가 경과할 때까지 유지 |
| Until Action | 관련 Action이 실행되거나 소비될 때까지 유지 |
| Until Condition | 선언된 조건이 충족될 때까지 유지 |
| Until Removed | 명시적인 제거까지 유지 |
| Encounter Duration | 해당 Encounter 동안 유지 |
| Instant / Triggered | 즉시 또는 선언된 Trigger에 따라 처리 |

정확한 Runtime Schema와 Turn 계산 방식은 TECH_SPEC에서 정의한다.
개별 Duration 값은 Status Data가 소유한다.

---

# 9. Clear / Expiration

Status Definition은 하나 이상의 해제 조건을 선언할 수 있다.

```text
Time Expiration
Action Consumed
Successful Check
Specific Action
Specific Item
Encounter End
External System Removal
```

실제 해제 요청을 발생시키는 시스템은 해당 Owner가 담당한다.

---

# 10. Stack Model

Status Effect는 중첩 여부와 방식을 선언할 수 있다.

| 모델 | 의미 |
|---|---|
| No Stack | 중첩하지 않음 |
| Stack Count | 중첩 수로 관리 |
| Refresh Duration | 지속시간 갱신 |
| Replace | 기존 Instance 교체 |
| Independent Instances | 독립 Instance로 관리 |

정확한 수치와 최대 Stack은 개별 Status Data가 소유한다.
모든 Status가 중첩 가능하다고 가정하지 않는다.

---

# 11. Status Application

적용은 개념적으로 다음 흐름을 따른다.

```text
Apply Request
↓
Target Validation
↓
Immunity / Resistance / Requirement Evaluation
↓
Application Resolution
↓
Runtime Status Added / Updated
```

모든 단계가 항상 필요한 것은 아니다.
일부 Status는 Check 없이 확정 적용되며, 일부는 Check 결과에 따라 적용될 수 있다.

---

# 12. Check Integration

적용 또는 해제에 Check가 필요하면 `MECH_Check_System`을 사용한다.
Status System은 Dice 공식을 소유하지 않는다.

```text
Escape from Bound
↓
Check Request
↓
Check Result
↓
Status Removed or Maintained
```

Legacy Dice Modifier, 확률 실패, 과거 d6 Pool 규칙을 Core Contract에 복제하지 않는다.

---

# 13. Modifier Boundary

Status Effect는 Check Modifier Source가 될 수 있다.
예를 들어 Pain이 특정 Check에 Modifier를 제공할 수 있다.

Modifier Aggregation과 Final Modifier Clamp는 `MECH_Check_System`이 소유한다.
Status System은 최종 Modifier 계산 공식을 복제하지 않는다.

---

# 14. Combat Action Availability

Status Effect는 특정 Action 금지, 특정 Action만 허용,
Action Requirement 또는 Target Requirement 충족에 영향을 줄 수 있다.

Status System은 개별 Action의 정의를 소유하지 않는다.
Action System은 Status ID를 Requirement로 참조한다.

---

# 15. Damage / Healing Boundary

Status Effect는 Damage 또는 Healing을 발생시킬 수 있다.
Bleed의 Periodic Damage는 개념적 예시이며 개별 효과 승인이 아니다.

실제 Damage 계산 공식은 Combat Resolver / 향후 Damage Owner가 소유한다.
Status Definition은 Effect Payload 또는 Damage 요청만 선언한다.
Legacy Damage 값은 본 문서에서 승인하지 않는다.

---

# 16. Position Boundary

Status Effect는 Position 또는 Movement에 영향을 줄 수 있다.
Bound에 의한 이동 제한은 개념적 예시다.

Status System은 Positioning 규칙 자체를 소유하지 않는다.
Position 변경 또는 제한은 Positioning Owner와 연계한다.

---

# 17. AI Boundary

Monster AI와 NPC Behavior는 Status Effect를 판단 자료로 사용할 수 있다.
예를 들어 Target의 `ST_Bound`를 보고 특정 Action의 우선도를 판단할 수 있다.

Status System은 AI Weight 또는 Decision Algorithm을 소유하지 않는다.

---

# 18. Quirk Boundary

```text
Combat Status Effect
≠
Quirk
```

Legacy의 `combat_quirk`는 현행 정본 용어로 사용하지 않는다.
출혈, 낙인, 공포 등의 Combat Runtime 상태를 `전투기벽`이라고 부르지 않는다.

---

# 19. Permanent Quirk Conversion

전투 상태효과는 영구 Quirk 획득의 조건 또는 입력이 될 수 있다.
그러나 Status System이 직접 Quirk를 생성하거나 데이터를 수정하지 않는다.

```text
Combat Status Runtime
↓
Combat Result / Event
↓
Quirk System Evaluation
↓
Quirk Acquisition
```

Status에서 Quirk를 직접 생성하는 구조를 Core Contract로 사용하지 않는다.

---

# 20. Legacy combat_quirk Migration

기존 `MECH_Status_Effect_DB`의 `kind: combat_quirk`는 Legacy 분류다.
해당 Status 자체를 삭제하지 않는다.

향후 각 Status의 Duration Model, Stacking, Clear Condition,
Persistence, Conversion Eligibility를 다시 정의한다.
이번 문서에서 개별 데이터의 Migration은 수행하지 않는다.

---

# 21. Core / Optional Boundary

Core Status System은 Optional Module에 직접 의존하지 않는다.
Core는 R18 전용 Status를 알 필요가 없다.
Optional Module이 Core 계약을 확장해 사용한다.

---

# 22. Optional R18 Status

Legacy DB의 `r18`, `submission` 계층 Status는 Core Status Catalog에 포함하지 않는다.
향후 별도 Optional Catalog로 분리한다.

`DATA_R18_Combat_Status_Effect_Catalog`는 향후 문서의 예시이며
현재 의존 문서나 이번 작업의 생성 대상이 아니다.

---

# 23. Dependency Direction

```text
Optional R18 Status
↓ depends on
Combat Status Effect System
```

Core에서 R18 Status로 의존하는 반대 방향은 금지한다.
Legacy DB는 Migration Source로만 참조하며,
그 안의 Optional 데이터가 Core Runtime의 필수 의존성이 되지 않는다.

---

# 24. Encounter Boundary

전투 상태효과는 기본적으로 Combat Runtime State다.
Encounter 종료 시 즉시 제거, 후속 결과로 변환, 다른 시스템에 결과 전달 등의 처리가 가능하다.

어떤 Status가 Encounter 이후 지속되는지는 개별 Definition이 명시한다.
Core System이 모든 Status의 자동 제거를 강제하지 않는다.

---

# 25. Persistence

Status의 지속 범위는 개념적으로 다음처럼 구분할 수 있다.

```text
Combat Only
Encounter Result Transfer
External Persistent Effect
```

영구 NPC State는 Status System이 직접 소유하지 않는다.

---

# 26. Special Effect Handler

단순 데이터로 표현하기 어려운 전투 상태효과는 Special Effect Handler를 참조할 수 있다.
Status Definition은 `special_effect_id`와 같은 Handler ID까지만 참조한다.

실제 C# Handler 구현은 TECH_SPEC / Runtime Code가 소유한다.
본 문서에서 구현이나 정확한 Schema를 확정하지 않는다.

---

# 27. Data-Driven Priority

Duration, Stack Count, Action Lock, Simple Modifier,
Periodic Effect, Clear Condition 같은 단순 효과는 가능한 한 Data Definition으로 표현한다.

불필요한 Handler 생성을 피한다.

---

# 28. Existing Legacy Status DB

기존 `MECH_Status_Effect_DB v1.1.0`은 삭제하지 않는다.
현재 역할은 `LEGACY STATUS ASSET SOURCE`다.

이번 작업에서 원본 파일을 수정하거나 개별 Status를 이관하지 않는다.
Legacy Source의 보존이 기존 효과의 현행 승인을 의미하지 않는다.

---

# 29. Legacy Status Assets

다음 일반 Combat Status ID는 Migration 후보로 보존한다.

```text
ST_Bound
ST_Pain
ST_SeverePain
ST_Fear
ST_Cower
ST_Stun
ST_Bleed
ST_Brand
ST_Exposed
ST_Stagger
ST_Paralysis
ST_Reinforce
ST_Stealth
```

개별 Effect와 Balance는 현행 정본으로 자동 승격하지 않는다.

---

# 30. High Review Priority

아래 내용은 Legacy 동작의 문제를 설명하는 조사 메모이며 현행 규칙이 아니다.

| Legacy ID | 검토할 기존 동작 | Migration 검토 사항 |
|---|---|---|
| ST_Fear | 피격마다 영구 기벽 증가 | Status가 Quirk를 직접 관리하지 않도록 결과 전달 경계 재설계 |
| ST_Exposed | 강공 보너스 | Legacy Light / Heavy 구조 의존성 재검토 |
| ST_Reinforce | 일정 턴 후 Swarm 규모 증가 | Delayed Encounter Effect일 가능성 및 Owner 재검토 |
| ST_Paralysis | 일정 확률로 행동 실패 | 현행 Check System 연결 방식 재설계 |

해당 데이터나 수치를 이번 Core Contract에서 수정하거나 확정하지 않는다.

---

# 31. Legacy Balance

Dice 증감, Combat Stat 반감, 확률 실패, Damage 배율,
고정 지속시간, Legacy Light / Heavy 연동은 현행 수치로 승인하지 않는다.

향후 Status Data Migration 시 `LEGACY_BALANCE`, `REBALANCE_REQUIRED`로 처리한다.

---

# 32. Consumer Principle

Action / Monster / AI / Event 등 Consumer는 Status ID만 참조한다.
Consumer 내부에서 전투 상태효과 Definition을 복제하지 않는다.

---

# 33. Runtime Operations

Core System은 개념적으로 다음 Runtime Operation을 지원한다.

```text
Apply
Remove
Query
Refresh
Stack
Expire
```

정확한 API 이름과 C# 인터페이스는 TECH_SPEC에서 정의한다.

---

# 34. Save Boundary

현재 Combat Status Runtime의 Save 방식은 본 문서에서 확정하지 않는다.
Encounter 중 Save를 지원한다면 Save System이 필요한 Runtime State를 직렬화한다.

Status System은 Save Schema를 직접 소유하지 않는다.

---

# 35. Multiplayer Boundary

향후 Multiplayer에서는 Host가 Authoritative Status Runtime을 소유한다.
Client가 Status 적용 / 해제의 최종 권한을 가지지 않는다.

정확한 Network Sync 방식은 TECH_SPEC에서 정의한다.

---

# 36. Ownership Summary

Combat Status Effect System owns:

```text
Combat Status Effect concept
Status lifecycle contract
Application / Remove / Expire model
Duration concept
Stacking concept
Runtime operation contract
Action / Check / Quirk / AI boundaries
Core / Optional boundary
Definition / Runtime separation
```

Combat Status Effect System does not own:

```text
Individual Status Data
Check Formula
Damage Formula
Action Definition
AI Decision
Quirk Definition
NPC Stat Definition
Position Rules
Save Schema
R18-specific Status Data
```

---

# 37. Stability Rule

다음 변경은 일반적으로 Core Contract 수정이 필요하지 않다.

- 신규 Status 추가
- Status Duration 수치 변경
- Status Stack 최대값 변경
- Status Modifier 값 조정
- 신규 Monster가 Status 사용
- 신규 Action이 Status 적용

다음 변경은 Core Contract 검토가 필요하다.

- Status와 Quirk의 경계 변경
- Status Lifecycle의 근본 변경
- Definition / Runtime 구조 변경
- Optional Module 의존 방향 변경
- Status ID Ownership 방식 변경

---

# 38. Migration Principle

이번 Core Contract 작성 이후에도 기존 Status DB는 즉시 삭제하지 않는다.

다음 단계에서 `DATA_Combat_Status_Effect_Catalog`로 Core General Status를 Migration한다.
Optional R18 / Submission Status는 별도 Optional Data Catalog로 분리한다.

두 Catalog 모두 향후 작업 대상이며 이번 작업에서 생성하지 않는다.

---

# 39. Final Principle

Combat Status Effect System의 목적은 개별 효과를 한 문서에서 전부 설명하는 것이 아니다.

목적은:

> 모든 Combat Status Effect가 동일한 Lifecycle과 공통 계약을 따르고,
> Action / Check / AI / Quirk / Optional Module과 명확한 책임 경계를 가지게 하는 것

이다.
