---
id: GOV_Project_Index
title: Downfall Project Documentation Index
type: governance
authority: CURRENT
status: APPROVED
version: 0.2.0

parent:
  - GOV_Project_Charter

references:
  - GOV_Document_Governance

summary: >
  Downfall 프로젝트의 공식 문서 탐색 진입점.
  각 도메인의 Primary Owner, 경로, Authority, Status와 관련 문서를 기록하여
  AI와 개발자가 올바른 Source를 찾도록 한다.

last_updated: 2026-10-16
---

# Downfall Project Documentation Index

## 1. Purpose

본 문서는 Downfall 프로젝트 문서의 공식 탐색 지도다.

이 문서는 게임 규칙 자체를 정의하지 않는다.

다음 질문에 답하는 것이 목적이다.

- 어떤 문서를 먼저 읽어야 하는가?
- 현재 문서 중 무엇이 정본인가?
- 무엇은 참고자료인가?
- 무엇은 레거시인가?
- 특정 규칙의 Owner는 누구인가?

세부 규칙은 각 Owner 문서가 소유한다.

---

# 2. Mandatory Reading Order

Codex 또는 다른 기술 AI가 프로젝트 작업을 시작할 때 기본 탐색 순서는 다음과 같다.

```text
AGENTS.md
↓
PROJECT_CHARTER
↓
PROJECT_INDEX
↓
Relevant Primary Owner
↓
Relevant References
↓
TECH_SPEC
```

모든 Wiki 문서를 한꺼번에 읽지 않는다.

---

# 3. Authority Safety Rule

본 Index에서 명시적으로 판정되지 않은 기존 프로젝트 문서는 기본적으로 다음과 같이 취급한다.

```text
Authority: UNKNOWN
```

이는 문서가 잘못되었다는 의미가 아니다.

아직 현재 프로젝트 기준으로 검증되지 않았다는 의미다.

검토되지 않은 문서를 구현 요구사항으로 직접 사용해서는 안 된다.

---

# 4. Implementation Gate

일반적으로 Codex가 직접 구현 기준으로 사용할 수 있는 문서는:

```text
Authority = CURRENT
Status = APPROVED
```

조건을 충족해야 한다.

다음 Authority는 구현 요구사항으로 직접 사용할 수 없다.

```text
CURRENT_CANDIDATE
REFERENCE
LEGACY
UNKNOWN
NON_CANON
```

Director가 특정 Task에 대해 명시적으로 예외를 승인할 수 있다.

---

# 5. Governance

## Project Instructions

ID:

`AGENTS`

Path:

`/AGENTS.md`

Authority:

CURRENT

Status:

APPROVED

Purpose:

Codex의 역할, 자율권, 조사·구현·테스트·Git 안전 규칙을 정의한다.

Use for:

모든 Codex 작업.

---

## Project Charter

ID:

`GOV_Project_Charter`

Path:

`docs/governance/PROJECT_CHARTER.md`

Authority:

CURRENT

Status:

APPROVED

Purpose:

Downfall 프로젝트의 최상위 운영 헌법.

Owns:

- 프로젝트 개발 우선순위
- 의사결정 권한
- AI 역할
- Source of Truth
- 문서 계층
- 개발 철학

---

## Documentation Governance

ID:

`GOV_Document_Governance`

Path:

`docs/governance/DOCUMENT_GOVERNANCE.md`

Authority:

CURRENT

Status:

APPROVED

Purpose:

문서 Authority, Status, Ownership, Frontmatter, Migration 및 Archive 정책.

Owns:

- 문서 권위 판정법
- 문서 Lifecycle
- Single Ownership
- Migration 절차
- 문서 검색 규칙

---

# 6. Project Canon and Design

## Project Canon

ID:

`SYS_Project_Canon`

Path:

`Wiki/00_System/PROJECT_CANON.md`

Authority: CURRENT
Status: APPROVED
Version: 1.0.0
Audit Result: PROMOTE / REFACTOR COMPLETE
Purpose: Downfall의 프로젝트 정의, 플레이어 전제와 고정 세계 규칙.

---

## Design Pillars

ID:

`SYS_Design_Pillars`

Path:

`Wiki/00_System/DESIGN_PILLARS.md`

Authority: CURRENT
Status: APPROVED
Version: 1.0.0
Audit Result: PROMOTE / REFACTOR COMPLETE
Purpose: Downfall의 핵심 플레이 경험과 디자인 우선순위를 정의한다.

