---
id: MECH_Combat_System
title: Downfall Combat Core System
type: mechanic
authority: CURRENT
status: APPROVED
version: 1.0.0

parent:
  - SYS_Design_Pillars

references:
  - MECH_NPC_Stats_System
  - MECH_Time_System
  - MECH_Resource_System
  - MONSTER_DB
  - MECH_Status_Effect_DB
  - MECH_Skill_Catalog

summary: >
  Downfall 전투의 Encounter Lifecycle, 참가자, 명령 전달,
  Action 해결 흐름과 전투 종료 조건 및 다른 시스템과의
  Ownership Boundary를 정의하는 Core Combat Contract.

tags:
  - mechanic
  - combat
  - encounter
  - turn_based
  - core

keywords:
  - 전투
  - 조우
  - 명령
  - 행동
  - 격파
  - 도주
  - 전투 상태효과
  - CombatResult

last_updated: 2026-10-21
---

# Downfall Combat Core System

## 1. Purpose

본 문서는 Downfall 전투 시스템의 가장 높은 수준의 구조를 정의한다.

본 시스템은 다음을 소유한다.

- Combat Encounter의 시작과 종료
- Combat Participant
- 전투 진행 단계
- 리더의 명령 전달
- Combat Action 제출과 해결 조정
- Combat Resolution
- Combat Result
- 전투 중 다른 시스템을 호출하기 위한 경계

본 문서는 개별 판정 공식, Skill 효과, Monster AI, Item 수치 또는 Optional Module 규칙을 직접 소유하지 않는다.

---

# 2. Combat Design Intent

Downfall의 전투는 단순한 피해량 경쟁을 목표로 하지 않는다.

전투의 핵심은:

> 현재 확보한 생존자들의 서로 다른 능력과 상태를 이용해
> 위험한 Encounter를 해결하거나 살아서 빠져나오는 것

이다.

전투에서는 파티 구성과 현재 상태에 따라 서로 다른 해결 방식이 가능해야 한다.

---

# 3. Leader Command Structure

플레이어는 생존자 집단의 `리더`로서 전투에 참여한다.

기본적인 상호작용은:

```text
Leader
↓
Command / Intent
↓
Survivor
↓
Resolved Combat Action
```

형태를 가진다.

플레이어가 모든 NPC의 행동을 직접적인 Puppet처럼 조작하는 것을 의미하지 않는다.

NPC의:

- 충성도
- 불만도
- 적응도
- 감정
- 기벽
- 관계
- 기억
- 현재 상태

등이 명령 수행 결과에 영향을 줄 수 있다.

정확한 명령 수락, 변경 또는 거부 규칙은 NPC Behavior System이 소유한다.

---

# 4. Combat Encounter

Combat은 하나의 `Encounter`로 취급한다.

Combat Encounter는 최소한 다음 상태를 가진다.

```text
NotStarted
↓
Active
↓
Resolved
```

Combat은 Campaign Time과 별개의 Runtime Context를 가진다.

---

# 5. Combat Participants

Combat에는 하나 이상의 Participant가 존재한다.

대표 Participant 유형:

```text
Survivor
Enemy Individual
Enemy Group / Swarm
Special Entity
```

Participant의 실제 Stat은 해당 Entity의 Owner가 소유한다.

Combat System은 전투 해결에 필요한 Runtime 참조만 사용한다.

---

# 6. Combat Start

Combat Encounter가 시작되면 다음과 같은 기본 Context를 구성할 수 있다.

```text
Participants
Combat Environment
Initial Position
Available Actions
Encounter Conditions
```

전투 시작 시 정확히 어떤 순서로:

- 선공
- 위치
- 상태
- 특수 규칙

을 초기화하는지는 하위 Combat Specification에서 정의한다.

Core Contract는 특정 Initiative 공식이나 수치를 강제하지 않는다.

---

# 7. Round-Based Structure

Downfall의 Core Combat은 턴 / 라운드 기반으로 진행한다.

개념적 Round는 다음 흐름을 가진다.

