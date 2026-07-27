---
id: MECH_R18_Rachel_Submission_Vertical_Slice
title: "수직 슬라이스 — 레이첼 로페즈 굴복 기술 7종"
type: mechanic
status: canonical-draft
version: 0.1.0
summary: >
  카운터 승부사형 생존자 레이첼 로페즈의 굴복 전용 기술 7종과 인간형 광신도 상대
  페이퍼 테스트 계약을 정의한다. 기술명은 디렉터 재작명 전까지 가칭으로 사용한다.
tags: [mechanic, r18, survivor, rachel, skill, vertical-slice, paper-test]
depends_on:
  - MECH_R18_Submission_Resource_System
  - MECH_R18_Body_Sensitivity_System
  - MECH_R18_Survivor_Submission_Skill_Design_Rules
  - MECH_R18_Cultist_Submission_Skill_Migration
last_updated: 2026-07-27
---

# 레이첼 로페즈 굴복 기술 수직 슬라이스 v0.1

> 본 문서의 기술명은 모두 가칭이다. 디렉터가 재작명하기 전까지 ID·기본 행동명·전술 역할을 정본으로 삼고 표시명은 콘텐츠 초안으로 취급한다.

---

## 1. 수직 슬라이스 목적

이 수직 슬라이스는 다음 항목을 실제 기술 데이터와 페이퍼 전투에서 검증한다.

1. 카운터 승부사형 생존자 정체성
2. Service 2종의 안정성·위험 차이
3. 정면 공격 전용 Tease 2종의 Gate 정확성
4. 전투당 횟수 제한이 없는 조건부 Domination
5. 절정도 관리형 Defiance
6. 인간형 광신도에게도 사용할 수 있는 Absorption
7. 광신도의 광기·신앙 집착 Bark
8. 자원·부위·감응·반복 보호 규칙의 실제 연결

---

## 2. 테스트 대상

### 2.1 생존자

```yaml
survivor_id: Rachel_Lopez
submission_archetype: CounterGambler
base_submission_max: 10
post_climax_residual_profile: Standard
```

### 2.2 상대

```yaml
opponent_id: Cultist_Humanoid_Test
monster_tier: StrongNormal
exhaustion_max: 12
submission_anatomy:
  body_groups: [Mouth, Chest, LowerBody, WholeBody]
  specific_parts:
    - Lips
    - Tongue
    - Breast
    - Genitals
```

광신도는 인간형 기본 부위를 사용하며, 첫 테스트에서는 `SpecialOrgan`을 추가하지 않는다.

---

## 3. 레이첼 전투 정체성

> 레이첼은 상대의 공격을 읽고 접근을 일부러 허용한 뒤, 정확한 카운터로 주도권을 빼앗아 약점을 집중 공략하는 승부사형 생존자다.

기본 전투 흐름:

```text
전조 관찰
→ 정면 Tease 성공
→ 주도권 탈취
→ Service로 약점·감응 축적
→ 조건 충족 시 Domination
→ 위험 시 Defiance
→ 체액성 공격은 Absorption으로 역이용
```

### 3.1 강점

- 정면 공격 패턴을 읽고 카운터하는 능력
- 정확한 Tease 성공 후 높은 전환 효율
- 상대가 한 부위를 보호할 때 다른 부위를 공략하는 유연성
- 불리한 상태에서 자세를 뒤집는 Domination

### 3.2 약점

- 후방 공격에 대응하는 전용 Tease가 없음
- 완전 구속·Mouth 완전 점유에 취약
- 선제적으로 몰아붙이는 순수 공격형이 아님
- Domination 실패 시 자기 절정·굴복 위험이 큼
- Absorption은 특정 Fluid 공격에만 반응함

---

## 4. 기술 구성

| 분류 | 수량 | 기술 ID | 기본 행동명 |
|---|---:|---|---|
| Service | 2 | `SRV_Rachel_Service_Chest` | 가슴 주무르기 |
| Service |  | `SRV_Rachel_Service_Handjob` | 핸드잡 |
| Tease | 2 | `SRV_Rachel_Tease_Chest` | 가슴 유혹 |
| Tease |  | `SRV_Rachel_Tease_Lower` | 하체 유혹 |
| Domination | 1 | `SRV_Rachel_Dom_MountReversal` | 기승위 역전 |
| Defiance | 1 | `SRV_Rachel_Def_BreathControl` | 호흡 정돈 |
| Absorption | 1 | `SRV_Rachel_Absorb_RitualFluid` | 체액 받아넘기기 |

표시명은 디렉터 재작명 전까지 가칭이다.

