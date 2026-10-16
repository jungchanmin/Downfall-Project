---
id: GOV_Document_Governance
title: Downfall Documentation Governance
type: governance
authority: CURRENT
status: APPROVED
version: 0.1.0
parent:
  - GOV_Project_Charter
references:
  - SYS_Document_Rules
  - SYS_Wiki_Operations
consumers:
  - GOV_Project_Index
summary: >
  Downfall 프로젝트의 문서 권위, 상태, 소유권, Frontmatter, 검색,
  승격, 분할, 이관, 폐기 및 레거시 관리 규칙을 정의한다.
last_updated: 2026-10-16
---

# Downfall Documentation Governance

## 1. Purpose

본 문서는 Downfall 프로젝트의 공식 문서관리 규칙을 정의한다.

목적은 다음과 같다.

- 현재 기준 문서를 명확하게 식별한다.
- 레거시와 현행 문서의 혼동을 방지한다.
- 하나의 규칙이 여러 문서에 중복 정의되는 것을 방지한다.
- AI가 필요한 문서를 빠르게 탐색할 수 있도록 한다.
- 문서 변경이 다른 시스템에 미치는 영향을 추적한다.
- 기존 프로젝트 자산을 안전하게 점진적으로 이전한다.

본 문서는 게임 규칙 자체를 정의하지 않는다.

게임 규칙은 각 Canon, System Contract, Data 또는 Content 문서가 소유한다.

---

# 2. Core Principle

문서가 저장소에 존재한다는 사실만으로 현재 정본이 되지 않는다.

문서의 사용 가능 여부는 최소한 다음 세 요소로 판단한다.

```text
Authority
+
Lifecycle Status
+
Ownership
```

구현 요구사항으로 직접 사용할 수 있는 문서는 원칙적으로:

```text
Authority = CURRENT
Status = APPROVED
```

조건을 충족해야 한다.

Director의 명시적 지시는 이 규칙보다 우선한다.

---

# 3. Documentation Domains

Downfall의 주요 문서 영역은 다음과 같이 구분한다.

## 3.1 Governance

Location:

`docs/governance/`

소유 내용:

- 프로젝트 운영 원칙
- 문서관리 규칙
- AI 협업 규칙
- 저장소 정책
- 승인 절차

예:

- PROJECT_CHARTER
- DOCUMENT_GOVERNANCE

---

## 3.2 Planning / Development

Location:

`docs/planning/`
`docs/development/`

소유 내용:

- 현재 개발 단계
- 로드맵
- 구현 계획
- 개발 절차
- 기술 운영 정보

이 문서는 게임 정본을 직접 소유하지 않는다.

---

## 3.3 Game Canon / Mechanics / Content

Primary Location:

`Wiki/`

소유 내용:

- 세계관 정본
- 게임 시스템
- DB
- 엔티티
- 이벤트
- 시나리오
- 콘텐츠 규칙

---

## 3.4 Creative Draft Source

Primary Location:

Google Drive / Downfall_Project

또는

`ConfigureBook/`

이 영역은 창작 원안과 등록 전 원고를 보존한다.

검수되지 않은 원고는 구현 정본으로 사용하지 않는다.

---

## 3.5 Technical Implementation

Primary Location:

Git Repository

소유 내용:

- Source Code
- Tests
- TECH_SPEC
- ADR
- Implementation Reports

---

# 4. Authority Classification

모든 중요 문서는 가능한 한 다음 Authority 중 하나를 가진다.

## CURRENT

현재 프로젝트 정본.

현재 설계 또는 구현 판단의 근거로 사용할 수 있다.

단, 실제 구현 요구사항으로 사용하려면 Status도 확인한다.

---

## CURRENT_CANDIDATE

현재 프로젝트 방향과 일치할 가능성이 높지만 Director 승인이 완료되지 않았다.

검토와 신규 설계의 참고자료로 사용할 수 있다.

최종 구현 요구사항으로 직접 사용하지 않는다.

---

## REFERENCE

중요한 설계 자산 또는 참고자료.

아이디어, 구조, 과거 연구, 일부 유효한 규칙을 재사용할 수 있다.

내용 전체를 현재 규칙으로 간주하지 않는다.

---

## LEGACY

과거에는 사용되었지만 현재 정본에서 벗어난 문서.

현재 구현 요구사항으로 사용할 수 없다.

역사와 설계 의도 확인을 위해 보존한다.

---

## UNKNOWN

출처, 최신성, 버전 또는 승계 관계가 확인되지 않았다.