```text
Round Start
↓
Command / Action Selection
↓
Action Resolution
↓
Enemy Resolution
↓
State Update
↓
Resolution Check
↓
Round End
```

정확한 행동 순서와 Initiative 알고리즘은 별도 Combat Resolution Specification이 소유한다.

---

# 8. Action Submission

Combat Participant는 전투 중 하나 이상의 가능한 Action을 가질 수 있다.

Action은 개념적으로 다음 정보를 포함할 수 있다.

```text
Actor
Action
Target
Context
```

필요한 경우:

```text
Resource Cost
Item Requirement
Position Requirement
Condition Requirement
```

등이 추가될 수 있다.

구체적인 Action 정의는 Combat Action / Skill Catalog가 소유한다.

---

# 9. Ability Use in Combat

NPC의 능력 Stat은 Combat Action에서 참조될 수 있다.

현재 Ability:

- 전투
- 탐색
- 대화
- 간호
- 제작
- 기술
- 매력
- 지능

은 모두 전투 상황에서 의미를 가질 가능성이 있다.

그러나:

> 모든 Ability가 반드시 하나의 고정 Combat Command를 가져야 하는 것은 아니다.

특정 Ability는:

- 적 종류
- 환경
- Equipment
- 상황
- Character Skill

등에 따라 Combat에서 사용할 수 있거나 사용할 수 없을 수 있다.

Combat Core는 Ability별 고정 Command 목록을 강제하지 않는다.

---

# 10. Check System Boundary

Combat System은 판정을 직접 정의하지 않는다.

Combat Action이 판정을 요구하는 경우:

```text
Combat Action
↓
Check Request
↓
Check / Resolution System
↓
Check Result
↓
Combat Resolution
```

순서로 처리한다.

Combat System은 다음을 소유하지 않는다.

```text
Dice Type
Dice Count
Target Number
DC
Success Pool
Modifier Formula
Critical Formula
Automatic Success / Failure
```

따라서 Check System이 변경되어도 Combat Core Contract는 변경되지 않아야 한다.

---

# 11. Combat Action Boundary

다음과 같은 구체적인 Action은 Core Contract의 직접 소유가 아니다.

예:

```text
Light Attack
Heavy Attack
Evade
Read
Brace
Emergency Care
Taunt
Trap
Disarm
```

이러한 Action의:

- 사용 조건
- 판정
- 효과
- Cooldown
- Target
- 수치

는 Combat Action / Skill Specification이 소유한다.

---

# 12. Combat Position

Combat은 `MECH_Combat_Positioning_System`이 정의하는 추상 Formation을 사용한다.

```text
Close
Mid
Far
```

Band 의미, 기본 Movement와 Line Compression은 Positioning Contract가 소유한다.
개별 Action / Weapon의 밸런스 수치와 Modifier는 해당 Data Owner가 정의한다.

---

# 13. Opening / Vulnerability Concept

전투에서는 적의 방어를 무너뜨리고 공격 기회를 만들어내는 Mechanic을 사용할 수 있다.

기존 설계의:

```text
압박
↓
개방
↓
무방비
↓
강한 공격 기회
```

개념은 보존 후보다.

그러나 Core Contract는 다음을 확정하지 않는다.

- Gauge 이름
- Gauge 수치
- 임계값
- 보너스
- 특정 Action과의 연동

세부 Mechanic은 Combat Action / Enemy Specification에서 정의한다.

---

# 14. Weapon and Weakness Boundary

Combat System은 Weapon과 Monster Weakness의 상호작용을 해결할 수 있다.

하지만 데이터를 직접 소유하지 않는다.

```text
Item System
→ Weapon properties

Monster Data
→ Weakness / Resistance

Combat Resolver
→ Interaction
```

형태를 따른다.

Combat Core는 특정 무기 분류 또는 Weakness 수치를 정의하지 않는다.

---

# 15. Combat Status Terminology

Downfall에서는 다음 두 개념을 반드시 구분한다.

```text
NPC 상태이상 Stat
≠
전투 상태효과
```

NPC Stats의 `상태이상`은:

