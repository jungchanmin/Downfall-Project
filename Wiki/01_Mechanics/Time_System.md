---
id: MECH_Time_System
title: Downfall Time System
type: mechanic
authority: CURRENT
status: APPROVED
version: 2.0.0

parent:
  - SYS_Project_Canon
  - SYS_Design_Pillars

summary: >
  Downfall의 25일 캠페인에서 현재 Day와 Phase,
  Phase 순서, Day 경계와 시간 전환 계약을 정의하는 Core Time System.

tags:
  - mechanic
  - time
  - phase
  - campaign
  - runtime

keywords:
  - 25일
  - 새벽
  - 아침
  - 점심
  - 저녁
  - 밤
  - Phase
  - Day

last_updated: 2026-10-19
---

# Downfall Time System

## 1. Purpose

본 문서는 Downfall 캠페인의 시간 상태와 전환 규칙을 정의한다.

Time System의 핵심 책임은 다음과 같다.

- 현재 Day
- 현재 Phase
- Phase 순서
- Phase 전환
- Day 전환
- 캠페인의 시간 경계
- 시간 변화 알림 계약

본 시스템은 시간에 반응하는 게임 콘텐츠를 직접 실행하지 않는다.

---

# 2. Core Time Model

Downfall의 시간은 실시간 흐름이 아닌 명시적인 Phase 진행 방식으로 동작한다.

기본 구조:

```text id="txa12v"
Campaign
↓
Day
↓
Phase
```

한 Campaign은 25일을 기준으로 한다.

한 Day는 5개의 Phase로 구성된다.

---

# 3. Campaign Length

Downfall의 기본 캠페인은:

```text id="v1lr61"
25 Days
```

이다.

Day 25는 Project Canon에서 정의한 의식의 완성일이다.

Time System은 25일이라는 시간 경계를 제공한다.

그러나 Day 25에서 어떤 Narrative Result 또는 Ending이 발생하는지는 Ending / Campaign Resolution System이 소유한다.

Time System 자체가 엔딩을 실행하지 않는다.

---

# 4. Day Number

Day는 다음 범위를 사용한다.

```text id="9itry5"
Day 1
~
Day 25
```

현재 진행 중인 Day는 Runtime State다.

개념적으로:

```text id="5f4z27"
CurrentDay
```

로 표현한다.

Time System은 현재 Day를 다른 시스템이 조회할 수 있도록 제공한다.

---

# 5. Five-Phase Structure

하루는 항상 다음 순서를 따른다.

```text id="zc5obx"
Dawn
↓
Morning
↓
Noon
↓
Evening
↓
Night
```

정식 한국어 명칭:

```text id="8ca1l3"
새벽
아침
점심
저녁
밤
```

정식 영문 식별자:

```text id="7zhz80"
Dawn
Morning
Noon
Evening
Night
```

`Afternoon`은 현행 Phase 식별자로 사용하지 않는다.

---

# 6. Dawn — 새벽

새로운 Day가 시작되는 Phase.

고수준 역할:

> 새로운 하루의 세계 상태가 적용될 수 있는 시작 지점.

Time System은 단지:

```text id="qk8jwu"
CurrentPhase = Dawn
```

상태를 제공한다.

다음과 같은 실제 처리는 Time System이 직접 소유하지 않는다.

- World Event 판정
- Day Type 결정
- Monster Spawn
- 지역 상태 갱신
- Faction 변화
- Event Token 생성

해당 시스템이 Dawn 전환 신호에 반응한다.

---

# 7. Morning — 아침

하루 활동을 준비하는 Planning Phase.

고수준 역할:

> 자원과 인력을 배치하고 당일 행동을 준비할 수 있는 시간대.

Time System은 Morning에서 어떤 Action을 사용할 수 있는지 직접 정의하지 않는다.

각 Action 또는 System이 자신의 사용 가능 Phase를 선언한다.

예:

```text id="5qoxlz"
Action:
PrepareExpedition

AvailablePhases:
- Morning
```

---

# 8. Noon — 점심

주요 낮 활동이 실행되는 Phase.

고수준 역할:

> 외부 활동과 거점 활동이 본격적으로 수행되는 시간대.

