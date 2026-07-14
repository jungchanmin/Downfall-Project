---
id: MECH_R18_Proficiency_Variant_Catalog
title: "핵심 시스템 사양서 — R18 Proficiency 대표 변종 카탈로그"
type: mechanic
status: wip
version: 1.0.0
summary: >
  생존자 굴복 기술 5대분류에 각 1종의 Proficiency 대표 변종을 부여하고,
  단순 위력 증가가 아닌 전술적 역할·추가 Risk·완화 중 정지 규칙을 정의한다.
tags: [mechanic, r18, skill, variant, proficiency]
depends_on:
  - MECH_R18_Skill_Catalog_Survivor_Core
  - MECH_R18_Quirk_Skill_Return_Map
  - MECH_R18_Quirk_Development_Priority
last_updated: 2026-07-14
---

# R18 Proficiency 대표 변종 카탈로그 v1.0

## 1. 공통 원칙

- 각 기술 분류당 대표 변종 1종만 먼저 구현한다.
- 각 변종은 하나의 원천 기벽을 가진다.
- 단순 피해·게이지 수치 상향이 아니라 새로운 선택과 대가를 제공한다.
- 원천 기벽의 관련 Risk가 완화 중이면 변종과 전용 effect를 비활성화한다.
- 기본 기술은 계속 사용할 수 있다.

```yaml
R18SkillVariant:
  variant_id:
  base_skill_id:
  source_quirk:
  required_memory_stage: proficiency
  required_part_level:
  tactical_role:
  added_risk:
  mitigation_policy:
  milestone_extension_slot:
```

---

## 2. 봉사형 — 접촉 안정

### `SBV_Service_TactileAnchor`

- **표시명**: 접촉의 닻
- **기본 기술**: `SB_Service_Kiss`
- **원천 기벽**: `#Trait_Tactile_Deprivation`
- **요구**: `Contact Proficiency`, `Mouth Lv1`
- **전술 역할**: 관계·안정 지원
- **효과 방향**:
  - 사용 후 자신 또는 동료 한 명의 다음 스트레스·굴복도 손실 완화 후보
  - 단독 배치·접촉 단절 상태에서 발생한 불이익을 전투 중 한시적으로 보완
  - 직접 공격력은 증가하지 않음
- **추가 Risk**:
  - 사용 후 Contact 로그 증가
  - 같은 전투에서 반복 사용하면 자기 욕구불만 상승 후보
- **완화 중**: 접촉 기갈 Risk가 안정화된 동안 변종 비활성
- **Milestone 슬롯**: 대상 2인 지원 또는 관계 비용 교환 중 하나

설계 의도: 봉사형을 단순 비용 감소가 아니라 파티 안정 지원 분류로 확장한다.

---

## 3. 유혹형 — 감각 패링

### `SBV_Tease_ChestFeint`

- **표시명**: 감각 유인
- **기본 기술**: `SB_Tease_Caress`
- **원천 기벽**: `#Trait_Hypersensitive_Nipples`
- **요구**: `Contact Proficiency`, `Chest Lv1`
- **전술 역할**: 패링·행동 지연
- **효과 방향**:
  - 적의 다음 접촉·인지 계열 행동을 Chest 방향으로 유도하는 패링 후보
  - 성공 시 적 행동 지연 또는 자세 전환 기회
  - 실패 시 Chest 로그와 자기 성감·스트레스 추가 상승
- **추가 Risk**:
  - 실패 비용이 기본 유혹보다 큼
  - 관련 부위가 봉쇄되면 사용 불가
- **완화 중**: 감각 차단 중 변종 비활성
- **Milestone 슬롯**: 대성공 시 주도권 탈취 또는 자세 해제 중 하나

설계 의도: 유혹형의 정체성을 ‘느린 위력 증가’가 아니라 고위험 능동 패링으로 강화한다.

---

## 4. 농락형 — 상태 제압

### `SBV_Dom_CruelCommand`

