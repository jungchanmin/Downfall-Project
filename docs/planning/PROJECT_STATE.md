# Downfall Project State

## Current Phase

**Phase 5J-2: R18 기벽 DB 로그 연결·획득·고착 정합성 마감**

Phase 5J-1에서 일반 Physical/Mental DB의 승인 결정을 본문에 반영했다. 현재는 R18 기벽 24종에 축·부위·행위 로그, 획득 조건, 고착 조건과 문서 책임을 직접 연결하고 괴물 성애 하드락을 최신 자제 판정 기준으로 교체하는 단계다.

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
- 괴물 성애 완전 하드락 제거 및 자제 판정 본문 반영

## In Progress

- R18 기벽 24종 `memory_log_links` 초안 적용
- 축·부위·행위 로그 연결
- 획득 조건과 고착 조건 분리
- 영구 기벽·지속 기벽·일시 기벽의 데이터 표현 통일
- Quirk DB / Memory Log / Skill Catalog / Event / Combat 책임 분리
- 재획득 횟수만으로 자동 영구화하지 않는 구조 적용

## Blockers

- 축별 Record / Proficiency / Milestone 실제 수치 미확정
- 부위 경험치와 민감도 레벨 공식 미확정
- 실제 사건 ID와 플래그명 미작성
- 재획득·고착 실제 임계값 미확정
- Return과 굴복 기술의 수치 보정 미확정
- R18 전용 완화 행동·설비·이벤트 목록 미작성
- 일부 기벽의 로그 연결은 콘텐츠 사건 확정 후 조정 필요
- 선행 PR #15~#25가 Draft 상태라 Phase 5J-2도 stacked 상태로 관리 중

## Next Priorities

1. `MECH_Quirk_R18.md` v1.3 검토
2. Phase 5J-3 R18 완화 행동·설비 후보 작성
3. R18 Skill Catalog와 Return 해금 연결
4. 실제 사건 ID·플래그 매핑
5. 치료·완화·고착 수치 테스트 계획 수립
6. Item 후보를 탐험·Loot·Hideout 태그와 재대조
7. 장소별 Loot Profile에 설비 후보 연결

## Known Technical Debt

- 레거시 문서의 과거 29일·30일 설정
- 구형 파일명과 문서 경로 참조
- 미해결 `depends_on`
- Event ID 및 파일명 불일치
- 일부 문서의 frontmatter 부재
- 일부 일반 기벽 명칭과 실제 의학적 상태의 심각도 불일치
- 일부 R18 로그 연결은 사건 콘텐츠 확정 전 임시 명칭 사용
- 일부 R18 Return이 선택지 해금 수준에 머물러 있음
- 설비 후보의 플레이어 표시명은 최종 빌드 단계에서 Downfall 톤으로 재명명 필요

## Update Rule

이 문서는 프로젝트 진행 상태만 기록한다. 세계관, 시스템 규칙과 밸런스 정의는 각 Wiki 정본 문서가 소유한다.
