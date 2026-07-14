---
id: MECH_R18_Skill_Catalog_Survivor_Core
title: "핵심 시스템 사양서 — R18 생존자 굴복 기술 코어"
type: mechanic
status: wip
version: 1.0.0
summary: >
  생존자 굴복 페이즈 공용 대표 기술 5종에 영문 정본 키, Return 해금 슬롯,
  기벽 전용 변종 슬롯과 완화 중 비활성 정책을 적용한다.
tags: [mechanic, r18, skill, survivor, catalog]
depends_on:
  - MECH_R18_Skill_Catalog
  - MECH_R18_Skill_Data_Contract
  - MECH_R18_Quirk_Skill_Return_Map
  - MECH_R18_Memory_Log
  - MECH_Quirk_R18_DB
last_updated: 2026-07-14
---

# R18 생존자 굴복 기술 코어 (v1.0)

## 0. 소유 및 마이그레이션 원칙

- 본 문서는 기존 `MECH_R18_Skill_Catalog` SECTION 4의 대표 기술 5종을 새 스키마로 옮기는 정본 샤드다.
- 기존 Skill ID는 변경하지 않는다.
- 전투 상성, 자세 게이팅과 effect 동작은 기존 카탈로그와 Combat System을 따른다.
- 런타임은 동일 ID가 중복되면 본 샤드의 정의를 우선한다.
- 기존 SECTION 4 교체가 완료되면 본 샤드는 카탈로그 하위 데이터 파일로 유지하거나 본문에 병합할 수 있다.

## 1. 공통 규칙

```yaml
survivor_core_skill_policy:
  base_pool_access: all_adult_survivors
  base_skill_requires_quirk: false
  proficiency_variant_limit_per_quirk: 1
  milestone_unlock:
    - second_variant_candidate
    - strong_special_effect_candidate
  mitigation:
    base_skill_available: true
    disable_quirk_variants: true
    disable_direct_return_effects: true
```

- 기벽은 기본 기술을 해금하지 않고 기술 변종과 Return을 해금한다.
- 하나의 기벽이 여러 분류와 연결되더라도 `Proficiency`에서는 대표 변종 1개만 활성화한다.
- `Milestone`에서 두 번째 변종 또는 강한 특수 효과를 추가할 수 있다.
- 완화 중에도 기본 기술은 사용 가능하다.

---

## 2. 봉사형 대표 기술

```yaml
- id: SB_Service_Kiss
  base_skill_id: SB_Service_Kiss
  variant_id: null
  name: 입맞춤
  side: survivor
  phase: submission
  sub_category: service
  target: single
  gauge_delta:
    arousal_target: 2
    arousal_self: 1
  progress_axis: Contact
  progress_part: Mouth
  display_part: 입
  required_target_parts: [Mouth]
  action_parts: [Mouth]
  valid_postures: [Front, Bound]
  variant_source_quirks: []
  return_unlock_id: null
  required_memory_stage: record
  required_part_level: 0
  required_flags: []
  mitigation_policy:
    base_skill_available: true
    disable_variant_when_suppressed: true
    disabled_effect_ids: []
  effect_id: null
  log:
    on_use: ["떨리는 입술을 가져다 댔다."]
    on_hit: ["맞닿은 곳에서 열이 옮아왔다."]
```

### 대표 변종 슬롯

- **Proficiency 우선 후보**: 접촉 기갈 또는 가학 복종의 정당성 중 실제 기벽 조건을 충족한 하나의 봉사 변종
- **Milestone 후보**: 관계 비용 교환형 또는 리더 연계형 특수 효과
- 수치만 높은 입맞춤은 별도 변종으로 만들지 않는다.

---

## 3. 유혹형 대표 기술

```yaml
- id: SB_Tease_Caress
  base_skill_id: SB_Tease_Caress
  variant_id: null
  name: 애무 지연
  side: survivor
  phase: submission
  sub_category: tease
  target: single
  gauge_delta:
    arousal_target: 1
  progress_axis: Contact
  progress_part: WholeBody
  display_part: 전신
  required_target_parts: [WholeBody]
  action_parts: [Hand]
  valid_postures: [Confrontation, Front, Mount]
  bypass_gating: false
  variant_source_quirks: []
  return_unlock_id: null
  required_memory_stage: record
  required_part_level: 0
  required_flags: []
  mitigation_policy:
    base_skill_available: true
    disable_variant_when_suppressed: true
    disabled_effect_ids: []
  status_inflict: [ST_Trance]
  effect_id: fx_sub_weaken_next
  log:
    on_use: ["손끝으로 천천히 윤곽을 그렸다."]
    on_hit: ["놈의 움직임이 한 박자 늦춰졌다."]
```

### 대표 변종 슬롯

- **Proficiency 우선 후보**: 유두 민감화 기반 `Chest` 부위 유혹 변종
- **Milestone 후보**: 전신 성감대화 또는 노출증 기반 자세·상태 교환형 변종
- 감각 완화 중 해당 기벽 전용 부위 변종만 비활성화한다.

---

## 4. 농락형 대표 기술

