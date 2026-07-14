# Downfall Project State

## Current Phase

**Phase 5K-1: R18 기벽 Return·굴복 기술 연결 정합성**

Phase 5J-4에서 R18 기벽 24종의 완화 행동과 일일 제한을 연결했다. 현재는 기벽 Return을 생존자 굴복 기술 5대분류와 대표 기술에 연결하고, 해금 로그 단계와 완화 중 정지 규칙을 정리하는 단계다.

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
- R18 기벽 24종 로그·획득·고착 조건 정합성
- R18 완화 행동 8종·확장 설비 5종 초안
- R18 기벽 24종 완화 행동 매핑
- 생존자별 일일 완화 1회 확정
- 설비별 일일 이용 2회 확정
- 안전 격리를 방·설비 실제 수용 인원 기준으로 확정
- 영구적 반복 완화 내성 폐기

## In Progress

- R18 기벽 24종 Return을 굴복 기술 5대분류에 연결
- 대표 기술 `SB_Service_Kiss / SB_Tease_Caress / SB_Dom_Ride / SB_Absorb_Drink / SB_Defiance_Focus` 연결
- Record / Proficiency / Milestone별 Return 해금 범위
- 기벽 전용 기술 변종과 기본 기술 분리
- 완화 중 Risk와 직접 연결 Return·기술 변종 동시 정지
- 단순 수치 상위호환보다 전략적 변종 우선 원칙

## Blockers

- 기벽별 실제 수치 보정 미확정
- 기술 변종 ID와 표시명 미작성
- 기술 사용 시 로그 증가량 미확정
- 침식·욕구불만 추가 비용 미확정
- 완화 중 정지되는 세부 effect_id 미작성
- 행동당 실제 지속시간 감소량 미확정
- 단계 하향·일시 억제 실제 난이도 미확정
- R18 설비의 획득 장소와 희귀도 미확정
- 실제 사건 ID와 플래그명 미작성
- 선행 PR #15~#28이 Draft 상태라 Phase 5K-1도 stacked 상태로 관리 중

## Next Priorities

1. `MECH_R18_Quirk_Skill_Return_Map` 검토
2. Skill Catalog 본문에 Return 연동 필드 정합성 반영
3. 기술 변종 ID 후보 작성
4. 실제 사건 ID·플래그 매핑
5. 치료·완화·고착 수치 테스트 계획
6. Item 후보를 탐험·Loot·Hideout 태그와 재대조
7. 장소별 Loot Profile에 설비 후보 연결
8. 일일 완화 횟수 UI·저장 데이터 초안

## Known Technical Debt

- `MECH_R18_Mitigation_System` v1.0의 반복 완화 내성 후보 문구를 승인된 일일 횟수 제한으로 직접 교체하는 정합성 패스 필요
- `MECH_R18_Skill_Catalog`의 제목 버전 표기와 frontmatter 버전 불일치
- Skill Catalog 일부 부위 키가 한글이고 Memory Log는 영문 키를 사용함
- 레거시 문서의 과거 29일·30일 설정
- 구형 파일명과 문서 경로 참조
- 미해결 `depends_on`
- Event ID 및 파일명 불일치
- 일부 문서의 frontmatter 부재
- 일부 일반 기벽 명칭과 실제 의학적 상태의 심각도 불일치
- 일부 R18 로그 연결은 사건 콘텐츠 확정 전 임시 명칭 사용
- R18 완화 설비의 표시명은 최종 톤 패스에서 재명명 필요

## Update Rule

이 문서는 프로젝트 진행 상태만 기록한다. 세계관, 시스템 규칙과 밸런스 정의는 각 Wiki 정본 문서가 소유한다.
