---
id: GOV_Project_Charter
title: Downfall Project Charter
type: governance
authority: CURRENT_CANDIDATE
status: REVIEW
version: 0.1.0
summary: >
  Downfall 프로젝트의 최상위 운영 헌법.
  프로젝트 목표, 의사결정 권한, AI 역할 분담, Source of Truth,
  문서 계층, 모듈 소유권, 변경 승인 원칙과 개발 철학을 정의한다.
---

# Downfall Project Charter

## 1. Purpose

본 문서는 Downfall 프로젝트의 최상위 운영 헌법이다.

이 문서는 게임의 개별 규칙이나 수치, 콘텐츠 내용을 정의하지 않는다.

대신 다음을 정의한다.

- 프로젝트의 최우선 목표
- 의사결정 권한
- AI 개발팀 역할
- Source of Truth
- 문서 계층
- 시스템 소유권 원칙
- 변경 승인 원칙
- 레거시 문서 처리
- 개발 및 구현 철학

세부 게임 규칙은 반드시 하위 문서가 소유한다.

---

# 2. Project Identity

Project Name:

Downfall

Project Category:

Survival RPG / TRPG-inspired simulation game

Primary Engine:

Unity

Primary Language:

C#

Primary Development Platform:

Windows

Primary Version Control:

Git / GitHub

Downfall은 장기적인 개발과 상용화를 목표로 하는 프로젝트다.

프로토타입의 빠른 완성보다 장기적인 일관성과 유지보수성을 우선한다.

---

# 3. Project Priority

Downfall의 모든 개발 및 설계 판단은 다음 우선순위를 따른다.

1. 프로젝트의 완성도
2. 설정 및 시스템의 일관성
3. 장기적인 유지보수성과 확장성
4. 플레이어 경험
5. 개발 효율성

두 목표가 충돌할 경우 상위 목표를 우선한다.

개발 속도는 중요하지만 구조적 부채를 정당화하는 근거가 될 수 없다.

---

# 4. Director Authority

Downfall의 최종 결정권자는 Director다.

Director는 다음 사항에 대한 최종 권한을 가진다.

- 프로젝트 방향
- 게임 디자인
- 세계관 정본
- 캐릭터 정본
- 밸런스
- 시스템 경계
- 기능 우선순위
- 프로젝트 범위
- 주요 기술 결정 승인
- 문서의 정본 승격 또는 폐기
- 상용화 방향

AI는 분석, 제안, 검토 및 구현을 담당하지만 최종 승인권을 갖지 않는다.

---

# 5. AI Development Team

Downfall은 여러 AI 시스템을 역할별로 분리해 사용한다.

각 AI는 자신에게 할당된 영역에 집중하며 다른 영역의 권한을 침범하지 않는다.

---

## 5.1 Argon — Creative Lead

Argon은 창작 영역을 담당한다.

주요 책임:

- 세계관
- 시나리오
- 캐릭터
- NPC
- 몬스터 콘셉트
- 대사
- 이벤트
- 로어
- 내러티브 연출

Argon은 다음을 정의한다.

- Creative Intent
- Narrative Intent
- Character Intent
- Gameplay Fantasy

Argon은 기술 아키텍처를 결정하지 않는다.

---

## 5.2 Sol — Design / Review / Coordination

Sol은 설계 검수 및 AI 간 중재를 담당한다.

주요 책임:

- 설정 정합성 검토
- 시스템 설계 검토
- 문서 구조 관리
- Creative → Technical Requirement 변환
- Architecture Review
- Data Contract Review
- 구현 결과 검수
- 문서 충돌 탐지
- 프로젝트 방향과 구현 사이의 연결

Sol은 필요 시 Creative Specification을 Technical Specification으로 변환한다.

Sol은 Director의 판단을 대체하지 않는다.

---

## 5.3 Codex — Technical Lead / Implementation

Codex는 실제 기술 구현을 담당한다.

주요 책임:

- Repository 조사
- Unity 구현
- C# 구현
- 기술 설계
- 리팩터링
- 디버깅
- 테스트
- 성능 분석
- 개발 도구 제작
- 코드 리뷰
- 기술 문서화

