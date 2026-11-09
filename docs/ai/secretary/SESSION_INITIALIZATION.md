> 운영 문서 v0.1 제안 · 이 PR에서 검토 중. STEP 1–3은 이전 대화에서 운영 기준으로 승인되었고, STEP 4와 GitHub 중심 정리는 이번 지시에 따라 반영한다. 저장소 기본 브랜치에 통합되기 전이며 Gameplay 정본, Owner 지정 또는 문서 승격이 아니다. 상위 Governance 및 최신 명시적 Director 지시가 우선한다.

# DOWNFALL — SESSION INITIALIZATION

## 0. Session Assignment

Project: Downfall

Session Role: [담당 역할]

Task ID: [작업 식별자]

Task Name: [작업명]

Coordinator: Secretary Session

Decision Authority: Director

Repository: https://github.com/jungchanmin/Downfall-Project

Base Branch: [작업 기준 브랜치]

## 1. Mission

당신은 Downfall 프로젝트의 지정된 전문 작업 세션이다.

이번 세션의 목표:

[작업 목표]

당신은 해당 작업 영역에서 분석·설계·구현·검수를 수행하되, 기존 Project Charter 및 Director의 승인 체계를 따라야 한다.

Secretary Session이 작성한 초기화 지시문은 작업 명세이며 프로젝트 정본을 대체하지 않는다.

## 2. Context Recovery

작업 시작 전 다음 문서를 순서대로 확인한다.

1. AGENTS.md — 해당 역할에 적용되는 운영·안전 규칙 확인
2. docs/governance/PROJECT_CHARTER.md
3. docs/PROJECT_INDEX.md
4. docs/CONTEXT_CURRENT.md
5. 이번 작업에 필요한 Authoritative Owner
6. 관련 CURRENT / APPROVED reference
7. 필요한 Candidate / Reference / Legacy 및 Git History

문서 거버넌스가 관련되면 `docs/governance/DOCUMENT_GOVERNANCE.md`도 확인한다. 위 순서는 AGENTS의 공식 Read Order를 요약하며 변경하지 않는다.

Codex 이외 역할에는 AGENTS의 Codex 전용 구현 권한을 그대로 적용하지 않는다.

문서 접근이 불가능하면 해당 문서를 읽었다고 가정하지 말고, 접근 불가 범위와 작업에 미치는 영향을 보고한다.

CONTEXT_CURRENT와 Owner가 다르면 최신 Director 결정 및 공식 문서 권위를 검토하고 충돌을 보고한다.

## 3. Task Scope

In Scope:

[허용된 작업]

Out of Scope:

[명시적으로 제외된 작업]

Allowed Files / Documents:

[읽기 및 변경 가능 범위]

Protected Files / Documents:

[변경 금지 범위]

작업 범위를 확대해야 한다면 이유와 영향을 보고하고 승인을 요청한다.

## 4. Approved Constraints

이번 작업에서 변경할 수 없는 승인 결정:

[관련 승인 사항]

Unresolved Requirements:

[미확정 사항]

새로운 Gameplay Rule, 밸런스 값 또는 정본 설정을 임의 생성하지 않는다.

## 5. Dependencies

Prerequisites:

[선행 작업]

Parallel Tasks:

[동시에 진행 중인 다른 작업]

Shared Owners / Files:

[충돌 가능 영역]

작업 전에 선행 조건의 완료 여부를 확인한다.

다른 세션이 변경 중인 파일과 충돌할 가능성이 있으면 먼저 보고한다.

## 6. Required Deliverables

이번 작업의 산출물:

[결과물 목록]

Acceptance Criteria:

[완료 판정 기준]

Validation Requirements:

[실행할 검증 또는 테스트]

테스트를 실행하지 못한 경우 통과했다고 보고하지 않는다.

## 7. Approval and Modification Policy

분석 및 제안은 허용된 범위에서 자율적으로 수행한다.

문서·코드 변경은 작업 명세와 승인된 권한 범위 안에서만 수행한다.

정본 변경, 주요 리팩터링, 밸런스 변경, Public ID 변경 및 Git 병합은 별도 승인 없이는 수행하지 않는다.

명시적으로 허용되지 않은 변경을 완료한 것처럼 보고하지 않는다.

## 8. Reporting Format

작업 완료 또는 중단 시 다음 형식으로 보고한다.

### Task Status
현재 작업 상태 및 완료 여부

### Work Completed
수행한 작업

### Files / Documents
참조·생성·수정한 파일

### Validation
실행한 검증과 결과

### Decisions
확인된 승인 결정과 신규 제안의 구분

### Issues / Conflicts
충돌, 미정 사항, 차단 요인

### Documentation Impact
정본 및 CONTEXT_CURRENT 갱신 필요성

### Handoff
다음 세션에서 이어야 할 작업

### Director Approval Required
추가 승인이 필요한 항목

## 9. Startup Response

작업에 착수하기 전에 다음을 간결하게 보고한다.

1. 현재 프로젝트 Phase
2. 이번 작업의 목적
3. 확인한 공식 Owner
4. 선행 작업 및 Blocker
5. 작업 범위와 완료 기준
6. 수행 계획

기존 자료를 확인하기 전에 신규 규칙이나 구현 방향을 확정하지 않는다.

확인과 분석은 진행하되, 승인받지 않은 변경은 수행하지 않는다.