---

# 5. Service 기술

## 5.1 SRV_Rachel_Service_Chest

### 기본 정보

```yaml
id: SRV_Rachel_Service_Chest
display_name: "가칭 — 약점을 짚는 손"
base_action_name: "가슴 주무르기"
side: survivor
phase: submission
command_category: Service
attack_axis: Contact
power_grade: Standard
climax_gain_grade: Minor
stability: High
cooldown: 0
```

### 부위·자세

```yaml
target_parts:
  - group: Chest
    specific_part: Breast
action_parts: [Hand]
valid_postures: [Confrontation, Front, Mount]
lock_conditions:
  - HandUnavailable
  - TargetChestUntargetable
```

### 효과

```yaml
resource_effects:
  exhaustion_damage: 2
  climax_gain_target: 0

self_resource_costs:
  self_climax_cost: 0
  failure_self_climax_cost: 0
  critical_failure_self_climax_cost: 1

sensitivity:
  progress_grade: Standard
  target_part: Breast
```

### 전술 역할

- 높은 안정성의 기본 탈진 공격
- 광신도의 Chest 감응을 빠르게 `Sensitive`로 올림
- Chest 보호 행동을 유도해 LowerBody를 노출시키는 준비기
- 직접 결착력은 낮음

### 상대 대응

- 가슴 감추기
- 레이첼 손목 붙잡기
- 자세 틀기
- 두 번째 동일 부위 공략부터 Chest 보호 행동 해금

### 결과 계약

| 결과 | 효과 |
|---|---|
| 대성공 | 탈진 3, 감응 진행 Standard, 주도권 유지 후보 |
| 성공 | 탈진 2, 감응 진행 Standard |
| 부분 성공 | 탈진 1 또는 감응 진행 Minor 중 하나 |
| 실패 | 효과 없음, 상대 주도권 |
| 대실패 | 자기 절정도 +1, 손 점유 후보 |

---

## 5.2 SRV_Rachel_Service_Handjob

### 기본 정보

```yaml
id: SRV_Rachel_Service_Handjob
display_name: "가칭 — 숨통을 끊는 손놀림"
base_action_name: "핸드잡"
side: survivor
phase: submission
command_category: Service
attack_axis: Contact
power_grade: Major
climax_gain_grade: Minor
stability: Medium
cooldown: 1
```

### 부위·자세

```yaml
target_parts:
  - group: LowerBody
    specific_part: Genitals
action_parts: [Hand]
valid_postures: [Front, Mount]
lock_conditions:
  - HandUnavailable
  - TargetLowerBodyUntargetable
```

### 효과

```yaml
resource_effects:
  exhaustion_damage: 3

self_resource_costs:
  self_climax_cost: 1
  failure_self_climax_cost: 0
  critical_failure_self_climax_cost: 2

sensitivity:
  progress_grade: Standard
  target_part: Genitals
```

### 전술 역할

- 가슴 주무르기보다 높은 탈진 피해
- LowerBody 약점과 중첩할 때 결정타 후보
- 자기 절정 비용과 쿨타임으로 반복 사용 억제
- 상대가 Chest를 보호한 뒤 노출된 LowerBody를 공략하는 연계기

### 상대 대응

- 하체 감추기
- 허리 빼기
- 레이첼 손목 점유
- 자세를 RearEntry로 전환해 정면 접근 차단

### 결과 계약

| 결과 | 효과 |
|---|---|
| 대성공 | 탈진 4, 감응 진행 Standard, 상대 안정성 -1 후보 |
| 성공 | 탈진 3, 감응 진행 Standard, 자기 절정 +1 |
| 부분 성공 | 탈진 2, 자기 절정 +1 |
| 실패 | 효과 없음 |
| 대실패 | 자기 절정 +2, 상대 주도권·손 점유 후보 |

---

# 6. Tease 기술

## 6.1 SRV_Rachel_Tease_Chest

### 기본 정보

```yaml
id: SRV_Rachel_Tease_Chest
display_name: "가칭 — 받아치는 가슴 유혹"
base_action_name: "가슴 유혹"
side: survivor
phase: submission
command_category: Tease
attack_axis: Contact
power_grade: Standard
climax_gain_grade: Minor
stability: Medium
cooldown: 0
```

### 카운터 범위

```yaml
counter_profile:
  required_tags:
    - FrontEntry
    - ChestTarget
    - GrabOrCaress
  forbidden_tags:
    - RearEntry
    - FullBound
    - MouthOccupied
  required_action_parts:
    - UpperBody
```

후방 공격에는 대응하지 않는다.

