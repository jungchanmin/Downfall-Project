# Downfall Project State

## Current Phase

**Phase 5L-1: R18 굴복 페이즈 주도권·전조·게이팅 코어 규칙 정본화**

Phase 5K에서 기벽 Return과 생존자 기술 변종 구조를 정리했다. 현재는 괴물 6축과 생존자 5분류가 주도권·불완전 전조·자세·부위·행동 점유·상성·상태이상 콤보로 충돌하는 합 단위 코어 규칙을 정본화하는 단계다.

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
- 신규 기벽 개발 우선순위와 Proficiency 대표 변종 초안

## In Progress

- 괴물 6축·생존자 5분류 코어 역할 정본화
- 경험·지식·기록 기반 공격 전조 단계와 신뢰도
- 인지 교란에 의한 확정형 거짓 전조
- 자세·부위·행동 게이트 우선 검사
- 행동 취소 후 기본 주도권 이전
- `initiative_hold` 예외와 연속 주도권 유지 상한
- 역상성 카운터 성공 시 확정 주도권 탈취
- 중립 상성 결과 단계
- 상태이상 해제·내성과 주도권 분리
- 1대1 활성 전투 + 대기 생존자 지원·교대 초안

## Blockers

- 기본 `combo_chain_limit` 실제 수치 미확정
- 중립 상성 결과 차이 임계 미확정
- 전조 판정식과 경험·기록 보정값 미확정
- 상태이상별 내성 증가·감쇠량 미확정
- 교대 가능 시점과 구속 중 구조 규칙 미확정
- 지원 행동 횟수·비용 미확정
- 대표 변종이 기존 오해석을 반영한 부분 재정렬 필요
- 대표 변종 실제 effect_id 미작성
- 기벽별 실제 수치 보정 미확정
- 기존 Skill Catalog SECTION 4와 정본 샤드 최종 병합 필요
- 괴물 공유 기술과 굴복 커맨드 영문 키 치환 미완료
- 선행 PR #15~#31이 Draft 상태라 Phase 5L-1도 stacked 상태로 관리 중

## Next Priorities

1. `MECH_R18_Submission_Core_System` 검토
2. Phase 5L-2 기존 Proficiency 변종 5종 역할 재정렬
3. 상태이상·내성 데이터 계약
4. 전조 판정·정보 신뢰도 UI 계약
5. 태그 교대·지원 행동 초안
6. 기존 Skill Catalog SECTION 11·SECTION 4 정합성 패스
7. 중립 상성·콤보 상한 밸런스 테스트 계획

## Known Technical Debt

- 기존 `MECH_Combat_System`의 굴복 페이즈는 완전 정보 공개와 기존 커맨드 역할 해석을 포함함
- Phase 5K-4 대표 변종 중 Service·Domination·Defiance 역할 재조정 필요
- `MECH_R18_Mitigation_System` v1.0 반복 완화 내성 후보 문구 직접 교체 필요
- `MECH_R18_Skill_Catalog` 제목 `v1.0`과 frontmatter `v1.4.0` 불일치
- 기존 Skill Catalog SECTION 4와 생존자 코어 기술 샤드가 동일 ID를 임시 중복 소유
- Skill Catalog의 한글 부위·자세 키가 Memory Log 영문 키와 불일치
- 레거시 문서의 과거 29일·30일 설정
- 구형 파일명과 문서 경로 참조
- 미해결 `depends_on`
- Event ID 및 파일명 불일치
- 일부 문서의 frontmatter 부재
- 일부 R18 로그 연결은 사건 콘텐츠 확정 전 임시 명칭 사용

## Update Rule

이 문서는 프로젝트 진행 상태만 기록한다. 세계관, 시스템 규칙과 밸런스 정의는 각 Wiki 정본 문서가 소유한다.