```yaml
- id: SB_Dom_Ride
  base_skill_id: SB_Dom_Ride
  variant_id: null
  name: 역제압
  side: survivor
  phase: submission
  sub_category: domination
  target: single
  gauge_delta:
    arousal_target: 4
  progress_axis: Subjugation
  progress_part: LowerBody
  display_part: 하복부
  required_target_parts: [LowerBody, WholeBody]
  action_parts: [LowerBody]
  valid_postures: [Mount]
  posture_force: Mount
  scaling: erosion
  variant_source_quirks: []
  return_unlock_id: null
  required_memory_stage: record
  required_part_level: 0
  required_flags: []
  mitigation_policy:
    base_skill_available: true
    disable_variant_when_suppressed: true
    disabled_effect_ids: []
  status_inflict: [ST_Afterglow]
  effect_id: fx_sub_dom_scaling
  log:
    on_use: ["몸을 일으켜 흐름을 뒤집었다."]
    on_hit: ["놈의 호흡이 거칠게 무너졌다."]
```

### 대표 변종 슬롯

- **Proficiency 우선 후보**: 가학증 또는 피학증 중 하나의 역전 역할 변종
- **Milestone 후보**: 자궁 개발·전신 성감대화·쾌감 수용체 폭주 기반 고위험 피니셔
- 강한 변종은 침식·로그 증가·실패 비용 중 하나 이상을 반드시 동반한다.

---

## 5. 흡수형 대표 기술

```yaml
- id: SB_Absorb_Drink
  base_skill_id: SB_Absorb_Drink
  variant_id: null
  name: 동화 섭취
  side: survivor
  phase: submission
  sub_category: absorption
  target: single
  gauge_delta:
    arousal_target: 2
  progress_axis: Fluid
  progress_part: Mouth
  display_part: 입
  required_target_parts: [Mouth]
  action_parts: [Mouth]
  valid_postures: [Front, Bound]
  scaling: sens_level
  variant_source_quirks: []
  return_unlock_id: null
  required_memory_stage: record
  required_part_level: 0
  required_flags: []
  mitigation_policy:
    base_skill_available: true
    disable_variant_when_suppressed: true
    disabled_effect_ids: []
  effect_id: fx_sub_absorb_recover
  log:
    on_use: ["흘러나온 것을 받아 삼켰다."]
    on_hit: ["몸 안쪽이 뜨겁게 채워졌다."]
```

### 대표 변종 슬롯

- **Proficiency 우선 후보**: 정액 중독 기반 의존·회복 변종
- **Milestone 후보**: 피부 유즙화 또는 쾌감 수용체 폭주 기반 자원 교환 변종
- 흡수 Return 완화 중에는 전용 회복·강화만 정지하고 기본 `Fluid` 진척은 유지한다.

---

## 6. 저항형 대표 기술

```yaml
- id: SB_Defiance_Focus
  base_skill_id: SB_Defiance_Focus
  variant_id: null
  name: 정신 집중
  side: survivor
  phase: submission
  sub_category: defiance
  target: self
  gauge_delta: {}
  progress_axis: null
  progress_part: null
  display_part: null
  required_target_parts: []
  action_parts: []
  valid_postures: [Confrontation, Front, RearEntry, Mount, Bound]
  bypass_gating: true
  variant_source_quirks: []
  return_unlock_id: null
  required_memory_stage: record
  required_part_level: 0
  required_flags: []
  mitigation_policy:
    base_skill_available: true
    disable_variant_when_suppressed: true
    disabled_effect_ids: []
  status_inflict: []
  effect_id: fx_sub_defiance
  log:
    on_use: ["이를 악물고 의식을 붙들었다."]
    on_hit: ["흐려지던 시야가 잠시 또렷해졌다."]
```

### 대표 변종 슬롯

- **Proficiency 우선 후보**: 괴물 성애의 자제 판정 또는 후장 개발의 버티기 변종
- **Milestone 후보**: 피학증 기반 피해 전환 또는 강박적 자위벽 기반 행동 회복 효과
- 저항형의 `bypass_gating`은 기본 기술 안전판이므로 기벽 완화로 비활성화하지 않는다.

---

## 7. 변종 해금 선택 규칙

하나의 생존자가 동일 기벽으로 여러 변종 후보를 충족하면 다음 순서로 선택한다.

```text
1. 현재 기벽의 primary_return_category 확인
2. Proficiency 대표 변종 1개 해금
3. 다른 분류 후보는 잠금 유지
4. Milestone 도달 시 두 번째 변종 또는 특수 효과 중 하나를 선택
```

- 자동으로 모든 후보를 해금하지 않는다.
- NPC 고유 특성이나 사건 선택으로 대표 분류가 달라질 수 있다.
- 선택한 변종은 저장 데이터에 `selected_quirk_variants`로 기록한다.

```yaml
selected_quirk_variants:
  survivor_id:
    quirk_id:
      proficiency_variant_id: null
      milestone_unlock_id: null
```

---

## 8. 검증 규칙

- 5개 기본 Skill ID가 기존 카탈로그와 동일해야 한다.
- `progress_part`에는 영문 정본 키만 사용한다.
- `display_part`는 판정에 사용하지 않는다.
- 기본 기술은 `variant_source_quirks: []`여야 한다.
- 기벽 변종은 반드시 `base_skill_id`, 원천 기벽과 해금 조건을 가져야 한다.
- 완화 중 기본 기술은 선택 목록에서 제거하지 않는다.
- Proficiency 단계에서 동일 기벽의 활성 변종은 최대 1개다.

---

## 9. 버전 관리

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.0.0 | 2026-07-14 | 생존자 대표 기술 5종에 정본 키·Return 슬롯·완화 정책·변종 단계 제한 적용. |

**갱신 기준**: 대표 변종 ID·effect·비용을 확정하고 기존 Skill Catalog SECTION 4 교체 검증 후 정본 잠금.