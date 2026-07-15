---
id: MECH_R18_Proficiency_Variant_Catalog
title: "핵심 시스템 사양서 — R18 Proficiency 대표 변종 카탈로그"
type: mechanic
status: wip
version: 1.1.0
summary: >
  생존자 굴복 기술 5대분류에 각 1종의 Proficiency 대표 변종을 부여하고,
  굴복 페이즈 코어 역할·주도권·게이팅·카운터·상태이상과 연결되는 효과 계약을 정의한다.
tags: [mechanic, r18, skill, variant, proficiency]
depends_on:
  - MECH_R18_Skill_Catalog_Survivor_Core
  - MECH_R18_Quirk_Skill_Return_Map
  - MECH_R18_Quirk_Development_Priority
  - MECH_R18_Submission_Core_System
last_updated: 2026-07-15
---

# R18 Proficiency 대표 변종 카탈로그 v1.1

## 1. 공통 원칙

- 각 기술 분류당 대표 변종 1종만 먼저 구현한다.
- 각 변종은 하나의 원천 기벽을 가진다.
- 변종은 기본 커맨드 역할을 대체하지 않고 특정 교환 지점을 강화한다.
- 단순 피해·게이지 수치 상향이 아니라 새로운 선택과 대가를 제공한다.
- 원천 기벽의 관련 Risk가 완화 중이면 변종과 전용 effect를 비활성화한다.
- 기본 기술은 계속 사용할 수 있다.
- 역상성 카운터 성공 시 주도권 탈취는 코어 규칙을 따른다.
- 행동 취소 후 주도권 유지가 필요하면 `initiative_hold`를 명시한다.

```yaml
R18SkillVariant:
  variant_id:
  base_skill_id:
  source_quirk:
  required_memory_stage: proficiency
  required_part_level:
  tactical_role:
  trigger_window:
  gate_requirements: []
  success_effects: []
  partial_success_effects: []
  failure_effects: []
  initiative_effect:
  added_risk: []
  mitigation_policy:
  milestone_extension_slot:
```

---

## 2. 봉사형 — 저부담 능동 견제

### `SBV_Service_TactileAnchor`

- **표시명**: 접촉의 닻
- **기본 기술**: `SB_Service_Kiss`
- **원천 기벽**: `#Trait_Tactile_Deprivation`
- **요구**: `Contact Proficiency`, `Mouth Lv1`
- **전술 역할**: 저부담 능동 견제·점유 준비 방해
- **발동 시점**: 주도권 보유 시 능동 사용
- **게이트**: Mouth 사용 가능, Front 또는 Confrontation
- **효과 방향**:
  - 낮은 자기 부담으로 상대 흥분·탈진을 안정적으로 누적한다.
  - 성공 시 상대의 다음 자세 강제 또는 부위·행동 점유 강도를 약화하는 견제 effect 후보.
  - 상대의 `initiative_hold` 준비 상태를 1회 약화하거나 제거하는 후보.
  - 동료 지원은 부가 Milestone 후보로 이동한다.
- **부분 성공**:
  - 기본 견제만 적용하고 점유 약화는 적용하지 않는다.
  - 주도권은 기본 규칙에 따라 처리한다.
- **실패**:
  - 자기 Contact 로그와 흥분 부담 증가.
  - 상대가 강제 자세·점유 준비 보정을 얻을 수 있다.
- **주도권**: 기본적으로 자동 유지하지 않는다.
- **추가 Risk**:
  - Contact 로그 증가.
  - 같은 전투 반복 사용 시 욕구불만 또는 자기 흥분 누적 후보.
- **완화 중**: 접촉 기갈 Risk 안정화 중 변종 비활성.
- **Milestone 슬롯**: 동료 전조 보조 또는 상대 점유 effect 1회 무효 중 하나.

설계 의도: Service의 공세·견제 정체성을 유지하면서, 큰 피해 대신 상대의 다음 콤보 준비를 흐트러뜨린다.

---

## 3. 유혹형 — 즉응 패링·카운터

### `SBV_Tease_ChestFeint`

- **표시명**: 감각 유인
- **기본 기술**: `SB_Tease_Caress`
- **원천 기벽**: `#Trait_Hypersensitive_Nipples`
- **요구**: `Contact Proficiency`, `Chest Lv1`
- **전술 역할**: 현재 공격에 대한 고위험 패링·카운터
- **발동 시점**: 피주도권 상태에서 전조 확인 후 대응
- **게이트**: Chest 접근 가능, 구속으로 대응 자체가 봉쇄되지 않음
- **효과 방향**:
  - 현재 들어오는 Contact·Cognition 계열 공격을 Chest 방향으로 받아 역이용한다.
  - 역상성 카운터 성공 시 상대 공격 무효 또는 대폭 약화 + 확정 주도권 탈취.
  - 큰 성공 시 자세 해제 또는 역상태이상 후보.
