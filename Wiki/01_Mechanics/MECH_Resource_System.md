---
id: MECH_Resource_System
title: Downfall Resource System
type: mechanic
authority: CURRENT
status: APPROVED
version: 2.0.0

parent:
  - SYS_Design_Pillars

references:
  - MECH_NPC_Stats_System
  - MECH_Time_System

summary: >
  Downfall에서 수량 또는 진행 가치로 축적·획득·소비·전환되는
  Core Resource의 종류와 관리 경계를 정의한다.

tags:
  - mechanic
  - resource
  - survival
  - progression
  - reward

keywords:
  - 식량
  - 부품
  - 금화
  - 명성
  - 단서
  - 자원
  - 보상
  - 진행

last_updated: 2026-10-21
---

# Downfall Resource System

## 1. Purpose

본 문서는 Downfall에서 플레이어 집단이 획득하고 관리하는 Resource의 종류와 기본 계약을 정의한다.

Resource System은 다음을 소유한다.

- Resource Identity
- Resource Amount 또는 Resource State
- Resource 획득
- Resource 소비
- Resource 변화
- Resource 전환을 위한 기본 계약
- Resource 변경의 유효성

본 문서는 개별 Event의 보상량이나 세부 밸런스를 직접 소유하지 않는다.

---

# 2. Resource Design Purpose

Downfall의 Resource는 단순한 숫자 수집 요소가 아니다.

Resource는 플레이어가:

- 어디를 탐험할 것인가
- 어떤 위험을 감수할 것인가
- 무엇을 소비할 것인가
- 어떤 목표를 우선할 것인가

를 선택하게 만드는 Gameplay Motivation으로 기능한다.

특히 높은 위험을 감수해야 얻을 수 있는 Resource는 그 위험을 감수할 이유를 제공해야 한다.

---

# 3. Core Resource Categories

현재 Core Resource는 다음 계열로 구분한다.

| 계열 | Resource | 주요 역할 |
|---|---|---|
| 생존 자원 | 식량 | 생존 유지 |
| 제작 자원 | 부품 | 제작·수리·시설 |
| 거래 자원 | 금화 | 거래와 특수 서비스 |
| 진행 자원 | 명성 | 위험 보상·진행·특수 콘텐츠 접근 |
| 정보 자원 | 단서 | 정보 획득 및 특수 Gameplay 지원 |

장비, 유물, NPC와 관계값은 Resource System의 직접 소유 대상이 아니다.

---

# 4. Resource Model

Resource는 기본적으로 다음 개념을 가진다.

```text
Resource Definition
↓
Resource Runtime State
↓
Gain / Spend / Convert
```

예:

```text
Food = 12
Parts = 7
Gold = 4
Fame = 23
```

단, 모든 Resource가 반드시 동일한 저장 형태를 사용해야 하는 것은 아니다.

특히 `Clue`는 현재 구조 재검토 대상이다.

---

# 5. Food — 식량

식량은 생존자들의 식사를 제공하기 위한 Core Survival Resource다.

기본 관리 방식:

```text
Pooled Integer Resource
```

높은 보유량은 장기 생존 안정성을 높인다.

---

## 5.1 Food Consumption

식량은 생존자에게 식사를 제공할 때 소비된다.

기본 개념:

```text
Food
↓
Meal / Distribution
↓
NPC Hunger State
```

식량 소비 자체는 Resource System이 처리할 수 있다.

그러나 소비 결과 NPC의 허기가 얼마나 변화하는지는 NPC State / Survival Rule이 소유한다.

---

## 5.2 Food Ownership Boundary

Resource System owns:

```text
현재 식량량
식량 획득
식량 소비
식량 부족 여부
```

Resource System does not own:

```text
허기 감소 공식
굶주림 Damage
체력 감소
사망 판정
불만도 변화
충성도 변화
```

---

## 5.3 Starvation Rule

기존 문서에는 식량 고갈 시 허기와 체력에 대한 세부 규칙이 존재했다.

그러나 현재 해당 규칙의 정확한 설계 의도가 확인되지 않았다.

