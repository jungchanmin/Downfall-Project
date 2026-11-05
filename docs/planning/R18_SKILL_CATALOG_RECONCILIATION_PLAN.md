# R18 Skill Catalog Reconciliation Plan

## 목적

기존 `MECH_R18_Skill_Catalog.md`의 기술 ID·괴물 기술 예시·생존자 대표 기술·연출 텍스트를 보존하면서, 구형 소유권·축 상성·한글 키·랜덤 기술 풀 규칙을 최신 정본에 맞춰 순차 교체한다.

## 최신 적용 상태

Phase 5M-4에서 다음 규칙 골격을 별도 정본 오버라이드로 적용했다.

```text
Wiki/01_Mechanics/MECH_R18_Skill_Catalog_Core_Rules_Override.md
```

이 문서는 기존 카탈로그의 SECTION 0·1·5·7·8 해석을 즉시 대체한다. 원문은 기술 예시 보존을 위해 아직 직접 전면 교체하지 않는다.

## 적용 우선순위

1. `MECH_R18_Submission_Core_System`
2. `MECH_R18_Skill_Ownership_Unlock_Contract`
3. `MECH_R18_Gate_Tag_Standard`
4. `MECH_R18_Skill_Catalog_Core_Rules_Override`
5. `MECH_R18_Skill_Catalog`

## SECTION별 교체 계획

| SECTION | 구형 문제 | 최신화 방향 | 상태 |
|---|---|---|---|
| 0 | 생존자 기술 전원 공용 | 생존자별 `known_skills` | 오버라이드 적용 |
| 1 | 한글 키·혼합된 부위 필드 | 영문 키·대상/행동 부위 분리 | 오버라이드 적용 |
| 3 | 랜덤 축 풀 비중 과다 | 고정 시그니처·코어 키트 중심 | 상위 계약 완료, 원문 미병합 |
| 4 | 대표 5종 전원 사용 | 분류 기준 템플릿으로 변경 | 오버라이드 적용 |
| 5 | 축 상성이 카운터 직접 결정 | Gate Tag 카운터 우선 | 오버라이드 적용 |
| 7 | 생존자 기술 참조 불필요 | 생존자·괴물별 기술 목록 | 오버라이드 적용 |
| 8 | 한글 자세·부위 저장 | 영문 정본 키·Gate Tag | 오버라이드 적용 |

## 순차 병합 순서

### Pass A — 규칙 골격

- SECTION 0 직접 교체
- SECTION 1 직접 교체
- SECTION 5 직접 교체
- SECTION 7 직접 교체
- SECTION 8 직접 교체

### Pass B — 기존 기술 예시 마이그레이션

- `progress_part` 영문 키 치환
- `required_parts`를 `required_target_parts`와 `action_parts`로 분리
- `valid_postures`와 `posture_force` 영문 키 치환
- `base_power`·`stability`·`self_cost` 슬롯 추가
- 게이팅 기술에 `gate_attack` 추가
- Tease 기술에 `counter_profile` 추가

### Pass C — 괴물 키트

- `r18_submission_draw` 제거 또는 레거시 읽기 전용화
- `signature_skills / core_skills / conditional_skills / variant_pools` 적용
- 조건부 피니셔 복수 조건 검증
- 기술 쿨타임과 시그니처 콤보 연결

## 대표 기술 5종 처리

다음 ID는 삭제하지 않는다.

```text
SB_Service_Kiss
SB_Tease_Caress
SB_Dom_Ride
SB_Absorb_Drink
SB_Defiance_Focus
```

이들은 전원 공용 기술이 아니라 5대 커맨드 분류의 기준 기술·설계 템플릿으로 유지한다. 실제 보유 여부는 생존자 데이터가 결정한다.

## 레거시 읽기 정책

- 한글 부위·자세 키는 읽을 수 있다.
- 저장 시 영문 정본 키로 변환한다.
- `required_parts`는 자동 추정 저장하지 않는다. 문맥 검수 후 대상 부위와 행동 부위로 분리한다.
- 기존 축 상성 주석은 친화도 설명으로만 해석한다.
- 공용 기술 주석은 분류 템플릿 설명으로 해석한다.

## 회귀 방지

- 기존 기술 ID 삭제 금지
- 기존 effect ID 무단 변경 금지
- 괴물·광신도·자경단 기술 예시 보존
- 기술별 `required_parts` 자동 일괄 변환 금지
- 원문 직접 교체 전 오버라이드 기준 검증
- 각 SECTION 교체 후 별도 diff 검수

## 다음 작업

1. 원문 SECTION 0·1 직접 병합
2. SECTION 5·7·8 직접 병합
3. 기존 기술 예시의 부위 필드 분리
4. 괴물 기술 1종에 Gate Tag·전조 프로필 샘플 적용
5. 생존자 Tease 기술 1종에 Counter Profile 샘플 적용
