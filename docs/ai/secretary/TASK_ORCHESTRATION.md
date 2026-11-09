> 운영 문서 v0.1 제안 · 이 PR에서 검토 중. STEP 1–3은 이전 대화에서 운영 기준으로 승인되었고, STEP 4와 GitHub 중심 정리는 이번 지시에 따라 반영한다. 저장소 기본 브랜치에 통합되기 전이며 Gameplay 정본, Owner 지정 또는 문서 승격이 아니다. 상위 Governance 및 최신 명시적 Director 지시가 우선한다.

# Downfall — Task Orchestration Protocol

Version: 0.1.0  
Status: PR REVIEW (대화상 v0.1 승인; 저장소 반영 대기)  
Scope: Task Decomposition / Parallel Work / Conflict Control / Integration  
Parent: Secretary Session Operating Protocol v0.1

## 1. Purpose

본 프로토콜은 여러 AI 작업 세션의 효율적인 분배와 통합을 정의한다.

목표는 병렬 작업량의 극대화가 아니라, 프로젝트의 정합성과 복구 가능성을 유지하면서 독립적인 작업을 안전하게 수행하는 것이다.

## 2. Orchestration Lifecycle

모든 다중 세션 작업은 다음 절차를 따른다.

1. INTAKE — 디렉터 요청 접수
2. RECOVERY — 프로젝트 현재 상태 복구
3. DECOMPOSITION — 작업 분해
4. DEPENDENCY REVIEW — 의존성 및 충돌 분석
5. ASSIGNMENT — 담당 세션 및 작업 범위 지정
6. INITIALIZATION — 세션 초기화 프롬프트 생성
7. EXECUTION — 작업 실행
8. COLLECTION — 산출물과 증거 수집
9. INTEGRATION REVIEW — 결과 통합 검수
10. DIRECTOR DECISION — 필요한 승인 요청
11. CLOSEOUT — 승인된 변경 반영 확인 및 인수인계

절차는 작업 규모에 따라 간소화할 수 있지만 검증과 승인 경계를 생략해서는 안 된다.

## 3. Task Classification

### 3.1 Independent

선행 결과를 필요로 하지 않으며, 서로 다른 Owner 또는 독립된 결과물을 다룬다.

병렬 수행을 권장한다.

### 3.2 Read-only Shared

여러 세션이 동일한 자료를 읽거나 분석하되 수정하지 않는다.

병렬 수행할 수 있지만 기준 문서와 버전을 공유해야 한다.

### 3.3 Dependent

다른 작업의 확정된 결과가 필요하다.

선행 결과가 제출되고 필요한 승인까지 완료된 후 진행한다.

### 3.4 Shared Contract

두 작업 이상이 동일한 System Contract, 데이터 계약 또는 공개 인터페이스에 의존한다.

공통 계약을 먼저 확정하거나 작업 범위를 명확히 분리한다.

### 3.5 Shared Files

여러 작업이 동일 파일을 수정한다.

변경 책임을 분리할 수 없으면 순차 진행을 기본으로 한다.

### 3.6 Blocked

필요한 자료·권한·승인·선행 결정이 없다.

차단 원인과 해제 조건을 명시한다.

## 4. Task Identity

각 작업에 고유 식별자를 부여한다.

권장 형식:

DF-[DOMAIN]-[TOPIC]-[SEQUENCE]

예시:

DF-COMBAT-CLAWLUNGE-01

작업 ID는 운영용 식별자이며 기존 Gameplay ID를 변경하지 않는다.

기존 이슈·티켓 ID가 존재하면 새 ID 생성보다 재사용을 우선한다.

## 5. Task Contract

각 작업 명세에는 다음 정보를 포함한다.

- Task ID / Name
- Goal
- Assigned Role
- Source of Truth
- Base Branch / Base Commit
- Read Scope / Write Scope
- Protected Scope
- Approved Constraints
- Dependencies
- Deliverables
- Acceptance Criteria
- Validation Requirements
- Required Approvals
- Handoff Requirements

작업 명세는 기존 정본을 대체할 수 없다.

## 6. Dependency Management

작업 의존성은 DAG(Directed Acyclic Graph)를 기준으로 표현한다.

작업 A의 승인 결과가 작업 B에 필요하면 A → B로 기록한다.