> 감정, 기벽 및 부정적 변화 획득에 대한 취약성

을 의미한다.

Combat에서 발생하는:

- 속박
- 출혈
- 기절
- 공포
- 무방비
- 마비

등은 **전투 상태효과(Combat Status Effect / Combat Condition)** 라고 부른다.

---

# 16. Status Effect Ownership

전투 상태효과의 정의는 Combat Core가 소유하지 않는다.

Combat은 상태효과의:

```text
Apply
Remove
Query
Expire
```

과 같은 Runtime 동작을 요청할 수 있다.

실제 상태효과 정의는 Status Effect DB가 소유한다.

Skill과 Monster Data는 Status Effect ID를 참조한다.

---

# 17. Quirk Boundary

Quirk는 Combat Status Effect가 아니다.

Quirk는 NPC에게 귀속될 수 있는 별도 특성 시스템이다.

Combat 결과가 Quirk 획득 조건에 영향을 줄 수는 있지만,

```text
Combat
→ Quirk 직접 생성
```

을 기본 Ownership으로 사용하지 않는다.

Quirk 획득과 변화는 Quirk System이 소유한다.

---

# 18. Monster AI Boundary

Combat System은 Enemy가 행동할 수 있는 시점을 제공한다.

그러나:

> Enemy가 어떤 Action을 선택하는가?

는 Monster AI System이 결정한다.

개념:

```text
Enemy Turn
↓
Monster AI
↓
Selected Action
↓
Combat Resolver
```

Combat Core는 AI의 Weight, Utility, Personality Profile 또는 Gauge를 정의하지 않는다.

---

# 19. Monster AI Complexity

모든 Monster가 동일한 수준의 AI를 요구하지 않는다.

향후 Monster AI는 최소 다음과 같이 구분할 수 있다.

```text
Simple AI
Advanced AI
```

Simple AI:

- 일반 Monster
- 제한된 Action Pool
- 간단한 조건 또는 Weight

Advanced AI:

- Named Monster
- Mutant
- Ruin-class Threat
- 복잡한 Tactical Decision

정확한 분류와 알고리즘은 Monster AI System이 소유한다.

---

# 20. Swarm Boundary

다수의 동일 또는 유사 Enemy는 하나의 Group Unit으로 추상화할 수 있다.

기존 `Swarm` 구조는 재사용 후보로 유지한다.

Core Contract는 다음만 허용한다.

```text
Combat Participant
= Individual
or
Grouped Unit
```

Swarm의:

- 규모
- 개체 체력
- 피해 분배
- 공격력 증가
- 분리 승격

등의 세부 공식은 별도 Swarm Specification이 소유한다.

---

# 21. Combat Resolution Paths

적을 처치하는 것만이 Combat의 정상적인 성공 조건은 아니다.

Combat Encounter는 여러 Resolution Path를 가질 수 있다.

대표적인 결과:

```text
Enemy Defeated
Escape
Enemy Withdrawal
Objective Completed
Special Resolution
Defeat
```

Encounter마다 사용 가능한 Resolution Path가 다를 수 있다.

---

# 22. Escape

도주는 Downfall에서 정상적인 전략적 선택이다.

특히 플레이어가 모든 Encounter를 제거해야 할 필요는 없다.

Escape는:

- Combat Action
- Encounter Rule
- Environment
- Enemy Trait

등에 영향을 받을 수 있다.

정확한 도주 Gauge 또는 Check 공식은 Core Contract에서 정의하지 않는다.

---

# 23. Defeat

Combat에서 패배했다고 해서 항상 동일한 결과가 발생하는 것은 아니다.

Defeat 결과는 Encounter 특성에 따라:

```text
Death
Injury
Capture
Loss
Forced Withdrawal
Special Consequence
```

등으로 이어질 수 있다.

Combat System은 Defeat를 결과로 반환하고,

정확한 Campaign Consequence는 해당 Owner가 처리한다.

---

# 24. Combat Result

Combat 종료 시 `CombatResult`에 해당하는 결과 Context를 생성한다.