### 성공 효과

```yaml
on_perfect_counter:
  cancel_incoming_attack: true
  exhaustion_damage: 3
  steal_initiative: true
  sensitivity_progress:
    target_part: Breast
    grade: Standard
```

### 자기 비용

```yaml
self_resource_costs:
  self_climax_cost: 0
  failure_self_climax_cost: 1
  critical_failure_self_climax_cost: 2
```

### 전술 역할

- 광신도의 `가슴 주무르기`·유사 Chest Grab 카운터
- 공격을 읽고 일부러 접촉 거리를 허용하는 레이첼의 대표 기술
- 정확한 Gate 불일치 시 공격 취소 불가
- 의복만 노리는 기술은 완전 카운터 대상이 아님

---

## 6.2 SRV_Rachel_Tease_Lower

### 기본 정보

```yaml
id: SRV_Rachel_Tease_Lower
display_name: "가칭 — 다리 사이의 함정"
base_action_name: "하체 유혹"
side: survivor
phase: submission
command_category: Tease
attack_axis: Contact
power_grade: Standard
climax_gain_grade: Minor
stability: Medium
cooldown: 0
```

### 카운터 범위

```yaml
counter_profile:
  required_tags:
    - FrontEntry
    - LowerBodyTarget
    - TouchOrDrive
  forbidden_tags:
    - RearEntry
    - FullBound
    - LowerBodyUnavailable
```

정면 공격만 대응한다. RearEntry 공격은 항상 카운터 범위 밖이다.

### 성공 효과

```yaml
on_perfect_counter:
  cancel_incoming_attack: true
  exhaustion_damage: 3
  steal_initiative: true
  sensitivity_progress:
    target_part: Genitals
    grade: Standard
```

### 자기 비용

```yaml
self_resource_costs:
  self_climax_cost: 0
  failure_self_climax_cost: 1
  critical_failure_self_climax_cost: 2
```

### 전술 역할

- 하반신 애무·밀착 Drive 계열 정면 공격 카운터
- 후방 공격에 취약하다는 레이첼의 명확한 약점을 보존
- 성공 시 핸드잡 또는 기승위 역전으로 연결

---

# 7. Domination 기술

## 7.1 SRV_Rachel_Dom_MountReversal

### 기본 정보

```yaml
id: SRV_Rachel_Dom_MountReversal
display_name: "가칭 — 승부사의 기승"
base_action_name: "기승위 역전"
side: survivor
phase: submission
command_category: Domination
attack_axis: Subjugation
power_grade: Major
climax_gain_grade: Major
stability: Low
cooldown: 2
usage_limit_per_battle: null
```

전투당 1회 제한은 두지 않는다. 대신 조건·쿨타임·실패 비용으로 통제한다.

### 발동 조건

```yaml
requirements:
  submission_ratio_at_or_below: 0.60
  initiative_holder: opponent
  valid_postures: [Front, RearEntry]
  required_action_parts: [LowerBody]
  forbidden_states:
    - FullBound
    - LowerBodyUnavailable
    - ClimaxAfterglow
```

### 효과

```yaml
on_success:
  cancel_incoming_pressure: true
  posture_force: Mount
  steal_initiative: true
  exhaustion_damage: 4
  sensitivity_progress:
    target_part: Genitals
    grade: Standard

self_resource_costs:
  self_climax_cost: 2
  failure_self_climax_cost: 2
  critical_failure_self_climax_cost: 4
  failure_submission_damage: 1
```

### 전술 역할

- 굴복도 60% 이하에서 해금되는 반복 가능한 위기 역전기
- 횟수 제한은 없지만 쿨타임 2와 높은 실패 비용을 가짐
- 성공 시 Mount와 주도권을 동시에 확보
- 단순 고화력 기술이 아니라 피주도권·불리한 자세 전용

### 반복 사용 통제

- 성공 후 Mount에서는 발동 조건이 사라짐
- 쿨타임 2
- 자기 절정 +2
- 실패 시 굴복 피해·절정 위험
- 상대가 LowerBody를 봉쇄하면 사용 불가

---

# 8. Defiance 기술

## 8.1 SRV_Rachel_Def_BreathControl

### 기본 정보

```yaml
id: SRV_Rachel_Def_BreathControl
display_name: "가칭 — 호흡 정돈"
base_action_name: "호흡 정돈"
side: survivor
phase: submission
command_category: Defiance
power_grade: Minor
stability: High
cooldown: 2
```

### 효과

