# Downfall Project State

## Current Phase

**Phase 5I-3: R18 기벽 Risk & Return·완화·고착 데이터 마이그레이션**

Phase 5H에서 일반 기벽 제거와 R18 기벽 완화·고착의 상위 규격을 분리했고, Phase 5I-1과 5I-2에서 일반 육체·정신 기벽의 치료 메타데이터를 정리했다. 현재는 R18 기벽 24종에 Risk, Return, 처리 모델, 고착 상태, 완화 방식과 메모리 로그 보존 규칙을 적용하는 단계다.

## Completed

- 프로젝트 핵심 정의 및 디자인 필러 3+1 확정
- 25일 의식과 오벵마을 고정 지리 정본화
- 외출 8단계 플레이 흐름과 지속 괴물 조우
- Loot Distribution Draft
- 아지트 영구 주 개조·자율행동·명령 저항·설비 후보 Draft
- 일반 기벽 제거와 R18 Risk & Return·완화·고착 상위 규격
- 일반 육체 기벽 치료 메타데이터 적용
- 일반 정신 기벽 치료 메타데이터 Draft
- 평화주의자를 살상 경험 기반 트라우마로 확정
- 색광증의 공통 기벽 + R18 모듈 중첩 구조 확정
- 만성 피로를 육체적 원인으로 확정

## In Progress

- R18 기벽 24종의 Risk / Return 분리
- `self_expiring / suppressible / irreversible` 처리 모델
- `temporary / persistent / permanent` 고착 상태
- `duration_reduction / stage_down / temporary_suppression / none` 완화 방식
- 완화·지속 종료 후 메모리 로그 기록 보존
- 일반 색광증과 R18 기벽 중첩 경계
- 순수 패널티 기벽에 선택지·기술·이벤트 Return 보강

## Blockers

- 기벽별 실제 메모리 로그 키와 해금 임계값 미확정
- `괴물 성애`의 도주·기습 하드락 강도 검토 필요
- 영구 기벽의 `temporary_suppression`이 어느 효과까지 억제하는지 미확정
- 고착 단계 상승 임계값 미확정
- R18 전용 완화 행동·설비·이벤트 목록 미작성
- 일반 Physical/Mental DB의 승인 결정에 따른 최종 항목 이동·번호 재정렬 필요
- 선행 PR #15~#22가 Draft 상태라 Phase 5I-3도 stacked 상태로 관리 중

## Next Priorities

1. `MECH_Quirk_R18.md` Risk & Return 검토
2. Phase 5I-4 `MECH_R18_Memory_Log` 고착 단계와 기록 보존 반영
3. 일반 Physical/Mental DB의 평화주의자·만성 피로 최종 이동 반영
4. 기벽별 실제 로그 키와 해금 임계값 지정
5. R18 완화 행동·설비 후보 작성
6. 치료·완화 수치 테스트 계획 수립
7. Item 후보를 탐험·Loot·Hideout 태그와 재대조

## Known Technical Debt

- 레거시 문서의 과거 29일·30일 설정
- 구형 파일명과 문서 경로 참조
- 미해결 `depends_on`
- Event ID 및 파일명 불일치
- 일부 문서의 frontmatter 부재
- 일부 일반 기벽 명칭과 실제 의학적 상태의 심각도 불일치
- R18 기벽의 개별 메모리 로그 키·기술 연결 미확정
- 일부 R18 Return이 구체적 보상 수치보다 선택지 해금 수준에 머물러 있음
- 설비 후보의 플레이어 표시명은 최종 빌드 단계에서 Downfall 톤으로 재명명 필요

## Update Rule

이 문서는 프로젝트 진행 상태만 기록한다. 세계관, 시스템 규칙과 밸런스 정의는 각 Wiki 정본 문서가 소유한다.