순환 의존성이 발견되면 직접적인 병렬 실행 대신 공통 계약 분리 또는 작업 순서 재설계를 검토한다.

승인이 필요한 미확정 결과는 완료된 선행 조건으로 취급하지 않는다.

## 7. Parallel Execution Safety

병렬 작업 시작 전에 다음을 확인한다.

1. 각 작업의 Base Commit
2. 담당자의 변경 가능 파일
3. 공유 Owner 및 Contract
4. Public ID 및 Data Schema 영향
5. 기존 미병합 작업과의 중복 여부
6. 결과 통합 순서

독립 작업은 별도 브랜치 또는 격리된 작업 공간에서 수행한다.

다른 작업자의 미커밋 변경 사항을 덮어쓰지 않는다.

같은 브랜치를 여러 세션에서 동시에 직접 변경하는 방식은 기본적으로 피한다.

## 8. Change and Conflict Control

충돌을 다음과 같이 구분한다.

- FILE_CONFLICT: 동일 파일 또는 동일 코드 영역 수정 충돌
- CONTRACT_CONFLICT: 인터페이스 및 시스템 책임 충돌
- SEMANTIC_CONFLICT: 문서 간 규칙 해석 충돌
- AUTHORITY_CONFLICT: 정본과 Candidate·Legacy의 혼용
- DEPENDENCY_CONFLICT: 선행 승인 또는 계약 미충족
- VERSION_CONFLICT: 상이한 Base Commit 또는 문서 버전
- SCOPE_VIOLATION: 허용 범위를 벗어난 작업

충돌이 발생하면:

1. 영향을 받는 작업을 식별한다.
2. 충돌한 자료와 기준 버전을 기록한다.
3. 이미 완료된 독립 작업은 보존한다.
4. 충돌 부분의 추가 변경을 중단한다.
5. 해결 대안과 영향을 보고한다.
6. 필요한 디렉터 결정을 요청한다.

승인 없이 정본 충돌을 임의 해소하지 않는다.

## 9. Result Collection

작업자는 다음을 보고한다.

- Task ID
- 수행한 작업
- 변경 파일
- Commit / PR / Diff
- 테스트 및 검증 결과
- 승인된 규칙과의 정합성
- 발생한 문제
- 남은 작업
- 필요한 승인
- CONTEXT_CURRENT 갱신 필요 여부

증거가 없는 완료 주장은 검증 완료로 취급하지 않는다.

## 10. Integration Review

통합 검수는 다음 순서를 따른다.

1. 모든 필수 산출물 수집
2. Task별 Acceptance Criteria 확인
3. 기준 커밋 및 변경 범위 검토
4. 전문 검수 결과 확인
5. 작업 간 Contract 정합성 확인
6. 파일 및 의미적 충돌 확인
7. 테스트·빌드 증거 확인
8. 잔여 위험 및 Blocker 식별
9. 디렉터 승인 요청
10. 승인된 결과의 반영 여부 재확인

비서 세션의 VERIFIED는 공식 승인을 의미하지 않는다.

## 11. Recovery and Handoff

중단된 작업은 다음 정보로 복구한다.

- Task Contract
- 최신 Git 상태
- 승인된 결정
- 제출된 산출물
- 검증 결과
- 미해결 문제
- 다음 작업

GitHub의 CONTEXT_CURRENT는 프로젝트 전체 상태의 기본 체크포인트로 유지한다.

개별 작업의 상세 기록을 CONTEXT_CURRENT에 무제한 축적하지 않는다.

작업 규모에 따라 PR, Issue, ExecPlan 또는 별도 Handoff를 사용한다.

새 기록 방식은 기존 문서와 중복되지 않도록 검토한다.

## 12. Closure Rule

작업은 결과물을 작성했다는 이유만으로 CLOSED가 되지 않는다.

종료 전 확인할 사항:

- 필수 요구사항 충족
- 필요한 검증 완료 또는 한계 명시
- 프로젝트 정합성 확인
- 필요한 디렉터 승인 완료
- 변경 반영 상태 확인
- 후속 작업 및 인수인계 처리

외부 저장소 변경을 요구하지 않는 분석 작업도 최종 결과가 승인되거나 종료 처리되어야 CLOSED로 기록한다.

## 13. Final Principle

Parallelize independent work.

Serialize unresolved decisions.

Preserve authoritative ownership.

Integrate only verified results.

Never confuse task completion with project approval.