---

# 7. Legacy Project Manifest

## Context Manifest

ID:

`SYS_Manifest`

Path:

`Wiki/ConText_Manifest.md`

Authority:

LEGACY

Legacy Status:

complete

Reason:

현재 프로젝트와 충돌하는 과거 설계가 존재한다.

Known conflict example:

- 과거 29일 구조
- 일부 과거 NPC 권한 및 시스템 철학

Usage:

역사적 설계 의도와 과거 시스템 이해에만 사용한다.

Implementation:

PROHIBITED as current implementation authority.

---

# 8. Documentation Legacy Governance

## Old Document Rules

ID:

`SYS_Document_Rules`

Path:

`Wiki/00_System/DOCUMENT_RULES.md`

Authority:

REFERENCE

Legacy Status:

draft

Purpose:

기존 Wiki/docs 역할, 문서 Ownership, Core/Module 분리 및 Migration 원칙.

Notes:

유효한 원칙 상당수가 `GOV_Document_Governance`에 흡수되었다.

Future:

흡수 확인 후 LEGACY 또는 DEPRECATED 전환 검토.

---

## Old Wiki Operations

ID:

`SYS_Wiki_Operations`

Path:

`Wiki/Wiki_Operations.md`

Authority:

REFERENCE

Legacy Status:

complete

Purpose:

기존 Frontmatter 생성 및 Wiki Index 운영 규칙.

Notes:

기존 `draft / wip / complete / deprecated` 상태 체계를 사용한다.

신규 Governance의 Authority / Lifecycle 체계와 의미가 다르므로 직접 적용하지 않는다.

---

# 9. Combat Domain

## Combat System

ID:

`MECH_Combat_System`

Path:

`Wiki/01_Mechanics/MECH_Combat_System.md`

Authority:

REFERENCE

Legacy Status:

wip

Version:

0.3.6

Review Flag:

REWORK_REQUIRED

Purpose:

기존 Downfall 전투 시스템의 주요 설계 자산.

Valuable concepts include:

- 역할 기반 전투 행동
- 격파 / 이탈 복수 해결 경로
- 거리
- Swarm
- 약점
- 전조
- 상태 기반 전투
- 데이터 중심 Skill / Monster 연계

Known Conflict:

기존 d6 성공 풀 판정 구조가 최신 프로젝트 판정 방향과 충돌한다.

Known Structural Issue:

Core Combat, 세부 계산, Monster 연계, Skill, Status 및 Optional Module 규칙이 한 문서에 과도하게 결합되어 있다.

Implementation:

BLOCKED as direct implementation specification.

Planned Direction:

기존 설계 가치를 보존하면서 향후 System Contract와 세부 문서로 분리 검토.

---

# 10. Monster Domain

## Monster Database

ID:

`MONSTER_DB`

Path:

`Wiki/03_Entities/Monsters/MONSTER_DB.md`

Authority:

REFERENCE

Legacy Status:

wip

Version:

0.2.5

Purpose:

괴물 분류, Archetype, 개체 데이터, AI Profile 연결 및 Monster 콘텐츠 구조.

Strong Candidate Ownership:

- Monster identifiers
- Monster classification
- Monster definition
- Monster-specific properties

Does Not Automatically Own:

- Combat resolution
- Shared Skill definition
- Status definition
- AI decision algorithm

Review Notes:

데이터 중심 구조는 재사용 가치가 높다.

Combat 및 다른 WIP 시스템과 연결된 세부 수치와 규칙은 재검증이 필요하다.

---

# 11. NPC Domain

## NPC Stats System

ID:
MECH_NPC_Stats_System

Path:
Wiki/01_Mechanics/MECH_NPC_Stats_System.md

Authority: CURRENT
Status: APPROVED
Version: 2.0.0
Audit Result: REFACTOR COMPLETE

Purpose:
NPC의 현재 상태, 능력, 사회·행동 상태 및 기본 성격 데이터의 의미와 소유 경계를 정의한다.


---

# 12. Time Domain

## Time System

ID:

`Time_System`

Path:

`Wiki/01_Mechanics/Time_System.md`

Authority:

UNKNOWN

Status:

UNREVIEWED

Purpose:

게임 시간 및 Phase 진행 관련 기존 시스템 문서.