Codex는 승인된 기능 범위 내에서 HOW를 결정할 수 있다.

Codex는 WHAT 또는 WHY를 독립적으로 변경할 수 없다.

---

# 6. Source of Truth

Downfall은 하나의 저장소가 모든 종류의 정보를 소유하지 않는다.

정보의 성격에 따라 Source of Truth를 분리한다.

---

## 6.1 Creative Source of Truth

Primary:

Google Drive / Downfall_Project

주요 대상:

- 세계관
- 시나리오
- 캐릭터
- NPC
- 몬스터 Creative Design
- 대사
- 이벤트 원안
- 로어

Creative Source는 창작 의도를 정의한다.

Creative Source는 구현 아키텍처를 직접 정의하지 않는다.

---

## 6.2 Technical Source of Truth

Primary:

Git / GitHub Repository

주요 대상:

- Governance
- System Contracts
- Architecture
- Technical Specifications
- Source Code
- Tests
- ADR
- Implementation Reports

기술 구현은 승인된 Technical Source를 기준으로 수행한다.

---

# 7. Documentation Hierarchy

Downfall 문서는 다음 계층으로 관리한다.

```text
L0 Governance
↓
L1 Project Canon / Design
↓
L2 System Contract
↓
L3 Feature / Data Specification
↓
L4 Code / Tests / Runtime Content
```

상위 문서는 하위 문서보다 높은 개념적 권위를 가진다.

상위 문서는 방향과 불변 규칙을 정의한다.

하위 문서는 세부 규칙과 구현을 정의한다.

---

# 8. L0 — Governance

Governance 문서는 프로젝트 운영 방식을 정의한다.

대표 문서:

- AGENTS.md
- PROJECT_CHARTER.md
- DOCUMENT_GOVERNANCE.md
- PROJECT_INDEX.md

Governance는 게임 규칙을 직접 정의하지 않는다.

---

# 9. L1 — Project Canon / Design

Project Canon은 Downfall의 정체성과 불변 규칙을 정의한다.

예:

- 게임의 기본 전제
- 세계관 핵심 규칙
- 플레이어의 역할
- 25일 구조
- 핵심 디자인 필러

Project Canon에는 구현 알고리즘이나 세부 밸런스 값을 넣지 않는다.

---

# 10. L2 — System Contract

System Contract는 각 게임 시스템의 책임과 경계를 정의한다.

예:

- Combat
- NPC
- Time
- Event
- Inventory
- Resource
- Save
- Relationship

System Contract는 다음을 정의한다.

- 시스템 목적
- 시스템 책임
- 입력
- 출력
- 상태 소유권
- 다른 시스템과의 계약
- 시스템이 소유하지 않는 영역

System Contract는 가능한 한 세부 데이터와 구현 알고리즘을 소유하지 않는다.

---

# 11. L3 — Feature / Data Specification

이 계층은 구체적인 규칙과 데이터를 소유한다.

예:

- Monster Database
- Skill Database
- Status Effect Database
- Quirk Database
- Item Database
- Feature TECH_SPEC

세부 수치, ID, 조건, 지속시간, 성공 기준 등은 이 계층에서 관리한다.

---

# 12. L4 — Code / Tests

실제 구현 계층.

포함:

- Unity
- C#
- Automated Tests
- Runtime Data
- Editor Tooling

코드는 승인된 상위 계약과 Technical Specification을 구현한다.

코드가 게임 디자인 정본을 독립적으로 정의하지 않는다.

---

# 13. Single Ownership Principle

하나의 규칙에는 하나의 Owner만 존재해야 한다.

같은 규칙을 여러 문서에서 중복 정의하지 않는다.

예:

Combat owns:
- Combat flow
- Combat resolution

Status Effect DB owns:
- Status definitions

Monster DB owns:
- Monster definitions

Monster AI owns:
- Monster decision behavior

Skill DB owns:
- Reusable skill definitions

NPC System owns:
- NPC runtime behavior

다른 문서는 해당 Owner의 규칙을 참조만 한다.

---

# 14. No Circular Ownership

문서와 시스템은 가능한 한 단방향 의존 구조를 가진다.

권장:

```text
Project Canon
↓
System Contract
↓
Data / Feature Spec
↓
Implementation
```

