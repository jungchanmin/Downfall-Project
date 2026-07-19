---
id: MECH_R18_Cultist_Submission_Skill_Migration
title: "핵심 시스템 사양서 — 광신도 굴복 기술 6종 마이그레이션"
type: mechanic
status: wip
version: 1.0.0
summary: >
  기존 광신도 굴복 기술 6종을 최신 R18SkillDef, Gate Tag, 전조, 쿨타임,
  주도권, 콤보·피니셔 계약에 맞춰 마이그레이션한다.
tags: [mechanic, r18, skill, cultist, migration, telegraph, gate]
depends_on:
  - MECH_R18_Skill_Catalog_Core
  - MECH_R18_Gate_Tag_Standard
  - MECH_R18_Submission_Core_System
  - MECH_R18_Telegraph_Bark_Content_Policy
last_updated: 2026-07-19
---

# 광신도 굴복 기술 6종 마이그레이션 v1.0

## 0. 적용 범위

대상 기술:

- `SR_Cog_ForcedKiss`
- `SR_Cog_EarLick`
- `SR_Cog_Caress`
- `SR_Sub_Pin`
- `SR_Sub_Gag`
- `SR_Sub_Thrust`

기존 Skill ID, 표시명, 기본 연출 의도와 로그 문장은 보존한다.

이번 문서는 다음 필드를 최신 정본으로 제공한다.

- `base_power`
- `stability`
- `cooldown`
- `required_target_parts`
- `action_parts`
- `valid_postures`
- `posture_force`
- `gate_attack`
- `telegraph_profile_id`
- `initiative_effects`
- `ai_conditions`
- `combo_links`
- `finisher_conditions`

정확한 수치 밸런스는 아직 확정하지 않는다. 이번 단계의 숫자는 상대 등급과 역할 구분을 위한 임시 등급값이다.

---

## 1. 광신도 기술 키트 정체성

광신도는 다음 전투 흐름을 가진다.

```text
Cognition 기술
→ 전조 판독·행동 선택·상태 저항 약화
→ 자세·행동 부위 점유
→ Subjugation 기술
→ 굴복도 압박·주도권 유지
→ 조건부 피니셔
```

핵심은 강한 단일 공격이 아니라, 인지 교란으로 잘못된 대응을 유도한 뒤 함락 기술을 연결하는 것이다.

### 권장 기술 키트

```yaml
monster_submission_kit:
  kit_id: KIT_Cultist_Submission_Core

  signature_skills:
    - SR_Cog_ForcedKiss
    - SR_Sub_Pin

  core_skills:
    - SR_Cog_EarLick
    - SR_Cog_Caress
    - SR_Sub_Gag

  conditional_skills:
    - SR_Sub_Thrust

  variant_pools: []

  opening_patterns:
    - PAT_Cultist_Approach_Whisper

  combo_patterns:
    - PAT_Cultist_Cognition_To_Pin
    - PAT_Cultist_Pin_To_Gag

  finisher_patterns:
    - PAT_Cultist_Subjugation_Finish
```

첫 수직 슬라이스에서는 랜덤 변주 슬롯을 사용하지 않는다. 광신도 기술 흐름을 플레이어가 학습할 수 있어야 하기 때문이다.

---

## 2. 공통 전조 원칙

광신도는 완전한 기술명을 UI로 공개하지 않는다.

```text
내부 데이터
→ Gate Tag·전조 아키타입·관찰 단계

플레이어 출력
→ 물리 Cue·Narration·상황 Bark
```

일반 관찰 실패:

```text
“뭔가 속삭이고 있어… 의도를 읽기 어려워.”
```

인지 교란 상태의 거짓 확신:

```text
“정면으로 밀어붙일 거야. 확실해.”
```

거짓 Bark는 `Cognition` effect가 명시적으로 생성할 때만 사용한다.

---

## 3. 인지 기술 3종

### 3-1. `SR_Cog_ForcedKiss` — 강제 입맞춤

