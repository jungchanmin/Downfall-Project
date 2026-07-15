# Downfall Project State

## Current Phase

**Phase 5L-2: R18 Proficiency 대표 변종 역할·주도권 계약 재정렬**

Phase 5L-1에서 굴복 페이즈의 주도권·전조·게이팅·카운터 코어를 정본화했다. 현재는 기존 Proficiency 대표 변종 5종을 Service·Tease·Domination·Absorption·Defiance의 정확한 전술 역할에 맞춰 재배치하고, 성공·부분 성공·실패·주도권·완화 중 비활성 계약을 정리하는 단계다.

## Completed

- 프로젝트 핵심 정의 및 디자인 필러 3+1 확정
- 25일 의식과 오벵마을 고정 지리 정본화
- 외출 8단계 플레이 흐름과 지속 괴물 조우
- Loot Distribution Draft
- 아지트 영구 주 개조·자율행동·명령 저항·설비 후보 Draft
- 일반 기벽 치료와 R18 Risk & Return·완화·고착 상위 규격
- 일반 육체 16종·정신 24종 분류 정합성
- R18 메모리 로그의 획득·재획득·고착·기록 보존 구조
- 공통 축 단계 + 기벽별 개별 조건의 혼합형 임계값 구조
- R18 기벽 24종 로그·획득·고착 조건 정합성
- R18 완화 행동·설비·일일 이용 제한
- R18 기벽 Return과 굴복 기술 5대분류 연결
- R18 기술 정본 데이터 계약과 생존자 대표 기술 5종 샤드
- 신규 기벽 개발 우선순위
- 굴복 페이즈 주도권·전조·게이팅 코어 규칙

## In Progress

- Service 대표 변종을 저부담 능동 견제·점유 준비 방해로 재정렬
- Tease 대표 변종을 현재 공격 즉응 패링·카운터로 재정렬
- Domination 대표 변종을 상태 제압에서 조건부 고위력 역전기로 교체
- Absorption 대표 변종을 Fluid 카운터 증폭형으로 정리
- Defiance 대표 변종을 기본 방어 위 원천 기벽 전용 추가 효과로 축소
- 변종별 발동 시점·게이트·성공·부분 성공·실패 계약
- 주도권 탈취·유지·비탈취 조건 명시
- effect 태그 후보 작성

## Blockers

- 대표 변종 실제 `effect_id` 미확정
- 실제 게이지·로그·침식 수치 미확정
- 반복 사용·쿨타임 제한 미확정
- Domination 역전 조건의 실제 임계 미확정
- 기본 `combo_chain_limit` 실제 수치 미확정
- 중립 상성 결과 차이 임계 미확정
- 전조 판정식과 경험·기록 보정값 미확정
- 상태이상별 내성 증가·감쇠량 미확정
- 교대 가능 시점과 구속 중 구조 규칙 미확정
- 기존 Skill Catalog SECTION 4와 정본 샤드 최종 병합 필요
- 괴물 공유 기술과 굴복 커맨드 영문 키 치환 미완료
- 선행 PR #15~#32가 Draft 상태라 Phase 5L-2도 stacked 상태로 관리 중

## Next Priorities

1. `MECH_R18_Proficiency_Variant_Catalog` v1.1 검토
2. Phase 5L-3 상태이상·내성 데이터 계약
3. 전조 판정·정보 신뢰도 UI 계약
4. 태그 교대·지원 행동 초안
5. 기존 Skill Catalog SECTION 11·SECTION 4 정합성 패스
6. 중립 상성·콤보 상한 밸런스 테스트 계획
7. 실제 effect_id 발급과 기술 데이터 연결

## Known Technical Debt

- 기존 `MECH_Combat_System` SECTION 11은 완전 정보 공개와 구형 커맨드 역할을 포함함
- `SBV_Dom_CruelCommand`는 대표 변종이 아닌 후순위 상태 제압 변종으로 이동 필요
- `MECH_R18_Mitigation_System` v1.0 반복 완화 내성 후보 문구 직접 교체 필요
- `MECH_R18_Skill_Catalog` 제목 `v1.0`과 frontmatter `v1.4.0` 불일치
- 기존 Skill Catalog SECTION 4와 생존자 코어 기술 샤드가 동일 ID를 임시 중복 소유
- Skill Catalog의 한글 부위·자세 키가 Memory Log 영문 키와 불일치
- 레거시 문서의 과거 29일·30일 설정
- 구형 파일명과 문서 경로 참조
- 미해결 `depends_on`
- Event ID 및 파일명 불일치
- 일부 문서의 frontmatter 부재

## Update Rule

이 문서는 프로젝트 진행 상태만 기록한다. 세계관, 시스템 규칙과 밸런스 정의는 각 Wiki 정본 문서가 소유한다.
