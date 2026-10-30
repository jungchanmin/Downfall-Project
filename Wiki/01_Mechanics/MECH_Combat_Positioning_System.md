---
id: MECH_Combat_Positioning_System
title: Downfall Combat Positioning System
type: mechanic
authority: CURRENT
status: APPROVED
version: 1.0.0

parent:
  - MECH_Combat_System

references:
  - MECH_Combat_Action_System
  - MECH_Combat_Action_Runtime_System
  - MECH_Monster_AI
  - MECH_Combat_Status_Effect_System
  - MECH_Encounter_Resolution_System

summary: >
  Close / Mid / Far의 추상 Combat Formation을 통해
  전열·후열, 무기 운용 거리, 타겟 우선순위, Movement와
  Line Compression을 정의한다.

tags:
  - mechanic
  - combat
  - positioning
  - formation

keywords:
  - Close
  - Mid
  - Far
  - Formation
  - Movement
  - Line Compression
  - Frontline
  - Target Priority

last_updated: 2026-10-28
---

# Downfall Combat Positioning System

## 1. Purpose

본 문서는 Close / Mid / Far의 추상 Combat Formation으로 무기 운용 거리,
전열·후열 역할, Target Priority, 전열 교대와 Line Compression을 정의한다.

Positioning은 정밀 좌표 전술이나 Universal Dodge System이 아니다.
Cover, 실제 거리 단위, 개별 무기 밸런스, Position 기반 Modifier 수치와 개별 Monster AI Weight는 확정하지 않는다.

---

# 2. Abstract Formation

Positioning은 실제 좌표나 미터 단위가 아니라 전투 중 참가자의 전열 / 중열 / 후열 관계를 표현한다.
Close, Mid, Far를 각각 정확한 물리 거리로 해석하지 않는다.

```text
Close = 적의 직접적인 압박을 받는 전열
Mid   = 전열 뒤에서 교전하는 중간 위치
Far   = 더 가까운 전열이 적의 접근을 받아내는 동안 유지되는 후열
```

---

# 3. Shared Combat Band

Close / Mid / Far는 참가자별 Band다. 개별 Actor Pair마다 저장하는 상대 거리 Matrix가 아니다.

```text
Participant → Position Band

Close: Heinz, Gavin
Mid:   Rachel
Far:   Helena
```

다대다 전투에서도 Survivor ↔ Monster의 모든 조합에 별도 거리값을 저장하지 않는다.
모든 참가자는 같은 추상 Band 의미를 사용하며, 이는 실제 좌표 공유를 뜻하지 않는다.

---

# 4. Positioning Goals

Positioning은 Weapon Range Differentiation, Frontline / Backline Role,
Target Exposure / Priority, Formation Change, Aggro / Pressure Handoff와 Close-range AoE Exposure를 표현한다.

Positioning 자체를 주요 회피 미니게임으로 만들지 않는다.

---

# 5. Position Change Is Not Universal Dodge

```text
Position Change ≠ Universal Dodge
```

일반 공격이나 Strong Action을 Band를 한 단계 바꾸는 것만으로 자동 회피하지 않는다.
Positioning은 Telegraph / Strong Action 파훼 시스템을 대체하지 않는다.

---

# 6. Prepared Action and Position

Prepared Action이 Position Requirement를 명시적으로 가질 때만 Position 변화가 해당 Requirement의 실패 원인이 될 수 있다.
예를 들어 Target이 Close에 있어야 하는 Action에서 Position 변화가 파훼 후보가 될 수 있다.

변경 후 Eligibility가 false이면 Action Runtime의 기존 Fizzle 계약을 따른다.
단순 이동이 Prepared Action을 자동 취소하지 않으며, 모든 Prepared Action을 이동만으로 파훼할 수 있다는 규칙도 없다.
Action-specific Position Requirement는 제한적으로 사용한다.

---

# 7. Weapon Differentiation

Positioning은 무기 종류의 운용 차이를 제공한다. 다음은 개념적 방향이다.

