# Downfall Project State

## Current Phase

**Phase 5M-1: R18 기술 접근·회상 규칙과 전조 Bark 제작 확장성 정책**

Phase 5L에서 굴복 페이즈 코어와 대표 변종 역할을 재정렬했다. 현재는 생존자별 개별 기술 소유를 유지하면서 고정 장착 슬롯 없이 전투 상황에 맞는 기술을 우선 노출하는 접근 구조와, 전조 Bark 콘텐츠 폭증을 막는 Narration 중심 재사용 정책을 정본화하는 단계다.

## Completed

- 프로젝트 핵심 정의 및 디자인 필러 3+1 확정
- 25일 의식과 오벵마을 고정 지리 정본화
- 외출 8단계 플레이 흐름과 지속 괴물 조우
- Loot Distribution Draft
- 아지트 영구 주 개조·자율행동·명령 저항·설비 후보 Draft
- 일반 기벽 치료와 R18 Risk & Return·완화·고착 상위 규격
- 일반 육체 16종·정신 24종 분류 정합성
- R18 메모리 로그의 획득·재획득·고착·기록 보존 구조
- R18 기벽 24종 로그·획득·고착 조건 정합성
- R18 완화 행동·설비·일일 이용 제한
- R18 기벽 Return과 굴복 기술 연결
- R18 기술 정본 데이터 계약
- 신규 기벽 개발 우선순위
- 굴복 페이즈 주도권·전조·게이팅 코어
- Proficiency 대표 변종 역할 재정렬

## In Progress

- 생존자별 `known_skills`와 초기 기술 2~4개 구조
- 공용 커맨드 기술 대신 공용 안전 행동 분리
- 고정 장착 슬롯 폐기
- 자세·부위·상태·전조 기반 기술 우선 노출
- `Instinctive / Practiced / Known` 회상 단계
- 사용 제한 없는 전투 전 `preparation_focus` 후보
- 전조 아키타입 기반 Narration 재사용
- Bark를 첫 조우·시그니처·카운터 가능·치명적 오판 등 고가치 순간으로 제한
- 공용 Narration·직업 Bark·캐릭터 고유 Bark 제작 예산 분리
- 최근 출력 기록·화자 쿨다운·침묵 허용

## Blockers

- 초기 기술 수의 최종 범위 미확정
- 회상 단계 승급 조건 미확정
- `preparation_focus` 실제 효과 미확정
- 기술 학습 이벤트 빈도 미확정
- 전조 아키타입 최종 목록 미확정
- Bark 실제 출력 확률·화자 우선순위 미확정
- 조합형 문장 엔진 적용 범위 미확정
- 대표 변종 실제 `effect_id` 미확정
- 실제 게이지·로그·침식 수치 미확정
- 기본 `combo_chain_limit` 실제 수치 미확정
- 상태이상별 내성 수치 미확정
- 기존 Skill Catalog 공용 풀 규칙과 정합성 패스 필요
- 선행 PR #15~#33이 Draft 상태라 Phase 5M-1도 stacked 상태로 관리 중

## Next Priorities

1. `MECH_R18_Skill_Access_And_Recall_System` 검토
2. `MECH_R18_Telegraph_Bark_Content_Policy` 검토
3. Phase 5M-2 생존자·괴물 기술 소유·해금 데이터 계약
4. 유혹형을 자세·부위·행동 게이팅 카운터로 정본화
5. 괴물 기술별 `telegraph_profile / counter_tags / cooldown / combo` 스키마
6. 기존 Skill Catalog 공용 풀·축 상성표 정합성 패스
7. 상태이상·내성 데이터 계약

## Known Technical Debt

- 기존 `MECH_R18_Skill_Catalog`은 생존자 굴복 기술을 전원 공용 풀로 규정함
- 기존 축×분류 상성표는 유혹형을 Contact 카운터로 직접 연결함
- 기존 `MECH_Combat_System` SECTION 11은 완전 정보 공개와 구형 커맨드 역할을 포함함
- `SBV_Dom_CruelCommand` 후순위 변종 이동 필요
- `MECH_R18_Mitigation_System` 반복 완화 내성 후보 문구 직접 교체 필요
- `MECH_R18_Skill_Catalog` 제목·frontmatter 버전 불일치
- Skill Catalog의 한글 부위·자세 키와 Memory Log 영문 키 불일치
- 레거시 문서의 과거 29일·30일 설정
- 구형 파일명과 문서 경로 참조
- 미해결 `depends_on`

## Update Rule

이 문서는 프로젝트 진행 상태만 기록한다. 세계관, 시스템 규칙과 밸런스 정의는 각 Wiki 정본 문서가 소유한다.
