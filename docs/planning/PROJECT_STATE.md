# Downfall Project State

## Current Phase

**Phase 5D: 아지트 운영·개조 시스템 정본화**

Phase 5B에서 외출 8단계 흐름과 지속 괴물 조우를 정리했고, Phase 5C에서 카테고리 등장도·지역 특성·위험도·잔존 자원도에 따른 Loot Distribution을 Draft로 작성했다. 현재는 기존 아지트의 고정 방을 개조하고 설비를 배치해 자율행동, 치료, 경계, 제작, 관계와 아지트 전투를 변화시키는 시스템을 정본화하는 단계다.

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

## In Progress

- 기존 아지트 방 기반 개조 분기
- 리모델링 + 설비 배치 혼합 구조
- 아침·저녁 자율행동
- 방별 수용 인원과 행동 슬롯
- 기벽별 난이도·의약품·시설 기반 치료
- 시설 손상·봉쇄·파괴·오염·점거
- 방 복구와 설비 회수
- 아지트 전투 구역 연결
- 공통 방 ID를 참조하는 R18 확장 인터페이스

## Blockers

- 방별 실제 수용 인원 미확정
- 행동 횟수와 피로 비용 미확정
- 개조별 부품 비용·판정 난이도 미확정
- 시설 단계와 설비 슬롯 수 미확정
- 실제 아지트 설비 목록 미작성
- 방 파괴·복구 수치 미확정
- 기벽 치료 DC와 자원 소비량 미확정
- 일반/R18 Quirk DB 제거 조건 정규화 필요
- PR #15와 #16이 Draft 상태라 Phase 5D도 선행 브랜치 기반으로 관리 중

## Next Priorities

1. Phase 5B PR Ready 전환 및 병합
2. Phase 5C Loot Distribution 검토 후 main 기준 재설정
3. Phase 5D Hideout System 검토 후 main 기준 재설정
4. `HIDEOUT_ROOM_PROFILE` 방별 수용 인원·개조 목록 초안
5. `HIDEOUT_FACILITY_DB` 실제 설비 후보 작성
6. `HIDEOUT_ACTION_PROFILE` 자율행동 판정 구조 작성
7. 일반/R18 Quirk DB 제거 조건 정규화
8. Item 후보를 탐험·Loot·Hideout 태그와 재대조

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