- **부분 성공**:
  - 피해·게이지 일부 경감.
  - 주도권 탈취는 역상성 카운터 성공 조건을 충족한 경우에만 적용.
- **실패**:
  - 상대 공격 정상 또는 증폭 적용.
  - Chest 로그·성감·스트레스 추가 상승.
  - 상대 점유나 `initiative_hold`가 강화될 수 있다.
- **주도권**: 카운터 성공 시 확정 탈취.
- **추가 Risk**:
  - 실패 비용이 기본 Tease보다 큼.
  - Chest 봉쇄 시 사용 불가.
- **완화 중**: 감각 차단 중 변종 비활성.
- **Milestone 슬롯**: 대성공 시 역상태이상 또는 유리 자세 강제 중 하나.

설계 의도: 다음 공격을 미리 유도하는 기술이 아니라, 현재 공격을 읽고 받아치는 즉응형 패링으로 고정한다.

---

## 4. 농락형 — 조건부 고위력 역전

### `SBV_Dom_OverturningMount`

- **표시명**: 전복 기승
- **기본 기술**: `SB_Dom_Ride`
- **원천 기벽**: `#Trait_Masochistic_Surrender`
- **요구**: `Subjugation Proficiency`, 반복 부상·굴복 기록
- **전술 역할**: 피주도권 상태의 조건부 고위력 역전·강공
- **발동 시점**: 피주도권 상태 또는 불리 자세에서 사용 가능한 위험 역전 창
- **게이트**:
  - LowerBody 사용 가능.
  - 완전 구속 상태에서는 사용 불가.
  - 일정 피해·굴복도 손실·피학 조건 중 하나를 요구하는 후보.
- **효과 방향**:
  - 성공 시 상대 흥분·탈진을 크게 누적한다.
  - 자세를 Mount로 전환하고 주도권을 탈취한다.
  - 큰 성공 시 `initiative_hold` 1회 후보.
- **부분 성공**:
  - 게이지 압박은 적용하지만 자세 전환 또는 주도권 탈취 중 하나만 적용.
- **실패**:
  - 상대 함락·결정타 기술에 노출되는 취약 상태 후보.
  - 굴복도·성감·Subjugation 로그 추가 상승.
  - 상대가 주도권 유지 효과를 얻을 수 있다.
- **주도권**: 성공 시 탈취, 큰 성공 시 1회 유지 후보.
- **추가 Risk**:
  - 부상·굴복 상태를 전제로 하므로 반복 사용이 위험하다.
  - 실패 비용이 5분류 중 가장 높다.
- **완화 중**: 피학증 Risk가 억제된 동안 변종 비활성.
- **Milestone 슬롯**: 성공 시 콤보 상한 1회 확장 또는 실패 시 함락 노출 완화 중 하나.

설계 의도: Domination의 대표 변종은 상태 제압이 아니라 하이리스크 하이리턴 역전기여야 한다.

### 후순위 변종 보존

`SBV_Dom_CruelCommand`는 삭제하지 않고 Milestone 이후 또는 별도 기벽의 상태 제압 변종 후보로 이동한다.

---

## 5. 흡수형 — Fluid 카운터 증폭

### `SBV_Absorb_DependencyCycle`

- **표시명**: 의존 순환
- **기본 기술**: `SB_Absorb_Drink`
- **원천 기벽**: `#Trait_Semen_Dependency`
- **요구**: `Fluid Proficiency`, `Mouth Lv2`
- **전술 역할**: 평시 저효율 회복·Fluid 공격 카운터 시 증폭
- **발동 시점**: 능동 사용 또는 피주도권 상태에서 Fluid 공격 대응
- **게이트**: Mouth 사용 가능, 체액 흡수 가능한 대상·상태
- **효과 방향**:
  - 일반 사용 시 낮은 회복과 낮은 공격 효율.
  - Fluid 공격 대응 성공 시 상대 효과 일부 무효화 + 회복·굴복도 안정 증폭.
  - 증폭 성공은 Fluid 로그·의존 부채를 더 크게 누적한다.
- **부분 성공**:
  - 공격 경감과 회복 중 하나만 적용.
  - 의존 부채는 정상 발생.
- **실패**:
  - 상대 Fluid 효과 정상 적용.
  - 추가 의존·오염·Mutation 후보.
- **주도권**:
  - 일반 성공만으로 자동 탈취하지 않는다.
  - 역상성 카운터로 판정된 경우 코어 규칙에 따라 주도권 획득.
