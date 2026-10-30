---
id: MECH_Combat_Action_System
title: Downfall Combat Action System
type: mechanic
authority: CURRENT
status: APPROVED
version: 1.0.0

parent:
  - MECH_Combat_System

references:
  - MECH_Check_System
  - MECH_NPC_Stats_System
  - MECH_Status_Effect_DB
  - MONSTER_DB
  - MECH_Skill_Catalog

summary: >
  Downfall 전투에서 실행 가능한 Action의 공통 정의,
  사용 가능 조건, Check 연결, Effect 처리 및
  Survivor / Monster 전용 확장 경계를 정의한다.

tags:
  - mechanic
  - combat
  - action
  - skill
  - command

keywords:
  - 전투 행동
  - Action
  - Skill
  - Command
  - Target
  - Requirement
  - Check
  - Effect

last_updated: 2026-10-23
---

# Downfall Combat Action System

## 1. Purpose

본 문서는 Downfall의 Combat Encounter에서 실행 가능한 `Action`의 공통 구조와 책임을 정의한다.

Combat Action System은 다음을 소유한다.

- Action의 개념
- Action Definition의 공통 구조
- Action 사용 가능 조건
- Action과 Check System의 연결
- Action 결과 Effect 전달
- Action과 Combat Status Effect 연결
- Survivor / Monster Action의 공통 계약
- Action과 Skill / Passive의 경계

본 문서는 개별 Action의 실제 밸런스 수치나 Character / Monster의 행동 선택 AI를 직접 소유하지 않는다.

---

# 2. Action Definition

Combat Action은:

> Combat Participant가 전투 중 의도적으로 선택하거나 실행하는 하나의 행동 단위

를 의미한다.

대표적인 Action:

```text id="ca01"
Attack
Move
Evade
Use Item
Grab
Disarm
Heal
Escape
Special Attack
```

Action은 전투 흐름에 제출되고 Combat Resolver를 통해 해결된다.

---

# 3. Action and Skill

Downfall에서는 `Action`과 `Skill`을 구분한다.

### Action

Combat 중 실제로 실행되는 행동.

예:

```text id="ca02"
Attack
Evade
Move
Grab
Use Item
```

### Skill

Character 또는 Monster가 가진 능력으로,

- 새로운 Action을 제공하거나
- 기존 Action을 강화하거나
- Action의 조건 또는 효과를 변경하거나
- 특수한 전투 상호작용을 가능하게 하는

Definition을 의미한다.

예:

```text id="ca03"
Weapon Disarm
Veteran Marksmanship
Death Roll
Special Tactical Training
```

따라서:

```text id="ca04"
Skill
→ may grant or modify
→ Action
```

관계를 가질 수 있다.

---

# 4. Passive Boundary

Passive는 Action과 구분한다.

Passive는 Participant가 직접 선택해서 실행하지 않는:

- 상시 효과
- 자동 Trigger
- 조건부 반응
- 고유 특성

등을 의미한다.

예:

```text id="ca05"
Regeneration
Predator Instinct
Natural Armor
Fear Aura
```

Passive는 Monster Trait / Character Trait 관련 Owner가 소유한다.

Combat Action Catalog에 Passive를 Action처럼 등록하지 않는다.

---

# 5. Common Action Contract

모든 Combat Action은 개념적으로 다음 정보를 가질 수 있다.

```text id="ca06"
Action ID
Display Name
Action Role
Target Rule
Range
Requirements
Check
Effects
Presentation
```

정확한 Data Schema는 Technical Specification에서 정의한다.

---

# 6. Action ID

모든 실행 가능한 Action은 고유한 ID를 가진다.

예:

```text id="ca07"
ACT_BasicAttack
ACT_Evade
ACT_Grab
ACT_DeathRoll
```

공유 여부와 관계없이 독립 ID를 부여하는 것을 기본 원칙으로 한다.

따라서:

> 하나의 Monster만 사용하는 Signature Action이라도 Monster DB 내부에 전체 정의를 중복 저장하지 않는다.

Monster / Survivor Definition은 Action ID를 참조한다.

---

# 7. Single Source Principle

Action Definition은 하나의 Authoritative Source에서만 정의한다.

예:

```text id="ca08"
ACT_Bite
```

가 정의된 경우 Monster DB는:

