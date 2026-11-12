---
id: TECH_SPEC_DayCycle_Prototype
title: DayCycle Prototype Technical Specification
type: technical_specification
authority: CURRENT
status: APPROVED
version: 0.1.0
---

# DayCycle Prototype Technical Specification

The Director approved this prototype scope and its technical choices on 2026-11-12, including no initialization events, isolated subscriber failures with continued transition, scene-lifetime ownership by `DayCycleHost`, and exclusion of save and cross-scene persistence. This specification does not supersede `Wiki/01_Mechanics/Time_System.md` or approve additional gameplay rules.

## Scope and state

The plain C# `DayCycle` owns `CurrentDay`, `CurrentPhase` and `IsCampaignTimeEnded`. A new instance starts at Day 1 / Dawn and emits no initialization events. Consumers read the initial state explicitly. Campaign length is 25 days and the order is Dawn, Morning, Noon, Evening, Night. Save/load and other gameplay systems are outside this prototype.

## Completion and events

`CompletePhase()` advances only on an explicit request. It returns `false` during an existing transition or after campaign time ends; otherwise it returns `true` after the transition. A normal phase transition dispatches `PhaseEnded`, changes phase, and dispatches `PhaseStarted`. A day transition dispatches `PhaseEnded(Night)`, `DayEnded`, updates day and phase to Dawn, then dispatches `DayStarted` and `PhaseStarted(Dawn)`. Day 25 Night dispatches `PhaseEnded`, `DayEnded`, then `CampaignTimeEnded`, without creating Day 26.

Subscribers are invoked individually in subscription order. Exceptions are collected as event-name/exception pairs in `LastNotificationFailures` and do not interrupt remaining subscribers or roll back the transition. The collection reflects the latest accepted completion request and is cleared on the next accepted request; rejected reentrant or ended requests do not clear it. The prototype `DayCycleHost` logs collected failures after an accepted completion. No global event bus or save schema is introduced.

## Unity and UI boundaries

`DayCycleHost` owns the runtime instance for its scene lifetime. `DayCycleView` references the host, reads initial state, subscribes while enabled and unsubscribes while disabled. Its button requests completion through the host. The UI does not create a second runtime instance. Disabling and re-enabling the view does not reset the host; transition log entries are view-local and bounded to eight entries.

The prototype scene uses uGUI with a Screen Space Overlay Canvas and a 1920 x 1080 Scale With Screen Size reference with Match 0.5. It uses Unity's built-in uGUI Text and font in place of TextMeshPro to avoid adding or importing font resources for the prototype. Placeholder content has no gameplay behavior.

## Verification and limitations

Edit Mode tests cover initial state, phase ordering, day boundary and event ordering, reentrancy, campaign boundary and subscriber exceptions. Play Mode checks cover button event binding, displayed phase and log, view disable/re-enable without runtime reset, and campaign end display. The current design has no persistence across scene destruction or application restart. It does not specify future system ownership, save representation, or cross-scene lifetime; those require subsequent approved work.