| 무기 | 운용 방향 |
|---|---|
| Bare Hands / Knife | Close 중심 |
| Blunt / Melee Weapon | Close 중심, 일부 Mid 연계 후보 |
| Handgun | Mid 중심, Close / Far에서 일부 불리 가능 |
| Rifle | Mid / Far 활용, Close에서 불리 가능 |

정확한 수치, Modifier, Accuracy 공식과 개별 무기 밸런스는 여기서 정의하지 않는다.

---

# 8. Position and Action Availability

Action Definition은 허용 Position 또는 Position Requirement를 가질 수 있다.
Action Range는 Close, Mid, Far 또는 여러 Band를 참조할 수 있다.

Positioning은 현재 Band와 Action Range Validity에 필요한 Context를 제공한다.
실제 Action Eligibility는 Action / Runtime Owner가 판단한다.

---

# 9. Close / Mid / Far Exposure

Close는 Monster의 직접 압박을 가장 먼저 받는 전열이다.
Close Survivor가 존재하면 일반 Monster는 Close를 기본 Target Pool로 우선할 수 있다.
이는 절대 Target 규칙이 아니며 AI Profile / Action / Monster-specific Rule이 예외를 제공할 수 있다.

Mid는 Close 뒤의 지원 위치다. Target Exposure가 낮을 수 있고 원거리 / 일부 범용 무기 운용에 적합하며,
전열이 붕괴하면 앞으로 압축될 수 있다.

Far는 안전지대가 아니다. 더 가까운 Survivor가 압박을 받아내는 동안 유지되는 후열이며,
Closer Survivor가 사라지면 Line Compression으로 앞으로 이동할 수 있다.

---

# 10. Basic Movement

Position 변경은 Combat Action Economy를 사용한다.

```text
1 Action → 1 Band 이동

Close ↔ Mid
Mid ↔ Far
```

기본 Movement 한 번으로 Close → Far 또는 Far → Close를 이동하지 않는다.
Dash / Sprint / Charge / Retreat 등 특수 Action은 2 Band 이상 이동할 수 있으며 개별 Action Definition이 소유한다.

---

# 11. Forward and Backward Movement

Forward: Far → Mid, Mid → Close. 전열 강화, 근접무기 운용과 동료 교대에 사용할 수 있다.

Backward: Close → Mid, Mid → Far. Hostile Combat에서 무조건 자유로운 후퇴는 아니다.

---

# 12. Frontline Anchor Rule

Director 승인: 뒤로 물러나려면 이동 후 자신의 Band보다 가까운 Band에서
적의 압박을 받아낼 **다른 유효 Survivor**가 존재해야 한다.

```text
Close: Heinz, Gavin
Gavin Close → Mid 가능 후보: Heinz가 Close를 유지

Close: Gavin만 존재
Gavin Close → Mid 불가: 기본 Movement의 Anchor 부재
```

Solo 전열 Survivor는 기본 Movement만으로 계속 거리를 벌리는 Kite를 할 수 없다.
전투에서 완전히 이탈하려면 Escape / Withdrawal Resolution을 사용한다.

---

# 13. Mid → Far Anchor

```text
Close: Heinz / Mid: Rachel
Rachel Mid → Far 가능 후보: Heinz가 더 가까운 Band에 존재

Close: 비어 있음 / Mid: Rachel만 존재
Rachel Mid → Far 불가: 더 가까운 Band에 Anchor 부재
```

정확히 어떤 Survivor가 유효 Anchor인지 판정하는 세부 조건은 후속 Contract / TECH_SPEC에서 확인한다.

---

# 14. Movement vs Escape

```text
Combat Movement ≠ Escape Encounter
```

Band 이동은 Combat 내부 Formation 변경이다.
전투 자체의 이탈은 `MECH_Encounter_Resolution_System`의 Escape / Withdrawal Resolution이다.

---

# 15. Line Compression

Hostile Combat이 계속되는 동안 Close Survivor Band가 비면 Formation이 자동으로 압축될 수 있다.
Line Compression은 Monster의 지속적인 접근, 전열 붕괴와 후열에 전달되는 압박을 표현한다.

```text
Hostile Combat continues
↓
Close Survivor exists?
├─ YES → Formation 유지
└─ NO  → Line Compression 가능
```