```text id="ca09"
actions:
  - ACT_Bite
```

와 같이 참조한다.

Monster DB에서 동일한 Action의 효과를 다시 정의하지 않는다.

---

# 8. Shared and Signature Action

공유 Action과 고유 Action 모두 Action Definition으로 관리한다.

### Shared Action

복수 Participant가 사용할 수 있는 행동.

예:

```text id="ca10"
Basic Strike
Bite
Grab
Brace
```

### Signature Action

특정 Character 또는 Monster에게 사실상 고유한 행동.

예:

```text id="ca11"
Death Roll
Execution Ritual
Unique Tactical Maneuver
```

두 종류 모두 독립 Action ID를 가진다.

차이는 `공유 여부`이지 `데이터 소유 방식`이 아니다.

---

# 9. Action Role

Action은 기능적 역할을 가질 수 있다.

대표 Role:

```text id="ca12"
Attack
Defense
Movement
Control
Support
Recovery
Information
Escape
Special
```

Role은 Action의 기능적 의미를 나타낸다.

Role이 반드시 UI 버튼 분류와 일치할 필요는 없다.

---

# 10. Action Tier

필요한 경우 Action은 강도 또는 AI용 Tier를 가질 수 있다.

예:

```text id="ca13"
Basic
Advanced
Signature
```

Tier는 Role과 별개의 개념이다.

예:

```text id="ca14"
Role: Attack
Tier: Basic

Role: Attack
Tier: Signature
```

가 모두 가능하다.

기존의:

```text id="ca15"
light
semi_heavy
heavy
```

분류는 Legacy 참고 자료로 유지하며 현행 Tier로 그대로 강제하지 않는다.

---

# 11. Target Rule

Action은 유효 Target 범위를 정의한다.

대표 개념:

```text id="ca16"
Self
Single Ally
Single Enemy
Multiple Targets
Area
All Participants
```

정확한 Target Selection Logic은 Combat Runtime / Technical Specification에서 구현한다.

---

# 12. Range

Action은 필요한 경우 `MECH_Combat_Positioning_System`에서 정의하는 Position Band를 참조한다.

```text id="ca17"
Close
Mid
Far
```

Action은 허용 Band나 Position Requirement를 정의할 수 있다.
Action System은 Band의 의미를 직접 정의하지 않는다.

Band 및 Formation 규칙은 Combat Positioning Owner가 소유한다.

---

# 13. Action Availability

Action은 항상 사용 가능한 것이 아닐 수 있다.

Action은 `Requirements`를 가질 수 있다.

예:

```text id="ca18"
Weapon equipped
Target has specific Combat Status Effect
Required Range
Required Item
Required Skill
Specific Encounter State
```

Requirements가 충족되지 않으면 Action은 사용할 수 없다.

---

# 14. Structured Requirements

기존 Legacy의:

```text id="ca19"
lock_condition: weapon_held
```

같은 자유 문자열 중심 구조를 장기 정본으로 사용하지 않는다.

Action Requirement는 구조화된 조건으로 표현한다.

개념:

```text id="ca20"
Actor Requirement
Target Requirement
Equipment Requirement
Position Requirement
Encounter Requirement
```

정확한 Schema는 Technical Specification에서 정의한다.

---

# 15. Check Integration

Action이 불확실한 결과를 요구하는 경우 Check System을 사용한다.

기본 흐름:

```text id="ca21"
Action Selected
↓
Check Request
↓
Check Result
↓
Action Effect Resolution
```

Action Definition은 어떤 Check가 필요한지를 정의할 수 있다.

---

# 16. Check Source

Action은 하나의 Check Source를 요구할 수 있다.

예:

```text id="ca22"
Combat
Search
Knowledge
Care
Dialogue
```

Action System은 Check 계산 공식을 직접 소유하지 않는다.

---

# 17. Composite Check

Action은 필요에 따라 복합 Source Check를 사용할 수 있다.

예:

```text id="ca23"
Combat + Knowledge
Search + Intelligence
```

복합 Check의 실제 계산은 `MECH_Check_System`이 소유한다.

기본 복합 Check의 계산 규칙은 Check System이 소유한다. 본 문서는 계산 방식을 복제하거나 확정하지 않는다.

Action은 필요한 Source 목록만 선언한다.

---

# 18. Difficulty

