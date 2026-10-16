# Downfall Project Documentation Index

## 0. Purpose

This document is the primary navigation map for Downfall project documentation.

Codex should use this file to locate relevant project specifications instead of searching or loading every available document.

This index does not itself define gameplay rules.

Authoritative rules belong to the documents referenced by this index.

---

# 1. Documentation Principles

Before implementing a feature:

1. Identify the system or data domain involved.
2. Locate the relevant documentation through this index.
3. Read only the documents required for the task.
4. Compare documentation with the existing implementation.
5. Report conflicts instead of silently resolving them.

Do not assume that every available document is current or approved.

Document status and Director decisions take precedence according to AGENTS.md.

---

# 2. Source-of-Truth Locations

## Technical Source

Primary location:

Git repository

Contains:

- Approved technical specifications
- Architecture documentation
- Source code
- Tests
- Technical decisions
- Implementation reports

---

## Creative Source

Primary location:

Google Drive / Downfall_Project

Contains:

- Worldbuilding
- Scenario
- Character material
- NPC material
- Monster lore
- Dialogue
- Events
- Creative DRB documents

Creative source material should normally be treated as read-only by Codex.

Creative material may express gameplay intent but does not automatically define implementation architecture.

---

# 3. Core System Documents

## Combat

Domain:

Combat rules, actions, resolution, damage, turn behavior and related mechanics.

Current source document:

MECH_Combat_System

Planned repository location:

Docs/Systems/MECH_Combat_System.md

Status:

Migration pending

Use when working on:

- Combatants
- Attacks
- Damage
- Combat turns
- Combat actions
- Combat resolution
- Combat-related dice logic

---

## NPC Memory

Domain:

NPC memory storage and related memory behavior.

Current source document:

MECH_R18_Memory_Log

Planned repository location:

Docs/Systems/MECH_R18_Memory_Log.md

Status:

Migration pending

Use when working on:

- NPC memory
- Memory records
- Memory persistence
- Memory-related runtime state

---

# 4. Database Documents

## Monster Database

Domain:

Monster definitions and monster-related data.

Current source document:

MONSTER_DB

Planned repository location:

Docs/Database/MONSTER_DB.md

Status:

Migration pending

Use when working on:

- MonsterDefinition
- Monster identifiers
- Monster statistics
- Monster traits
- Monster content data
- Monster combat integration

Do not modify monster IDs without explicit approval.

---

## Quirk Database

Domain:

Quirk definitions and related gameplay data.

Current source document:

MECH_Quirk_R18_DB

Planned repository location:

Docs/Database/MECH_Quirk_R18_DB.md

Status:

Migration pending

Use when working on:

- Quirk definitions
- Quirk IDs
- Quirk effects
- Quirk-related state or modifiers

Do not modify Quirk IDs without explicit approval.

---

# 5. Creative Documentation

Creative documents currently exist primarily in Google Drive under:

Downfall_Project

Known creative document categories include:

- World concept
- Obeng lore
- Monster lore
- Faction lore
- Ritual lore
- NPC-specific folders
- Character writing rules
- Event-generation rules
- Lore-reference protocols

Codex should access these only when creative context is necessary for the requested implementation.

Do not treat creative prose as a technical data contract unless it has been converted into an approved TECH_SPEC.

---

# 6. Technical Architecture

Repository location:

Docs/Architecture/

Current state:

Not yet established.

Future architecture documents may include:

- Data architecture
- Runtime state architecture
- Save/load architecture
- Dependency rules
- Event architecture
- NPC architecture
- Combat architecture
- Unity project structure

Until an approved architecture document exists, follow AGENTS.md and existing repository patterns.

Do not invent project-wide architecture solely to fill missing documentation.

---

# 7. Implementation Specifications

Repository location:

Docs/Specifications/

Purpose:

Contains implementation-ready specifications.

Standard document type:

TECH_SPEC

Only APPROVED technical specifications should normally be treated as binding implementation requirements.

Typical specification structure:

- Goal
- Functional requirements
- Data contracts
- Runtime requirements
- Dependencies
- Scope
- Out of scope
- Acceptance criteria
- Open questions

---

# 8. Technical Decisions

Repository location:

Docs/Decisions/

Purpose:

Record important decisions whose reasoning should survive future sessions.

Preferred format:

ADR_<ID>_<Title>.md

Use ADRs for significant decisions such as:

- Static data versus runtime state boundaries
- Save architecture
- Dependency direction
- Serialization strategy
- Major framework selection
- System ownership

Do not create ADRs for trivial implementation details.

---

# 9. AI Collaboration Documents

The project uses three primary AI roles.

Argon:
Creative Lead

Sol:
Design / Review / Coordination

Codex:
Technical Lead / Implementation

Expected handoff flow:

Creative intent
→ CREATIVE_SPEC
→ Technical review
→ TECH_SPEC
→ Codex implementation
→ IMPLEMENTATION_REPORT
→ Review
→ Director approval

The detailed exchange protocol will be documented separately.

---

# 10. Documentation Routing Rules

For a combat task:

Read the Combat system documentation first.

For a monster task:

Read MONSTER_DB and any relevant Combat or Monster AI specification.

For Quirk work:

Read MECH_Quirk_R18_DB and the system affected by the Quirk.

For NPC memory work:

Read MECH_R18_Memory_Log and relevant NPC runtime architecture.

For creative or narrative behavior:

Consult the relevant Google Drive creative source and any corresponding approved TECH_SPEC.

For architecture changes:

Read Docs/Architecture and relevant ADRs before proposing modifications.

For implementation requests with an approved TECH_SPEC:

Treat that TECH_SPEC as the primary task contract while preserving higher-priority project rules.

---

# 11. Missing Documentation

A missing document does not grant permission to invent Downfall-specific behavior.

If implementation depends on undocumented project rules:

Report:

UNDEFINED REQUIREMENT

and identify the missing decision.

Technical implementation details that do not alter game design may still be decided according to AGENTS.md.

---

# 12. Current Documentation Migration State

The Downfall documentation system is currently being established.

Known source documents have not yet all been migrated into the Git repository.

Until migration is complete:

- Do not assume absence from Docs means the source does not exist.
- Check this index.
- Check explicitly provided source documents.
- Check the approved creative source when relevant.
- Report unavailable required documentation rather than replacing it with assumptions.

---

# 13. Maintenance Rule

When a new authoritative document is created, renamed, deprecated, or replaced:

Update this index.

This file should remain a navigation map.

Do not copy entire specifications into PROJECT_INDEX.md.