---

# 16. Band-wide Shift

Compression은 특정 한 명을 임의로 뽑기보다 Survivor Formation 전체를 앞으로 한 단계 압축한다.
각 Survivor는 한 번의 Compression에서 최대 한 Band 앞으로 이동한다.

```text
Before                 After one Compression
Close: -               Close: Gavin, Rachel
Mid:   Gavin, Rachel   Mid:   Helena
Far:   Helena          Far:   -
```

---

# 17. Compression Limit and Timing

Director 승인: `Line Compression = maximum 1 Band per Round`.

```text
Close: - / Mid: - / Far: Helena
한 번의 Compression: Far → Mid
다음 Round에도 Close가 비어 있으면: Mid → Close 가능
```

정확한 Runtime Event 이름은 TECH_SPEC에서 정하며 Round Boundary 평가를 권장한다.
핵심 조건은 Hostile Combat 지속, Close 비어 있음, 최대 1 Band / Round다.

---

# 18. Compression Is Not Movement Action

```text
Player Movement ≠ Line Compression
```

Compression은 플레이어가 선택한 Movement가 아니라 적의 지속적 압박으로 인한 Formation Runtime 결과다.
일반 Movement Action Cost를 소비하지 않는다.

---

# 19. Target Exposure and Priority

Mid / Far의 방어적 이점은 주로 Target Pool Exposure 감소로 표현한다.
모든 Mid / Far 대상에게 고정 회피 보너스를 부여하지 않는다.

기본 Monster Targeting 방향은 `Nearest valid Survivor Band first`다.

```text
Close Survivor 존재 → Close Target Pool 우선
Close 없음 → Mid
Close / Mid 없음 → Far
```

동일 Band 안에서 실제 Target은 Monster AI가 선택한다.

---

# 20. Target Priority Override

Nearest Band는 기본 선호이며 절대적인 Target 법칙이 아니다.
Ranged Monster, Sniper형 AI, 부상자를 노리는 Predator,
취약 대상을 노리는 Opportunist, Special Action, Scripted Boss Rule은 예외를 제공할 수 있다.

Positioning은 Current Bands, Nearest Valid Band와 Movement Availability Context를 제공한다.
최종 Target / Action은 Monster AI가 선택한다.

---

# 21. Aggro Handoff / Tanking

Close에 Heinz와 Gavin이 있을 때 Heinz가 부상으로 Mid로 물러나면,
기본 Monster는 Close의 Gavin을 더 우선적으로 노릴 수 있다.

전열 배치로 직접 압박을 받는 대상을 간접 조절할 수 있지만,
명시적인 MMO Threat Meter나 Aggro 수치를 요구하지 않는다.

---

# 22. Area-of-Effect Bands

Close 전체를 대상으로 하는 Action을 지원한다. 예: Tail Sweep이 All Close Survivors를 대상으로 할 수 있다.
여러 Survivor가 Close에 모이는 위험이 된다.

모든 AoE가 Close 전용인 것은 아니다. Close only, Close + Mid, Mid + Far, All Bands 등은
개별 Action Definition이 정할 수 있다.

---

# 23. Position / Weapon Balance Boundary

Mid / Far는 Target Exposure 감소의 이점과 함께 Accuracy Penalty,
Action Availability Restriction, Weapon Effectiveness Loss 같은 공격 효율 Trade-off를 가질 수 있다.

Positioning은 Band Context, Action Range Validity와 Formation State를 제공한다.
Weapon / Action Data는 Optimal Band, Allowed Band, Accuracy / Damage Modifier를 정의할 수 있다.
이 문서는 개별 무기 밸런스나 Modifier 수치를 소유하지 않는다.

---

# 24. Movement Eligibility

Movement도 Eligibility 검사를 받는다. Status / Runtime Owner가 Movement Available 여부를 제공할 수 있다.

예를 들어 ST_Bound에 대해 Owner가 Movement Eligibility false를 반환하면 이동할 수 없다.
이것은 연계 예시이며 ST_Bound의 현행 개별 효과를 승인하는 것이 아니다.
Positioning은 특정 Status 이름을 하드코딩하지 않는다.

