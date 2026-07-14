# R18 Survivor Core Skill Changelog

## 수정 이유

기존 R18 Skill Catalog의 생존자 대표 기술 5종은 한글 부위 키와 구형 스키마를 사용하고 있어 Memory Log·Quirk Return·완화 시스템과 직접 연결하기 어려웠다. 전체 카탈로그 재작성은 괴물 기술·상성·자세 게이팅의 회귀 위험이 커 대표 기술만 안전하게 분리했다.

## 변경 내용

- 생존자 대표 기술 5종 정본 샤드 작성
- 영문 부위·자세 키 적용
- 대상 부위와 시전자 행위 부위 분리
- Return·변종·완화 정책 슬롯 적용
- Proficiency 변종 1개 제한과 Milestone 추가 해금 원칙 적용
- 동일 ID 임시 우선순위와 검증 체크리스트 작성

## 영향받는 문서

- `MECH_R18_Skill_Catalog_Survivor_Core`
- `MECH_R18_Skill_Catalog`
- `MECH_R18_Skill_Data_Contract`
- `MECH_R18_Quirk_Skill_Return_Map`
- `PROJECT_STATE`

## 추가 검토가 필요한 항목

- 대표 변종 ID·표시명·effect
- 기술별 로그 증가량과 비용
- 기존 Skill Catalog SECTION 4 교체
- 괴물 기술의 영문 키 마이그레이션