- **표시명**: 잔혹한 명령
- **기본 기술**: `SB_Dom_Ride`
- **원천 기벽**: `#Trait_Sadistic_Cruelty`
- **요구**: `Subjugation Proficiency`, 가학 행동 기록
- **전술 역할**: 상태 제압·행동 선택 제한
- **효과 방향**:
  - 순수 게이지 폭증 대신 적의 다음 행동 후보를 제한하거나 특정 행동을 강요하는 효과 후보
  - 이미 약화·구속된 대상에게 강하지만 일반 대상에게는 효율 낮음
- **추가 Risk**:
  - 사용 시 대상 및 목격자의 관계 비용 후보
  - 실패하면 적의 반격 우선권 또는 사용자 스트레스 증가
- **완화 중**: 가학증 Risk가 억제된 동안 변종 비활성
- **Milestone 슬롯**: 행동 강제 강화 또는 관계 비용 일부 전환 중 하나

설계 의도: 농락형의 과밀을 인정하되 단순 최고 위력기가 아닌 제압형으로 역할을 제한한다.

---

## 5. 흡수형 — 위험 자원 전환

### `SBV_Absorb_DependencyCycle`

- **표시명**: 의존 순환
- **기본 기술**: `SB_Absorb_Drink`
- **원천 기벽**: `#Trait_Semen_Dependency`
- **요구**: `Fluid Proficiency`, `Mouth Lv2`
- **전술 역할**: 긴급 회복·후속 의존
- **효과 방향**:
  - 즉시 회복 또는 굴복도 안정 효과 후보
  - 전투 종료 후 미충족 상태가 더 강해지는 부채를 생성
  - 회복량 자체보다 ‘지금 회복하고 나중에 대가를 치르는’ 선택을 제공
- **추가 Risk**:
  - Fluid 로그 증가
  - 의존 카운터 또는 다음 새벽 컨디션 Risk 증가 후보
- **완화 중**: 중독 관련 Risk 억제 중 변종 비활성
- **Milestone 슬롯**: 부채를 침식으로 전환하거나 회복을 동료에게 분배 중 하나

설계 의도: 흡수형을 무료 회복이 아니라 미래 비용을 당겨 쓰는 자원 전환형으로 만든다.

---

## 6. 저항형 — 자제 실패 완충

### `SBV_Defiance_XenoRestraint`

- **표시명**: 이질 충동 억제
- **기본 기술**: `SB_Defiance_Focus`
- **원천 기벽**: `#Trait_Xenophilic_Obsession`
- **요구**: `Cognition Proficiency`, 괴물 친화 기록
- **전술 역할**: 자제·도주·부분 성공 비용 완화
- **효과 방향**:
  - 괴물 성애로 인한 도주·기습 자제 판정에 보정 후보
  - 실패를 부분 성공으로 한 단계 완화할 수 있으나 추가 스트레스·침식 비용 발생
  - 공격 위력 증가는 없음
- **추가 Risk**:
  - Cognition 로그 증가
  - 사용 후 해당 전투에서 괴물 상호작용 Return 일부 정지 후보
- **완화 중**: 자제 훈련·인지 고정으로 Risk가 억제된 동안 변종 비활성
- **Milestone 슬롯**: 파티원 1명의 실패 완충 또는 자신의 비용 감소 중 하나

설계 의도: 저항형을 단순 상태 해제에서 ‘통제 불가능한 기벽의 실패를 관리하는 안전판’으로 확장한다.

---

## 7. 분류별 역할 분산 결과

| 분류 | 대표 변종 역할 | 직접 위력 강화 |
|---|---|---|
| 봉사 | 관계·안정 지원 | 없음 |
| 유혹 | 고위험 패링·지연 | 제한적 |
| 농락 | 상태 제압·행동 제한 | 조건부 |
| 흡수 | 현재 회복 ↔ 미래 부채 | 없음 |
| 저항 | 실패 완충·자제 | 없음 |

농락형만 전투 제압 역할을 유지하며, 다른 네 분류는 지원·패링·자원 교환·안전판으로 분리한다.

## 8. 미확정 항목

- 실제 effect_id
- 실제 게이지·로그·침식 수치
- 반복 사용 제한
- Milestone 선택 방식
- UI에서 변종 선택·비활성 사유 표시

## 9. 버전 관리

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.0.0 | 2026-07-14 | 5대분류 Proficiency 대표 변종 1종씩과 전술 역할·추가 Risk 정의. |
