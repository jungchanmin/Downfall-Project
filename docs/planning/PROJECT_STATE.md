# Downfall Project State

## Current Phase

**Phase 5M-3: R18 Gate Tag 정본·구형 Skill Catalog 정합성 패스**

Phase 5M-2에서 생존자·괴물별 기술 소유·해금·기술 키트 계약을 정리했다. 현재는 Tease의 자세 게이팅 카운터를 최소 조합형 Gate Tag로 고정하고, 구형 Skill Catalog의 공용 기술·Contact 자동 카운터·한글 키·랜덤 기술 풀 규칙을 최신 정본에 맞춰 순차 교체하는 단계다.

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
- 생존자·괴물별 기술 소유·해금·키트 데이터 계약

## In Progress

- 접근·방향·목표 부위·행동 부위·통제·동작·결과 Gate Tag 정본
- 복합 태그 대신 기본 태그 조합 사용
- Tease `required_matches / optional_matches / forbidden_tags` 계약
- Gate Tag 완전 일치·부분 일치·불일치 처리
- 공격축과 Gate Tag 책임 분리
- Skill Catalog SECTION 0 공용 풀 규칙 교체
- SECTION 1 기술 스키마 최신화
- SECTION 3 괴물 고정 키트 중심 전환
- SECTION 4 대표 5종을 공용 기술에서 분류 템플릿으로 전환
- SECTION 5 축 상성표 책임 축소
- SECTION 7 생존자·괴물 참조 방식 교체
- SECTION 8 영문 자세·부위 키 전환

## Blockers

- 부분 일치 카운터의 실제 경감 범위 미확정
- Gate Tag별 실제 `gate_strength` 수치 미확정
- 생존자 초기 기술 최종 개수 미확정
- 분류·기술 숙련 범위와 성장식 미확정
- 기술별 실제 기본 위력 수치 미확정
- 괴물 등급별 키트 크기 미확정
- 쿨타임 기본 범위 미확정
- 기술 정보 해금 속도 미확정
- 대표 변종 실제 `effect_id` 미확정
- 기본 `combo_chain_limit` 실제 수치 미확정
- 상태이상별 내성 수치 미확정
- 기존 Skill Catalog 본문 실제 순차 치환 미완료
- 선행 PR #15~#35가 Draft 상태라 Phase 5M-3도 stacked 상태로 관리 중

## Next Priorities

1. `MECH_R18_Gate_Tag_Standard` 검토
2. Skill Catalog SECTION 0·1·5·7·8 실제 순차 치환
3. 상태이상·내성 데이터 계약
4. 전조 아키타입 최종 목록과 기술 연결 샘플
5. 생존자 1명·괴물 1종의 실제 기술 키트 수직 슬라이스
6. 중립 상성·콤보 상한·쿨타임 밸런스 테스트 계획
7. 대표 변종 실제 `effect_id` 발급

## Known Technical Debt

- 기존 `MECH_R18_Skill_Catalog` 본문은 아직 생존자 굴복 기술을 전원 공용 풀로 규정함
- 기존 축×분류 상성표는 유혹형을 Contact 카운터로 직접 연결함
- 기존 괴물 기술 운용은 랜덤 축 풀 비중이 큼
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
