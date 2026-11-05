---
id: MECH_R18_Quirk_Skill_Return_Map
title: "핵심 시스템 사양서 — R18 기벽 Return·기술 연결표"
type: mechanic
status: wip
version: 1.0.0
summary: >
  R18 기벽 24종의 Return을 생존자 굴복 기술 5대분류와 대표 기술에 연결하고,
  해금 로그 단계, 적용 범위와 완화 중 정지 규칙을 정의한다.
tags: [mechanic, r18, quirk, skill, return]
depends_on:
  - MECH_Quirk_R18_DB
  - MECH_R18_Memory_Log
  - MECH_R18_Skill_Catalog
  - MECH_R18_Mitigation_System
last_updated: 2026-07-14
---

# R18 기벽 Return·기술 연결표

## 1. 목적

기벽 Return은 단순한 상시 스탯 보너스가 아니라 다음 중 하나로 작동한다.

- 기존 굴복 기술 분류 강화
- 대표 기술 사용 조건 완화
- 특수 선택지 또는 사건 해금
- 특정 Risk를 감수한 상황에서만 발동하는 양날 보상

현재 실제 수치는 확정하지 않는다. 본 문서는 소유권과 연결 방향만 정의한다.

## 2. 공통 원칙

1. 기본 5분류 기술은 모든 생존자가 사용할 수 있다.
2. 기벽은 기술 자체를 독점하기보다 효율·변종·추가 선택지를 해금한다.
3. `Record`는 서사·표시, `Proficiency`는 제한적 강화, `Milestone`은 강한 변종·특수 기술 해금 후보로 사용한다.
4. 완화로 특정 Risk가 억제되면 직접 연결된 기술 Return도 함께 정지한다.
5. 기술 사용으로 로그가 증가할 수 있으므로 Return은 추가 고착 Risk를 가진다.
6. 하나의 기벽이 모든 기술 분류를 강화하지 않는다.

## 3. 연결 데이터 구조

```yaml
quirk_skill_return:
  quirk_id:
  skill_categories: []
  representative_skills: []
  required_axis_stage:
  required_part_level:
  return_mode: potency | cost_reduction | option_unlock | variant_unlock | recovery
  active_conditions: []
  paused_by_mitigation: true
  progress_on_use: []
```

## 4. 기벽별 연결

| 기벽 | 기술 분류·대표 기술 | 최소 로그 방향 | Return 방향 |
|---|---|---|---|
| 살점 융기 | 유혹 `SB_Tease_Caress` | Mutation Proficiency + Chest | 외형 반응 변종·유혹 선택지 |
| 이종 이식 | 봉사·농락 | Mutation Milestone + LowerBody | 신체 개조 전용 변종 해금 |
| 피부 유즙화 | 흡수 `SB_Absorb_Drink` | Fluid Proficiency | 영양·회복 사건 선택지 |
| 음핵 비대증 | 농락 `SB_Dom_Ride` | Mutation/Penetration Milestone | 감도 기반 농락 위력 후보 |
| 유두 민감화 | 유혹 `SB_Tease_Caress` | Contact Proficiency + Chest | 가슴 부위 유혹 변종 |
| 자궁 개발 | 농락·흡수 | Penetration Milestone + LowerBody | 하복부 기술 강화·침식 가속 |
| 후장 개발 | 농락·저항 | Penetration Proficiency + Rear | 후방 자세 변종·저항 비용 완화 후보 |
| 전신 성감대화 | 유혹·농락 | Contact/Mutation Milestone + WholeBody | 전신 감도 스케일링 |
| 피학증 | 저항 `SB_Defiance_Focus`·농락 | Subjugation Milestone | 피해 상황 회복·역전 강화 |
| 노출증 | 유혹·농락 | Contact Proficiency + WholeBody | 노출 상태 보상·변종 |
| 정액 중독 | 흡수 `SB_Absorb_Drink` | Fluid Milestone | 흡수 회복 강화, 추가 의존 Risk |
| 가학증 | 농락 `SB_Dom_Ride` | Subjugation/Cognition Proficiency | 제압·도발 계열 강화 |
| 괴물 성애 | 봉사·유혹 | Cognition Milestone | 괴물 상호작용 선택지·조우 보정 |
| 강박적 자위벽 | 저항·봉사 | Contact Proficiency | 자가 안정 선택지·짧은 회복 |
| 도구 고착증 | 농락·흡수 | Cognition/Penetration Milestone | 도구 기반 기술 변종 |
| 수치성 노예벽 | 봉사 `SB_Service_Kiss` | Subjugation Milestone | 봉사 비용 감소·굴복 기술 강화 |
| 무조건적 성적 개방 | 봉사·유혹 | Cognition Proficiency | 협상·관계 선택지 해금 |
| 가학 복종의 정당성 | 봉사·농락 | Cognition/Subjugation Milestone | 리더 연계 기술 비용 감소 |
| 성적 보상 주의 | 봉사·흡수 | Cognition Proficiency | 보상 교환 사건·회복 선택지 |
| 수치심 상실 | 유혹·농락 | Cognition Milestone | 노출·수치 패널티 일부 무시 |
| 발정 상태 | 농락·흡수 | Contact/Fluid Record | 단기 위력 강화, 사용 시 침식 증가 |
| 접촉 기갈 | 봉사 `SB_Service_Kiss` | Contact Proficiency | 동행·접촉 회복 효과 강화 |
| 음어 증후군 | 유혹·농락 | Cognition Proficiency + Mouth | 도발·음어 변종 해금 |
| 쾌감 수용체 폭주 | 농락 `SB_Dom_Ride`·흡수 | Subjugation/Mutation Milestone | 고위력 스케일링·침식 가속 |