따라서:

```text
UNDEFINED REQUIREMENT
```

로 처리한다.

현재 확정되는 것은:

> 식량이 부족하면 모든 생존자에게 정상적인 식사를 제공할 수 없다.

까지다.

식량 부족이 허기, 체력, 감정 및 행동에 미치는 정확한 영향은 Survival / NPC State 규칙 검토 시 확정한다.

---

# 6. Parts — 부품

부품은 제작, 수리와 시설 작업에 사용되는 물질적 Resource다.

기본 관리 방식:

```text
Pooled Integer Resource
```

Resource System은 부품의 보유량과 증감을 소유한다.

다음은 다른 System이 소유한다.

- 제작 Recipe
- 장비 제작 요구량
- 시설 강화 비용
- 수리 비용
- 제작 판정

해당 시스템은 필요한 Parts의 소비를 Resource System에 요청한다.

---

# 7. Gold — 금화

금화는 Downfall에서 특정 거래에 사용되는 Currency Resource다.

기본 관리 방식:

```text
Pooled Integer Resource
```

대표적인 사용 맥락:

- 암시장
- 특수 거래
- 뇌물
- 특수 서비스

Resource System은 금화의 보유량과 증감을 소유한다.

상품, 가격, 거래 가능 조건은 Trade / Market 관련 System이 소유한다.

---

# 8. Fame — 명성

명성은 생존자 집단이 위험한 활동과 중요한 업적을 수행하면서 획득하는 Progression Resource다.

세계관적으로는 생존자 무리의 사회적 위상을 나타낸다.

그러나 Gameplay에서의 핵심 역할은:

> 플레이어에게 위험한 목표에 도전할 이유를 제공하고,
> 캠페인의 특별한 진행 조건을 형성하는 것

이다.

---

# 9. Fame Acquisition

명성은 일반적인 안전 행동보다 위험하거나 중요한 업적에 대한 보상으로 획득하는 것을 기본 방향으로 한다.

대표적 예:

- 위험도가 높은 지역 탐험 성공
- 공장 또는 연구소 등의 고위험 지역 목표 달성
- 멸망의 괴물 처치
- 중요한 세력 의뢰 성공
- 특별한 Campaign Achievement

정확한 Fame 획득량은 Content / Balance Specification이 소유한다.

---

# 10. Fame as Risk Incentive

명성은 다음 디자인 문제를 해결하기 위해 존재한다.

> 안전한 지역에서 생존만 하면 되는 상황에서
> 플레이어가 왜 위험한 지역에 들어가야 하는가?

명성은 위험한 활동에 장기적인 Gameplay Value를 제공한다.

따라서 명성 획득 구조는 Design Pillar의:

- 의미 있는 선택
- 위험과 보상
- 반복 플레이 변동성

을 지원해야 한다.

---

# 11. Fame Usage

명성은 단순히 축적되는 Score에 한정하지 않는다.

다음과 같은 기능을 가질 수 있다.

### Progression Gate

특정 Event, Scenario 또는 Ending Route의 접근 조건.

예:

```text
Fame >= Requirement
→ Special Scenario Eligible
```

---

### Conversion

명성을 다른 가치로 전환할 수 있다.

대표적인 방향:

```text
Fame
→ Faction Reputation
```

정확한 전환 비율과 조건은 해당 Feature / Faction System이 소유한다.

Resource System은 Fame 감소 또는 전환 Transaction만 처리한다.

---

### Ending / Scenario Requirement

명성은 특정 Campaign Result 또는 특수 Scenario의 진입 조건으로 참조될 수 있다.

예:

```text
광신도의 시험
True Ending 관련 조건
특수 Campaign Branch
```

정확한 Ending 조건은 Narrative / Campaign Resolution System이 소유한다.

---

# 12. Fame Is Not Faction Reputation

다음 두 개념을 구분한다.

```text
Fame
≠
Faction Reputation
```

Fame:

> 플레이어 집단이 캠페인 중 축적하는 Progression Resource.

Faction Reputation:

> 특정 세력과 플레이어 집단 사이의 관계값.

