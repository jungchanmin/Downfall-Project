# STEP 5 — ClawLunge 읽기 전용 운영 시험

Version: 0.1.0  
Status: READY FOR TEST, NOT EXECUTED  
Authority: REFERENCE / 시험 명세; Gameplay 정본 아님

목적은 초기화 → 제출 → 비서 검수 → 인수인계의 복구 가능성과 증거 경계를 시험하는 것이다. 아래는 **향후 실행용** 지시문이며 지금 설계 검토가 완료되었다는 뜻이 아니다. 적용 전 이 PR의 반영 상태와 최신 Director 지시를 확인한다. 저장소 기본 브랜치의 상태 및 Owner를 재확인하고 기준 SHA를 고정한다. 작업 세션이 접근 불가 자료를 발견하면 영향을 보고하고 추측하지 않는다.

## 작업 초기화 명세

# DOWNFALL — SESSION INITIALIZATION

## Session Assignment

Project: Downfall

Role: Sol — Design / Review

Task ID: DF-COMBAT-CLAWLUNGE-REVIEW-01 (임시)

Task Name: ClawLunge Recent Action Context Review

Coordinator: Secretary Session

Repository: https://github.com/jungchanmin/Downfall-Project

Base Branch: main

Base Commit: 실행 직전 main의 SHA를 직접 확인해 기록 (초기 참고 스냅샷: 5d1ee18ca0e74cfa29cf4bacacff609195b3a047; 변경되었다면 새 기준으로 재검토)

Working Branch: 없음 (읽기 전용)

Write Scope: 없음; 결과는 세션 응답으로만 제출

Protected Scope: 저장소 전체, 특히 Gameplay Owner / Catalog / 코드 / CONTEXT_CURRENT

Execution Mode: Read-only Investigation / Design Review

## Mission

현재 승인된 SK_ClawLunge의 추격 Eligibility를 유지하면서, 이를 평가하는 데 필요한 최근 교전 및 이동 Context의 소유권과 Runtime 구조를 검토한다.

이번 작업은 새로운 ClawLunge 기능을 설계하거나 수치 밸런스를 조정하는 작업이 아니다.

## Context Recovery

작업 시작 시 다음을 확인한다.

1. AGENTS.md
2. docs/governance/PROJECT_CHARTER.md
3. docs/PROJECT_INDEX.md
4. docs/CONTEXT_CURRENT.md
5. 관련 Owner → CURRENT / APPROVED references → 필요한 Candidate / Reference / Legacy (AGENTS의 공식 Read Order)

거버넌스가 관련되면 DOCUMENT_GOVERNANCE도 확인한다.

이후 PROJECT_INDEX에서 다음 문서의 실제 위치와 Authority를 확인하고 필요한 내용을 읽는다.

- MECH_Combat_Action_System
- MECH_Combat_Action_Runtime_System
- MECH_Combat_Positioning_System
- MECH_Monster_AI
- DATA_Monster_Action_Catalog

각 문서의 현재 버전과 승인 상태를 확인할 것.

## Approved Behavior

CONTEXT_CURRENT에 기록된 다음 의미를 검증 기준으로 사용한다.

- ClawLunge는 일반 Monster Activation에서 선택된다.
- Reaction이 아니다.
- 직전 Player Action 전 유효한 Close 교전 대상이 해당 Action 중 Close → Mid로 이동한 경우 해당 대상에 대해 추격 Eligibility가 유지된다.
- ClawLunge 자체는 양측 Position을 이동시키지 않는다.

실제 확정 근거는 Authoritative Owner와 최신 Director 승인 내역에서 확인한다.

## Review Questions

1. 최근 유효 Close 교전 대상의 Source of Truth는 어디인가?
2. 직전 Player Action에서의 Close → Mid 이동은 어느 시스템이 기록하는가?
3. 행동 실행 전후 상태 중 어떤 시점의 정보를 보존해야 하는가?
4. 최근 Action Context는 언제 생성·갱신·폐기되어야 하는가?
5. 일반 Positioning State와 Action Runtime State 사이의 소유권 충돌은 없는가?
6. Monster AI는 이 Context를 어떤 형태로 읽어 Eligibility를 평가하는가?
7. 기존 Runtime Contract를 확장해야 한다면 최소 변경 범위는 무엇인가?

## Constraints

- 새로운 Gameplay Rule 확정 금지
- 기존 승인 결정 변경 금지
- 수치 Balance 작업 금지
- Catalog의 무단 승격 금지
- 기존 파일 수정 금지
- 코드 구현 금지
- 불명확한 Context를 임의로 가정하지 말 것

## Deliverables

1. Current Contract Summary
2. Context Ownership Analysis
3. Runtime Data / Lifecycle Proposal
4. Alternative Options and Trade-offs
5. Compatibility / Conflict Review
6. Unresolved Requirements
7. Recommended Design
8. Director Decision Required

## Acceptance Criteria