다음과 같은 실제 활동은 각 시스템이 소유한다.

- 탐색
- 전투
- 세력 접촉
- 거래
- 거점 경계
- 지역 이벤트

Time System은 Noon이라는 시간 Context만 제공한다.

---

# 9. Evening — 저녁

낮 활동을 마무리하고 밤을 준비하는 Phase.

고수준 역할:

> 외부 활동의 결과를 수습하고 야간 준비를 수행할 수 있는 시간대.

다음은 Time System이 직접 소유하지 않는다.

- 귀환 처리
- Inventory 정산
- 부상 정산
- Night Watch 배치
- 복귀 Event

---

# 10. Night — 밤

하루의 마지막 Phase.

고수준 역할:

> 야간 생존과 위험이 발생할 수 있는 시간대.

Night 완료 후 현재 Day가 종료된다.

다음과 같은 실제 처리는 관련 시스템이 소유한다.

- Night Watch
- 거점 침입
- 야간 Event
- 수면
- 야간 NPC Incident
- 정신적 이상 현상

---

# 11. Phase Transition

Phase는 다음 고정 순서를 따른다.

```text id="8biwpk"
Dawn
→ Morning
→ Noon
→ Evening
→ Night
```

현재 Phase 완료 후 다음 Phase로 진행한다.

Time System은 자동 실시간 타이머에 의해 Phase를 변경하지 않는다.

기본 전환 개념:

```text id="788n0y"
Complete Current Phase
↓
End Current Phase
↓
Advance
↓
Start Next Phase
```

---

# 12. No Real-Time Clock

Core Time System에는 실제 시간 경과가 존재하지 않는다.

다음과 같은 값은 Core Contract에 포함하지 않는다.

```text id="twyus8"
60초 후 자동 진행
PhaseDurationSeconds
실시간 Countdown
```

연출상의 지연, Animation Duration 또는 UI Timer가 필요한 경우 Presentation Layer가 소유한다.

Presentation 시간이 Campaign Time을 결정하지 않는다.

---

# 13. Day Transition

Night Phase가 완료되면 현재 Day가 종료된다.

개념적 순서:

```text id="10wxrp"
Night Complete
↓
Current Day Ends
↓
Day + 1
↓
Dawn Begins
```

예:

```text id="dw86de"
Day 7 / Night
↓
Day 8 / Dawn
```

---

# 14. Day 25 Boundary

Day 25는 일반적인 Campaign Time의 마지막 Day다.

Day 25 Night 이후 임의로:

```text id="9bbzqx"
Day 26
```

으로 진행하지 않는다.

Time System은 Campaign End Boundary에 도달했음을 전달한다.

실제 결말 처리와 이후 Scene은 상위 Campaign / Ending System이 수행한다.

---

# 15. Transition Events

Time System은 다른 시스템을 직접 호출하기보다 시간 변화 사실을 알리는 것을 우선한다.

권장 Domain Event 개념:

```text id="vz1ck6"
PhaseStarted
PhaseEnded
DayStarted
DayEnded
CampaignTimeEnded
```

정확한 코드 Event 이름과 구현 방식은 Technical Specification에서 결정한다.

---

# 16. Event Ordering

시간 전환 시 의미적 순서는 다음과 같다.

Phase 전환:

```text id="7tgsg4"
PhaseEnded(Current)
↓
CurrentPhase 변경
↓
PhaseStarted(New)
```

Day 전환:

```text id="tm497d"
PhaseEnded(Night)
↓
DayEnded(CurrentDay)
↓
CurrentDay 증가
↓
CurrentPhase = Dawn
↓
DayStarted(NewDay)
↓
PhaseStarted(Dawn)
```

실제 코드 구현에서는 중복 Event 발행을 방지해야 한다.

---

# 17. Phase Completion

Time System은 Phase가 완료되었다는 요청을 받아 다음 Phase로 진행할 수 있다.

그러나:

> 무엇을 완료해야 해당 Phase가 끝나는가?

는 Time System이 전부 직접 정의하지 않는다.

예:

Morning 종료 조건이:

- 인원 배치 완료
- 자원 분배 완료
- 필수 선택 완료

등을 요구한다면,

해당 조건은 각 시스템 또는 Phase Coordination Layer에서 제공한다.

Time System은 완료 요청을 받은 뒤 시간 상태를 변경한다.

---

# 18. Phase Availability

특정 기능이 어느 Phase에서 가능한지는 해당 기능의 Owner가 정의한다.

예:

```text id="jmupjj"
Craft Action
Available:
- Morning
- Evening
```

Time System에서 모든 행동 가능 목록을 중앙 관리하지 않는다.

이를 통해 신규 Action을 추가해도 Time System Contract를 수정하지 않도록 한다.

---

# 19. Time Context

다른 시스템은 현재 시간 정보를 Context로 사용할 수 있다.

개념적 Context:

```text id="yuo2yr"
TimeContext

CurrentDay
CurrentPhase
```

예:

```text id="bkh5bu"
Event Eligibility
= Event Conditions + TimeContext

NPC Behavior
= Runtime State + TimeContext

World Update
= Campaign State + TimeContext
```

Time System은 해당 시스템의 결과를 결정하지 않는다.

---

# 20. Day Type Boundary

다음 개념은 구분한다.

```text id="rsvfkg"
CurrentDay
≠
DayType
```

예:

```text id="gjp22p"
CurrentDay = 12
DayType = Omen
```

CurrentDay는 Time System이 소유한다.

Day Type:

- 고요의 날
- 전조의 날
- 멸망의 날

의 결정 방식, 확률과 효과는 별도 Day Type / Campaign System이 소유한다.

Time System은 Doomsday Probability를 계산하지 않는다.

---

# 21. Event System Boundary

다음은 Event System이 소유한다.

- Event 발생 조건
- Phase별 Event Pool
- Event Weight
- Zone Event 제한
- Group Event 제한
- NPC Incident 횟수
- Event Trigger

Time System은 Event System에게 현재 Day와 Phase만 제공한다.

---

# 22. Resource System Boundary

다음은 Resource System이 소유한다.

- 식량 분배
- 물자 소비
- 미배급 기록
- 허기 변화
- 자원 정산

Time System은 Morning 또는 Day Transition Context만 제공한다.

---

# 23. NPC System Boundary

다음은 NPC 관련 시스템이 소유한다.

- 행동 지정
- 명령 수락 / 거부
- 휴식
- 훈련
- 제작
- 감정 변화
- 불침번 행동
- 돌발 행동

Time System은 NPC 행동을 직접 실행하지 않는다.

---

# 24. Combat Boundary

Combat은 Time System 내부 Phase가 아니다.

Combat은 특정 Phase Context에서 시작될 수 있는 별도 시스템이다.

예:

```text id="yrk32m"
CurrentPhase = Noon
↓
Exploration Encounter
↓
Combat Starts
```

Combat이 시작되었다고 해서 Campaign Phase가 자동 변경되지 않는다.

Combat 종료 후 기존 Phase Context로 복귀한다.

구체적인 전투 중 Campaign Time 정지 여부는 Combat System이 정의한다.

---

# 25. World System Boundary

World System은 Time Context를 이용해 세계 변화를 수행할 수 있다.

예:

```text id="pq561j"
DayStarted
↓
World System evaluates daily changes
```

그러나 Time System은:

- 괴물 Spawn
- 기후
- 지역 위험도
- 세력 배치
- 환경 변화

를 직접 결정하지 않는다.

---

# 26. Save Boundary

다음 Runtime 정보는 Save 대상이 될 수 있다.

```text id="scs3t5"
CurrentDay
CurrentPhase
```

하지만 실제 Save Schema, Version, Serialization Format은 Save System이 소유한다.

Runtime Time State와 Save Data Structure를 동일한 객체로 취급하지 않는다.

---

# 27. Runtime State vs Definition

Time System에서도 Definition과 Runtime State를 구분한다.

Definition 예:

```text id="6xtrbc"
CampaignLength = 25
PhaseOrder =
Dawn
Morning
Noon
Evening
Night
```

Runtime 예:

```text id="0gwzax"
CurrentDay = 8
CurrentPhase = Evening
```