Fame은 Faction Reputation으로 전환될 수 있지만 동일한 데이터는 아니다.

---

# 13. Clue — 단서

단서는 정보 기반의 특수 Resource다.

단서의 원래 디자인 목적은:

> 정체불명의 정보나 쪽지를 획득하여
> 플레이어에게 괴물, 지역 또는 상황에 대한 유용한 지식을 제공하는 것

이다.

대표적인 형태:

- 괴물의 약점
- 위험 회피법
- 특정 장소에 대한 정보
- 상황에 대한 편리한 Tip
- 숨겨진 사실

---

# 14. Original Clue Gameplay Intent

초기 설계에서는 Clue가 판정에서 추가 Dice를 제공하는 범용 Gameplay Resource 역할도 가졌다.

그러나 현재 Check / Resolution System이 과거 버전에서 변경되었으므로 해당 Mechanics를 그대로 유지하지 않는다.

따라서:

```text
Legacy Mechanic:
Additional Dice
```

는 현재 구현 기준이 아니다.

새 Check System이 확정된 이후 Clue의 Gameplay Bonus를 재설계한다.

---

# 15. Clue Review State

Clue는 현재 다음 두 성격을 함께 가지고 있다.

```text
Narrative Information
+
Gameplay Resource
```

두 역할을 어떻게 결합할지는 아직 최종 확정하지 않는다.

따라서 Clue는 Core Resource 목록에는 보존하지만:

```text
REWORK_REQUIRED
```

상태로 취급한다.

확정이 필요한 사항:

- 단서가 소비 가능한가
- 수량형인가 개별 Entry형인가
- 하나의 단서가 고유 정보를 가지는가
- Check에 어떤 방식으로 영향을 주는가
- 단서를 조합하거나 교환할 수 있는가

이 사항은 Check System과 Exploration/Event 구조 검토 후 확정한다.

---

# 16. Equipment and Relic Boundary

장비와 유물은 넓은 의미에서 플레이어가 획득하는 자산이지만 Core Resource Pool로 관리하지 않는다.

다음은 Item / Inventory System이 소유한다.

```text
Equipment
Relic
Consumable Item
Weapon
Medical Item
Luxury Item
```

Resource System은 Item을 수량형 Resource로 강제 변환하지 않는다.

---

# 17. Item Reward

Resource가 아니더라도 탐험이나 Event의 보상이 될 수 있다.

예:

```text
Exploration Success

Reward:
- Food +2
- Gold +1
- Equipment: Medical Kit
```

Food와 Gold는 Resource Change다.

Medical Kit은 Item Acquisition이다.

둘 다 Reward일 수 있지만 동일한 Runtime Type일 필요는 없다.

---

# 18. Survivor Boundary

동료 NPC 자체는 Resource가 아니다.

Survivor는 독립적인 Entity다.

따라서:

```text
Survivor Amount += 1
```

형태의 일반 Resource로 취급하지 않는다.

---

# 19. Survivor as Reward

동료는 Resource가 아니지만 **Campaign Reward의 한 종류**가 될 수 있다.

Downfall은 소수의 초기 동료와 함께 시작하고,

플레이 과정에서:

- 탐험
- 구조
- Event
- Scenario
- 특정 성공 결과

등을 통해 새로운 동료를 얻을 수 있다.

특히 지역 탐험의 대성공 결과로 동료 합류 기회를 얻는 것은 유효한 Gameplay Reward 구조다.

개념적으로:

```text
Exploration
↓
Success / Great Success
↓
Recruitment Opportunity
↓
Survivor joins Roster
```

로 처리한다.

---

# 20. Survivor Acquisition Ownership

Resource System은:

> 동료가 보상이 될 수 있다

는 Reward Category만 참조한다.

다음은 Survivor / Roster / Recruitment System이 소유한다.

- NPC Entity
- 합류 조건
- Roster 등록
- NPC 초기 상태
- 관계 초기화
- 거점 수용 인원
- 합류 거부 가능성

---

# 21. Faction Reputation Boundary

세력 평판은 Resource가 아니다.

