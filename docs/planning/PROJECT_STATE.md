# Downfall Project State

## Current Phase

**Phase 5K-2: R18 기술 데이터 계약·레거시 마이그레이션 정합성**

Phase 5K-1에서 R18 기벽 24종의 Return을 굴복 기술 5대분류와 대표 기술에 연결했다. 현재는 기존 Skill Catalog의 전투 콘텐츠를 보존하면서 영문 정본 키, UI 표시명, 기본 기술·기벽 변종, 완화 중 비활성 정책과 레거시 치환 순서를 정본화하는 단계다.

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
- 생존자별 일일 완화 1회·설비별 2회·격리 수용량 기준 확정
- R18 기벽 Return과 굴복 기술 5대분류 연결

## In Progress

- `Mouth / Chest / LowerBody / Rear / WholeBody` 정본 키 정의
- 한글 UI 표시명과 구현 키 분리
- `base_skill_id / variant_id / variant_source_quirks` 계약
- Memory Log 기반 Return 해금 필드
- 완화 중 기본 기술 유지·기벽 변종 비활성 정책
- 레거시 한글 부위·자세 키 호환 로더와 순차 치환
- Skill Catalog 제목 버전 불일치 정리 계획

## Blockers

- 기존 Skill Catalog 항목별 영문 키 실제 치환 미완료
- 기술 변종 ID와 표시명 미작성
- 기벽별 실제 수치 보정 미확정
- 기술 사용 시 로그 증가량 미확정
- 침식·욕구불만 추가 비용 미확정
- 완화 중 정지되는 세부 effect_id 미작성
- 행동당 실제 지속시간 감소량 미확정
- 단계 하향·일시 억제 실제 난이도 미확정
- R18 설비의 획득 장소와 희귀도 미확정
- 실제 사건 ID와 플래그명 미작성
- 선행 PR #15~#29가 Draft 상태라 Phase 5K-2도 stacked 상태로 관리 중

## Next Priorities

1. `MECH_R18_Skill_Data_Contract` 검토
2. Skill Catalog 대표 기술 5종부터 정본 필드 적용
3. 괴물 공유 기술의 부위 키 순차 치환
4. 굴복 커맨드의 자세·행위 부위 키 치환
5. 기술 변종 ID 후보 작성
6. 치료·완화·고착 수치 테스트 계획
7. Item 후보를 탐험·Loot·Hideout 태그와 재대조
8. 장소별 Loot Profile에 설비 후보 연결

## Known Technical Debt

- `MECH_R18_Mitigation_System` v1.0의 반복 완화 내성 후보 문구 직접 교체 필요
- `MECH_R18_Skill_Catalog` 제목 `v1.0`과 frontmatter `v1.4.0` 불일치
- Skill Catalog의 한글 부위·자세 키가 Memory Log 영문 키와 불일치
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
