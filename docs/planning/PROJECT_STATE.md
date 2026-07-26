# Downfall Project State

## Current Phase

**Phase 5N-3: 부위 약점·감응·과자극 시스템 정본화**

Phase 5N-2에서 특수 굴복페이즈의 굴복도·탈진력·절정도·절정 여운·결착 규칙을 별도 정본으로 분리했다. 현재는 해당 자원 규칙을 실제 신체 부위 공략에 연결하기 위해 부위 계층, 개체 고유 약점, 감응 단계, 반복 공략과 보호 행동, 비인간형 특수 기관 계약을 정본화하는 단계다.

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
- 광신도 굴복 기술 6종 최신 계약 마이그레이션
- 굴복페이즈 페이퍼 전투 테스트 6회
- 굴복도·탈진력·절정도 책임 분리
- 공격자 효과 우선 결착 규칙
- 일반전투 수치 패널티 비이관·구조 조건 제한 이관
- 반복 절정·잔여 프로필·기술 등급별 절정 상한
- 절정 여운 행동 스킵과 자기 절정 비용 분리

## In Progress

- 신체 부위의 대분류·세부 부위 계층 구조
- 약점과 감응도의 독립 데이터 계약
- `Normal / Sensitive / Overstimulated` 단계
- 기술 등급별 감응 진행 표식
- 생존자·괴물 감응 효과 프로필 분리
- `Exhaustion / Control / ClimaxSensitivity` 약점 유형
- `Unknown / Suspected / Confirmed / Mastered` 약점 공개 단계
- 동일 부위 반복 공략과 보호 행동 해금
- 비인간형 괴물 `SpecialOrgan` 계약
- 일반전투 부상·파괴와 굴복 감응의 경계

## Blockers

- 기술별 실제 감응 진행값 미배정
- Major 기술의 즉시 단계 상승 범위 미확정
- 세 번째 동일 부위 공략 반응 `+1` 실제 범위 미확정
- 약점 등급별 기본 수치 미확정
- 탈진 피해 등급별 최종 상한 미확정
- Critical 약점의 즉시 결착 허용 여부 미확정
- 전투 후 `ResidualSensitivity` 지속·회복 미확정
- 의복 상태와 부위 접근 Gate 정식 계약 미완료
- 다대일 전투의 감응 정보·약점 정보 공유 미확정
- Memory Log·괴물 도감의 약점 공개 승계 미확정
- 굴복도 성장 획득 경로와 일반 범위 미확정
- 반복 절정 피해의 장기 상한 필요성 미검증
- Defiance 굴복도 회복의 판정·주도권 비용 미확정
- 일반·정예 괴물의 연속 주도권 상한 미확정
- 실제 `base_power` 수치 범위 미확정
- 실제 쿨타임 턴 수 미확정
- `ST_Trance / ST_Enthrall` 세부 데이터 계약 미완료
- 부분 일치 Tease의 실제 경감 범위 미확정
- Unity effect ID 최종 명명 미완료

## Next Priorities

1. `MECH_R18_Body_Sensitivity_System` 검토
2. 굴복 전용 생존자 기본 기술 풀 작성 규칙
3. 의복 상태·부위 접근 Gate 정본
4. Combat Narration 조건 블록과 상태 우선순위
5. 전투 시나리오 기반 재사용 Bark 후보 추출
6. 광신도 6종 기술에 부위·감응·약점 필드 재배정
7. 비인간형 괴물 1종 SpecialOrgan 수직 테스트
8. Absorption·Fluid·Mutation 페이퍼 전투 테스트
9. 광신도 기술을 실제 Monster DB 개체·등급에 배정

## Known Technical Debt

- 기존 `MECH_R18_Skill_Catalog` 본문은 구형 규칙 문구를 포함하지만 `MECH_R18_Skill_Catalog_Core`가 최신 정본을 소유함
- 기존 광신도 기술 예시는 레거시 필드를 유지하며 신규 마이그레이션 문서가 최신 데이터를 소유함
- 기존 괴물 기술 운용은 랜덤 축 풀 비중이 큼
- 기존 `MECH_Combat_System` SECTION 11은 완전 정보 공개·공용 기술 풀·구형 결착 표현을 포함함
- `MECH_R18_Submission_Core_System`에는 자원·감응·반복 공략 최신 규칙 직접 병합이 필요함
- `MECH_R18_Skill_Data_Contract`에는 자원·부위·약점·감응 필드 직접 병합이 필요함
- `MECH_R18_Cultist_Submission_Skill_Migration`에는 직접 기술명과 부위 계층 재배정이 필요함
- `SBV_Dom_CruelCommand` 후순위 변종 이동 필요
- `MECH_R18_Mitigation_System` 반복 완화 내성 후보 문구 직접 교체 필요
- `MECH_R18_Skill_Catalog` 제목·frontmatter 버전 불일치
- Skill Catalog 개별 예시의 한글 부위·자세 키와 Memory Log 영문 키 불일치
- 레거시 문서의 과거 29일·30일 설정
- 구형 파일명과 문서 경로 참조
- 미해결 `depends_on`

## Update Rule

이 문서는 프로젝트 진행 상태만 기록한다. 세계관, 시스템 규칙과 밸런스 정의는 각 Wiki 정본 문서가 소유한다.