개념적으로 포함 가능한 정보:

```text
ResolutionType
Participants
DefeatedEntities
EscapedEntities
Damage / State Changes
Consumed Resources
Applied Conditions
Encounter Flags
```

정확한 Runtime / Save Schema는 Technical Specification에서 정의한다.

---

# 25. Reward Boundary

Combat System은 Reward를 직접 지급하는 Owner가 아니다.

기본 흐름:

```text
Combat Resolved
↓
CombatResult
↓
Encounter / Reward System
↓
Reward
```

Reward는:

- Resource
- Item
- Fame
- Clue
- Recruitment Opportunity
- Access Unlock

등이 될 수 있다.

---

# 26. Resource Boundary

Combat Action이 Resource 또는 Item을 소비할 수 있다.

예:

```text
Use Medical Item
Spend Ammunition
Consume Special Resource
```

Combat은 해당 소비를 Resource / Inventory System에 요청한다.

Combat System 자체가 Resource State를 소유하지 않는다.

---

# 27. Time System Boundary

Combat은 Campaign Time 내부의 특정 Phase에서 시작될 수 있다.

예:

```text
CurrentPhase = Noon
↓
Exploration Encounter
↓
Combat
```

Combat 시작 자체가 Campaign Phase를 자동 진행시키지는 않는다.

Combat 종료 후 기존 Campaign Time Context로 복귀한다.

Campaign Time 진행 여부는 Time / Encounter Coordination이 소유한다.

---

# 28. Combat Runtime State

Combat 동안만 존재하는 Runtime State가 있을 수 있다.

예:

```text
CurrentRound
Temporary Position
Action Availability
Temporary Combat Condition
Encounter-specific Gauge
```

이러한 Runtime State는 Character Definition과 구분한다.

Combat 종료 후 유지되어야 하는 State만 해당 시스템으로 전달한다.

---

# 29. Persistent State Boundary

전투 중 발생한 모든 것이 영구적으로 저장되는 것은 아니다.

예:

```text
Temporary Position
Temporary Combat Modifier
Encounter Gauge
```

는 Combat 종료 시 폐기될 수 있다.

반면:

```text
HP Change
Injury
Item Consumption
Quirk Acquisition
Relationship Effect
```

등은 관련 Owner에 따라 Campaign State에 반영될 수 있다.

---

# 30. Optional Module Extension

Core Combat은 Optional Module의 존재를 전제로 하지 않는다.

Optional Module은 승인된 Extension Point를 통해 Combat을 확장할 수 있다.

개념:

```text
Core Combat
↑
Optional Combat Extension
```

Optional Module은 다음을 추가할 수 있다.

- Action
- Status Effect
- Encounter Rule
- Gauge
- Resolution Path
- Presentation

Core Combat이 Optional Module의 데이터나 규칙을 직접 참조해서는 안 된다.

---

# 31. R18 Combat Boundary

기존 Combat v0.3.x에 포함되어 있던 다음 내용은 Core Combat Ownership에서 제거한다.

```text
R18 Gauge
R18 Command
Arousal Mechanic
Submission Phase
Tempo System
R18 Skill Categories
R18 Status Effects
R18 Resolution
```

이들은 Optional R18 Combat Module이 소유한다.

Core Combat은 해당 Module이 없어도 완전하게 동작해야 한다.

---

# 32. Submission Phase

기존의 굴복 페이즈는 단순한 Combat Action이 아니라 별도의 규칙과 승패 구조를 가진 Mini-game에 가깝다.

따라서 향후:

```text
Optional R18 Combat Module
└─ Submission / Tempo System
```

형태의 독립 하위 시스템으로 취급한다.

Core Combat에는 해당 규칙을 복제하지 않는다.

---

# 33. Data Ownership

Combat Core는 Data Definition의 중앙 저장소가 아니다.

다음 데이터는 각각의 Owner가 소유한다.

```text
NPC Stats
→ NPC Stats System

Monster Stats / Weakness
→ Monster DB

Weapon
→ Item System

Combat Action
→ Skill / Action Catalog

Status Effect
→ Status Effect DB

AI Profile
→ Monster AI

Reward
→ Reward / Encounter
```