```yaml
resource_effects:
  climax_reduction: 2
  submission_recovery: 0

status_effects:
  next_reactive_modifier: 1
  duration: NextReactiveCheck

initiative_policy:
  on_success: pass_to_opponent
```

### 제한

- 절정 여운의 행동 스킵을 무효화하지 않음
- 굴복도를 회복하지 않음
- 완전 구속 상태에서는 사용 불가
- 절정도 0~1에서는 선택 가치가 낮도록 UI 후순위

### 전술 역할

- 레이첼의 낮은 탱킹 능력을 보완하는 절정도 관리
- 공격 기회를 포기하고 다음 Tease 성공률을 높이는 준비 행동
- 카운터 승부사형 루프에 직접 연결

---

# 9. Absorption 기술

## 9.1 SRV_Rachel_Absorb_RitualFluid

### 설계 의도

인간형 광신도 테스트에서 Absorption을 검증하기 위해, 광신도의 강제 키스·입 막기·의식성 체액 공격을 역이용하는 제한적 반응 기술로 설계한다.

이 기술은 일반적인 키스 기술이 아니라 `Fluid` 속성을 가진 적 기술에만 반응한다.

### 기본 정보

```yaml
id: SRV_Rachel_Absorb_RitualFluid
display_name: "가칭 — 체액 받아넘기기"
base_action_name: "체액 삼켜 넘기기"
side: survivor
phase: submission
command_category: Absorption
attack_axis: Fluid
power_grade: Standard
climax_gain_grade: Standard
stability: Low
cooldown: 3
```

### 반응 조건

```yaml
absorption_input:
  required_attack_axis: Fluid
  allowed_sources:
    - ForcedKiss
    - RitualSaliva
    - FluidGag
  required_target_group: Mouth
  forbidden_states:
    - MouthFullySealed
    - Unconscious
```

광신도의 모든 `강제 키스`가 자동으로 Fluid 공격이 되는 것은 아니다. 실제 기술 데이터에 `FluidPayload` 태그가 있어야 한다.

### 효과

```yaml
on_success:
  incoming_climax_gain_reduction: 2
  exhaustion_damage: 2
  apply_to_target:
    - ST_BreathDisrupted

self_resource_costs:
  self_climax_cost: 2
  failure_self_climax_cost: 2
  critical_failure_self_climax_cost: 4

risk:
  contamination_mark: 1
  mutation_risk: TestOnly
```

### 전술 역할

- Fluid 공격을 완전히 피하지 않고 일부 받아들여 자원 효과로 전환
- 절정도 증가를 낮추고 광신도의 호흡·집중을 무너뜨림
- 성공해도 자기 절정 +2와 오염 표식을 받는 양날 기술
- 일반 Contact 강제 키스에는 사용 불가

### 페이퍼 테스트용 오염 규칙

첫 수직 슬라이스에서는 오염 공식 전체를 만들지 않는다.

```text
오염 표식 1
→ 전투 종료 후 후유 검토 태그만 남김
→ 즉시 능력치 변화 없음
```

Absorption 자체의 입력·출력·위험 구조만 검증한다.

---

# 10. 기술 간 연계

## 10.1 기본 연계

```text
가슴 유혹 성공
→ 광신도 Chest Sensitive
→ 가슴 주무르기 또는 핸드잡
```

```text
하체 유혹 성공
→ 광신도 LowerBody Sensitive
→ 핸드잡
→ 탈진 임계에서 결정타
```

```text
호흡 정돈
→ 절정도 -2
→ 다음 반응 +1
→ Tease 성공 가능성 상승
```

```text
굴복도 60% 이하·피주도권
→ 기승위 역전
→ Mount 확보
→ Service 연계
```

```text
FluidPayload 강제 키스
→ 체액 받아넘기기
→ 절정 증가 경감
→ 광신도 호흡 붕괴
```

## 10.2 금지되는 연계

- 후방 공격에 하체 유혹 사용
- 의복 손상 준비기에 가슴 유혹 완전 카운터
- 일반 Contact 키스에 Absorption 사용
- 절정 여운 상태에서 호흡 정돈으로 행동 스킵 무효화
- 굴복도 60% 초과 상태에서 기승위 역전

---

# 11. 광신도 Bark 방향

광신도 Bark는 단순한 성적 도발이 아니라 다음 세 요소를 동시에 가져야 한다.

```text
광적인 신앙
+ 대상의 반응을 제물·계시로 해석
+ 현재 전투 행동에 대한 정보
```

## 11.1 기본 어휘 축

- 어머니
- 계시
- 축복
- 제물
- 성찬
- 정화
- 은총
- 문
- 목소리
- 내려오신다
- 받아들여라

