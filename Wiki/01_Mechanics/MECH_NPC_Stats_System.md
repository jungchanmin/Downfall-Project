----
id: MECH_NPC_Stats_System
title: NPC Survivor Stat System
type: mechanic
authority: CURRENT
status: APPROVED
version: 2.0.0

parent:
  - SYS_Design_Pillars

references:
  - MECH_Resource_System

summary: >
  Downfall NPC가 보유하는 현재 상태, 능력, 사회·행동 상태와
  기본 성격 데이터의 의미와 소유 경계를 정의하는 NPC Stat System Contract.

tags:
  - mechanic
  - npc
  - stats
  - runtime-state

keywords:
  - 체력
  - 정신력
  - 멘탈
  - 허기
  - 컨디션
  - 피로도
  - 충성도
  - 불만도
  - 적응도
  - 상태이상
  - 욕구불만
  - 성격

last_updated: 2026-10-30
---

# NPC Survivor Stat System

## 1. Purpose

본 문서는 Downfall 생존자 NPC가 어떤 종류의 수치 데이터를 가지는지 정의한다.

본 문서가 소유하는 것은:

- Stat Category
- 각 Stat의 의미
- 기본적인 값의 방향
- Stat의 가변성
- Definition과 Runtime State의 경계
- 다른 NPC 시스템과의 Ownership 경계

이다.

본 문서는 다음을 직접 소유하지 않는다.

- 주사위 판정 공식
- 난이도 공식
- 행동 AI 가중치
- 관계 데이터
- 감정 정의
- 기벽 정의
- 상태 변화의 세부 공식
- 개별 NPC의 실제 수치
- Optional Module 전용 데이터

---

# 2. NPC State Architecture

NPC 데이터는 개념적으로 다음과 같이 분리한다.

```text
NPC Definition
↓
NPC Runtime State
↓
Behavior / System Evaluation
↓
Save Data
```

각 계층은 동일한 개념이 아니다.

---

## 2.1 NPC Definition

캐릭터 자체의 비교적 안정적인 정의.

예:

- 기본 능력값
- 기본 성격값
- Stat 상한 또는 초기 범위
- 캐릭터 고유 특성

Definition은 Runtime 진행 중의 현재 상태를 직접 저장하지 않는다.

---

## 2.2 NPC Runtime State

현재 플레이 회차에서 계속 변화하는 값.

예:

- 현재 체력
- 현재 정신력
- 현재 멘탈
- 현재 허기
- 현재 피로도
- 현재 충성도
- 현재 불만도

Runtime State는 Definition과 분리한다.

---

## 2.3 Save Data

Save Data는 Runtime State의 영속화 표현이다.

Runtime Class 자체를 Save Schema로 간주하지 않는다.

Save 구조와 Version 정책은 별도의 Save System이 소유한다.

---

# 3. Stat Categories

NPC Stat은 크게 네 계열로 분류한다.

| 계열 | 역할 |
|---|---|
| 현재 상태 | NPC의 현재 생존·신체·정신 상태 |
| 능력 | NPC가 무엇을 얼마나 잘하는가 |
| 사회·행동 상태 | 현재 집단과 상황에 어떻게 반응하고 있는가 |
| 성격 | NPC가 본래 어떤 사람인가 |

감정, 기벽, 관계는 별도 시스템이다.

---

# 4. Current State

현재 상태값은 플레이 과정에서 지속적으로 변한다.

## 4.1 체력 — HP

NPC의 신체적 생존 상태.

기본 범위:

`0 ~ 100`

높을수록 양호하다.

체력 감소 또는 회복의 세부 규칙은 해당 행동 및 생존 시스템이 소유한다.

---

## 4.2 정신력 — Sanity

NPC가 장기적으로 유지하고 있는 정신적 안정성과 정신적 내구성.

기본 범위:

`0 ~ 100`

높을수록 양호하다.

정신력은 단기적인 감정 변화와 구분한다.

정신력 임계에 따른 붕괴, 기벽 획득 등의 구체적 규칙은 관련 시스템이 소유한다.

---

## 4.3 멘탈 — Mental

현재 순간의 정신적 여유와 안정 상태.

기본 범위:

