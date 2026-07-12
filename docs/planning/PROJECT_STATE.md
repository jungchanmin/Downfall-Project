# Downfall Project State

## Current Phase

**Phase 4D: 외곽 및 외곽 심부 장소 원고 세부 Import**

Phase 4C에서 중간 지대 4개 장소의 세부 Import를 완료했다. 현재는 외곽 및 외곽 심부 7개 장소의 ConfigureBook 원고를 검토하고, 공통 장소 정본·R18 확장·괴물/전투 DB·핵심 로어 후보를 분리하는 단계다.

## Completed

- 프로젝트 핵심 정의 확정
- 디자인 필러 3+1 확정
- 25일 의식 및 위험도 구조 정본화
- 어머니와 그릇 설정 정본화
- 문서 소유권 및 목표 폴더 구조 정의
- 프로젝트 거버넌스 및 Wiki 검증 자동화 구축
- Planning 문서의 docs/archive 이동
- World Concept deprecated 전환
- Entity 인덱스 작성
- 오벵마을 공식 표기와 고정 지리 원칙 반영
- ConfigureBook 원고 등록 정책 수립
- `Wiki/02_World/Locations/` 장소별 상세 문서 생성
- 중심부 4개 장소 원고 세부 Import
- 중간 지대 4개 장소 원고 세부 Import

## In Progress

- 외곽 및 외곽 심부 7개 장소 원고 세부 Import
- 정본 충돌 설정 명시적 보류
- 공통 장소 정본과 R18 확장 요소 분리
- 자원·괴물·고유 NPC·보상·수치 효과를 TODO로 분리

## Blockers

- Resource System 또는 Item DB 기준 자원 목록 정리가 필요함
- Monster DB 및 Entity 문서 기준 등장 후보 정리가 필요함
- 고유 NPC와 세력 보상은 Entity/Faction 문서 대조가 필요함
- 연구소 원고의 플레이어 괴물화·미확정 진엔딩·고유 악신 설정은 디렉터 승인 없이 사용 불가
- Combat 세부 구조 분리는 아직 승인·실행 전
- R18 모듈의 실제 파일 이동은 후속 단계
- Event ID 및 파일명 불일치 경고가 남아 있음

## Next Priorities

1. Phase 4D 외곽 장소 Import PR 검토 및 병합
2. Place 원고 15개 Archive 이동 승인 여부 판단
3. Resource System 또는 Item DB 기준 자원 후보 정리
4. Monster DB 및 Entity 문서 기준 등장 후보 정리
5. Combat 상위 허브와 세부 문서 소유권 설계
6. R18 모듈 이동 계획 작성

## Known Technical Debt

- 레거시 문서의 과거 29일 설정
- 구형 파일명과 문서 경로 참조
- 미해결 `depends_on`
- Event ID 및 파일명 불일치
- 일부 문서의 frontmatter 부재
- 장소별 자원·괴물·고유 NPC·보상 후보의 DB 불일치 가능성
- 연구소 원고의 미승인 엔딩 및 플레이어 변이 설정

## Update Rule

이 문서는 프로젝트 진행 상태만 기록한다. 세계관, 시스템 규칙과 밸런스 정의는 각 Wiki 정본 문서가 소유한다.