## 5. 대표 기술별 Return 소유

### `SB_Service_Kiss`

- 봉사형 기본기.
- 수치성 노예벽, 접촉 기갈, 가학 복종의 정당성 등이 비용·관계 효과 변종을 제공한다.
- 기본 기술은 기벽 없이도 사용 가능하다.

### `SB_Tease_Caress`

- 유혹형 안전 기술.
- 유두 민감화, 전신 성감대화, 노출증이 부위·상태 기반 변종을 제공한다.
- 기벽 완화 중 관련 감도 Return은 정지한다.

### `SB_Dom_Ride`

- 농락형 고위력 역전기.
- 음핵 비대증, 자궁 개발, 가학증, 쾌감 수용체 폭주와 강하게 연결된다.
- 강한 Return만큼 침식·로그 증가 또는 실패 비용을 함께 가진다.

### `SB_Absorb_Drink`

- 흡수형 회복·변질 가속 기술.
- 피부 유즙화, 정액 중독, 성적 보상 주의와 연결된다.
- 회복 Return과 Fluid 로그 증가가 동시에 발생한다.

### `SB_Defiance_Focus`

- 저항형 안전판.
- 피학증, 후장 개발, 강박적 자위벽의 자제·회복 변종과 연결 가능하다.
- 저항 기술 강화가 기벽 제거를 의미하지 않는다.

## 6. 해금 단계

| 단계 | 허용 Return |
|---|---|
| Record | 전용 설명, 사건 반응, 약한 선택지 |
| Proficiency | 비용 감소, 제한적 보정, 기술 변종 |
| Milestone | 강한 변종, 특수 기술, 규칙 변화 후보 |

기벽 획득만으로 Milestone Return이 자동 활성화되지 않는다. Memory Log가 실제 단계와 부위 레벨을 검사한다.

## 7. 완화 중 정지

```text
Risk 억제
→ 직접 연결 Return 정지
→ 기본 기술은 유지
→ 기벽 전용 변종·보정만 비활성
```

예:

- 정액 중독의 컨디션 Risk를 억제하면 `SB_Absorb_Drink`의 중독 전용 강화도 정지한다.
- 괴물 성애 자제 훈련은 도주 판정 보조를 제공하지만 괴물 상호작용 기벽 자체를 삭제하지 않는다.
- 감도 기벽의 감각 차단 중에는 해당 부위 기술 변종이 정지한다.

## 8. 신규 기술 추가 원칙

신규 기술은 다음 경우에만 추가한다.

- 기존 5분류 대표 기술로 표현할 수 없는 전략적 역할
- 자세·부위·축이 실제로 다른 판정 구조를 요구
- 단순 수치 차이가 아니라 새로운 의사결정을 제공

단순 위력 상위호환은 신규 기술이 아니라 기존 기술 변종으로 처리한다.

## 9. 미확정 항목

- 기벽별 실제 수치 보정
- 변종 기술 ID와 명칭
- 사용 시 로그 증가량
- 침식·욕구불만 추가 비용
- 완화 중 정지되는 세부 effect_id
- 자세·부위별 추가 기술 목록

## 10. 버전 관리

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.0.0 | 2026-07-14 | R18 기벽 24종 Return을 5대 기술 분류와 대표 기술에 연결. |
