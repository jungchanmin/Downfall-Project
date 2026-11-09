> 운영 문서 v0.1.0 · STEP 1–3은 이전 대화에서 운영 기준으로 Director 승인을 받았다. STEP 4의 Director 승인 여부는 별도 근거로 확인한다. 이 문서는 운영 보조 자료이며 Gameplay 정본이나 Owner 지정이 아니다. 상위 Governance와 최신 명시적 Director 지시가 우선한다. GitHub의 PR 상태와 대상 브랜치 반영 여부는 별도로 확인한다.

# Downfall — Review & Handoff Protocol

Version: 0.1.0  
Status: REVIEW (STEP 4의 Director 승인 여부 별도 확인)  
Scope: Task Verification / Closure / Session Recovery  
Parent: Secretary Session Operating Protocol v0.1

## 1. Purpose

본 프로토콜은 작업 결과의 검증, 공식 종료, 세션 간 인수인계 및 중단된 작업의 복구 절차를 정의한다.

기존 AGENTS.md, PROJECT_CHARTER, DOCUMENT_GOVERNANCE 및 CONTEXT_CURRENT의 역할을 변경하지 않는다.

## 2. Core Principles

1. 작업 완료 주장은 검증 증거로 확인한다.
2. 작업자 제출, 검수 통과, 디렉터 승인을 구분한다.
3. 검증되지 않은 사항을 완료로 기록하지 않는다.
4. 미완료 작업의 상태와 복구 지점을 보존한다.
5. 프로젝트 전체 상태와 개별 작업 상태를 구분한다.
6. 정본의 권위와 문서 소유권을 존중한다.
7. 복구에 필요한 정보는 대화 메모리에만 의존하지 않는다.

## 3. Review Responsibilities

### 3.1 Task Owner

담당 작업자는 결과물과 검증 증거를 제출한다.

수행하지 않은 테스트를 수행했다고 기록해서는 안 된다.

### 3.2 Specialist Reviewer

Sol, Codex 또는 해당 영역의 전문 담당자는 지정된 설계·구현·콘텐츠의 전문적인 정합성을 검토한다.

### 3.3 Secretary Session

Secretary Session은 다음을 검수한다.

- 결과물 완전성
- 작업 범위 준수
- Acceptance Criteria 충족 여부
- 필요한 승인 여부
- 검증 증거의 존재와 적합성
- 전문 검수 수행 여부
- 시스템 간 충돌
- 미해결 사항의 처리
- 인수인계 가능성

전문 영역에 대한 독립 검증이 필요한 경우 담당 전문 AI에게 검수를 요청한다.

### 3.4 Director

Director는 승인 권한이 필요한 변경의 최종 결정을 내린다.

Secretary Session의 PASS 판정은 Director 승인을 대체하지 않는다.

## 4. Review Inputs

검수에는 다음 자료를 활용한다.

- Task Contract
- Session Initialization Prompt
- 승인된 Owner / TECH_SPEC
- 담당자의 결과 보고
- 산출물 원문
- 변경 파일 및 Git Diff
- Commit / PR
- 테스트 및 실행 결과
- 전문 검수 보고
- 기존 미해결 사항
- 최신 Director 결정

존재하지 않거나 확인하지 못한 자료는 확인된 것으로 간주하지 않는다.

## 5. Verification Gates

### Gate A — Scope Verification

작업이 승인된 범위 안에서 수행되었는지 확인한다.

### Gate B — Requirement Verification

필수 요구사항과 Acceptance Criteria 충족 여부를 확인한다.

### Gate C — Authority Verification

정본, Candidate, Legacy의 권한을 올바르게 적용했는지 확인한다.

### Gate D — Technical / Creative Verification

해당 전문 담당자의 검토와 필요한 테스트를 확인한다.

### Gate E — Integration Verification

다른 작업과의 충돌, 데이터·인터페이스·문서 영향 범위를 확인한다.

### Gate F — Recovery Verification

작업 결과와 남은 과제를 새로운 세션에서도 재구성할 수 있는지 확인한다.

필수 Gate를 통과하지 못한 작업은 VERIFIED로 처리하지 않는다.

작업 유형에 해당하지 않는 Gate는 N/A로 기록하며, 사유를 명시한다.

## 6. Verification Results

공식 비서 세션 검수 판정:

- PASS
- PASS_WITH_NOTES
- REVISION_REQUIRED
- BLOCKED
- REJECTED

각 판정에는 반드시 판단 근거를 남긴다.

비차단 후속 과제가 존재한다면 담당자와 추적 위치를 명시한다.

## 7. Evidence Policy

다음 증거를 구분한다.

- Reported: 작업자의 주장
- Inspected: 결과물 및 문서 내용 확인
- Tested: 검증 절차를 실제 실행하고 결과 확인
- Approved: 승인권자의 명시적 결정
- Integrated: 승인된 결과가 대상 저장소에 실제 반영됨

하나의 증거 상태가 다른 상태를 자동으로 의미하지 않는다.

Git Commit의 존재는 기능 정상 동작이나 설계 승인을 보장하지 않는다.

PR 생성은 Merge 완료를 의미하지 않는다.

## 8. Handoff Triggers

다음 상황에서는 인수인계를 검토한다.

- 작업 세션 종료 또는 변경
- 장기 작업 중단
- 작업 담당 AI 변경
- 컨텍스트 손실 또는 복구 실패
- 선행 작업 완료 후 다음 담당자로 전환
- 주요 Blocker 발생
- 중요한 승인 결정
- 장기 병렬 작업의 중간 통합

가벼운 작업은 최종 보고만으로 충분할 수 있다.

## 9. Minimum Handoff Package

인수인계에는 다음을 포함한다.

1. Task Identity
2. Current State
3. Source Snapshot
4. Approved Decisions
5. Completed Work
6. Artifacts and Evidence
7. Open Issues
8. Required Approvals
9. Next Action
10. Scope and Safety Constraints

Source Snapshot에는 가능하면 Base Commit, 현재 Head Commit, 브랜치와 관련 Owner 버전을 기록한다.

실제로 검증하지 못한 SHA 또는 파일 버전을 추정해서는 안 된다.

## 10. Recovery Procedure

인수받은 세션은 다음 순서로 복구한다.

1. AGENTS.md의 공식 Read Order를 수행한다 (CONTEXT_CURRENT와 관련 Owner 포함).
2. Task Contract와 Handoff Package를 확인한다.
3. 현재 Git / PR 상태와 승인 결정, 미확정 항목을 재검증한다.
4. 이전 완료 작업의 실제 반영 상태를 확인한다.
5. 불일치 또는 누락 사항을 보고하고 허용 범위에서 재개한다.

인수인계 문서 자체는 Gameplay Rule의 정본이 아니다.

## 11. CONTEXT_CURRENT Update Policy

기존 CONTEXT_CURRENT의 갱신 조건을 따른다.

- 주요 승인 결정
- Phase 변경
- 신규 CURRENT / APPROVED Contract
- 주요 Blocker 생성 또는 해결
- Candidate Promotion
- Next Task 변경

작업별 세부 일지와 모든 대화 기록을 CONTEXT_CURRENT에 축적하지 않는다.

갱신이 필요한 경우 변경 사유와 영향을 먼저 확인하고, 허용된 범위 및 승인 절차에 따라 수행한다.

## 12. Closure Procedure

작업 종료 전 다음을 확인한다.

- 필수 검수 통과
- 필요한 Director 승인 완료
- 요구된 Git 반영 상태 확인
- 후속 작업과 Blocker 이관
- CONTEXT_CURRENT 갱신 필요 여부 처리
- 인수인계 자료 접근 가능 여부 확인

분석·검토만 요구된 작업은 저장소 변경 없이 종료할 수 있다.

코드·문서 반영이 필수인 작업은 결과 제출만으로 CLOSED 처리하지 않는다.

## 13. Context Loss Protocol

세션이 이전 작업을 정확하게 재구성하지 못하면 다음 절차를 따른다.

1. 추측에 기반한 변경 중지
2. 공식 프로젝트 상태 재확인
3. 관련 Owner 재확인
4. 이전 작업 증거 확인
5. 작업 명세 및 승인 범위 재구성
6. 불확실성을 보고
7. 필요한 경우 Director 결정 요청

메모리 부족을 새로운 규칙이나 임의 가정으로 보완하지 않는다.

## 14. Final Principles

**Reported is not Verified.  
Verified is not Approved.  
Approved is not Integrated.  
Integrated is not necessarily Closed.**

완료된 작업은 검증 가능해야 하며, 미완료 작업은 복구 가능해야 한다.