현재 상태를 정의 데이터에 저장하지 않는다.

---

# 28. Implementation Boundary

본 문서는 다음 구현 구조를 강제하지 않는다.

```text id="6krumc"
MonoBehaviour
ScriptableObject
Singleton
Service
State Machine
Event Bus
```

기술 구조는 승인된 Contract를 만족하는 범위에서 Technical Specification과 Codex가 결정한다.

단 다음 프로젝트 Architecture 원칙을 준수한다.

- Definition과 Runtime State를 분리한다.
- Save Data를 Runtime 객체와 분리한다.
- 불필요한 Global Dependency를 피한다.
- 시스템 간 의존성은 명확하게 한다.
- Core Domain Logic은 가능한 한 테스트 가능하게 유지한다.

---

# 29. Migration Notes

기존 Time System에서 다음 내용을 유지한다.

## Preserve

```text id="ircyih"
5 Phase structure
Dawn → Morning → Noon → Evening → Night

Phase-based progression

Night 이후 다음 Day
```

---

## Rename

기존 구현의:

```text id="kkafje"
Afternoon
```

은 현행 Canon 기준:

```text id="nqldk7"
Noon
```

으로 교체한다.

---

## Correct

기존 구현의:

```text id="c7dy1d"
29 Days
```

는 현행 Canon:

```text id="t243yp"
25 Days
```

로 교체한다.

---

## Remove From Core Time Ownership

다음은 Time System에서 분리한다.

```text id="xnl8wo"
Doomsday Probability
Monster Spawn
World Event
Resource Penalty
NPC Action
NPC Incident Limit
Combat
Faction Encounter
Inventory Settlement
AI Event Authoring Guide
```

---

## Remove From Core Runtime Concept

```text id="0xhuck"
PhaseDurationSeconds
```

를 Core Campaign Time 개념으로 사용하지 않는다.

---

# 30. Legacy Implementation

다음 기존 구현은 현행 Contract 이전에 작성된 Prototype이다.

```text id="2l3fb8"
Scripts/Core/DayCycleData.cs
Scripts/Core/DayCycleManager.cs
Scripts/Core/TimeDebugger.cs
```

이 구현은 다음 과거 가정을 포함한다.

- 29일 캠페인
- Afternoon 명칭
- Doomsday Probability의 Time System 소유
- Phase Duration 데이터
- Global Singleton 접근

따라서 기존 구현을 그대로 확장하지 않는다.

기존 코드에서 재사용 가능한 것은 개념 수준으로 제한한다.

예:

- CurrentDay
- CurrentPhase
- AdvancePhase
- Phase change notification
- Day change notification

새 구현은 별도 Technical Specification 승인 후 수행한다.

---

# 31. Stability Rule

다음 변경은 Time System Contract 변경을 일반적으로 요구하지 않는다.

- 새로운 Event 추가
- Monster 추가
- Resource 수치 변경
- NPC Action 추가
- Combat 공식 변경
- Day Type 확률 변경

반대로 다음은 Contract 검토가 필요하다.

- 25일 캠페인 구조 변경
- Phase 수 변경
- Phase 순서 변경
- 실시간 Campaign Clock 도입
- Day 경계 변경
- Campaign End Boundary 변경

---

# 32. Ownership Summary

Time System owns:

```text id="fx67rz"
CurrentDay
CurrentPhase
Campaign Length
Phase Order
Phase Transition
Day Transition
Campaign Time Boundary
Time Domain Events
```

Time System does not own:

```text id="x8xzm5"
Day Type
Event Rules
Resources
NPC Actions
Combat
Monster Spawn
World Update Logic
Faction Logic
Ending Logic
Save Schema
Presentation Timer
```

---

# 33. Final Principle

Time System의 목적은:

> 하루 동안 무엇이 일어나는지를 모두 통제하는 것

이 아니다.

목적은:

> 지금이 언제이며,
> 다음 시간으로 언제 전환되는지를
> 다른 시스템에 안정적으로 제공하는 것

이다.

다른 시스템은 이 시간 Context에 반응하며 자신의 책임을 독립적으로 수행한다.