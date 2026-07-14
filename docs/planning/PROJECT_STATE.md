# Downfall Project State

## Current Phase

**Phase 5I-4: R18 메모리 로그·기벽 고착 연결 정본화**

Phase 5I-3에서 R18 기벽 24종의 Risk & Return, 처리 모델, 고착 상태와 완화 방식을 정리했다. 현재는 메모리 로그에 기벽 획득·재획득·완화 후 기록 보존·고착 단계·Return 및 굴복 기술 해금을 연결하는 단계다.

## Completed

- 프로젝트 핵심 정의 및 디자인 필러 3+1 확정
- 25일 의식과 오벵마을 고정 지리 정본화
- 외출 8단계 플레이 흐름과 지속 괴물 조우
- Loot Distribution Draft
- 아지트 영구 주 개조·자율행동·명령 저항·설비 후보 Draft
- 일반 기벽 제거와 R18 Risk & Return·완화·고착 상위 규격
- 일반 육체·정신 기벽 치료 메타데이터 Draft
- R18 기벽 24종 Risk & Return·완화·고착 데이터 Draft
- 평화주의자·색광증·만성 피로 방향 확정
- 괴물 성애 완전 하드락 제거 및 자제 판정 방향 확정

## In Progress

- R18 변질 6축과 부위·행위 로그 유지
- 기벽 획득 기록과 현재 활성 기벽 분리
- 동일 기벽 재획득 처리
- `temporary / persistent / permanent` 고착 전이 구조
- 완화·지속 종료 후 기록·해금 보존
- Risk 억제 시 직접 연결 Return 동시 억제
- 메모리 로그 기반 Return·굴복 기술 해금
- 괴물 성애의 정신력·자제 판정 연결

## Blockers

- 축별 기록·숙련·업적 실제 임계값 미확정
- 부위 경험치와 민감도 레벨 공식 미확정
- 기벽별 실제 `memory_log_links` 미지정
- 재획득·고착 실제 임계값 미확정
- Return과 굴복 기술의 수치 보정 미확정
- R18 전용 완화 행동·설비·이벤트 목록 미작성
- 일반 Physical/Mental DB의 승인 결정에 따른 최종 항목 이동·번호 재정렬 필요
- `MECH_Quirk_R18.md`의 괴물 성애 하드락 문구를 승인 결정으로 직접 교체하는 정합성 패스 필요
- 선행 PR #15~#23이 Draft 상태라 Phase 5I-4도 stacked 상태로 관리 중

## Next Priorities

1. `MECH_R18_Memory_Log` 검토
2. 일반 Physical/Mental DB의 평화주의자·만성 피로 최종 이동 반영
3. `MECH_Quirk_R18.md` 괴물 성애 하드락 표현 교체
4. 기벽별 실제 로그 키 매핑표 작성
5. R18 완화 행동·설비 후보 작성
6. R18 Skill Catalog와 Return 해금 연결
7. 치료·완화·고착 수치 테스트 계획 수립
8. Item 후보를 탐험·Loot·Hideout 태그와 재대조

## Known Technical Debt

- 레거시 문서의 과거 29일·30일 설정
- 구형 파일명과 문서 경로 참조
- 미해결 `depends_on`
- Event ID 및 파일명 불일치
- 일부 문서의 frontmatter 부재
- 일부 일반 기벽 명칭과 실제 의학적 상태의 심각도 불일치
- R18 기벽의 개별 로그 키·기술 연결 미확정
- 일부 R18 Return이 선택지 해금 수준에 머물러 있음
- 설비 후보의 플레이어 표시명은 최종 빌드 단계에서 Downfall 톤으로 재명명 필요

## Update Rule

이 문서는 프로젝트 진행 상태만 기록한다. 세계관, 시스템 규칙과 밸런스 정의는 각 Wiki 정본 문서가 소유한다.