## 11.2 금지 방향

- 모든 Bark에서 큰소리로 웃는 표현 반복
- 의미 없는 “미쳤다”식 횡설수설
- 전투 정보가 전혀 없는 장문 설교
- 같은 종교 어휘를 매 합 반복
- 현대적인 튜토리얼 문장

## 11.3 상황별 Bark 후보

### 공격 전조

> “가슴이 먼저 떨리는군. 어머니께서 그곳을 고르셨다.”

> “입을 열어라. 네 숨까지 성찬으로 바칠 테니.”

### 기술 성공

> “그래, 그 반응이다. 계시는 거짓말하지 않아.”

> “몸은 벌써 문을 열었는데, 네 입만 부정하는군.”

### 기술 실패·카운터당함

> “아니… 방금 그 움직임은 계시에 없었다.”

> “어머니의 손길을 흉내 내다니. 네가 감히.”

### 레이첼 절정 직전

> “조금만 더. 네 몸 안에서 문이 열리는 소리가 들린다.”

### 광신도 탈진 임계

> “이건 고통이 아니다… 시험이다. 어머니께서 보고 계신다.”

### 결착 직전

> “무릎을 꿇어라. 네가 아니라 네 몸이 먼저 믿게 될 것이다.”

## 11.4 출력 빈도

- 기술 최초 공개
- 정확한 카운터를 당했을 때
- 의복 방호 상실
- 절정 임계
- 광신도 탈진 25% 이하
- 피니셔 전조
- 결착

모든 합에 Bark를 출력하지 않는다.

---

# 12. 수직 슬라이스 페이퍼 테스트 계획

## 테스트 A — 기본 루프

목적:

- Service 선택 차이
- 정면 Tease 성공
- 반복 보호 행동

필수 장면:

1. 가슴 유혹으로 광신도 Chest 공격 카운터
2. 가슴 주무르기로 Sensitive 상승
3. 광신도가 Chest 보호
4. 핸드잡으로 LowerBody 전환

## 테스트 B — 패배 압박과 Domination

목적:

- 굴복도 60% 조건
- 전투당 제한 없는 기승위 역전
- 실패 비용과 쿨타임

필수 장면:

1. 레이첼 굴복도 6 이하
2. 광신도 주도권
3. 기승위 역전 1회 성공
4. 이후 조건 재충족 여부 확인
5. 두 번째 사용 가능하지만 비용 때문에 최적해가 아닌지 검증

## 테스트 C — Defiance

목적:

- 호흡 정돈의 절정도 -2
- 주도권 포기 비용
- 다음 반응 +1의 실질 가치

## 테스트 D — Absorption

목적:

- Contact와 Fluid 강제 키스 구분
- FluidPayload 전조 인지
- 성공 시 절정 증가 경감
- 오염 표식이 지나친 추가 시스템이 되지 않는지 검증

## 테스트 E — 광신도 Bark

평가 항목:

- 광기와 신앙이 느껴지는가
- 행동 전조 정보가 남는가
- 장문 설교로 전투 템포를 끊지 않는가
- 동일 어휘 반복이 심하지 않은가
- 레이첼 Bark와 화자 구분이 되는가

---

# 13. 완료 기준

- 7종 기술의 역할이 중복되지 않는다.
- 후방 공격은 레이첼의 명확한 약점으로 남는다.
- 기승위 역전은 횟수 제한 없이도 조건·비용·쿨타임으로 통제된다.
- Absorption은 FluidPayload 없이는 선택 목록에 나타나지 않는다.
- Service 반복보다 부위 전환이 유리한 장면이 발생한다.
- 호흡 정돈이 만능 회복기가 아니다.
- 광신도 Bark에서 신앙적 광기와 전투 정보가 동시에 드러난다.
- 기술명 변경 후에도 ID와 전술 역할은 유지된다.
- 승리·패배 양쪽 결과가 가능하다.

---

# 14. 미확정 항목

- 디렉터의 최종 기술명
- 실제 `base_power` 환산 공식
- 쿨타임의 합·행동 단위 정의
- 부분 성공 Tease의 경감량
- 오염·Mutation 장기 공식
- FluidPayload 광신도 기술의 정식 ID
- 레이첼 초기 보유 기술과 학습 기술 구분
- 전투 후 오염 표식 처리
- 광신도 Bark 개체별 말투 변종

---

# 15. 변경 이력

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| 0.1.0 | 2026-07-27 | 레이첼 카운터 승부사형 기술 7종, 인간형 광신도 Bark 방향, 페이퍼 테스트 계획 작성 |