- **추가 Risk**:
  - Fluid 로그 증가.
  - 전투 종료 후 의존 부채 또는 다음 새벽 컨디션 Risk.
- **완화 중**: 중독 관련 Risk 억제 중 변종 비활성.
- **Milestone 슬롯**: 부채를 침식으로 전환하거나 회복 일부를 대기 생존자에게 전달 중 하나.

설계 의도: Absorption은 언제나 강한 회복기가 아니라, Fluid 상황을 정확히 읽었을 때만 효율이 폭증하는 양날 카운터다.

---

## 6. 저항형 — 기본 방어 위 기벽 추가 효과

### `SBV_Defiance_XenoRestraint`

- **표시명**: 이질 충동 억제
- **기본 기술**: `SB_Defiance_Focus`
- **원천 기벽**: `#Trait_Xenophilic_Obsession`
- **요구**: `Cognition Proficiency`, 괴물 친화 기록
- **전술 역할**: 기본 방어·상태 해제 위에 괴물 성애 전용 자제 보조 추가
- **발동 시점**: Defiance 사용 시 또는 괴물 성애로 인한 자제 판정 직전
- **게이트**: Defiance 기본 우회 규칙을 유지
- **효과 방향**:
  - 기본 `SB_Defiance_Focus`의 상태 해제·굴복도 경감·탈출 기능은 그대로 수행.
  - 추가로 `#Trait_Xenophilic_Obsession`이 원인이 된 도주·기습 자제 실패만 1단계 완화할 수 있다.
  - 일반 최면·공포·혼란 등 범용 판정에는 적용하지 않는다.
- **부분 성공**:
  - 기본 방어 효과만 적용하고 자제 실패 완충은 적용하지 않는다.
- **실패**:
  - 기본 Defiance 실패 결과를 적용.
  - Cognition 로그 또는 스트레스 비용 추가 후보.
- **주도권**:
  - 상태 해제만으로 자동 획득하지 않는다.
  - 동일 상태 내성·다음 경합 보정만 제공한다.
- **추가 Risk**:
  - Cognition 로그 증가.
  - 사용 후 괴물 상호작용 Return 일부 정지 후보.
- **완화 중**: 자제 훈련·인지 고정으로 관련 Risk가 억제된 동안 변종 비활성.
- **Milestone 슬롯**: 관련 자제 비용 감소 또는 거짓 전조 1회 간파 중 하나.

설계 의도: 기벽 변종이 Defiance의 범용 방어 역할을 대체하지 않고, 원천 기벽 때문에 발생한 특정 실패만 관리한다.

---

## 7. 분류별 역할 분산 결과

| 분류 | 대표 변종 역할 | 주도권 관계 | 직접 위력 강화 |
|---|---|---|---|
| Service | 저부담 견제·점유 준비 방해 | 자동 유지 없음 | 낮음 |
| Tease | 즉응 패링·카운터 | 성공 시 확정 탈취 | 조건부 |
| Domination | 고위력 역전·강공 | 성공 시 탈취, 큰 성공 시 유지 후보 | 높음 |
| Absorption | Fluid 카운터·회복 증폭 | 역상성 성공 시만 탈취 | 없음 |
| Defiance | 방어·해제·특정 기벽 실패 완충 | 자동 탈취 없음 | 없음 |

---

## 8. effect 계약 후보

| 변종 | 핵심 effect 후보 |
|---|---|
| `SBV_Service_TactileAnchor` | `occupancy_weaken`, `hold_break` |
| `SBV_Tease_ChestFeint` | `counter_cancel`, `initiative_take`, `reverse_status` |
| `SBV_Dom_OverturningMount` | `posture_force_mount`, `initiative_take`, `initiative_hold` |
| `SBV_Absorb_DependencyCycle` | `fluid_absorb`, `recovery_amplify`, `dependency_debt` |
| `SBV_Defiance_XenoRestraint` | `status_cleanse`, `resistance_gain`, `source_quirk_failure_stepdown` |

실제 `effect_id`와 수치는 후속 데이터 계약에서 확정한다.

---

## 9. 미확정 항목

- 실제 effect_id
- 실제 게이지·로그·침식 수치
- 반복 사용·쿨타임 제한
- Domination 역전 조건의 실제 임계
- Milestone 선택 방식
- UI에서 대응 창·변종 선택·비활성 사유 표시

## 10. 버전 관리

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.0.0 | 2026-07-14 | 5대분류 Proficiency 대표 변종 1종씩과 전술 역할·추가 Risk 정의. |
| v1.1.0 | 2026-07-15 | 굴복 페이즈 코어에 맞춰 Service·Tease·Domination·Absorption·Defiance 역할, 주도권과 실패 계약 재정렬. |
