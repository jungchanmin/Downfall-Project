# Downfall Project State

## Current Phase

**Phase 4A: 장소 상세 문서 분리**

Phase 1의 핵심 정본, Phase 2의 문서 구조 개편, Phase 3의 오벵마을 표기·고정 지리·ConfigureBook 정책을 병합했다. 현재는 `Obeng_Village_Lore.md`를 상위 인덱스로 유지하고, 15개 고정 지역의 세부 공간과 이벤트 제작 정보를 `Wiki/02_World/Locations/` 하위 문서로 분리하는 단계다.

## Completed

- 프로젝트 핵심 정의 확정
- 디자인 필러 3+1 확정
- 25일 의식 및 위험도 구조 정본화
- 어머니와 그릇 설정 정본화
- 문서 소유권 및 목표 폴더 구조 정의
- 프로젝트 거버넌스 및 Wiki 검증 자동화 구축
- 기능 브랜치 Manifest push 경쟁 상태 완화
- Planning 문서의 docs/archive 이동
- World Concept deprecated 전환
- Entity 인덱스 작성
- Migration Backlog 정리
- 오벵마을 공식 표기와 고정 지리 원칙 반영
- ConfigureBook 원고 등록 정책 수립

## In Progress

- `Wiki/02_World/Locations/` 장소별 상세 문서 작성
- ConfigureBook Place 원고와 Wiki 상세 문서 대응표 갱신
- 장소 원고 세부 공간·이상현상 시드 Import 여부 판단

## Blockers

- Combat 세부 구조 분리는 아직 승인·실행 전
- R18 모듈의 실제 파일 이동은 후속 단계
- ConfigureBook 생존자·이벤트 원고의 Wiki 등록률은 아직 조사 중
- Event ID 및 파일명 불일치 경고가 남아 있음

## Next Priorities

1. Phase 4A 장소 상세 문서 PR 검토 및 병합
2. Place 원고별 세부 공간·이상현상 시드 전체 Import 여부 판단
3. Imported 판정된 ConfigureBook Place 원고의 Archive 이동 승인
4. Combat 상위 허브와 세부 문서 소유권 설계
5. R18 모듈 이동 계획 작성

## Active Pull Request

Phase 4A 작업 완료 후 이 항목을 해당 Draft PR로 갱신한다.

## Known Technical Debt

- 레거시 문서의 과거 29일 설정
- 구형 파일명과 문서 경로 참조
- 미해결 `depends_on`
- Event 파일명과 ID 불일치
- 일부 문서의 frontmatter 부재
- ConfigureBook 원고와 Wiki 정본의 중복 가능성

## Update Rule

이 문서는 프로젝트 진행 상태만 기록한다. 세계관, 시스템 규칙과 밸런스 정의는 각 Wiki 정본 문서가 소유한다.