세력 평판은 플레이어 집단과 개별 세력 사이의 Relationship State다.

개념:

```text
Player Group
↔
Faction
```

각 Faction은 서로 독립적인 관계값을 가진다.

세력평판의 실제 데이터와 상태 단계는 Faction Relationship System이 소유한다.

---

# 22. Major Faction NPC Relationships

세력과의 관계와 세력 주요 NPC와의 개인 관계도 구분한다.

예:

```text
Player Group ↔ Vigilante Faction

Leader ↔ Vigilante Commander
```

첫 번째는 Faction Relationship이다.

두 번째는 Entity Relationship이다.

하나의 값을 다른 값으로 대체하지 않는다.

필요한 경우 서로 영향을 줄 수 있다.

---

# 23. Resource Transaction

다른 시스템은 Resource 변경을 요청할 수 있다.

개념:

```text
Source System
↓
Resource Change Request
↓
Resource System
↓
Validate
↓
Apply
↓
Notify
```

예:

```text
Exploration Reward
→ Food +3

Trade
→ Gold -2

Fame Conversion
→ Fame -5
```

Event 또는 Feature가 Resource State를 임의로 직접 변경하는 구조는 피한다.

---

# 24. Gain

Resource 획득은 Resource Amount를 증가시킨다.

예:

```text
Gain(Food, 3)
Gain(Fame, 5)
```

정확한 기술 API는 Technical Specification에서 정의한다.

---

# 25. Spend

소비 가능한 Resource는 충분한 보유량이 있을 때 감소시킬 수 있다.

개념:

```text
CanSpend(Resource, Amount)
↓
Spend
```

음수 Resource State를 허용할지는 Resource별 정의에서 결정한다.

Core Resource는 기본적으로 음수가 되지 않는 방향을 권장한다.

---

# 26. Convert

Resource는 승인된 Gameplay Rule을 통해 다른 가치로 변환될 수 있다.

예:

```text
Fame
↓
Faction Reputation
```

Resource System은 입력 Resource의 소비를 담당할 수 있다.

출력 대상 적용은 해당 Owner가 수행한다.

즉 Resource System이 Faction Reputation 자체를 소유하지 않는다.

---

# 27. Resource Change Notification

Resource가 변하면 다른 시스템이 변경 사실을 확인할 수 있어야 한다.

개념적 Event:

```text
ResourceChanged
```

이를 통해:

- UI
- Quest
- Event
- Tutorial
- Achievement

등이 반응할 수 있다.

구체적인 Event Architecture는 Technical Specification에서 정의한다.

---

# 28. Reward Is Broader Than Resource

다음 개념을 구분한다.

```text
Reward
≠
Resource
```

Reward는 Gameplay 결과로 플레이어가 얻는 모든 가치를 포함할 수 있다.

예:

```text
Resource
Item
Relic
Clue
Fame
Recruitment Opportunity
Relationship Change
Access Unlock
```

따라서 어떤 대상이 탐험 보상이라는 이유만으로 Resource가 되는 것은 아니다.

---

# 29. Event Ownership

Event는 보상 또는 비용을 정의할 수 있다.

예:

```text
effects:
  fame: +3
  food: +2
```

하지만 Resource의 의미와 상태 변경 규칙은 Resource System이 소유한다.

Event는 변경을 요청하는 Consumer다.

---

# 30. Balance Boundary

본 System Contract는 다음을 강제하지 않는다.

```text
Food reward max +3
Parts reward max +3
Gold reward max +5
Fame reward max +10
```

이와 같은 수치는 Content / Balance Guideline이 소유한다.

매우 위험한 행동은 일반적인 활동보다 훨씬 큰 보상을 제공할 수 있다.

Resource Contract가 콘텐츠 보상 범위를 불필요하게 제한하지 않는다.

---

# 31. Time Boundary

Time System은 Resource를 직접 소비하지 않는다.

예:

```text
Morning Started
```

라는 Time Event가 발생하면,

Meal / Resource 관련 시스템이 필요한 분배 절차를 시작할 수 있다.