Combat은 이 데이터를 Runtime에서 조합한다.

---

# 34. Implementation Boundary

본 문서는 구체적인 코드 Architecture를 강제하지 않는다.

예:

```text
CombatManager
State Machine
Command Pattern
Event Bus
Turn Queue
Unity MonoBehaviour
Plain C# Domain
```

중 어떤 구조를 사용할지는 Technical Specification에서 결정한다.

다만 다음 원칙은 유지한다.

- Combat Domain Logic은 테스트 가능해야 한다.
- 데이터와 Runtime State를 구분한다.
- 다른 시스템을 Global Singleton으로 직접 탐색하는 구조를 최소화한다.
- Combat은 다른 Owner의 데이터를 복제하지 않는다.

---

# 35. Migration Notes

기존 Combat v0.3.x에서 다음 철학을 보존한다.

## Preserve

```text
Turn-based Combat
Leader Command
NPC composition matters
Kill is not the only solution
Escape is valid
Opening / Vulnerability concept
Abstract Distance concept
Swarm concept
Multiple resolution paths
```

---

## Move to Check System

```text
d6 Success Pool
4+ Success
Success Requirement
Dice Modifier
```

기존 판정 공식은 현행 판정의 정본이 아니다.

---

## Move to Action / Skill

```text
Light Attack
Heavy Attack
Evade
Read
Craft Action
Knowledge Action
Intelligence Action
Dialogue Action
Care Action
Charm Action
Brace
```

---

## Move to Combat Detail

```text
Initiative Formula
Distance Modifier
Opening Gauge
Weakness Precision Formula
Escape Gauge
Swarm Formula
```

---

## Move to Data Owners

```text
Weapon Type
→ Item

Monster Weakness
→ Monster DB

Combat Status Effect
→ Status Effect DB

Monster Action Selection
→ Monster AI
```

---

## Move to Optional Module

```text
R18 Combat
Submission Phase
R18 Gauge
R18 Skills
R18 Conditions
```

---

# 36. Legacy Document Value

Combat v0.3.x의 세부 내용은 폐기하지 않는다.

해당 내용은:

```text
REFERENCE / LEGACY DESIGN ASSET
```

으로 보존하여 하위 System을 재구축할 때 참고한다.

다만 기존 세부 규칙을 현재 구현의 정본으로 직접 사용하지 않는다.

---

# 37. Stability Rule

다음 변경은 일반적으로 Combat Core 수정이 필요하지 않다.

- Check 공식 변경
- 신규 Skill 추가
- Weapon 추가
- Monster 추가
- Status Effect 추가
- AI Weight 변경
- Swarm 수치 변경
- R18 Module 변경

반대로 다음은 Combat Core 검토가 필요하다.

- 턴제 Encounter 폐기
- 리더 명령 구조 폐기
- Participant Model 변경
- Combat Resolution 구조 근본 변경
- Combat과 Campaign Time 관계의 근본 변경
- Optional Module이 Core 필수가 됨

---

# 38. Ownership Summary

Combat Core owns:

```text
Encounter Lifecycle
Participants
Round Flow
Leader Command Interface
Action Resolution Coordination
Combat End Conditions
Resolution Paths
CombatResult
System Boundaries
Extension Points
```

Combat Core does not own:

```text
Check Formula
Skill Data
Weapon Data
Monster Data
Status Effect Definitions
Monster AI
Reward
Quirk
Resource State
Inventory State
R18 Rules
```

---

# 39. Final Principle

Combat System의 목적은:

> 모든 전투 규칙과 데이터를 하나의 문서에 모으는 것

이 아니다.

목적은:

> 서로 다른 생존자와 적이 Encounter 안에서 행동하고,
> 다른 시스템의 규칙을 조합하여 결과를 만들며,
> 그 결과를 Campaign에 안정적으로 반환할 수 있는
> 전투의 공통 골격을 제공하는 것

이다.