`0 ~ 10`

높을수록 양호하다.

멘탈은 기존 문서에서 사용되던 `스트레스` 개념을 긍정 방향으로 재정의한 현행 용어다.

예:

```text
구형 표현:
스트레스 +2

현행 표현:
멘탈 -2
```

체력, 정신력 등 다른 상태값과 변화 방향을 통일하여 읽기 쉽게 만드는 것이 목적이다.

`Stress`는 현행 NPC Stat 명칭으로 사용하지 않는다.

---

## 4.4 허기 — Hunger

NPC가 현재 얼마나 충분히 섭취한 상태인지 나타낸다.

기본 범위:

`0 ~ 10`

높을수록 양호하다.

식량 소비량, 식사 횟수와 허기 변화 공식은 Resource System이 소유한다.

---

## 4.5 컨디션 — Condition

질병이 아닌 현재의 전반적인 신체 상태와 활동 효율을 나타낸다.

기본 범위:

`-5 ~ +5`

높을수록 양호하다.

컨디션이 실제 판정에 어떤 Modifier를 주는지는 Check System이 소유한다.

---

## 4.6 피로도 — Fatigue

활동과 수면 부족에 의해 누적되는 육체적 피로.

기본 범위:

`0 ~ 10`

높을수록 악화된 상태다.

피로 발생량과 회복량은 행동, 시간, 휴식 시스템이 정의한다.

---

# 5. Ability Stats

능력 스탯은 NPC가 특정 종류의 행동을 수행하는 기본 능력을 나타낸다.

기본 범위:

`0 ~ 10`

능력 스탯은 다음 8종을 사용한다.

---

## 5.1 전투 — Combat

직접적인 전투 및 물리적 대치 능력.

---

## 5.2 탐색 — Exploration

관찰, 위험 감지, 흔적 탐색과 정보 획득 능력.

---

## 5.3 대화 — Dialogue

설득, 협상, 의사소통과 사회적 문제 해결 능력.

---

## 5.4 간호 — Care

응급처치, 치료 및 신체·정신적 돌봄 능력.

---

## 5.5 제작 — Craft

제작, 수리, 시설 작업과 물리적 가공 능력.

---

## 5.6 기술 — Technique

전문 지식과 기술적 문제 해결 능력.

---

## 5.7 매력 — Charm

외적·사회적 매력을 활용하는 능력.

---

## 5.8 지능 — Intelligence

분석, 추론, 학습과 전략적 사고 능력.

---

# 6. Ability Ownership Boundary

능력 스탯은:

> NPC가 얼마나 잘하는가

만 정의한다.

다음은 본 문서가 소유하지 않는다.

```text
주사위 종류
성공 공식
난이도
DC
요구치
Modifier 누적
Critical
자동 성공 / 실패
```

이들은 별도의 Check / Resolution System이 소유한다.

따라서 판정 시스템이 변경되어도 NPC Ability 정의는 변경되지 않아야 한다.

---

# 7. Social / Behavioral State

이 계열은 NPC가 현재 집단과 상황에 어떻게 반응하고 있는지를 나타내는 가변값이다.

성격보다 실제 행동 판단에 더 직접적인 영향을 줄 수 있다.

---

## 7.1 충성도 — Loyalty

NPC가 현재 리더와 집단에 얼마나 강하게 소속되어 있고 협조하려 하는지 나타낸다.

기본 범위:

`0 ~ 10`

높을수록 충성적이다.

충성도가 실제 명령 수행과 행동 선택에 미치는 정확한 영향은 NPC Behavior System이 소유한다.

---

## 7.2 불만도 — Dissatisfaction

리더, 조직 또는 현재 상황에 대해 누적된 불만.

기본 범위:

`0 ~ 10`

높을수록 부정적이다.

반항 또는 명령 거부 임계값은 NPC Behavior System이 소유한다.

---

## 7.3 적응도 — Adaptation

현재 생존환경과 집단생활에 얼마나 적응했는지를 나타낸다.

기본 범위:

`0 ~ 10`

높을수록 현재 상황에 잘 적응한 상태다.

---

## 7.4 상태이상 — Abnormality Susceptibility

