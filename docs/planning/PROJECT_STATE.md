# Downfall Project State

## Current Phase

**Phase 5I-1: 일반 육체 기벽 치료 데이터 마이그레이션**

Phase 5H에서 일반 기벽 제거와 R18 기벽 완화·고착의 상위 규격을 분리했다. 현재는 육체적 기벽 16종에 제거 가능 여부, 치료 등급, 요구 의료품·시설과 특수 조건을 적용하고 삭제된 스탯 참조를 정리하는 단계다.

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
- 일반 기벽 제거와 R18 기벽 Risk & Return·완화·고착 상위 규격

## In Progress

- 육체 기벽 16종의 `removable` 모델 적용
- easy / normal / hard / professional 치료 등급 적용
- 일반·전문 의료품 분리
- 의무실·회복실·상담실·샤워실·전문 의료장비 연결
- 오염·감염·이상현상 선행 조건 정리
- 삭제된 `#Stat_Knowledge` 참조 제거
- 애매한 기벽의 검토 포인트 분리

## Blockers

- `환각성 옴`의 실제 피부 질환 / 감각 이상 설정 미확정
- `내이 파열`의 hard / professional 최종 등급 미확정
- `만성 두개 박동`의 `#Stat_Intelligence -2` 패널티 강도 검토 필요
- 기벽별 실제 치료 DC와 자원 소비량 미확정
- 치료 후 회복 행동과 부분 성공 수치 미확정
- 정신 기벽 DB 마이그레이션 미진행
- R18 기벽별 Risk & Return 재검토 필요
- 선행 PR #15~#20이 Draft 상태라 Phase 5I-1도 stacked 상태로 관리 중

## Next Priorities

1. `MECH_Quirk_Physical_DB`의 세 검토 항목 확정
2. Phase 5I-2 `MECH_Quirk_Mental_DB` 치료 필드 적용
3. Phase 5I-3 `MECH_Quirk_R18_DB` Risk / Return / 완화 / 고착 필드 적용
4. Phase 5I-4 `MECH_R18_Memory_Log` 고착 단계와 기록 보존 반영
5. 치료 DC·자원 소비량 테스트 계획 수립
6. Item 후보를 탐험·Loot·Hideout 태그와 재대조
7. 장소별 Loot Profile에 설비 후보 연결

## Known Technical Debt

- 레거시 문서의 과거 29일·30일 설정
- 구형 파일명과 문서 경로 참조
- 미해결 `depends_on`
- Event ID 및 파일명 불일치
- 일부 문서의 frontmatter 부재
- 장소별 자원·괴물·보상 후보의 DB 불일치 가능성
- 정신 Quirk DB에 삭제·변경 스탯 참조가 남아 있을 가능성
- 일부 일반 기벽 명칭과 실제 의학적 상태의 심각도가 불일치
- R18 Quirk DB의 `mitigable` 불리언이 완화 방식과 고착 단계를 표현하지 못함
- 일부 R18 기벽이 Risk & Return보다 순수 패널티에 가까움
- 설비 후보의 플레이어 표시명은 최종 빌드 단계에서 Downfall 톤으로 재명명 필요

## Update Rule

이 문서는 프로젝트 진행 상태만 기록한다. 세계관, 시스템 규칙과 밸런스 정의는 각 Wiki 정본 문서가 소유한다.