```yaml
id: SR_Cog_ForcedKiss
name: 강제 입맞춤
side: monster
phase: submission
attack_axis: Cognition

base_power: 2
stability: 3
cooldown: 2

progress_axis: Cognition
progress_part: Mouth

required_target_parts:
  - Mouth

action_parts:
  - Mouth
  - Hand

valid_postures:
  - Confrontation
  - Front

posture_force: Front

gate_attack:
  approach: Close
  directions: [Front]
  target_parts: [Mouth]
  action_parts: [Mouth, Hand]
  controls: [Grab, Pull]
  motions: [Telegraphed]
  results: [PostureForce, TargetOccupy, ActionOccupy]
  occupy_target_parts: [Mouth]
  occupy_action_parts: [Mouth]

telegraph_profile_id: TEL_CULTIST_FORCED_KISS

status_inflict:
  - ST_Trance

effect_ids:
  - cognition_hint_distort
  - mouth_occupy

initiative_effects:
  on_gate_cancel: pass_to_defender
  on_status_combo: initiative_hold_candidate

ai_conditions:
  requires_initiative: true
  avoid_if_target_mouth_occupied_by_self: true
  priority_bonus_if_target_cognition_resistance_low: true

combo_links:
  on_success:
    - SR_Sub_Pin
    - SR_Sub_Gag
```

전술 역할:

- 광신도의 대표 접근기.
- Mouth를 점유하고 `ST_Trance`를 부여해 다음 전조 판독을 흐린다.
- 기본적으로 행동 취소 후 주도권은 넘기지만, `ST_Trance`가 콤보 유지 조건을 충족하면 `initiative_hold` 후보가 된다.

전조 아키타입:

```text
TEL_CLOSE_DISTANCE
TEL_FRONTAL_GRAB
TEL_PART_FIXATION:Mouth
TEL_COGNITION_FOCUS
```

Narration 후보:

- 광신도의 시선이 입가에 고정된 채 거리를 좁혔다.
- 한 손이 턱 아래로 올라오고, 상체가 정면으로 기울었다.

Bark 후보:

- “턱을 잡으려 해. 정면에서 들어온다.”
- “입을 노리고 있어. 손부터 쳐내!”

Tease 카운터 후보 태그:

```text
Front + Mouth + Grab
```

---

### 3-2. `SR_Cog_EarLick` — 귓속 애무

```yaml
id: SR_Cog_EarLick
name: 귓속 애무
side: monster
phase: submission
attack_axis: Cognition

base_power: 1
stability: 4
cooldown: 1

progress_axis: Cognition
progress_part: Mouth

required_target_parts:
  - WholeBody

action_parts:
  - Mouth

valid_postures:
  - Front
  - RearEntry
  - Bound

posture_force: null

gate_attack:
  approach: Close
  directions: [Front, Rear]
  target_parts: [WholeBody]
  action_parts: [Mouth]
  controls: [Hold]
  motions: [Subtle]
  results: [ActionDisrupt]

action_parts_affected:
  - Mouth

telegraph_profile_id: TEL_CULTIST_EAR_WHISPER

status_inflict:
  - ST_Enthrall

effect_ids:
  - telegraph_confidence_down
  - quirk_resistance_down

initiative_effects:
  on_success: no_automatic_take
  on_status_combo: initiative_hold_support

ai_conditions:
  prefer_if_target_has_seen_signature_telegraph: true
  prefer_if_target_support_bark_active: true
  avoid_if_target_cognition_resistance_high: true

combo_links:
  on_success:
    - SR_Cog_Caress
    - SR_Sub_Gag
```

전술 역할:

- 낮은 위력의 안정적인 인지 교란기.
- 자세를 강제하기보다 전조 신뢰도와 기벽 저항을 낮춘다.
- 자체 피니셔가 아니라 후속 기술의 오판 확률을 높이는 연결기다.

전조 아키타입:

```text
TEL_CLOSE_DISTANCE
TEL_REAR_APPROACH
TEL_COGNITION_FOCUS
```

Narration 후보:

- 광신도가 고개를 비스듬히 기울이며 귀 가까이 파고들었다.
- 숨결이 목덜미와 귓가를 따라 느리게 스쳤다.

Bark 후보:

- “뒤로 붙고 있어. 시야 밖으로 보내지 마.”
- “말을 듣지 마. 호흡부터 끊어.”

Tease 카운터 후보 태그:

```text
Rear + Close + Hold
```

이 기술은 강한 자세 게이팅기가 아니므로 부분 일치 카운터 시 상태 부여만 차단하는 결과가 적합하다.

---

### 3-3. `SR_Cog_Caress` — 농밀한 더듬기