Pinned, Rooted, Immobilized, Environmental Lock, Scripted Lock도 향후 이동 제한의 예가 될 수 있다.
정확한 Definition은 해당 Status / 조건 Owner가 소유한다.

---

# 25. Cover Boundary

Director 승인: `Cover = OUT OF SCOPE for v1`.
이번 Core Contract에 Cover State를 추가하지 않는다.

향후 별도 시스템 또는 Extension으로 검토할 수 있으나 Cover Quality, Destruction,
Movement와 Accuracy Modifier는 현재 정의하지 않는다.

---

# 26. Monster Position

Monster도 필요하면 Position Band Context를 가질 수 있다.
Survivor ↔ Monster Pair Distance를 생성하지 않는다.
정확한 Monster Position Data와 Movement Rule은 Action / Monster Data 단계에서 구체화한다.

---

# 27. Definition vs Runtime

Definition / Data 예:

```text
Action allowed bands / target bands
Monster preferred bands
Weapon optimal bands
Special Movement behavior
```

Runtime 예:

```text
Participant current band
Movement eligibility result
Line Compression state
```

정확한 Runtime Schema는 TECH_SPEC가 정의한다. 정적 Definition에 현재 상태를 저장하지 않는다.

---

# 28. Initial Formation / Opening

Combat 시작 시 Position은 Encounter / Monster / Event / Character Context가 결정할 수 있다.
Surprise Encounter, 사전 Formation, Ambush, Normal Encounter는 가능한 Context의 예다.

Combat 시작 전이나 Opening에서 초기 Formation 선택 또는 자동 배치가 가능하다.
모든 Encounter에 고정 시작 위치를 강제하지 않으며 배치 UI와 선제 행동은 후속 설계다.

---

# 29. Combat End Cleanup

Combat 종료 시 Combat-only Position Runtime을 폐기하며 다음 Encounter에 Close / Mid / Far 상태를 그대로 유지하지 않는다.
연속 Phase가 같은 Combat이면 유지할 수 있다.

---

# 30. Save / Multiplayer / Optional Boundary

Combat 중 Save를 지원한다면 Position Runtime을 저장할 수 있다. Save Schema는 Save System이 소유한다.

향후 Multiplayer에서 Position Runtime과 Line Compression 결과는 Host Authoritative다.
Client가 최종 이동이나 Compression을 확정하지 않으며 Network Sync Schema는 TECH_SPEC가 정의한다.

Core Positioning은 R18 문서나 전용 규칙에 의존하지 않는다.

---

# 31. Ownership Summary

Positioning owns: 공통 Band 의미, Formation State, Movement / Frontline Anchor 계약,
Line Compression, Band Context와 기본 Target Exposure / Priority 방향.

Positioning does not own: Action Definition / 최종 Eligibility, Monster AI 최종 선택,
Status Definition, Damage / Check 공식, 개별 무기 수치, Escape Resolution,
Cover v1, Save Schema 또는 R18 전용 규칙.

---

# 32. Stability Rule

다음 변경은 일반적으로 Core Contract 수정이 필요하지 않다.

- Weapon별 Position Modifier 변경
- Action별 Target Band 변경
- 특정 Monster Position Preference 변경
- 특정 Action의 Position Requirement 추가
- 초기 Formation Data 변경

다음 변경은 Core Contract 검토가 필요하다.

- Close / Mid / Far 구조 변경
- Line Compression 제거 또는 의미 변경
- Compression 1 Band / Round 규칙 변경
- Frontline Anchor Rule 변경
- Movement 1 Action = 1 Band 기본 규칙 변경
- Positioning을 Universal Dodge로 변경
- Cover를 Core 필수 상태로 편입

---

# 33. Final Principle

Positioning은 전투 중 실제 미터 거리나 만능 회피를 계산하는 것이 아니다.

> 추상 Formation을 통해 무기 운용, 전열 교대와 압박·노출의 결과를 표현하고,
> Action, Status, AI와 Encounter가 해당 Context를 사용하도록 하는 것

이 목적이다.