검증 전에는 설계 및 구현의 권위 있는 근거로 사용하지 않는다.

---

## NON_CANON

실험, 폐기, 테스트, 쓰레기통, 임시 생성물 등.

정본 판단에서 제외한다.

예:

`Wiki/Garbage/**`

---

# 5. Lifecycle Status

Authority와 문서의 작업 상태는 별개다.

공식 Lifecycle Status는 다음과 같다.

## DRAFT

초안 작성 단계.

내용이 크게 변경될 수 있다.

---

## REVIEW

검토 중.

구조와 내용에 대한 논의가 진행되고 있다.

---

## APPROVED

Director 또는 정의된 승인 절차를 통과했다.

현재 Authority가 CURRENT라면 구현 기준이 될 수 있다.

---

## IMPLEMENTED

APPROVED된 요구사항이 실제 구현과 연결되어 있다.

IMPLEMENTED는 APPROVED보다 더 높은 권위가 아니라 구현 상태를 나타낸다.

---

## DEPRECATED

현재 사용하지 않는 문서.

대체 문서가 있거나 의도적으로 폐기되었다.

---

# 6. Legacy Content-State Compatibility

기존 Downfall 문서에는 다음과 같은 구형 상태가 존재한다.

```text
draft
wip
complete
deprecated
```

신규 체계에서는 이를 즉시 일괄 변경하지 않는다.

기존 값은 다음과 같이 해석한다.

`draft`

초안임을 의미한다.
신규 체계의 DRAFT와 대체로 호환된다.

`wip`

작성 중임을 의미한다.
Authority와 승인 여부는 별도로 판정해야 한다.

`complete`

문서 작성이 완료되었다는 의미다.

중요:

`complete`는 `APPROVED`와 동일하지 않다.

작성 완료되었더라도 레거시일 수 있다.

`deprecated`

현재 사용하지 않는 문서라는 의미다.
대체로 신규 DEPRECATED와 호환된다.

점진적 Migration 과정에서 신규 Status 체계로 전환한다.

---

# 7. Authority and Status Examples

예:

```text
Authority: CURRENT
Status: APPROVED
```

현재 구현 기준.

---

```text
Authority: CURRENT
Status: REVIEW
```

현재 방향의 문서지만 아직 구현 금지.

---

```text
Authority: REFERENCE
Status: complete (legacy metadata)
```

작성은 완료됐지만 참고자료일 뿐이다.

---

```text
Authority: LEGACY
Status: DEPRECATED
```

과거 기록.

---

```text
Authority: UNKNOWN
Status: complete
```

작성 완료 여부와 관계없이 현재 사용 금지.

---

# 8. Single Ownership

모든 프로젝트 규칙은 하나의 공식 Owner를 가진다.

예:

Combat Flow
→ Combat System

Monster Definition
→ Monster DB

Status Effect
→ Status Effect DB

NPC Stats
→ NPC Stats System

World Canon
→ Project / World Canon

다른 문서는 같은 규칙을 다시 정의하지 않는다.

필요한 경우 Owner 문서를 참조한다.

---

# 9. Ownership Declaration

신규 또는 Migration 완료 문서는 자신이 소유하는 영역을 명확히 해야 한다.

System Contract의 경우 권장 형식:

```text
Owns:
- ...

Does Not Own:
- ...
```

예:

```text
MECH_Combat_Core

Owns:
- Combat lifecycle
- Action resolution
- Victory / retreat resolution

Does Not Own:
- Monster definitions
- Status definitions
- Skill data
```

경계가 모호하면 구현 전 정리한다.

---

# 10. Duplicate Rule Policy

같은 규칙이 여러 문서에서 발견되면 즉시 한 문서를 삭제하거나 덮어쓰지 않는다.

다음 절차를 따른다.

```text
Duplicate Detected
↓
Candidate Owner Identification
↓
Authority Comparison
↓
Conflict Review
↓
Director Approval
↓
Single Owner Assignment
↓
Other Documents Replace Definition With Reference
```

중복 제거 과정에서 원래 의미를 잃지 않도록 한다.

---

# 11. Document Hierarchy

문서는 다음 계층을 따른다.

```text
L0 Governance
L1 Canon / Design
L2 System Contract
L3 Feature / Data Specification
L4 Implementation
```

하위 계층은 상위 계층의 범위를 재정의하지 않는다.

상위 계층에는 하위 구현 세부사항을 과도하게 포함하지 않는다.

---