Downfall에서 `상태이상`은 일반적인 RPG의 `Status Effect`와 다른 의미를 가진 프로젝트 고유 Stat이다.

기본 범위:

`0 ~ 10`

높을수록 악화된 상태다.

상태이상은 NPC가:

- 부정적인 감정
- 기벽
- 정신적 이상
- 신체적 이상

등을 새롭게 획득하거나 악화시키는 것에 얼마나 취약한지를 나타낸다.

개념적으로:

```text
상태이상 증가
↓
감정 / 기벽 획득 저항 감소
↓
부정적 변화에 더 취약
```

로 작동한다.

정확한 저항 공식과 획득 판정은 Emotion / Quirk 관련 시스템이 소유한다.

---

## 7.5 욕구불만 — Frustration

NPC가 자신의 육체적·정신적·개인적 욕구를 충분히 충족하지 못하고 있는 정도.

기본 범위:

`0 ~ 10`

높을수록 악화된 상태다.

구체적인 돌발 행동이나 욕구 관련 Event Trigger는 NPC Behavior / Event System이 소유한다.

---

# 8. Terminology Guard — 상태이상

아래 두 개념을 혼동하지 않는다.

```text
상태이상 Stat
≠
Status Effect
```

Downfall의 `상태이상` Stat은:

> 부정적 감정·기벽·이상 획득에 대한 취약성

이다.

반면:

```text
공포
다리 부상
우울
공황
특정 기벽
```

등은 `상태이상 수치` 그 자체가 아니다.

이들은 별도 Emotion / Quirk 시스템에서 NPC에게 부여되는 상태 또는 특성이다.

따라서 구현 시:

```text
npc.AbnormalitySusceptibility
```

같은 scalar value와

```text
npc.Emotions
npc.Quirks
```

같은 부여형 collection을 동일한 구조로 취급하지 않는다.

실제 코드 명칭은 구현 명세에서 확정한다.

---

# 9. Relationship Ownership

친밀도는 NPC 자체의 독립 Stat으로 소유하지 않는다.

관계값은 두 Entity 사이의 관계 데이터다.

개념:

```text
NPC A → NPC B
NPC A → Leader
NPC B → NPC A
```

관계 방향에 따라 값이 다를 수 있다.

따라서:

```text
친밀도
신뢰
적대
기타 관계값
```

의 실제 데이터와 변화 규칙은 Relationship System이 소유한다.

NPC Stats System은 Relationship을 참조만 한다.

---

# 10. Emotion System Boundary

감정은 scalar NPC Stat이 아니다.

감정은 사건과 경험을 통해 NPC에게 형성되는 가변 상태다.

예:

- 공포
- 분노
- 불안
- 안도
- 호감
- 혐오

구체적인 Emotion Type, 지속시간, 중첩, 효과와 기억 연계는 Emotion System이 소유한다.

감정은 NPC의 Stat 및 행동 판단에 영향을 줄 수 있다.

---

# 11. Quirk System Boundary

기벽은 NPC가 사건과 경험을 통해 획득할 수 있는 고유한 특성 시스템이다.

기벽은 단순 Stat 수치가 아니다.

기벽은 NPC에게 부여되며 다음에 영향을 줄 수 있다.

- Stat
- 행동 선택
- 판정
- 감정
- 이벤트 조건
- Narrative

기벽의 획득, 제거, 강화와 효과 정의는 Quirk System이 소유한다.

---

# 12. Personality Stats

성격은 NPC의 기본적인 캐릭터 성향이다.

기본 범위:

`0 ~ 10`

기본 성격값은 캐릭터 Definition에 속하며 일반적인 플레이 과정에서는 변경하지 않는다.

성격 스탯은 다음 6종이다.

- 신경성
- 인내심
- 외향성
- 공격성
- 성욕
- 양심

---

# 13. Personality Influence Principle

성격은 NPC 행동에 영향을 미치지만 절대적인 행동 결정 요소가 아니다.

Downfall에서 실제 행동은 현재 상황과 경험에 더 크게 영향받는다.

개념적 우선순위는 다음과 같다.

```text
현재 상황
+
가변 사회·행동 상태
+
감정
+
기벽
+
관계
+
기억
↓
행동 판단

성격
↓
기본적인 성향 보정
```

