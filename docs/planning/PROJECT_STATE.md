# Downfall Project State

## Current Phase

**Phase 5E: 아지트 방 프로필 및 개조 분기 정본화**

Phase 5D에서 아지트 운영·개조 시스템의 공통 구조를 Draft로 작성했다. 현재는 기존 아지트 고정 방별로 공간 규모, 기본 행동, 주 개조 분기, 설비 적합성과 손상 우선순위를 정의하는 단계다.

## Completed

- 프로젝트 핵심 정의 및 디자인 필러 3+1 확정
- 25일 의식과 오벵마을 고정 지리 정본화
- 15개 고정 지역 상세 문서 및 Place 원고 후보 Import
- 자원·아이템 상위 체계 Draft 작성
- 레거시 아이템 후보 및 일반 장비 후보 검토
- R18 아이템 확장 경계 정의
- 외출 8단계 플레이 흐름
- 지역 필수 이벤트와 맵 배치 괴물 지속 조우 구조
- 제한된 선택지와 스탯 + 장비 기능 태그 구조
- 카테고리·지역·위험도·잔존 자원도 기반 Loot Distribution Draft
- 기존 방 개조 + 설비 배치 기반 Hideout System Draft

## In Progress

- 방마다 하나의 주 개조를 선택하는 구조
- 개조 교체와 일부 투자 보존 규칙
- 소형 / 중형 / 대형 / 실외 수용 규모
- 방별 기본 행동과 전문 행동
- 설비 적합도: native / compatible / forbidden
- 방별 개조 분기와 전투 역할
- 손상 시 전문 기능부터 제한하는 우선순위
- 공통 방 ID를 참조하는 R18 확장 수준

## Blockers

- 규모별 실제 수용 인원 미확정
- 단계별 설비 슬롯 수 미확정
- 개조 교체 비용과 투자 보존 비율 미확정
- 개조별 부품 비용·판정 난이도 미확정
- 실제 아지트 설비 목록 미작성
- 자율행동의 지시·자율 선택 우선순위 미확정
- 행동 횟수와 피로 비용 미확정
- 일반/R18 Quirk DB 제거 조건 정규화 필요
- PR #15~#17이 Draft 상태라 Phase 5E도 선행 브랜치 기반으로 관리 중

## Next Priorities

1. Phase 5B~5D 선행 PR 검토 및 병합 순서 정리
2. Phase 5E Room Profile 검토 후 main 기준 재설정
3. `HIDEOUT_FACILITY_DB` 실제 설비 후보 작성
4. `HIDEOUT_ACTION_PROFILE` 자율행동·명령 행동 구조 작성
5. 규모별 수용 인원과 설비 슬롯의 테스트용 초기값 설정
6. 일반/R18 Quirk DB 제거 조건 정규화
7. Item 후보를 탐험·Loot·Hideout 태그와 재대조

## Known Technical Debt

- 레거시 문서의 과거 29일·30일 설정
- 구형 파일명과 문서 경로 참조
- 미해결 `depends_on`
- Event ID 및 파일명 불일치
- 일부 문서의 frontmatter 부재
- 장소별 자원·괴물·보상 후보의 DB 불일치 가능성
- 일반 Quirk DB에 삭제된 스탯 참조 일부 존재
- R18 Quirk DB의 간호 제거 배제 전제
- 아지트 레거시 문서의 물·멘탈·고문 등 구형 개념 검토 필요

## Update Rule

이 문서는 프로젝트 진행 상태만 기록한다. 세계관, 시스템 규칙과 밸런스 정의는 각 Wiki 정본 문서가 소유한다.