```yaml
id: SR_Cog_Caress
name: 농밀한 더듬기
side: monster
phase: submission
attack_axis: Cognition

base_power: 2
stability: 3
cooldown: 2

progress_axis: Cognition
progress_part: Chest

required_target_parts:
  - Chest

action_parts:
  - Hand

valid_postures:
  - Confrontation
  - Front
  - Bound

posture_force: Front

gate_attack:
  approach: Close
  directions: [Front]
  target_parts: [Chest]
  action_parts: [Hand]
  controls: [Grab, Hold]
  motions: [Feint, Telegraphed]
  results: [PostureForce, TargetOccupy]
  occupy_target_parts: [Chest]

telegraph_profile_id: TEL_CULTIST_COG_CARESS

status_inflict:
  - ST_Enthrall

effect_ids:
  - chest_occupy
  - false_cue_seed

initiative_effects:
  on_gate_cancel: pass_to_defender
  on_false_response: initiative_hold_candidate

ai_conditions:
  prefer_if_target_received_false_telegraph: true
  prefer_if_chest_counter_unavailable: true
  avoid_if_target_chest_occupied_by_other_effect: true

combo_links:
  on_success:
    - SR_Sub_Pin
```

전술 역할:

- 인지축이지만 실제로는 Chest를 점유하는 페인트형 게이팅 공격.
- 이전 인지 교란으로 잘못된 대응을 선택하게 만든 뒤 자세를 Front로 고정한다.
- `false_cue_seed`는 다음 전조에서 구체적이지만 잘못된 Bark를 생성할 수 있는 후보 effect다.

전조 아키타입:

```text
TEL_CLOSE_DISTANCE
TEL_FRONTAL_GRAB
TEL_PART_FIXATION:Chest
TEL_FEINT
```

Narration 후보:

- 광신도의 손이 한차례 어깨를 향했다가 갑자기 가슴께로 꺾였다.
- 시선과 손끝이 서로 다른 방향을 가리켰다.

Bark 후보:

- “시선은 속임수야. 손목을 봐!”
- “가슴을 노린다. 정면에서 잡으려 해.”

Tease 카운터 후보 태그:

```text
Front + Chest + Grab
```

---

## 4. 함락 기술 3종

### 4-1. `SR_Sub_Pin` — 짓누르기

```yaml
id: SR_Sub_Pin
name: 짓누르기
side: monster
phase: submission
attack_axis: Subjugation

base_power: 3
stability: 3
cooldown: 3

progress_axis: Subjugation
progress_part: WholeBody

required_target_parts:
  - WholeBody

action_parts:
  - Hand
  - LowerBody

valid_postures:
  - Front
  - RearEntry

posture_force: Bound

gate_attack:
  approach: Close
  directions: [Front, Rear]
  target_parts: [WholeBody]
  action_parts: [Hand, LowerBody]
  controls: [Push, Pin]
  motions: [Committed, Telegraphed]
  results: [PostureForce, FullRestraint, TargetOccupy, ActionOccupy]
  occupy_target_parts: [WholeBody]
  occupy_action_parts: [Hand, LowerBody]

telegraph_profile_id: TEL_CULTIST_FULL_PIN

effect_ids:
  - will_break
  - full_restraint

initiative_effects:
  on_gate_cancel: initiative_hold
  chain_cost: 1

ai_conditions:
  requires_initiative: true
  prefer_if_target_trance_or_enthrall: true
  avoid_if_combo_chain_limit_reached: true

combo_links:
  on_success:
    - SR_Sub_Gag
    - SR_Sub_Thrust
```

전술 역할:

- 광신도의 핵심 구속기.
- 성공 시 `Bound` 자세와 WholeBody 점유를 만든다.
- 강한 게이팅 기술이므로 행동 취소 후 주도권 유지 effect를 명시적으로 가진다.
- 콤보 연속 상한을 1 소비한다.

전조 아키타입:

```text
TEL_CLOSE_DISTANCE
TEL_FULL_RESTRAINT
TEL_FINISHER_PREP
```

Narration 후보:

- 광신도가 무게중심을 낮추고 양팔을 크게 벌렸다.
- 어깨와 허리가 동시에 앞으로 쏠리며 몸 전체를 덮칠 준비를 했다.

Bark 후보:

- “전신으로 덮쳐온다. 잡히면 바닥에 묶여!”
- “중심을 빼! 정면으로 버티면 눌린다.”

Tease 카운터 후보 태그:

```text
Front|Rear + WholeBody + Pin
```

단일 범용 Tease로 대응하기 어려운 고위험 기술이다. 좁은 전용 카운터 또는 Domination 역전 조건을 요구하는 편이 적합하다.