Next Review:

Core Gameplay Audit 대상.

---

# 13. Resource Domain

## Resource System

ID:

`MECH_Resource_System`

Path:

`Wiki/01_Mechanics/MECH_Resource_System.md`

Authority:

UNKNOWN

Status:

UNREVIEWED

Next Review:

Core Gameplay Audit 대상.

---

# 14. Monster AI Domain

## Monster AI

ID:

`MECH_Monster_AI`

Path:

`Wiki/01_Mechanics/MECH_Monster_AI.md`

Authority:

UNKNOWN

Status:

UNREVIEWED

Purpose:

Monster 행동 결정 규칙.

Notes:

Monster Definition과 AI Decision Logic의 Ownership 분리 여부를 검토해야 한다.

---

# 15. Skill Domain

## General Skill Catalog

ID:

`MECH_Skill_Catalog`

Path:

`Wiki/01_Mechanics/MECH_Skill_Catalog.md`

Authority:

UNKNOWN

Status:

UNREVIEWED

Likely Ownership:

공유 가능한 Skill Definition.

Requires Review:

Combat과 중복 정의 여부.

---

# 16. Status Effect Domain

## Status Effect Database

ID:

`MECH_Status_Effect_DB`

Path:

`Wiki/01_Mechanics/MECH_Status_Effect_DB.md`

Authority:

UNKNOWN

Status:

UNREVIEWED

Likely Ownership:

상태이상 ID와 효과 정의의 Single Source 후보.

Requires Review:

Combat 및 Skill 문서와 중복 규칙 여부.

---

# 17. Quirk Domain

## Mental Quirk DB

ID:

`MECH_Quirk_Mental_DB`

Path:

`Wiki/01_Mechanics/MECH_Quirk_Mental_DB.md`

Authority:

UNKNOWN

Status:

UNREVIEWED

---

## Physical Quirk DB

ID:

`MECH_Quirk_Physical_DB`

Path:

`Wiki/01_Mechanics/MECH_Quirk_Physical_DB.md`

Authority:

UNKNOWN

Status:

UNREVIEWED

---

## R18 Quirk DB

ID:

`MECH_Quirk_R18_DB`

Current Git Path:

`Wiki/01_Mechanics/MECH_Quirk_R18.md`

Authority:

UNKNOWN

Review Flag:

VERSION_CONFLICT

Known Issue:

문서 ID와 실제 파일명이 일치하지 않는다.

GitHub 버전과 별도 프로젝트 사본 사이에 버전 차이가 관찰되었다.

Implementation:

PROHIBITED until version lineage is resolved.

---

# 18. Optional R18 Module

## R18 Memory Log

ID:

`MECH_R18_Memory_Log`

Path:

`Wiki/01_Mechanics/MECH_R18_Memory_Log.md`

Authority:

REFERENCE

Legacy Status:

wip

Version:

2.0.0

Purpose:

기존 R18 경험 기록 및 변질 진행 구조.

Notes:

GitHub v2는 확인된 이전 사본보다 발전된 버전이다.

그러나 Optional Module 구조와 Core 경계가 확정되기 전에는 직접 구현하지 않는다.

---

## Other R18 Documents

Authority:

UNKNOWN unless explicitly listed in this Index.

Policy:

R18은 Optional Module로 취급하며 Core 시스템의 직접 의존 대상이 되어서는 안 된다.

---

# 19. World Domain

Primary Location:

`Wiki/02_World/`

Current Overall Authority:

UNKNOWN / PARTIALLY MIGRATED

Notes:

기존 Migration 작업을 통해 일부 세계관과 지역 문서는 정본화 작업이 진행되었으나 신규 Governance 기준의 Audit은 아직 수행하지 않았다.

Important:

개별 World 문서는 각각 검증해야 한다.

`Wiki/Garbage/**` 자료는 포함하지 않는다.

---

# 20. Entity Domain

Primary Location:

`Wiki/03_Entities/`

Current Overall Authority:

UNKNOWN / PARTIALLY MIGRATED

Known reviewed exception:

`MONSTER_DB`
→ REFERENCE

Survivor / Character 문서는 별도 Audit 필요.

---

# 21. Event Domain

Primary Location:

`Wiki/05_Events/`

Authority:

UNKNOWN

Status:

UNREVIEWED

Known Technical Debt:

- 일부 Event ID와 파일명 불일치
- Template 및 Runtime Contract 검증 필요

개별 Event 콘텐츠를 구현 전에 Event System Contract가 먼저 필요하다.

---

# 22. ConfigureBook

Primary Location:

`ConfigureBook/`

Classification:

DRAFT SOURCE / REFERENCE

Authority:

Not automatically canonical.

Purpose:

Wiki 또는 Runtime Data 등록 전 콘텐츠 원고 저장소.

Rules:

- 원고와 등록본을 동시에 수정하지 않는다.
- Wiki 또는 Runtime 등록 후 Source 대응 관계를 확인한다.
- 삭제/Archive는 Director 승인 후 수행한다.

---

# 23. Archive

Primary locations:

`docs/archive/`

및 향후 승인된 Archive 경로.

Authority:

LEGACY

Implementation:

Do not use as current implementation requirement.

Purpose:

과거 설계와 개발 기록 보존.

---

# 24. Garbage

Path:

`Wiki/Garbage/**`

Authority:

NON_CANON

Implementation:

PROHIBITED

Usage:

역사 조사 또는 명시적인 Director 요청 시에만 참고.

---

# 25. Planning

## Current Project State

Path:

`docs/planning/PROJECT_STATE.md`

Authority:

LEGACY

Review Flag:

REPLACE_REQUIRED

Reason:

현재 문서는 이전 Wiki Migration 단계의 개발 상태를 기록하고 있으며 현재의 개발환경 구축 단계와 일치하지 않는다.

Do Not Use For:

현재 개발 우선순위 판단.

Future:

새 개발 Phase를 기준으로 재작성 예정.

---

# 26. Existing Migration Documents

## Documentation Migration Plan

Path:

`docs/governance/DOCUMENTATION_MIGRATION_PLAN.md`

Authority:

REFERENCE

Purpose:

이전 Wiki 정리 및 ConfigureBook Migration 과정 기록.

Notes:

일부 결정은 현재도 유효하지만 신규 Governance가 상위 규칙이다.

---

## Wiki Migration Backlog

Path:

`docs/WIKI_MIGRATION_BACKLOG.md`

Authority:

REFERENCE

Purpose:

기존 Migration에서 발견한 미완료 작업 및 기술부채 기록.

Usage:

Audit 후보와 과거 문제 탐색에 유용하다.

현재 프로젝트 로드맵으로 직접 사용하지 않는다.

---

# 27. Current Audit Queue

신규 Governance 기준의 권장 검토 순서:

```text
Phase A — Canon
1. PROJECT_CANON
2. DESIGN_PILLARS

Phase B — Core Gameplay
3. NPC Stats
4. Time
5. Combat
6. Resource

Phase C — Core Data
7. Status Effect
8. Skill
9. Monster
10. Quirk

Phase D — Runtime Systems
11. Monster AI
12. Event System
13. Save / Load
14. Relationship / NPC Behavior

Phase E — Optional Modules
15. R18 Systems

Phase F — Content
16. World
17. Locations
18. Survivors
19. Events
```

순서는 Director 결정에 따라 변경할 수 있다.

---

# 28. Review Result Vocabulary

Audit 결과는 다음 중 하나로 기록한다.

```text
KEEP
PROMOTE
REFACTOR
SPLIT
MERGE
LEGACY
DEPRECATE
ARCHIVE
```

필요한 경우:

```text
CONFLICT
UNDEFINED REQUIREMENT
VERSION_CONFLICT
REWORK_REQUIRED
```

Flag를 추가한다.

---

# 29. Maintenance Rule

다음 상황에서는 PROJECT_INDEX를 갱신한다.

- 신규 Primary Owner 생성
- Authority 변경
- Status 변경
- 문서 이동
- 문서 ID 변경
- 문서 승격 또는 Legacy 전환
- 기존 Primary Owner 교체
- System Contract 분할 또는 병합

세부 콘텐츠 변경만으로는 항상 Index를 수정할 필요가 없다.

---

# 30. Final Rule

PROJECT_INDEX는 문서 목록이 아니라 신뢰 지도다.

이 문서의 목적은 AI와 개발자가:

```text
What should I read?
↓
Which source owns the rule?
↓
Can I trust it?
↓
Can I implement from it?
```

을 빠르게 판단할 수 있게 하는 것이다.