# 12. Detail Escalation Rule

문서는 아래로 내려갈수록 구체적이어야 한다.

예:

Project Canon:

```text
전투는 생존 문제의 해결 수단 중 하나다.
```

System Contract:

```text
전투는 격파 또는 이탈 결과를 제공한다.
```

Detailed Mechanic:

```text
이탈 판정 조건과 전투 상태 전이.
```

Data:

```text
개별 괴물의 flee requirement 값.
```

Code:

```text
RetreatResolver implementation.
```

상위 문서에 하위 세부사항이 쌓이면 분리를 검토한다.

---

# 13. Document Split Criteria

다음 상황에서는 문서 분리를 검토한다.

- 서로 다른 Owner의 규칙이 한 문서에 섞여 있다.
- Core 규칙과 선택형 Module 규칙이 강하게 혼재한다.
- 개별 데이터가 System Contract를 압도한다.
- 세부 알고리즘 때문에 상위 설명이 읽기 어려워진다.
- 한 영역 변경이 문서 전체를 반복적으로 수정하게 만든다.
- 동일 섹션을 다른 시스템이 독립적으로 참조해야 한다.

문서 크기 자체만으로 분할하지 않는다.

책임 경계가 분할 기준이다.

---

# 14. Module Isolation

선택형 Module은 Core와 분리한다.

원칙:

```text
Core ← Module
```

피해야 할 구조:

```text
Core → Optional Module
```

Core는 선택 Module이 없어도 정상적으로 정의되고 구현될 수 있어야 한다.

Module 전용:

- 데이터
- 상태
- 콘텐츠
- 기술
- 연출

은 가능한 한 Module 소유 문서에서 관리한다.

---

# 15. Document Relationship Metadata

기존 `depends_on` 하나만으로 모든 관계를 표현하는 방식을 점진적으로 대체한다.

권장 관계:

```yaml
parent:
references:
consumers:
```

## parent

현재 문서의 상위 Contract 또는 개념.

## references

현재 문서가 사용하는 외부 규칙 또는 데이터.

## consumers

현재 문서를 직접 사용하는 주요 문서 또는 시스템.

consumers는 완전한 자동 dependency graph를 만들기 위한 것이 아니라 중요한 영향 범위를 빠르게 파악하기 위한 정보다.

---

# 16. Standard Frontmatter

Migration이 완료된 주요 Markdown 문서는 가능한 한 다음 Frontmatter를 사용한다.

```yaml
---
id: MECH_Example
title: Example Document
type: mechanic
authority: CURRENT
status: APPROVED
version: 1.0.0

parent:
  - SYS_Example

references:
  - DATA_Example

consumers:
  - TECH_Example

summary: >
  문서의 역할과 범위를 1~2문장으로 설명한다.

tags:
  - example

keywords:
  - keyword

last_updated: YYYY-MM-DD
---
```

모든 필드를 무조건 요구하지는 않는다.

다만 다음은 중요 문서에서 필수로 본다.

```text
id
title
type
authority
status
summary
last_updated
```

---

# 17. Stable Document ID

문서 ID는 파일 경로보다 안정적인 식별자로 사용한다.

파일을 이동해도 가능하면 ID는 변경하지 않는다.

권장 Prefix:

```text
GOV_       Governance
SYS_       Project / High-level System
MECH_      Gameplay Mechanic
DATA_      Data Definition
CONTENT_   Content
TECH_      Technical Specification
ADR_       Architecture Decision
AI_        AI Collaboration
TMPL_      Template
EVT_       Event
LORE_      Lore
```

기존 ID는 충돌이나 심각한 명명 문제가 없다면 무리하게 변경하지 않는다.

---

# 18. File Naming

신규 기술 및 관리 문서는 영문 파일명을 기본으로 한다.

예:

```text
PROJECT_CHARTER.md
DOCUMENT_GOVERNANCE.md
MECH_Combat_Core.md
DATA_Monster.md
```

본문은 한국어를 기본으로 사용할 수 있다.

파일명 변경은 검색, 링크, 외부 참조에 영향을 줄 수 있으므로 기존 문서는 Migration 과정에서만 변경한다.

---

# 19. Version Policy

Version은 문서의 내용 변경을 추적하기 위한 보조 수단이다.

권장 Semantic Style:

```text
Major.Minor.Patch
```

예:

`1.2.0`

Major:
문서의 핵심 Contract 또는 의미가 변경됨.

Minor:
새 규칙 또는 중요한 내용 추가.