Action은 필요한 경우 Difficulty Tier 또는 Requirement를 지정할 수 있다.

예:

```text id="ca25"
Difficulty: Normal
```

또는:

```text id="ca26"
Requirement: 13
```

실제 Dice 공식과 계산은 Check System이 처리한다. 승인된 Check 규칙을 본 문서에 복제하지 않는다.

---

# 19. Modifier Boundary

Action 또는 Skill은 Modifier Source를 제공할 수 있다.

예:

```text id="ca28"
This Skill grants +1 Modifier
```

그러나 최종 Modifier 합산과 Clamp는 Check System이 소유한다.

Action System은 Clamp 규칙을 복제하지 않는다.

---

# 20. Check Result Use

Action은 Check Result의:

```text id="ca30"
Success
Failure
Margin
```

을 활용할 수 있다.

예:

```text id="ca31"
Success
→ Effect A

Failure
→ Effect B

Margin >= X
→ Additional Effect
```

단, Great Success의 전역 Threshold를 Action System이 강제하지 않는다.

---

# 21. Effect

Action의 결과는 하나 이상의 Effect를 발생시킬 수 있다.

대표 Effect:

```text id="ca32"
Damage
Heal
Move
Apply Combat Status Effect
Remove Combat Status Effect
Consume Resource
Consume Item
Change Position
Change Encounter State
Trigger Special Logic
```

Action은 어떤 Effect가 발생하는지를 정의한다.

실제 다른 System State의 변경은 해당 Owner를 통해 처리한다.

---

# 22. Damage Boundary

Action은 기본적인 Damage 관련 정보를 가질 수 있다.

그러나 Damage Resolution Formula 전체를 Action Definition이 소유하지 않는다.

예:

```text id="ca33"
Action
→ Damage Effect

Combat Resolver
→ Target / Defense / Weakness 등을 반영

Entity State
→ HP Change
```

기존 Skill Catalog의:

```text id="ca34"
damage: 1
damage: 2
```

등은 Legacy Balance Value로 취급하고 향후 재검토한다.

---

# 23. Combat Status Effect

Action은 전투 상태효과 ID를 참조할 수 있다.

예:

```text id="ca35"
Apply:
  ST_Bleed
```

Action System은 `ST_Bleed`의 실제 효과를 다시 정의하지 않는다.

Combat Status Effect의 정의는 Status Effect DB가 소유한다.

---

# 24. Status Terminology

다음 용어를 구분한다.

```text id="ca36"
NPC 상태이상 Stat
≠
Combat Status Effect
```

Action에서 부여하는 속박, 출혈, 기절 등의 효과는:

> 전투 상태효과

라고 부른다.

---

# 25. Resource and Item Effect

Action이 Resource 또는 Item을 사용할 수 있다.

예:

```text id="ca37"
Use Medical Item
Consume Ammunition
Spend Special Resource
```

Action은 소비 요구를 선언할 수 있다.

실제 Resource / Inventory State 변경은 해당 System Owner가 처리한다.

---

# 26. Special Effect Handler

일반 데이터만으로 표현하기 어려운 특수 Action은 별도의 Effect Handler를 참조할 수 있다.

개념:

```text id="ca38"
SpecialEffectId
```

예:

```text id="ca39"
FX_DeathRoll
FX_LootBoundTarget
```

Action Definition은 Handler ID만 참조한다.

실제 코드 구현은 Technical Specification / Runtime Code가 소유한다.

---

# 27. Handler Usage Principle

Special Effect Handler는 예외적인 복잡 로직을 처리하기 위한 수단이다.

다음과 같은 단순 효과를 Handler로 구현하지 않는다.

```text id="ca40"
Damage
Heal
Apply Status
Move
Simple Resource Change
```

가능한 경우 Data-driven Effect를 우선한다.

Handler 난립을 피한다.

---

# 28. Survivor Action

Survivor가 사용할 수 있는 Action은 Common Action Contract를 따른다.

Survivor Action은 추가 Metadata를 가질 수 있다.

예:

```text id="ca41"
Leader Command Availability
Required Ability
Required Skill
Required Equipment
NPC Behavior Interaction
```

---

# 29. Leader Command

Survivor Action은 리더의 Command를 통해 요청될 수 있다.

개념:

```text id="ca42"
Leader Command
↓
NPC Behavior Evaluation
↓
Accepted / Modified / Rejected
↓
Combat Action
```

Action System은 NPC의 수락/거부 공식을 직접 소유하지 않는다.

---

# 30. Survivor Basic Actions

일부 Action은 특별한 Skill 없이 기본적으로 사용할 수 있다.

예:

```text id="ca43"
Basic Attack
Move
Defend
Use Item
Escape Attempt
```

정확한 기본 Action 목록은 Survivor Action Data에서 확정한다.

모든 기본 Action을 Skill로 취급하지 않는다.

---

# 31. Survivor Skill

Skill은 Survivor에게:

```text id="ca44"
New Action
Action Variant
Modifier
Special Requirement Override
Special Effect
```

등을 제공할 수 있다.

Skill이 존재한다고 해서 반드시 별도의 Action 버튼 하나가 생성되는 것은 아니다.

---

# 32. Ability Use

NPC의 8개 Ability는 Combat Action에서 Check Source 또는 Requirement로 사용될 수 있다.

그러나:

> 모든 Ability가 반드시 하나의 고정 Combat Action을 가져야 하는 것은 아니다.

환경, Equipment, Skill, Enemy Type에 따라 특정 Ability 기반 Action이 활성화될 수 있다.

---

# 33. Monster Action

Monster 역시 Common Action Contract를 사용한다.

Monster Action은 추가 Metadata를 가질 수 있다.

예:

```text id="ca45"
AI Category
AI Tags
Telegraph
Tier
Signature Flag
```

Monster AI는 이 Metadata를 이용하여 Action을 선택할 수 있다.

---

# 34. Monster AI Boundary

Monster AI는:

> 어떤 Action을 선택할 것인가

를 결정한다.

Action System은:

> 선택된 Action이 무엇을 요구하고 어떤 효과를 발생시키는가

를 정의한다.

따라서:

```text id="ca46"
Monster AI
→ Action Selection

Action System
→ Action Resolution Contract
```

으로 책임을 구분한다.

---

# 35. Telegraph

일부 Monster Action은 실행 전에 Telegraph를 가질 수 있다.

예:

```text id="ca47"
Powerful Bite
Execution
Area Attack
```

Telegraph의 존재 여부는 Monster Action Metadata가 정의할 수 있다.

Telegraph와 Prepared Action의 공통 관계는 `MECH_Combat_Action_Runtime_System`을 따른다.
구체 표시와 문장은 Presentation Owner가, 구현 세부 Timing은 후속 TECH_SPEC가 소유한다.

---

# 36. Signature Action

Signature Action은 특정 Monster 또는 Character의 정체성을 표현하는 고유 행동이다.

Signature 여부와 관계없이:

```text id="ca48"
Action ID
```

를 가진다.

Signature Action을 Monster DB 내부에 전체 정의하지 않는다.

---

# 37. Action Runtime State

Action Definition은 정적 데이터다.

전투 중 발생하는:

```text id="ca49"
Cooldown
Usage Count
Temporary Lock
Current Target
Prepared State
```

등은 Runtime State다.

Definition과 Runtime State를 분리한다.
Cooldown과 Prepared Action Runtime은 `MECH_Combat_Action_Runtime_System`이 소유한다.

---

# 38. Cooldown

Action은 필요하면 Cooldown을 사용할 수 있다.

Action Definition은 기본 Cooldown 정보를 가질 수 있다.
Round 기반 Cooldown의 의미와 Lifecycle은 `MECH_Combat_Action_Runtime_System`을 따른다.
Action별 Cooldown 수치와 정확한 구현 세부사항은 Data / TECH_SPEC에서 확정한다.

---

# 39. Presentation

Action은 Presentation Layer에서 사용할:

```text id="ca51"
Display Name
Description
Animation Key
Effect VFX Key
Log Key
```

등을 참조할 수 있다.

Mechanic Definition과 실제 Localization Text는 장기적으로 분리할 수 있다.

---

# 40. Existing Legacy Skill Catalog

기존:

```text id="ca52"
MECH_Skill_Catalog v1.3.0
```

는 주로 Monster의 공유 전투 행동을 정의한다.

기존 Catalog는 이번 작업에서 Migration하거나 삭제하지 않는다. 기존 SK_* ID, Action 수치와 밸런스는 변경하지 않는다.