피해야 할 구조:

```text
Combat ↔ Monster ↔ Skill ↔ Combat
```

상호 의존이 필요한 경우 공통 Contract 또는 별도 Data Owner를 만든다.

---

# 15. Document Relationship Types

향후 문서 관계는 하나의 `depends_on` 필드에 모두 넣지 않는다.

가능하면 다음 관계를 구분한다.

```yaml
parent:
references:
consumers:
```

parent:

상위 개념 또는 소유권 문서.

references:

현재 문서가 사용하는 외부 규칙 또는 데이터.

consumers:

현재 문서를 사용하는 주요 시스템 또는 문서.

---

# 16. Document Authority

문서의 존재 자체는 권위를 의미하지 않는다.

문서는 다음 Authority 중 하나를 가진다.

CURRENT

현재 정본이며 구현 기준으로 사용할 수 있다.

CURRENT_CANDIDATE

현재 방향과 일치하지만 Director 검토가 필요한 문서.

REFERENCE

중요한 설계 자료지만 그대로 구현 요구사항으로 사용할 수 없다.

LEGACY

과거 기준.

신규 설계의 직접 근거로 사용하지 않는다.

UNKNOWN

버전, 출처 또는 승계 관계가 불명확하다.

확인 전 구현 근거로 사용하지 않는다.

NON_CANON

실험, 폐기 또는 정본이 아닌 자료.

---

# 17. Document Status

Authority와 별개로 문서는 작업 상태를 가진다.

DRAFT

작성 중.

REVIEW

검토 중.

APPROVED

Director 또는 지정된 승인 절차를 통해 승인됨.

IMPLEMENTED

승인된 요구사항이 구현됨.

DEPRECATED

더 이상 사용하지 않음.

일반적으로 구현 요구사항은 다음 조건을 충족해야 한다.

```text
Authority = CURRENT
Status = APPROVED
```

예외는 Director의 명시적 지시가 있을 때만 허용한다.

---

# 18. Progressive Migration Policy

기존 Downfall 문서를 일괄 재구성하지 않는다.

기존 자료는 중요한 프로젝트 자산으로 취급한다.

문서는 실제 작업이 필요할 때 다음 절차로 이전한다.

```text
Existing Document
↓
Review
↓
Authority Classification
↓
Conflict Detection
↓
Ownership Assignment
↓
Director Approval
↓
Migration / Refactoring
```

대규모 폴더 이동이나 일괄 이름 변경은 피한다.

---

# 19. Legacy Policy

LEGACY는 삭제 대상과 동일하지 않다.

레거시 문서는 다음 목적으로 보존할 수 있다.

- 과거 설계 의도 확인
- 폐기된 방향 분석
- 신규 설계 비교
- 결정 과정 추적

하지만 LEGACY 문서는 현재 구현 요구사항으로 사용할 수 없다.

---

# 20. Conflict Policy

두 개 이상의 권위 있는 문서가 충돌하는 경우 임의 병합하지 않는다.

다음 형식으로 보고한다.

```text
CONFLICT

Source A:
Source B:

Conflict:

Impact:

Possible Resolutions:

Recommended Resolution:
```

최종 판단은 Director가 수행한다.

---

# 21. Undefined Requirement Policy

프로젝트 고유 규칙이 정의되지 않은 경우 일반적인 게임 개발 지식으로 임의 보완하지 않는다.

다음과 같이 표시한다.

```text
UNDEFINED REQUIREMENT
```

기술적 구현 세부사항은 기존 시스템과 플레이 경험을 변경하지 않는 범위에서 합리적으로 결정할 수 있다.

---

# 22. Change Approval

다음 변경은 Director의 승인을 요구한다.

- Project Canon 변경
- System Contract 변경
- 게임 규칙 변경
- Balance 변경
- Character 변경
- World Lore 변경
- Public ID 변경
- Save Format 변경
- 대규모 Architecture 변경
- 대규모 Refactoring
- 문서 대규모 이동
- 기존 Source of Truth 대체

작은 구현 세부사항은 승인된 기능 범위 내에서 Codex가 자율적으로 결정할 수 있다.

---

# 23. Guarded Autonomy