---

### 4-2. `SR_Sub_Gag` — 입 틀어막기

```yaml
id: SR_Sub_Gag
name: 입 틀어막기
side: monster
phase: submission
attack_axis: Subjugation

base_power: 2
stability: 4
cooldown: 2

progress_axis: Subjugation
progress_part: Mouth

required_target_parts:
  - Mouth

action_parts:
  - Hand
  - Mouth

valid_postures:
  - RearEntry
  - Bound

posture_force: null

gate_attack:
  approach: Close
  directions: [Rear]
  target_parts: [Mouth]
  action_parts: [Hand, Mouth]
  controls: [Cover, Hold]
  motions: [Subtle]
  results: [TargetOccupy, ActionOccupy, BarkSuppress]
  occupy_target_parts: [Mouth]
  occupy_action_parts: [Mouth]

telegraph_profile_id: TEL_CULTIST_GAG

effect_ids:
  - submission_offering
  - bark_suppress
  - support_call_lock

initiative_effects:
  on_success: initiative_hold_if_bound
  chain_cost: 1

ai_conditions:
  requires_target_posture_any: [RearEntry, Bound]
  prefer_if_support_bark_active: true
  prefer_if_target_submission_low: true

combo_links:
  on_success:
    - SR_Sub_Thrust
```

전술 역할:

- Mouth와 Bark를 동시에 봉쇄해 전조 정보 전달과 도움 요청을 약화한다.
- `Bound` 상태에서 성공하면 주도권 유지 후보가 된다.
- 광신도의 인지 교란 테마를 함락 단계까지 이어준다.

전조 아키타입:

```text
TEL_REAR_APPROACH
TEL_HAND_RESTRAINT
TEL_PART_FIXATION:Mouth
```

Narration 후보:

- 뒤쪽에서 팔이 목선을 감싸고, 다른 손이 입가로 올라왔다.
- 시야 밖의 손바닥이 입을 덮으려 빠르게 움직였다.

Bark 후보:

- “뒤야! 입을 막으려 해!”
- “손부터 떼어내. 도움을 부를 수 없게 만들 거야.”

Tease 카운터 후보 태그:

```text
Rear + Mouth + Cover
```

---

### 4-3. `SR_Sub_Thrust` — 깊숙이 박기

```yaml
id: SR_Sub_Thrust
name: 깊숙이 박기
side: monster
phase: submission
attack_axis: Subjugation

base_power: 4
stability: 2
cooldown: 4

progress_axis: Subjugation
progress_part: LowerBody

required_target_parts:
  - LowerBody

action_parts:
  - LowerBody

valid_postures:
  - Front
  - RearEntry
  - Bound

posture_force: null

gate_attack:
  approach: Close
  directions: [Front, Rear]
  target_parts: [LowerBody]
  action_parts: [LowerBody]
  controls: [Drive, Pin]
  motions: [Committed, Telegraphed]
  results: [TargetOccupy, Finisher]
  occupy_target_parts: [LowerBody]

telegraph_profile_id: TEL_CULTIST_SUBJUGATION_FINISHER

status_inflict:
  - ST_Afterglow

effect_ids:
  - subjugation_finisher
  - afterglow_apply

initiative_effects:
  on_success: initiative_hold_if_not_chain_limit
  chain_cost: 1

finisher_conditions:
  all_of:
    - target_submission_below: TBD
    - requires_initiative: true
    - target_posture_any: [Front, RearEntry, Bound]
    - required_status_any: [ST_Restraint, ST_Trance, ST_Enthrall]
    - previous_skill_any: [SR_Sub_Pin, SR_Sub_Gag]

ai_conditions:
  only_if_finisher_conditions_met: true
  avoid_if_combo_chain_limit_reached: true

combo_links:
  on_success:
    - END_COMBO
```

전술 역할:

- 광신도 키트의 조건부 결정타.
- 단순히 굴복도가 낮다는 이유만으로 사용할 수 없다.
- 주도권, 자세, 상태이상, 이전 콤보 기술 중 복수 조건을 요구한다.
- 실패하거나 카운터되면 광신도가 큰 빈틈을 노출하는 하이리스크 피니셔다.

전조 아키타입:

```text
TEL_PART_FIXATION:LowerBody
TEL_FINISHER_PREP
TEL_COMMITTED_ATTACK
```

Narration 후보:

