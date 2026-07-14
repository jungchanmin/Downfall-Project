# Downfall Project State

## Current Phase

**Phase 5J-1: 일반 기벽 DB 분류·종수·승인 결정 정합성 마감**

Phase 5I에서 일반 기벽 치료 구조와 R18 Risk & Return·메모리 로그 구조를 정리했다. 현재는 승인된 평화주의자·색광증·만성 피로 결정을 Physical/Mental DB 본문에 직접 반영하고, 혼합형 R18 임계값 구조를 정식 결정으로 기록하는 단계다.

## Completed

- 프로젝트 핵심 정의 및 디자인 필러 3+1 확정
- 25일 의식과 오벵마을 고정 지리 정본화
- 외출 8단계 플레이 흐름과 지속 괴물 조우
- Loot Distribution Draft
- 아지트 영구 주 개조·자율행동·명령 저항·설비 후보 Draft
- 일반 기벽 제거와 R18 Risk & Return·완화·고착 상위 규격
- R18 메모리 로그의 획득·재획득·고착·기록 보존 구조
- 괴물 성애 완전 하드락 제거 및 자제 판정 확정
- 공통 축 단계 + 기벽별 개별 조건의 혼합형 임계값 구조 확정

## In Progress

- 만성 피로를 정신 DB에서 제거하고 육체 DB로 이동
- 육체 기벽 16종·정신 기벽 24종 종수 정리
- 평화주의자를 살상 경험 기반 제거 가능한 트라우마로 확정
- 색광증의 공통 충동 기벽 + R18 장기 변화 중첩 규칙 확정
- Physical/Mental DB 검토 섹션을 승인 결정 섹션으로 교체
- R18 임계값 혼합형 결정 기록

## Blockers

- 축별 Record / Proficiency / Milestone 실제 수치 미확정
- 부위 경험치와 민감도 레벨 공식 미확정
- 기벽별 실제 `memory_log_links` 미지정
- 재획득·고착 실제 임계값 미확정
- Return과 굴복 기술의 수치 보정 미확정
- R18 전용 완화 행동·설비·이벤트 목록 미작성
- `MECH_Quirk_R18.md` 괴물 성애 자제 판정 본문 정합성 최종 확인 필요
- 선행 PR #15~#24가 Draft 상태라 Phase 5J-1도 stacked 상태로 관리 중

## Next Priorities

1. 일반 Physical/Mental DB 변경 검토
2. Phase 5J-2 R18 Quirk DB 정합성 패스
3. 기벽별 실제 로그 키 매핑표 작성
4. R18 완화 행동·설비 후보 작성
5. R18 Skill Catalog와 Return 해금 연결
6. 치료·완화·고착 수치 테스트 계획 수립
7. Item 후보를 탐험·Loot·Hideout 태그와 재대조

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