즉 높은 공격성을 가진 NPC라고 해서 항상 공격적인 행동을 선택하지 않는다.

예를 들어:

- 높은 충성도
- 높은 적응도
- 낮은 불만도
- 특정 감정
- 특정 기벽
- 현재 관계
- 최근 기억

등이 현재 행동에 더 강하게 작용할 수 있다.

성격은 캐릭터의 정체성을 유지하는 안정적인 기초값으로 기능한다.

정확한 행동 가중치는 NPC Behavior System이 소유한다.

---

# 14. Base Personality and Runtime Influence

기본 성격 자체를 Runtime에서 직접 변경하는 것을 기본 방식으로 사용하지 않는다.

필요한 경우:

```text
Base Personality
+
Runtime Influence
```

형태로 처리한다.

예:

```text
Base Aggression = 8
```

인 NPC가 공포, 부상, 관계 또는 경험 때문에 현재 공격적으로 행동하지 않을 수 있다.

이 경우 Base Aggression을 변경하는 것이 아니라 행동 평가 단계에서 Runtime State를 함께 계산한다.

---

# 15. Stat Effect Ownership

본 문서는 Stat의 의미를 소유한다.

하지만:

```text
Stat A가 N 이하이면 X 발생
Stat B가 N 이상이면 Y 발생
```

같은 Gameplay Trigger는 가능한 한 실제 행동을 소유하는 시스템이 정의한다.

예:

```text
HP = 0의 생존 처리
→ Life / Character State System

멘탈 감소와 정신력 손실
→ Mental State System

불만도에 따른 명령 거부
→ NPC Behavior System

상태이상에 따른 기벽 획득
→ Quirk System

허기에 따른 자원 소비
→ Resource System
```

이 원칙을 통해 Stat Definition과 Gameplay Rule을 분리한다.

---

# 16. Optional Module Boundary

Optional Module 전용 Stat은 Core NPC Stat에 직접 추가하지 않는다.

Optional Module이 필요로 하는 데이터는 해당 Module이 소유한다.

Core NPC는 Module이 없어도 정상적으로 존재하고 행동할 수 있어야 한다.

---

# 17. Individual Character Data

개별 생존자의 실제 Stat 값은 본 문서가 소유하지 않는다.

예:

```text
Rachel Combat = 9
Heinz Patience = 8
```

등은 Character Data가 소유한다.

본 System Contract에서 특정 NPC를 밸런스 기준값으로 직접 고정하지 않는다.

---

# 18. Ownership Summary

본 문서가 소유한다.

```text
NPC Stat Categories
Stat Meaning
Stat Direction
Basic Range
Mutability
Definition / Runtime Boundary
```

본 문서가 소유하지 않는다.

```text
Check Formula
AI Decision Formula
Relationship Data
Emotion Definition
Quirk Definition
Resource Consumption
Individual NPC Values
Optional Module Stats
Save Schema
```

---

# 19. Migration Notes

v1.x 문서에서 다음 내용을 분리한다.

## Preserve

- NPC Stat 4계열 구조
- 6개 Current State
- 8개 Ability
- 핵심 Social / Behavioral State
- 6개 Personality

## Rename

```text
스트레스
→ 멘탈
```

값 방향 역시 긍정형 기준으로 전환한다.

## Restore / Confirm

```text
충성도
```

를 Social / Behavioral State에 포함한다.

## Move

```text
친밀도
→ Relationship System

판정 / DC / Modifier
→ Check System

감정
→ Emotion System

기벽
→ Quirk System

개별 NPC 값
→ Character Data

Optional Module Stat
→ 해당 Module
```

---

# 20. Final Principle

NPC Stat System의 목적은:

> NPC의 모든 행동 규칙을 정의하는 것

이 아니다.

목적은:

> NPC가 어떤 상태와 능력을 가지고 있으며,
> 다른 시스템이 어떤 데이터를 참조할 수 있는지를 안정적으로 정의하는 것

이다.

행동은 이러한 데이터와 관계, 기억, 감정, 기벽 및 현재 상황을 조합한 결과로 결정된다.