- 기존 ClawLunge 의미가 유지된다.
- 필요한 Context의 생산자·소유자·소비자가 구분된다.
- Runtime 데이터의 생명주기가 분석된다.
- 기존 Owner와의 충돌 여부가 명시된다.
- 확정 사항과 신규 제안이 구분된다.
- 디렉터가 설계 대안을 비교하고 판단할 수 있다.

## Handoff

작업 종료 시 Secretary Session에 제출할 수 있도록 다음을 보고한다.

- 확인한 Owner 문서 및 버전
- 분석 결과
- 추천 구조
- 승인 필요한 결정
- 다른 시스템에 미치는 영향
- 다음 작업 제안

이번 작업에서는 실제 Repository 변경을 수행하지 않는다.

## 운영 시험 및 검수 시나리오

모든 시나리오는 자료를 조작한 가상 제출물 또는 실제 읽기 전용 제출물로 검사한다. 게임 규칙의 새로운 기대 동작을 정의하지 않는다. 각 Gate의 증거 링크·버전, 결과, 확인 주체와 미검증 범위를 기록한다.

| 시나리오 | 입력 / 실행 | 예상 운영 판정 |
|---|---|---|
| 정상 제출 | 확인한 Owner·버전, 승인 의미 근거, 분석 및 제안 구분, 미정 사항, 자료·검증과 인수인계가 모두 제출됨 | A–F 필수 Gate를 실제 검토 후 PASS 또는 비차단 이관이 있으면 PASS_WITH_NOTES. 전문 검수·승인은 별도다. |
| Owner 접근 불가 | 필수 Owner를 읽을 수 없고 대화 요약만 있음 | BLOCKED; 읽었다고 주장하거나 요약을 정본으로 승격하지 않는다. 접근 복구 후 재검수. |
| Candidate를 승인된 규칙으로 취급 | Catalog의 REVIEW 상태를 무시해 확정으로 보고 | REVISION_REQUIRED; Authority Gate 실패, 근거 수정 후 재제출. |
| 승인된 의미와 충돌 | ClawLunge를 반응 행동 또는 양측 이동으로 보고 | REVISION_REQUIRED, 또는 핵심 요구와 근본 충돌 시 REJECTED; Owner와 최신 승인 근거를 대조하고 임의 조정하지 않는다. |
| 승인되지 않은 쓰기 | 읽기 전용 작업에 저장소 변경이 포함됨 | SCOPE_VIOLATION, REVISION_REQUIRED; 변경 증거 보존·보고 후 허용 범위로 시정, 임의 삭제나 병합 금지. |
| 증거 없는 완료 / 미실행 검증 | 작업자가 검증을 주장하나 원문이나 테스트 기록 없음 | 필수 증거가 없으면 BLOCKED 또는 REVISION_REQUIRED; Reported와 Inspected / Tested를 분리한다. |
| 필수 기준 미충족을 비차단으로 분류 | 핵심 Acceptance Criterion이 빠졌는데 PASS_WITH_NOTES 요청 | REVISION_REQUIRED 또는 증거 부족이면 BLOCKED; 필수 기준을 면제하지 않는다. |
| 복구 / 버전 변동 | 인수자가 Task, 소스 SHA, 승인과 미정, 산출물, 다음 단계로 복구; main이 변한 경우 비교 | 이전 기준과 현행 기준을 명시해 재확인한다. 필수 근거가 없으면 BLOCKED; 오래된 결과를 자동 승인하지 않는다. |
| 제출 후 승인 전 | 검수 PASS 및 제안만 존재 | VERIFIED 가능하나 Director 승인이나 Owner 반영은 별개; 설계를 확정 규칙으로 사용하지 않는다. |

### Gate 기록

- A Scope: 읽기 전용 및 보호 범위 준수 증거.
- B Requirements: 명세의 각 완료 기준과 근거.
- C Authority: Owner, Candidate, Legacy, 최신 승인 구분.
- D Specialist: 적합한 전문 검토와 실제 실행 / 미실행 검증.
- E Integration: Runtime / Positioning / AI 사이 충돌과 영향 검토.
- F Recovery: Task, 스냅샷, 결정, 산출물, 미정, 승인, 다음 행동으로 재개 가능한지 확인.

해당하지 않는 Gate는 N/A와 이유를 적는다. 필수 Gate 실패는 VERIFIED가 아니다. 상태와 판정을 별도 기록하며 PASS도 Director 승인을 대신하지 않는다.

## 결과 제출 / 인수인계

[Task Handoff](templates/TASK_HANDOFF.md)를 사용해 Task ID, 현재 상태·판정, Base / Head 및 Owner 확인값, 확인된 결정과 제안, 산출물, 실행·미실행 검증, 미정·충돌·Blocker, 필요한 승인, 다음 행동을 남긴다. 시험은 실제 결과가 제출되고 검수·복구 가능성이 확인되기 전까지 미실행이다. 후속 Batch 3 상세 검토는 필요한 Director 결정 및 Owner 반영 여부를 확인한 뒤 별도 명세로 착수한다.
