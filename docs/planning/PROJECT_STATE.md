# Downfall Project State

## Current Phase

**Phase 5M-4: R18 Skill Catalog 규칙 골격 1차 적용**

Phase 5M-3에서 최소 조합형 Gate Tag와 카탈로그 정합성 계획을 확정했다. 현재는 기존 기술 예시와 연출 데이터를 보존하면서 `MECH_R18_Skill_Catalog`의 소유권·스키마·상성 책임·참조 방식·게이팅 규칙을 최신 정본 오버라이드로 실제 적용하는 단계다.

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
- 최소 조합형 Gate Tag 정본

## In Progress

- Skill Catalog SECTION 0 소유권 규칙 오버라이드
- SECTION 1 최신 `R18SkillDef` 스키마 적용
- `required_parts`를 대상 부위와 행동 부위로 분리
- SECTION 5 축 상성의 책임을 친화도 보정으로 축소
- Tease 카운터를 Gate Tag 완전 일치로 제한
- SECTION 7 생존자·괴물별 기술 참조 방식 적용
- SECTION 8 영문 자세·부위 키와 행동 취소 후 주도권 규칙 적용
- 대표 기술 5종을 전원 공용 기술에서 분류 템플릿으로 재해석
- 기존 기술 예시의 레거시 필드 읽기 변환 규칙

## Blockers

- 기존 Skill Catalog 원문 SECTION별 실제 병합 미완료
- 기존 개별 기술의 `required_parts` 의미 분리 미완료
- 개별 괴물 기술 Gate Tag·전조 프로필 배정 미완료
- 부분 일치 카운터의 실제 경감 범위 미확정
- Gate Tag별 실제 `gate_strength` 수치 미확정
- 생존자 초기 기술 최종 개수 미확정
- 분류·기술 숙련 범위와 성장식 미확정
- 기술별 실제 기본 위력 수치 미확정
- 괴물 등급별 키트 크기 미확정
- 쿨타임 기본 범위 미확정
- 대표 변종 실제 `effect_id` 미확정
- 기본 `combo_chain_limit` 실제 수치 미확정
- 상태이상별 내성 수치 미확정
- 선행 PR #15~#35가 Draft 상태라 Phase 5M-4도 stacked 상태로 관리 중

## Next Priorities

1. Skill Catalog 원문 SECTION 0·1 직접 병합
2. SECTION 5·7·8 직접 병합
3. 기존 기술별 대상 부위·행동 부위 분리 패스
4. 괴물 기술 Gate Tag·전조 아키타입 샘플 적용
5. 상태이상·내성 데이터 계약
6. 생존자 1명·괴물 1종의 실제 기술 키트 수직 슬라이스
7. 중립 상성·콤보 상한·쿨타임 밸런스 테스트 계획

## Known Technical Debt

- 기존 `MECH_R18_Skill_Catalog` 본문은 아직 구형 문구를 포함하며 오버라이드 문서가 최신 해석을 소유함
- 기존 괴물 기술 운용은 랜덤 축 풀 비중이 큼
- 기존 `MECH_Combat_System` SECTION 11은 완전 정보 공개와 구형 커맨드 역할을 포함함
- `SBV_Dom_CruelCommand` 후순위 변종 이동 필요
- `MECH_R18_Mitigation_System` 반복 완화 내성 후보 문구 직접 교체 필요
- `MECH_R18_Skill_Catalog` 제목·frontmatter 버전 불일치
- Skill Catalog 개별 예시의 한글 부위·자세 키와 Memory Log 영문 키 불일치
- 레거시 문서의 과거 29일·30일 설정
- 구형 파일명과 문서 경로 참조
- 미해결 `depends_on`

## Update Rule

이 문서는 프로젝트 진행 상태만 기록한다. 세계관, 시스템 규칙과 밸런스 정의는 각 Wiki 정본 문서가 소유한다.
