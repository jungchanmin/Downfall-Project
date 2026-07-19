# Downfall Project State

## Current Phase

**Phase 5M-2: R18 생존자·괴물 기술 소유·해금·키트 데이터 계약**

Phase 5M-1에서 고정 장착 제한을 폐기하고 상황 기반 기술 접근과 Narration 중심 전조 콘텐츠 정책을 정리했다. 현재는 생존자별 개별 기술 소유·초기 기술·학습·기벽 변종과 괴물별 고정 기술 키트·쿨타임·전조·게이팅·카운터 태그를 정본화하는 단계다.

## Completed

- 프로젝트 핵심 정의 및 디자인 필러 3+1 확정
- 25일 의식과 오벵마을 고정 지리 정본화
- 외출 8단계 플레이 흐름과 지속 괴물 조우
- 일반 기벽 치료와 R18 Risk & Return·완화·고착 상위 규격
- R18 메모리 로그의 획득·재획득·고착·기록 보존 구조
- R18 기벽 24종 로그·획득·고착 조건 정합성
- R18 완화 행동·설비·일일 이용 제한
- R18 기벽 Return과 굴복 기술 연결
- R18 기술 정본 데이터 계약
- 신규 기벽 개발 우선순위
- 굴복 페이즈 주도권·전조·게이팅 코어
- Proficiency 대표 변종 역할 재정렬
- 기술 장착 제한 폐기와 상황 기반 기술 접근·회상
- Narration 중심 Bark 제작 확장성 정책

## In Progress

- 생존자별 `known_skills / initial_skills / learned_skills / signature_skills`
- 분류 숙련과 기술별 숙련 분리
- 기술 기본 위력·안정성·자기 비용 계약
- 초기 기술 2~4개 권장 구조
- 공용 기술이 아닌 공용 안전 행동 분리
- Tease를 `gate_tags × counter_tags` 기반 게이팅 카운터로 정본화
- 괴물 고정 시그니처·코어·조건부 피니셔·소수 변주 슬롯
- 괴물 기술 쿨타임·AI 조건·시그니처 콤보
- 전조 프로필과 기술 정보 관찰 단계 연결
- 해금 경로 검증 규칙

## Blockers

- 생존자 초기 기술 최종 개수 미확정
- 분류·기술 숙련 범위와 성장식 미확정
- 기술별 실제 기본 위력 수치 미확정
- 게이트 태그 정본 목록 미확정
- 부분 일치 카운터 처리 미확정
- 괴물 등급별 키트 크기 미확정
- 쿨타임 기본 범위 미확정
- 기술 정보 해금 속도 미확정
- 대표 변종 실제 `effect_id` 미확정
- 기본 `combo_chain_limit` 실제 수치 미확정
- 상태이상별 내성 수치 미확정
- 기존 Skill Catalog 공용 풀·축 상성표 정합성 패스 필요
- 선행 PR #15~#34가 Draft 상태라 Phase 5M-2도 stacked 상태로 관리 중

## Next Priorities

1. `MECH_R18_Skill_Ownership_Unlock_Contract` 검토
2. 기존 Skill Catalog 공용 풀·축 상성표 정합성 패스
3. 게이트 태그 정본 목록 작성
4. 상태이상·내성 데이터 계약
5. 전조 아키타입 최종 목록과 기술 연결 샘플
6. 생존자 1명·괴물 1종의 실제 기술 키트 수직 슬라이스
7. 중립 상성·콤보 상한·쿨타임 밸런스 테스트 계획

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
