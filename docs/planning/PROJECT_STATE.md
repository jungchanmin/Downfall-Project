# Downfall Project State

## Current Phase

**Phase 5N-5: 레이첼 굴복 기술 수직 슬라이스**

Phase 5N-4에서 굴복 전용 생존자 기술의 판별 기준과 Service·Tease·Domination·Absorption·Defiance 작성 규칙을 정본화했다. 현재는 해당 작성 규칙을 레이첼 로페즈와 인간형 광신도에게 실제 적용해 기술 7종, 전투 정체성, 자원·부위·게이트·Bark 계약을 수직 검증하는 단계다.

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
- 굴복도·탈진력·절정도·반복 절정·절정 여운 정본화
- 공격자 효과 우선 결착과 일반전투 수치 패널티 비이관
- 계층형 신체 부위와 약점·감응도 독립 계약
- `Normal / Sensitive / Overstimulated` 감응 단계
- `Exhaustion / Control / ClimaxSensitivity` 약점 유형
- `Unknown / Suspected / Confirmed / Mastered` 약점 공개 단계
- 반복 공략과 보호 행동·비인간형 `SpecialOrgan` 계약
- 생존자 굴복 전용 기술 작성 규칙과 기술 도감 표준 항목

## In Progress

- 레이첼 `CounterGambler` 전투 정체성 수직 검증
- Service 2종: 가슴 주무르기·핸드잡
- Tease 2종: 가슴 유혹·하체 유혹
- Domination 1종: 기승위 역전
- Defiance 1종: 호흡 정돈
- Absorption 1종: FluidPayload 체액 공격 역이용
- 기술별 성공·실패·대실패 자기 절정 비용
- 굴복도 60% 이하 Domination 조건과 반복 사용 통제
- 정면 전용 Tease와 후방 공격 취약성
- 광신도의 광적 신앙 Bark 어휘·출력 조건
- 기본 루프·Domination·Defiance·Absorption 페이퍼 테스트 계획

## Blockers

- 레이첼 기술 최종 표시명 미확정
- 실제 `base_power` 환산 공식 미확정
- 쿨타임의 합·행동 단위 미확정
- 부분 성공 Tease의 실제 경감 범위 미확정
- 탈진력 피해 등급별 최종 상한 미확정
- Absorption 오염·Mutation 장기 공식 미확정
- FluidPayload 광신도 기술의 정식 ID 미확정
- 레이첼 초기 보유 기술과 학습 기술 구분 미확정
- 의복 상태와 부위 접근 Gate 정식 계약 미완료
- 다대일 지원·교대 기술 규칙 미완료
- 기술별 Narration 조건 블록과 Bark DB 미작성
- Unity effect ID 최종 명명 미완료
- 굴복도 성장 획득 경로와 일반 범위 미확정
- 반복 절정 피해의 장기 상한 필요성 미검증
- 전투 후 `ResidualSensitivity` 지속·회복 미확정
- Memory Log·괴물 도감의 약점 공개 승계 미확정

## Next Priorities

1. `MECH_R18_Rachel_Submission_Vertical_Slice` 검토
2. 레이첼 기술 7종 기본 루프 페이퍼 테스트
3. 기승위 역전 반복 사용·실패 비용 테스트
4. 호흡 정돈의 주도권 비용과 다음 반응 +1 테스트
5. FluidPayload 강제 키스와 Absorption 입력·출력 테스트
6. 광신도 광기 Bark의 정보성·반복도·화자 구분 평가
7. 레이첼 기술 최종 표시명 재작명
8. 의복 상태·부위 접근 Gate 정본
9. Combat Narration 조건 블록과 상태 우선순위
10. 광신도 6종 기술에 자원·부위·감응 필드 재배정

## Known Technical Debt

- `MECH_R18_Skill_Data_Contract`의 “기본 기술 5종 전원 사용” 문구는 최신 소유·해금 계약과 충돌하며 직접 개정 필요
- `MECH_R18_Skill_Data_Contract`에는 자원·부위·약점·감응·자기 비용 필드 직접 병합 필요
- 기존 `MECH_R18_Skill_Catalog` 본문은 구형 규칙 문구를 포함하지만 `MECH_R18_Skill_Catalog_Core`가 최신 정본을 소유함
- 기존 광신도 기술 예시는 레거시 필드를 유지하며 신규 마이그레이션 문서가 최신 데이터를 소유함
- 기존 괴물 기술 운용은 랜덤 축 풀 비중이 큼
- 기존 `MECH_Combat_System` SECTION 11은 완전 정보 공개·공용 기술 풀·구형 결착 표현을 포함함
- `MECH_R18_Submission_Core_System`에는 자원·감응·반복 공략 최신 규칙 직접 병합이 필요함
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