Time System은:

```text
Food -= N
```

을 직접 수행하지 않는다.

---

# 32. NPC Stat Boundary

Resource System은 NPC Stat을 직접 소유하지 않는다.

예:

```text
Food consumed
↓
Meal resolved
↓
Hunger changes
```

Resource는 Food 소비까지만 소유한다.

Hunger 변화와 그 결과는 NPC State 관련 Owner가 소유한다.

---

# 33. Quirk Boundary

Quirk는 Resource가 아니다.

Quirk는 NPC에게 부여되는 별도 특성 시스템이다.

또한 Downfall의 `상태이상` Stat과도 동일한 개념이 아니다.

기존 Resource v1의:

```text
기벽 = 상태이상의 특수 분류
```

표현은 현행 NPC 모델과 충돌하는 Legacy 정의이므로 폐기한다.

---

# 34. Definition and Runtime State

Resource에서도 Definition과 Runtime State를 분리한다.

Definition:

```text
Food
Parts
Gold
Fame
Clue
```

Runtime:

```text
Food = 8
Parts = 4
Gold = 2
Fame = 31
```

Runtime 수치를 Definition 데이터에 직접 저장하지 않는다.

---

# 35. Save Boundary

현재 Resource State는 Save 대상이다.

그러나 Save Schema는 Resource System이 소유하지 않는다.

Save System이 Resource Runtime State를 영속화한다.

Runtime 객체와 Save 객체를 동일 구조로 강제하지 않는다.

---

# 36. Migration Notes

기존 Resource v1에서 다음을 유지한다.

## Preserve

```text
Food
Parts
Gold
Fame
Clue
Resource gain / spend concept
```

---

## Move

```text
Equipment
Relic
→ Item / Inventory

Faction Reputation
→ Faction Relationship

Survivor
→ Survivor / Roster / Recruitment
```

---

## Redefine

```text
Fame
```

을 단순 사회적 위상이 아니라:

```text
Progression Resource
+
Risk Incentive
+
Scenario / Ending Gate
+
Convertible Value
```

로 명확히 한다.

---

## Review Required

```text
Clue
```

는 원래의 정보 + Gameplay Resource 의도를 보존하되 세부 Mechanics를 재검토한다.

---

## Remove

```text
Quirk acquisition rule
NPC death rule
Faction threshold
Individual Item details
Reward amount caps
```

을 Resource System의 Ownership에서 제거한다.

---

# 37. Current Undefined Requirements

다음 사항은 아직 확정하지 않는다.

### Starvation

식량이 부족할 때:

- Hunger가 정확히 어떻게 변화하는가
- 어느 시점부터 HP가 감소하는가
- Phase 기준인가 Day 기준인가
- 다른 Status와 어떻게 상호작용하는가

향후 Survival Rule에서 결정한다.

---

### Clue Mechanics

단서의:

- 저장 형태
- 소비 여부
- Check Bonus 방식
- 개별 정보 Entry 여부

를 향후 Check / Exploration 설계 후 확정한다.

---

# 38. Ownership Summary

Resource System owns:

```text
Food
Parts
Gold
Fame
Clue Resource Contract
Resource Gain
Resource Spend
Resource Convert
Resource State
Resource Change Validation
Resource Change Notification
```

Resource System does not own:

```text
Equipment
Relic
Inventory
Survivor Entity
Recruitment
Faction Relationship
NPC Relationship
NPC Stats
Starvation Damage
Ending Logic
Event Balance
Check Formula
Quirk
```

---

# 39. Final Principle

Resource System의 목적은:

> 플레이어가 획득한 모든 것을 하나의 자원으로 취급하는 것

이 아니다.

목적은:

> 수량 또는 진행 가치로 관리되는 핵심 자원을 안정적으로 관리하고,
> 다른 게임 시스템이 해당 가치를 획득·소비·전환할 수 있는 계약을 제공하는 것

이다.

보상은 Resource보다 넓은 개념이며,

Item, 동료, 관계 변화와 새로운 접근 권한 또한 중요한 보상이 될 수 있다.