- 광신도의 호흡이 거칠어지고, 하체가 한순간 뒤로 당겨졌다.
- 움직임이 멎은 직후, 체중이 한 방향으로 완전히 실렸다.

Bark 후보:

- “끝내려는 동작이야. 지금 못 끊으면 위험해!”
- “중심이 완전히 쏠렸어. 피하거나 뒤집을 마지막 기회야.”

Tease 카운터 후보 태그:

```text
Front|Rear + LowerBody + Drive
```

전용 Tease가 없으면 Defiance로 피해를 줄이거나 조건을 사전에 해제하는 것이 정공법이다.

---

## 5. 광신도 콤보 패턴

### 5-1. 인지 교란 진입

```text
SR_Cog_ForcedKiss
→ ST_Trance
→ SR_Cog_Caress 또는 SR_Sub_Pin
```

목적:

- Mouth 점유
- 전조 신뢰도 저하
- 잘못된 Tease 선택 유도

### 5-2. 후방 봉쇄

```text
SR_Cog_EarLick
→ ST_Enthrall
→ SR_Sub_Gag
```

목적:

- 지원 Bark 약화
- 도움 요청 봉쇄
- 함락 피니셔 준비

### 5-3. 구속 피니셔

```text
SR_Sub_Pin
→ Bound
→ SR_Sub_Gag
→ SR_Sub_Thrust
```

안전장치:

- 각 주도권 유지 시 `chain_count` 증가
- `chain_limit`에 도달하면 다음 합 종료 후 주도권 이전
- `SR_Sub_Thrust`는 복수 피니셔 조건이 없으면 AI가 선택하지 않음
- Defiance로 상태 또는 자세 조건을 제거하면 피니셔 잠금
- 전용 Tease 또는 Domination 역전으로 `SR_Sub_Pin`을 끊으면 전체 콤보 붕괴

---

## 6. 카운터 설계 요약

| 광신도 기술 | 주요 Gate Tag | 권장 대응 |
|---|---|---|
| ForcedKiss | Front + Mouth + Grab | Mouth·Hand 기반 Tease |
| EarLick | Rear + Close + Hold | 후방 접근 Tease 또는 거리 벌리기 |
| CogCaress | Front + Chest + Grab | Chest 카운터 Tease |
| Pin | Front/Rear + WholeBody + Pin | 전용 Tease, Domination 역전, Defiance |
| Gag | Rear + Mouth + Cover | 후방 Mouth 카운터 Tease |
| Thrust | Front/Rear + LowerBody + Drive | 전용 Tease, 조건 해제 Defiance, 역전 Domination |

Tease는 분류만으로 대응할 수 없다. 실제 보유 기술의 `counter_profile`이 해당 필수 태그를 만족해야 한다.

---

## 7. 데이터 검증

| ID | 검증 규칙 |
|---|---|
| CUL-001 | 6개 기술 모두 `base_power`와 `cooldown`을 가져야 한다. |
| CUL-002 | 게이팅 공격은 `gate_attack`과 `telegraph_profile_id`를 가져야 한다. |
| CUL-003 | `SR_Sub_Thrust`는 복수 피니셔 조건 없이 선택할 수 없다. |
| CUL-004 | `SR_Sub_Pin`의 `initiative_hold`는 콤보 상한을 소비한다. |
| CUL-005 | `SR_Sub_Gag`의 Bark 봉쇄는 Mouth 점유가 해제되면 종료한다. |
| CUL-006 | Cognition 기술의 거짓 Bark는 명시된 effect가 있을 때만 발생한다. |
| CUL-007 | 광신도 변주 슬롯은 첫 수직 슬라이스에서 비활성이다. |
| CUL-008 | 기술의 Gate Tag는 정본 기본 태그 조합만 사용한다. |

---

## 8. 미확정 항목

- 실제 `base_power` 수치 범위
- 실제 쿨타임 턴 수
- `ST_Trance / ST_Enthrall / ST_Afterglow` 세부 데이터 계약
- `chain_limit` 실제 수치
- 부분 일치 Tease의 실제 경감량
- 광신도 등급별 기술 키트 차이
- 광신도 전용 Bark 실제 문체와 음성 연출
- Unity effect ID 최종 명명

---

## 9. 버전 관리

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.0.0 | 2026-07-19 | 광신도 굴복 기술 6종의 최신 스키마·Gate Tag·전조·쿨타임·AI·콤보·피니셔 계약 마이그레이션. |
