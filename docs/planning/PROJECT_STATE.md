# Downfall Project State

## Current Phase

**Phase 5H: 일반 기벽 치료와 R18 기벽 완화·고착 구조 정본화**

Phase 5D~5G에서 아지트 개조, 자율행동, 명령 저항과 설치형 설비 후보를 정리했다. 현재는 일반 기벽의 제거 경로와 R18 기벽의 Risk & Return·비가역성·완화·고착을 분리하고, 기존 기벽 DB가 공통으로 사용할 치료 메타데이터를 정본화하는 단계다.

## Completed

- 프로젝트 핵심 정의 및 디자인 필러 3+1 확정
- 25일 의식과 오벵마을 고정 지리 정본화
- 15개 고정 지역 상세 문서 및 Place 원고 후보 Import
- 자원·아이템 상위 체계와 일반 장비 후보 Draft
- 외출 8단계 플레이 흐름과 지속 괴물 조우
- 카테고리·지역·위험도·잔존 자원도 기반 Loot Distribution Draft
- 기존 방 기반 아지트 개조·파괴·복구 구조
- 방별 영구 주 개조와 규모 등급
- 플레이어 직접 명령 + 미지정 생존자 자율행동
- 명령 저항·설득·타협·인원 교체·강제 구조
- 생활·의료·제작·정보·방어·저장·훈련·특수 설비 후보 Draft

## In Progress

- 일반 기벽의 제거 가능성·치료 등급·요구 자원·시설 필드
- R18 기벽의 Risk / Return 분리
- R18 기벽의 suppressible / self_expiring / irreversible 분류
- R18 메모리 로그의 기록 보존과 고착 단계
- 일반 치료와 R18 완화의 아지트 시설 연결
- 기존 `간호 요구치` 필드 마이그레이션 계획

## Blockers

- 일반 기벽별 실제 의료품·시설 요구 미확정
- 기벽별 치료 DC와 부분 성공 수치 미확정
- 삭제·변경된 스탯 참조 정리 필요
- R18 기벽별 최종 Risk & Return 재검토 필요
- 메모리 로그 해금·고착 임계값 미확정
- R18 전용 완화 설비·이벤트 목록 미작성
- 선행 PR #15~#19가 Draft 상태라 Phase 5H도 stacked 상태로 관리 중

## Next Priorities

1. `MECH_Quirk_Treatment_System` 검토
2. 일반 Physical/Mental Quirk DB에 `quirk_treatment` 필드 적용
3. R18 Quirk DB에 Risk / Return / mitigation / lock_state 필드 적용
4. R18 Memory Log에 고착 단계와 기록 보존 규칙 반영
5. 삭제·변경 스탯 참조 정리
6. Item 후보를 탐험·Loot·Hideout 태그와 재대조
7. 장소별 Loot Profile에 설비 후보 연결

## Known Technical Debt

- 레거시 문서의 과거 29일·30일 설정
- 구형 파일명과 문서 경로 참조
- 미해결 `depends_on`
- Event ID 및 파일명 불일치
- 일부 문서의 frontmatter 부재
- 장소별 자원·괴물·보상 후보의 DB 불일치 가능성
- 일반 Quirk DB에 삭제·변경 스탯 참조 존재
- 일반 Quirk DB의 `간호 요구치`가 난이도·자원·시설을 혼합
- R18 Quirk DB의 `mitigable` 불리언이 완화 방식과 고착 단계를 표현하지 못함
- 일부 R18 기벽이 Risk & Return보다 순수 패널티에 가까움
- 설비 후보의 플레이어 표시명은 최종 빌드 단계에서 Downfall 톤으로 재명명 필요

## Update Rule

이 문서는 프로젝트 진행 상태만 기록한다. 세계관, 시스템 규칙과 밸런스 정의는 각 Wiki 정본 문서가 소유한다.
