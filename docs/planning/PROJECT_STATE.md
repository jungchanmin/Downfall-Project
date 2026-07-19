# Downfall Project State

## Current Phase

**Phase 5N-1: 광신도 굴복 기술 6종 실제 마이그레이션**

Phase 5M-5에서 R18 Skill Catalog 규칙 코어를 별도 정본으로 분리했다. 현재는 기존 기술 데이터를 최신 `R18SkillDef`, Gate Tag, 전조, 쿨타임, AI 조건, 콤보·피니셔 계약에 맞춰 실제 변환하는 첫 수직 마이그레이션 단계다.

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
- Skill Catalog 규칙 코어 정본 분리

## In Progress

- 광신도 인지 기술 3종 최신 스키마 마이그레이션
- 광신도 함락 기술 3종 최신 스키마 마이그레이션
- 기술별 `base_power / stability / cooldown` 임시 등급
- 대상 부위와 행동 부위 분리
- Gate Attack·전조 프로필·AI 조건 배정
- 인지 교란 → 구속 → 함락 피니셔 콤보 구조
- `SR_Sub_Pin` 주도권 유지와 콤보 상한 소비
- `SR_Sub_Thrust` 복수 피니셔 조건
- 광신도 고정 시그니처·코어·조건부 기술 키트

## Blockers

- 실제 `base_power` 수치 범위 미확정
- 실제 쿨타임 턴 수 미확정
- `ST_Trance / ST_Enthrall / ST_Afterglow` 세부 데이터 계약 미완료
- `combo_chain_limit` 실제 수치 미확정
- 부분 일치 Tease의 실제 경감 범위 미확정
- Gate Tag별 실제 `gate_strength` 수치 미확정
- 광신도 등급별 기술 키트 차이 미확정
- Unity effect ID 최종 명명 미완료
- 생존자 초기 기술 최종 개수 미확정
- 분류·기술 숙련 범위와 성장식 미확정
- 기존 Skill Catalog frontmatter 콘텐츠 원본 축소 미완료
- 선행 PR #15~#37이 Draft 상태라 Phase 5N-1도 stacked 상태로 관리 중

## Next Priorities

1. `MECH_R18_Cultist_Submission_Skill_Migration` 검토
2. 광신도 기술 전조 아키타입 6종 정본화
3. 광신도 기술을 실제 Monster DB 개체·등급에 배정
4. 광신도 대응용 생존자 1명의 초기 기술 수직 슬라이스
5. 상태이상·내성 데이터 계약
6. 중립 상성·콤보 상한·쿨타임 밸런스 테스트 계획
7. 기존 Skill Catalog frontmatter를 콘텐츠 원본 역할로 축소

## Known Technical Debt

- 기존 `MECH_R18_Skill_Catalog` 본문은 구형 규칙 문구를 포함하지만 `MECH_R18_Skill_Catalog_Core`가 최신 정본을 소유함
- 기존 광신도 기술 예시는 레거시 필드를 유지하며 신규 마이그레이션 문서가 최신 데이터를 소유함
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