분류:

```text id="ca53"
LEGACY ACTION ASSET SOURCE
```

로 유지한다.

---

# 41. Legacy Asset Migration

기존 다음 Action은 재사용 후보로 유지한다.

```text id="ca54"
SK_Base_Strike
SK_Base_Threaten
SK_Base_Brace
SK_Base_Backstep
SK_Swing
SK_Shout
SK_Grab
SK_LootEquip
SK_Bite
SK_TailSwipe
SK_ClawLunge
SK_WaryStep
SK_Stab
SK_Brandmark
SK_OminousPrayer
SK_AimedShot
SK_CallSupport
SK_StunGun
```

각 Action은 현행 Combat / Check / Status 규칙에 맞게 재검토 후 Migration한다.

---

# 42. Legacy Balance Values

기존 Action의 다음 수치는 현행 정본으로 보지 않는다.

```text id="ca55"
damage: 1
damage: 2
+Dice
Percentage Effect
Opening Gauge Value
```

해당 수치는 Legacy Balance Value로 취급한다.

---

# 43. Legacy Requirement Migration

기존:

```text id="ca56"
lock_condition
```

은 Structured Requirement로 Migration한다.

예:

```text id="ca57"
weapon_held
→ Equipment Requirement

target_bound
→ Target Combat Status Requirement
```

---

# 44. Legacy Skill Ownership

기존 규칙:

```text id="ca58"
2개 이상 공유
→ Catalog

한 개체만 사용
→ Monster DB
```

은 폐기한다.

현행 원칙:

```text id="ca59"
All executable Actions
→ Independent Action ID

Participant
→ References Action IDs
```

를 사용한다.

---

# 45. Passive Migration

기존 Skill Catalog 또는 Monster DB에 포함된 Passive는 Action System에서 제외한다.

예:

```text id="ca60"
Regeneration
Predator Instinct
Natural Passive
```

이들은 Monster Trait / Passive Owner로 Migration한다.

---

# 46. Optional Module Boundary

Optional Module은 Core Action Contract를 확장할 수 있다.

Optional Module은:

```text id="ca61"
New Action
New Effect
New Requirement Type
New Status Effect Reference
```

를 추가할 수 있다.

Core Combat Action System은 Optional Module의 구체적인 Action을 직접 참조하지 않는다.

---

# 47. R18 Action Boundary

기존:

```text id="ca62"
MECH_R18_Skill_Catalog
```

의 Action은 Optional Module에 속한다.

R18 Action 역시 가능한 경우 Common Action Contract를 따른다.

그러나 Core Action System이 R18 전용 Field를 필수적으로 가지지 않는다.

---

# 48. Data Ownership Summary

Combat Action System owns:

```text id="ca63"
Action Concept
Common Action Contract
Action ID Rule
Role / Tier concept
Target / Range reference
Requirements
Check Integration
Effect Contract
Survivor / Monster extension boundary
Definition / Runtime separation
```

Combat Action System does not own:

```text id="ca64"
Check Formula
NPC Stats
Monster Stats
Monster AI Decision
Status Effect Definition
Weapon Data
Resource State
Passive Definition
Damage Balance
Optional R18 Rules
```

---

# 49. Stability Rule

다음 변경은 일반적으로 Combat Action Core 수정이 필요하지 않다.

- 신규 Action 추가
- 신규 Monster 추가
- 신규 Survivor Skill 추가
- Action Damage 조정
- Status Effect 추가
- AI Weight 변경
- Equipment 추가

다음 변경은 Core Contract 검토가 필요하다.

- Action의 정의 자체 변경
- Action과 Skill 관계 변경
- Action ID Ownership 방식 변경
- Requirement 모델 근본 변경
- Check Integration 제거
- Survivor / Monster Action 모델의 근본 분리

---

# 50. Final Principle

Combat Action System의 목적은:

> 모든 전투 기술을 하나의 거대한 목록에 모으는 것

이 아니다.

목적은:

> Survivor와 Monster가 사용하는 모든 실행 가능한 전투 행동이
> 동일한 공통 계약을 따르도록 만들고,
> 판정·상태효과·AI·아이템 등 다른 시스템과 안정적으로 연결될 수 있는
> Action의 공통 언어를 정의하는 것

이다.
