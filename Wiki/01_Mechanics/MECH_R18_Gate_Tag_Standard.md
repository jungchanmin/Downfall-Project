---
id: MECH_R18_Gate_Tag_Standard
title: "핵심 시스템 사양서 — R18 Gate Tag 정본"
type: mechanic
status: wip
version: 1.0.0
summary: >
  굴복 페이즈의 자세·부위·행동 점유 시도와 Tease 카운터를 최소 조합형 태그로 표현하고,
  태그 폭증·중복·개별 기술 전용 태그 남발을 방지하는 정본 규칙을 정의한다.
tags: [mechanic, r18, combat, gating, counter, tag]
depends_on:
  - MECH_R18_Submission_Core_System
  - MECH_R18_Skill_Ownership_Unlock_Contract
  - MECH_R18_Telegraph_Bark_Content_Policy
last_updated: 2026-07-19
---

# R18 Gate Tag 정본 v1.0

## 0. 목적

Gate Tag는 괴물 기술의 공격축을 다시 분류하는 체계가 아니다.

```text
공격축
→ 장기 진척·공격 성격

Gate Tag
→ 어떤 접근·방향·부위·통제 방식으로 자세 게이팅을 시도하는가

Counter Tag
→ 해당 게이팅 시도를 어떤 Tease 기술이 패링할 수 있는가
```

Tease 카운터 성립 여부는 공격축이 아니라 Gate Tag 일치로 판단한다.

---

## 1. 태그 설계 원칙

1. 기술 하나를 설명하기 위해 새 복합 태그를 만들지 않는다.
2. 소수의 축별 태그를 조합한다.
3. 태그는 전투 판정에 필요한 정보만 소유한다.
4. 연출 차이는 Bark·Narration·animation cue가 소유한다.
5. 동일 의미의 유사 태그를 병존시키지 않는다.
6. 신규 태그는 기존 조합으로 표현할 수 없는 판정 차이가 있을 때만 추가한다.

비권장:

```text
FastChestFrontalGrab
TwoHandRearWaistLock
TentacleFullBodyPin
```

권장:

```text
Approach: Close
Direction: Front
Target: Chest
Control: Grab
Speed: Fast
```

---

## 2. 정본 Gate Tag 축

### 2-1. 접근 거리 `ApproachTag`

| 키 | 의미 |
|---|---|
| `Close` | 거리를 좁혀 밀착을 시도 |
| `Lunge` | 짧은 돌진·급접근 |
| `Reach` | 팔·촉수·도구 등으로 거리 밖에서 접근 |
| `Stationary` | 현재 거리와 자세를 유지한 채 발동 |

### 2-2. 접근 방향 `DirectionTag`

| 키 | 의미 |
|---|---|
| `Front` | 정면 접근 |
| `Rear` | 후방 접근 |
| `Side` | 측면 접근 |
| `Above` | 상부에서 덮침 |
| `Below` | 아래쪽에서 파고듦 |
| `Omni` | 전신·다방향 접근 |

### 2-3. 목표 부위 `TargetPartTag`

구현 키는 Memory Log 정본 키를 따른다.

| 키 | UI 표시 |
|---|---|
| `Mouth` | 입 |
| `Chest` | 가슴 |
| `LowerBody` | 하복부 |
| `Rear` | 후부 |
| `WholeBody` | 전신 |

### 2-4. 행동 부위 `ActionPartTag`

| 키 | UI 표시 |
|---|---|
| `Mouth` | 입 |
| `Hand` | 손 |
| `LowerBody` | 하반신 |
| `WholeBody` | 전신 동작 |
| `External` | 도구·촉수·외부 기관 |

### 2-5. 통제 방식 `ControlTag`

| 키 | 의미 |
|---|---|
| `Grab` | 붙잡기·움켜쥐기 |
| `Pin` | 눌러 고정 |
| `Bind` | 속박·구속 수단 적용 |
| `Pull` | 끌어당김 |
| `Push` | 밀어붙임 |
| `Twist` | 비틀어 자세 전환 |
| `Mount` | 올라타거나 기승 자세 확보 |
| `Block` | 입·손·행동 부위 차단 |
| `Insert` | 침범·삽입 방식 |
| `Expose` | 의복·보호 상태 제거 |

### 2-6. 동작 속성 `MotionTag`

필요한 기술만 사용한다.

| 키 | 의미 |
|---|---|
| `Telegraphed` | 충분한 준비 동작 보유 |
| `Fast` | 전조 시간이 짧음 |
| `Sustained` | 지속 점유·연속 동작 |
| `Delayed` | 지연 후 발동 |
| `Feint` | 가짜 동작·방향 전환 포함 |

### 2-7. 결과 게이트 `GateResultTag`

| 키 | 의미 |
|---|---|
| `PostureForce` | 성공 시 자세 강제 |
| `TargetOccupy` | 대상 부위 점유 |
| `ActionOccupy` | 행동 부위 점유 |
| `FullRestraint` | 완전 구속 후보 |
| `InitiativeHold` | 행동 취소 후 주도권 유지 후보 |
| `FinisherGate` | 피니셔 조건을 형성 |

---

## 3. Gate Attack 데이터 계약

