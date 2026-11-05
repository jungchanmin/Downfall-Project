---
id: MECH_R18_Skill_Data_Contract
title: "핵심 시스템 사양서 — R18 기술 데이터 계약"
type: mechanic
status: wip
version: 1.0.0
summary: >
  R18 Skill Catalog의 영문 정본 키, UI 표시명, 기벽 Return·변종·완화 중 비활성 규칙과
  레거시 항목 마이그레이션 기준을 정의한다.
tags: [mechanic, r18, skill, schema, migration]
depends_on:
  - MECH_R18_Skill_Catalog
  - MECH_R18_Quirk_Skill_Return_Map
  - MECH_R18_Memory_Log
  - MECH_R18_Mitigation_System
last_updated: 2026-07-14
---

# R18 기술 데이터 계약 v1.0

## 1. 목적

기존 Skill Catalog의 전투 커맨드·상성·자세 게이팅 콘텐츠는 보존한다. 본 문서는 구현 데이터의 문자열 불일치와 기벽 Return 소유권 충돌을 막는 정본 계약이다.

## 2. 정본 키와 표시명

구현·저장·판정에는 영문 enum 키를 사용하고, 한글은 UI 표시명으로만 사용한다.

```yaml
R18PartKey:
  Mouth: 입
  Chest: 가슴
  LowerBody: 하복부
  Rear: 후부
  WholeBody: 전신

ActionPartKey:
  Mouth: 입
  Hand: 손
  LowerBody: 하반신

PostureKey:
  Confrontation: 대치
  Front: 정면
  RearEntry: 후배위
  Mount: 기승
  Bound: 구속
```

레거시 `progress_part: 가슴`은 `progress_part: Chest`로 마이그레이션한다. UI에서는 `display_part: 가슴`을 표시한다.

## 3. R18SkillDef 확장 계약

```yaml
R18SkillDef:
  id: str
  name: str
  side: monster | survivor
  phase: normal_r18 | submission
  sub_category: null | service | tease | domination | absorption | defiance

  progress_axis: null | Contact | Penetration | Fluid | Mutation | Cognition | Subjugation
  progress_part: null | Mouth | Chest | LowerBody | Rear | WholeBody
  display_part: null | str

  required_action_parts: []
  valid_postures: []
  posture_force: null
  bypass_gating: false

  base_skill_id: null | str
  variant_id: null | str
  variant_source_quirks: []
  return_unlock_id: null | str
  required_memory_stage: null | record | proficiency | milestone
  required_part_level: 0
  required_flags: []

  mitigation_policy:
    base_skill_available: true
    disable_variant_when_suppressed: true
    disabled_effect_ids: []

  gauge_delta: {}
  status_inflict: []
  scaling: null | erosion | quirk | sens_level
  effect_id: null | str
  log: {}
```

## 4. 기본 기술과 기벽 변종

- 기본 기술 5종은 모든 성인 생존자가 굴복 페이즈에서 사용할 수 있다.
- 기벽은 기본 기술을 대체하지 않고 변종·추가 효과·선택지를 해금한다.
- 단순 수치 상위호환은 변종으로 만들지 않는다.
- 변종은 자세, 부위, 비용, 위험 또는 전술 역할 중 하나 이상이 달라야 한다.

```yaml
base_skill_id: SB_Tease_Caress
variant_id: SBV_Tease_ChestSensitivity
variant_source_quirks: ["#Trait_Hypersensitive_Nipples"]
required_memory_stage: proficiency
required_part_level: 1
```

## 5. Return 해금 책임

- Quirk DB: Return의 방향과 원천 기벽
- Memory Log: 축 단계·부위 레벨·플래그 판정
- Return Map: 기벽과 기술 분류·대표 기술 연결
- Skill Catalog: 실제 기술·변종·effect_id
- Combat System: 적용 수치와 전투 처리

기술 데이터는 기벽 보유만 확인하지 않고 Memory Log의 해금 결과를 참조한다.

## 6. 완화 중 비활성

완화 중에도 기본 기술은 유지한다.

```text
기벽 Risk 억제
→ 직접 연결 Return 정지
→ 기벽 전용 기술 변종 정지
→ 기본 기술 사용 가능
```

`mitigation_policy.disable_variant_when_suppressed`가 `true`이면 해당 변종을 선택 목록에서 비활성화한다. 기본 기술의 `effect_id`는 제거하지 않는다.

## 7. 레거시 마이그레이션

### 우선 치환

- 본문 제목 `v1.0` → frontmatter와 동일한 `v1.4`
- `progress_part` 한글 값 → 영문 정본 키
- `required_parts`는 `required_action_parts`와 대상 부위 게이팅을 분리
- 한글 자세 값 → `PostureKey`

### 호환 로더

마이그레이션 기간에는 다음 별칭을 허용한다.

```yaml
legacy_part_alias:
  입: Mouth
  가슴: Chest
  하복부: LowerBody
  후부: Rear
  전신: WholeBody
```

저장 시에는 반드시 영문 키로 직렬화한다. 별칭 지원은 데이터 이전 완료 후 제거한다.

## 8. 검증 규칙

- `progress_part`가 enum 외 문자열이면 오류
- `variant_id`가 있으면 `base_skill_id` 필수
- `variant_source_quirks`가 있으면 `return_unlock_id` 또는 해금 조건 필수
- 완화로 정지되는 effect는 `disabled_effect_ids`에 명시
- SFW 빌드에서는 본 계약과 R18 Skill Catalog 전체를 로드하지 않음

## 9. 순차 적용 순서

1. 문서 제목 버전 정합
2. 생존자 대표 기술 5종 필드 적용
3. 괴물 공유 기술의 부위 키 치환
4. 굴복 커맨드 풀 부위·자세 키 치환
5. 기벽 전용 변종 ID 추가
6. 레거시 별칭 제거

## 10. 버전 관리

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.0.0 | 2026-07-14 | 영문 정본 키, UI 표시명, Return·변종·완화 정책과 레거시 마이그레이션 계약 정의. |