Patch:
의미를 바꾸지 않는 수정, 설명 보완, 오탈자 수정.

Git History가 실제 변경 기록의 최종 출처다.

Version 번호만으로 최신 권위를 판단하지 않는다.

---

# 20. Version Conflict Policy

같은 ID의 문서가 여러 위치 또는 외부 Source에 존재하고 버전이 다를 경우:

자동으로 높은 Version을 정본으로 선택하지 않는다.

다음을 비교한다.

- Git History
- last_updated
- Director 결정
- 현재 Canon
- 다른 문서의 참조
- 변경 내용

확정 전:

```text
Authority: UNKNOWN
```

으로 취급한다.

---

# 21. Searchability Policy

AI와 개발자가 문서를 빠르게 찾을 수 있어야 한다.

주요 문서는:

- 안정적인 ID
- 명확한 Title
- 1~2문장의 Summary
- 적절한 Keywords
- PROJECT_INDEX 등록

을 권장한다.

Summary는 문서 전체를 대신하는 것이 아니라:

> 이 문서를 읽어야 하는가?

를 빠르게 판단하기 위한 정보다.

---

# 22. PROJECT_INDEX Responsibility

`docs/PROJECT_INDEX.md`는 프로젝트 문서 탐색의 기본 진입점이다.

PROJECT_INDEX는 다음을 제공한다.

- Domain
- Primary Owner
- Document ID
- Path
- Authority
- Status
- 주요 관련 문서

PROJECT_INDEX 자체가 게임 규칙을 복제해서는 안 된다.

---

# 23. New Document Creation

신규 문서를 만들기 전에 확인한다.

1. 같은 Owner 역할의 문서가 이미 존재하는가?
2. 기존 문서를 확장하는 것이 더 적절한가?
3. 새로운 책임 경계가 실제로 필요한가?
4. PROJECT_INDEX에서 탐색 가능한가?

불필요한 문서 증식을 피한다.

---

# 24. Migration Policy

기존 문서는 일괄 이전하지 않는다.

Migration은 실제 작업 우선순위에 따라 점진적으로 수행한다.

절차:

1. 기존 문서 조사
2. 최신 Director 결정 확인
3. 관련 문서 조사
4. Authority 판정
5. Single Owner 판정
6. 충돌 목록 작성
7. 신규 구조 제안
8. Director 승인
9. 문서 수정 / 분리 / 이동
10. 참조 갱신
11. PROJECT_INDEX 갱신
12. 검증
13. Commit

---

# 25. Migration Outcomes

기존 문서는 검토 후 다음 중 하나로 처리한다.

## KEEP

현재 구조 그대로 사용.

## PROMOTE

CURRENT 정본으로 승격.

## REFACTOR

내용은 유지하되 책임 경계를 재구성.

## SPLIT

여러 책임을 별도 문서로 분리.

## MERGE

중복 문서를 공식 Owner 문서 하나로 통합.

## LEGACY

역사 자료로 유지.

## DEPRECATE

사용 중단.

## ARCHIVE

활성 탐색 경로에서 제거하고 기록 보관.

---

# 26. ConfigureBook Policy

`ConfigureBook/`은 콘텐츠 원고 영역으로 유지한다.

기본 원칙:

```text
ConfigureBook
= Draft Source

Wiki / Runtime Data
= Registered Source
```

원고를 Wiki 또는 Runtime Data에 등록한 뒤에는 양쪽을 동시에 수정하지 않는다.

등록된 문서가 현재 Authority를 획득했을 경우 원고는 Reference 또는 Archive 후보가 된다.

원고 삭제 또는 이동은 Director 승인 후 수행한다.

---

# 27. Google Drive Creative Source

Google Drive의 Creative 문서는 Argon의 주요 작업 Source다.

Creative Source가 GitHub Canon과 충돌할 경우 자동 병합하지 않는다.

다음 중 하나로 처리한다.

- 신규 Creative Proposal
- Canon Update Candidate
- Conflict

Creative Source는 Codex의 직접 구현 명세가 아니다.

필요한 경우 TECH_SPEC으로 변환한다.

---

# 28. Conflict Protocol

권위 있는 문서 사이의 충돌은 다음 형식으로 보고한다.

```text
CONFLICT

Topic:

Source A:
Authority:
Status:

Source B:
Authority:
Status:

Conflict:

Impact:

Recommended Resolution:

Alternatives:
```

충돌이 unresolved 상태인 영역은 구현을 잠글 수 있다.

---

