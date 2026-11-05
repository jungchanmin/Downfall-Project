# R18 Survivor Core Skill Migration Notes

## 적용 범위

Phase 5K-3은 기존 `MECH_R18_Skill_Catalog` 전체를 재작성하지 않고 생존자 대표 기술 5종만 정본 샤드로 분리한다.

대상 Skill ID:

- `SB_Service_Kiss`
- `SB_Tease_Caress`
- `SB_Dom_Ride`
- `SB_Absorb_Drink`
- `SB_Defiance_Focus`

## 우선순위 규칙

런타임 또는 문서 로더가 동일 Skill ID를 발견하면 `MECH_R18_Skill_Catalog_Survivor_Core` 정의를 우선한다.

이 임시 우선순위는 다음 목적을 가진다.

1. 기존 카탈로그의 괴물 기술·상성·자세 게이팅 회귀 방지
2. 새 스키마를 대표 기술에서 먼저 검증
3. 검증 후 기존 SECTION 4를 안전하게 교체

## 병합 종료 조건

- 5개 대표 기술 ID 일치 확인
- 기본 효과와 기존 effect_id 회귀 없음
- 영문 부위·자세 키 로드 성공
- 완화 중 기본 기술 유지 확인
- Proficiency 변종 1개 제한 확인
- 기존 SECTION 4 제거 또는 샤드 참조로 전환

최종 병합 전까지 동일 ID 중복은 알려진 기술 부채로 관리한다.