```yaml
GateAttackProfile:
  approach: Close | Lunge | Reach | Stationary
  directions: []
  target_parts: []
  action_parts: []
  controls: []
  motions: []
  results: []

  posture_force: null | Confrontation | Front | RearEntry | Mount | Bound
  occupy_target_parts: []
  occupy_action_parts: []

  gate_strength: TBD
  telegraph_profile_id:
```

예시:

```yaml
gate_attack:
  approach: Close
  directions: [Front]
  target_parts: [Chest]
  action_parts: [Hand]
  controls: [Grab, Pull]
  motions: [Telegraphed]
  results: [PostureForce, TargetOccupy]

  posture_force: Front
  occupy_target_parts: [Chest]
  occupy_action_parts: []
  telegraph_profile_id: TEL_FRONTAL_GRAB_CHEST
```

---

## 4. Tease Counter 데이터 계약

```yaml
TeaseCounterProfile:
  required_matches:
    approach: []
    directions: []
    target_parts: []
    controls: []

  optional_matches:
    action_parts: []
    motions: []
    results: []

  forbidden_tags: []
  counter_result: cancel | reverse | evade
  usable_parts: []
  valid_postures: []
```

Tease 분류라는 사실만으로 카운터가 성립하지 않는다.

```text
필수 태그 일치
+
현재 자세·사용 부위 게이트 통과
+
카운터 판정 성공
→ 상대 기술 취소 + 주도권 탈취
```

---

## 5. 일치 판정

### 5-1. 완전 일치

모든 `required_matches`가 충족된다.

```text
카운터 판정 가능
→ 성공 시 역상성 카운터
→ 상대 행동 취소
→ 주도권 확정 탈취
```

### 5-2. 부분 일치

필수 항목 일부만 일치하거나 선택 항목만 일치한다.

기본 정본에서는 **역상성 카운터로 취급하지 않는다.**

후보 처리:

- 피해·게이트 강도 일부 경감
- 자세 강제만 방지
- 부위 점유만 방지
- 일반 중립 판정으로 전환

정확한 부분 일치 효과는 후속 밸런스 단계에서 확정한다.

### 5-3. 불일치

Tease 기술이어도 카운터할 수 없다.

- 기술이 별도 능동 효과를 가지면 일반 효과만 시도
- 순수 카운터 기술이면 선택 불가 또는 매우 낮은 우선 노출

---

## 6. 태그와 공격축의 관계

공격축은 Gate Tag를 강제하지 않는다.

예:

```text
Contact + Front + Chest + Grab
Penetration + Front + LowerBody + Push
Cognition + Front + Mouth + Block
Subjugation + Omni + WholeBody + Pin
```

같은 `Contact`라도:

- 부위 점유가 없는 감각 자극
- 정면 붙잡기
- 후방 손목 제어

는 서로 다른 카운터 요구를 가진다.

축 상성은 다음만 담당한다.

- 진척 로그
- 일부 효과 친화도
- Absorption·Defiance·Domination 등 분류별 보정
- 상태이상·기벽 Return 연계

Tease의 패링 자격은 Gate Tag가 담당한다.

---

## 7. Telegraph 연계

Gate Tag는 플레이어에게 직접 노출하는 상태창 문구가 아니다.

```text
Gate Tag
→ telegraph archetype 선택
→ 물리 Cue
→ Narration
→ 필요 시 Bark
```

예:

```yaml
Gate:
  approach: Close
  directions: [Front]
  target_parts: [Chest]
  controls: [Grab]

Telegraph:
  archetypes:
    - TEL_CLOSE_DISTANCE
    - TEL_FRONTAL_GRAB
    - TEL_PART_FIXATION
```

출력 예:

```text
괴물의 상체가 앞으로 기울었다. 시선은 가슴께에서 떨어지지 않았다.

“저 녀석, 붙잡으려는 거야.”
```

---

## 8. 신규 태그 승인 체크리스트

```yaml
new_gate_tag_review:
  proposed_tag:
  axis:
  gameplay_difference:
  existing_combination_test:
  why_existing_tags_fail:
  affected_skills: []
  affected_counters: []
  telegraph_impact:
```

다음 질문에 모두 답할 수 있어야 한다.

- 기존 태그 조합으로 같은 판정 결과를 표현할 수 없는가
- 단순 연출 차이가 아니라 전투 판정 차이가 존재하는가
- 신규 태그가 최소 두 개 이상의 기술에서 재사용 가능한가
- 대응 Tease 기술이나 AI 판정에 실제 필요성이 있는가

---

## 9. 검증 규칙

- 게이팅 공격은 `ControlTag` 또는 `GateResultTag`를 최소 하나 보유한다.
- `PostureForce`가 있으면 `posture_force` 값이 필요하다.
- `TargetOccupy`가 있으면 `occupy_target_parts`가 비어 있을 수 없다.
- `ActionOccupy`가 있으면 `occupy_action_parts`가 비어 있을 수 없다.
- Tease 카운터는 최소 하나의 필수 일치 태그를 가진다.
- 기술 이름·괴물 이름·연출 표현을 Gate Tag로 사용하지 않는다.
- 한 태그가 여러 축의 의미를 동시에 소유하지 않는다.
- 신규 복합 태그는 금지하고 기본 태그 조합을 사용한다.

---

## 10. 버전 관리

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.0.0 | 2026-07-19 | 접근·방향·대상·행동 부위·통제·동작·결과의 최소 조합형 Gate Tag와 Tease 카운터 계약 확정. |