Downfall은 AI 개발 속도를 적극 활용한다.

Codex는 승인된 기능 경계 안에서 능동적으로 구현할 수 있다.

허용 예:

- Helper Class
- Interface
- Validation
- Automated Test
- Editor Utility
- Small Internal Refactor
- Debugging Tool

금지 예:

- 새로운 게임 규칙 발명
- 디자인 방향 변경
- 시스템 범위 확장
- 플레이어 경험을 변화시키는 임의 기능 추가

원칙:

> Move quickly inside clear boundaries.

---

# 24. Development Philosophy

Downfall은 빠른 기능 양산보다 재사용 가능한 시스템 기반을 우선한다.

권장 개발 흐름:

```text
Director Intent
↓
Relevant Source
↓
System / Design Review
↓
TECH_SPEC
↓
Codex Investigation
↓
Implementation
↓
Test
↓
Diff Review
↓
Director / Sol Review
↓
Commit
```

복잡한 기능은 계획 후 구현한다.

작은 기능은 과도한 문서화 없이 구현할 수 있다.

---

# 25. Vertical Slice Principle

초기 개발에서는 모든 기능을 동시에 완성하지 않는다.

각 핵심 시스템은 작은 Feature Seed부터 구축한다.

예:

- Combat
- NPC
- Time
- Event
- Inventory
- Save

이후 최소한의 end-to-end 플레이 흐름으로 연결한다.

검증된 패턴을 기반으로 확장한다.

---

# 26. Module Boundary

선택형 또는 확장형 기능은 Core 시스템과 분리할 수 있어야 한다.

Core 시스템은 특정 선택 모듈이 없어도 정상 작동해야 한다.

모듈은 Core Contract를 사용한다.

Core가 선택 모듈에 직접 의존하는 구조는 피한다.

---

# 27. Technical Quality

기술적 결정은 다음 기준을 우선한다.

1. Correctness
2. Maintainability
3. Clear Ownership
4. Testability
5. Extensibility
6. Performance
7. Development Convenience

성능 최적화는 실제 필요가 확인되기 전에 시스템 복잡도를 증가시키는 근거가 되지 않는다.

---

# 28. Documentation Quality

문서는 가능한 한 다음 질문 중 하나에 명확하게 답해야 한다.

- 프로젝트는 무엇인가?
- 이 시스템의 책임은 무엇인가?
- 이 데이터는 무엇을 정의하는가?
- 이번 기능은 무엇을 구현하는가?
- 왜 이 기술 결정을 했는가?

하나의 문서가 여러 역할을 동시에 수행하기 시작하면 분리 여부를 검토한다.

---

# 29. Searchability

모든 주요 문서는 안정적인 ID를 가져야 한다.

권장 prefix:

```text
GOV_      Governance
SYS_      Project/System
MECH_     Gameplay Mechanic
DATA_     Data Definition
CONTENT_  Game Content
TECH_     Implementation Specification
ADR_      Architecture Decision Record
AI_       AI Collaboration
```

파일명, ID, 문서 내부 참조는 가능한 한 일관되게 유지한다.

---

# 30. Current Migration State

Downfall은 현재 기존 기획 자산을 새로운 개발환경에 통합하는 단계다.

기존 GitHub Wiki에는:

- 현행 설계
- 개선이 필요한 설계
- 레거시 자료
- 중간 작업물
- 미확정 자료

가 혼재한다.

따라서 기존 문서를 존재한다는 이유만으로 구현 기준으로 사용하지 않는다.

새 문서 통합관리 체계에 따라 점진적으로 검증한다.

---

# 31. Final Principle

Downfall의 문서와 코드는 다음 흐름을 따라야 한다.

```text
Intent
↓
Ownership
↓
Contract
↓
Specification
↓
Implementation
↓
Verification
```

상위 계층은 안정적이어야 한다.

세부 구현은 하위 계층으로 내려갈수록 구체화되어야 한다.

상위 문서에 세부 구현 규칙을 축적하지 않는다.

좋은 프로젝트 구조는 많은 문서를 만드는 것이 아니라,

각 정보가 정확히 한 곳에 존재하고
필요할 때 쉽게 찾을 수 있는 구조를 만드는 것이다.