# 29. Missing Rule Protocol

필수 프로젝트 규칙이 정의되지 않았다면:

```text
UNDEFINED REQUIREMENT
```

으로 보고한다.

다음 내용을 함께 기록한다.

- 무엇이 정의되지 않았는가
- 어떤 시스템이 영향을 받는가
- 구현이 가능한 부분
- 구현을 중단해야 하는 부분
- 결정 가능한 대안

---

# 30. Modification Policy

현재 정본 문서를 수정할 때는 기존 문서의:

- 구조
- 용어
- ID
- 역할

을 가능한 한 보존한다.

단, 새로운 Governance 체계로 Migration하는 작업은 예외적으로 구조 변경을 제안할 수 있다.

이 경우에도 Director 승인 후 수행한다.

---

# 31. Deprecation Policy

문서를 Deprecated 처리할 때는 가능하면 대체 문서를 기록한다.

예:

```yaml
authority: LEGACY
status: DEPRECATED
superseded_by:
  - MECH_New_System
```

대체 문서가 없는 경우 이유를 기록한다.

Deprecated 문서의 본문을 최신 규칙으로 덮어쓰지 않는다.

---

# 32. Archive Policy

Archive의 목적은 삭제가 아니라 활성 탐색 영역에서 분리하는 것이다.

Archive 문서는:

- 기본 구현 자료로 사용하지 않는다.
- PROJECT_INDEX의 Primary Source로 등록하지 않는다.
- 역사 또는 Migration 조사 시 참조할 수 있다.

---

# 33. Change Impact Review

문서를 변경하기 전에 가능한 한 다음을 확인한다.

```text
What owns this rule?
Who references this rule?
Which documents consume it?
Does code depend on it?
Does runtime data depend on it?
Does Creative content depend on it?
```

특히 다음 변경은 영향 조사 없이 수행하지 않는다.

- ID 변경
- System Contract 변경
- Save 관련 데이터
- Public Data Schema
- 핵심 판정 공식
- 시스템 간 인터페이스

---

# 34. Documentation Review Checklist

주요 문서 검토 시 다음 질문을 사용한다.

1. 이 문서는 무엇을 소유하는가?
2. 이 내용은 현재 기준인가?
3. Authority가 명확한가?
4. Status가 명확한가?
5. 상위 문서와 충돌하는가?
6. 다른 문서와 규칙이 중복되는가?
7. 세부 구현이 너무 높은 계층에 있는가?
8. Optional Module이 Core에 침투했는가?
9. 참조 ID 또는 경로가 유효한가?
10. 구현 전에 미정 사항이 남아 있는가?

---

# 35. AI Reading Rule

AI는 모든 프로젝트 문서를 한꺼번에 읽지 않는다.

기본 탐색 순서:

```text
AGENTS.md
↓
PROJECT_CHARTER
↓
PROJECT_INDEX
↓
Relevant Owner Document
↓
Relevant References
↓
TECH_SPEC
```

필요하지 않은 문서는 컨텍스트에 포함하지 않는다.

---

# 36. Codex Implementation Gate

Codex는 일반적으로 다음 조건의 문서를 구현 기준으로 사용한다.

```text
Authority = CURRENT
Status = APPROVED
```

그리고 현재 Task의 TECH_SPEC 또는 Director 지시가 있어야 한다.

REFERENCE, LEGACY, UNKNOWN 문서는:

- 조사
- 비교
- 아이디어 추출

에는 사용할 수 있지만,

그 자체만으로 게임 규칙을 구현해서는 안 된다.

---

# 37. Governance Migration

기존 문서관리 문서:

- `Wiki/00_System/DOCUMENT_RULES.md`
- `Wiki/Wiki_Operations.md`
- `docs/governance/DOCUMENTATION_MIGRATION_PLAN.md`

은 즉시 삭제하지 않는다.

본 Governance 체계가 승인된 후 각각의 유효 규칙을 비교하고:

- 흡수 완료
- 부분 참조
- Legacy 전환

여부를 별도로 판정한다.

---

# 38. Final Principle

문서관리의 목표는 문서 수를 늘리는 것이 아니다.

목표는:

```text
One Rule
→ One Owner
→ One Authoritative Source
```

를 유지하는 것이다.

프로젝트 구성원이 어떤 정보를 찾을 때:

> 어디에 있는지 알 수 있고,
> 어떤 문서를 믿어야 하는지 알 수 있고,
> 누가 그 규칙을 소유하는지 알 수 있어야 한다.