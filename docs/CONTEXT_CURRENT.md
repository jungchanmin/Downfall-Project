# Downfall — Current Context Recovery

Last reviewed: 2026-10-30

이 문서는 세션 복구용 현재 상태 요약이다. **Gameplay Rule의 Authoritative Owner가 아니다.** 최신 Director 지시와 `PROJECT_INDEX`가 가리키는 실제 Owner를 확인하고 충돌은 보고한다. 이 요약으로 Candidate를 승인하거나 구현 요구사항을 새로 만들지 않는다.

역할: `AGENTS.md` = 운영 규칙; `PROJECT_CHARTER` = 프로젝트 방향; `PROJECT_INDEX` = Authority 경로; `CONTEXT_CURRENT` = 현재 상태 복구; Owner 문서 = 정본 규칙; Git History = 변경 이력.

## Current Phase

Combat System Refactor → Core Contract 정리 완료 단계 → Monster Action vNext Migration 준비. 다음 단계는 밸런스보다 구조 / 의미 Migration을 우선한다.

다음 Owner는 로컬에서 `CURRENT / APPROVED`다: `MECH_Combat_System`, `MECH_Check_System`, `MECH_Combat_Action_System`, `MECH_Combat_Action_Runtime_System`, `MECH_Combat_Positioning_System`, `MECH_Combat_Status_Effect_System`, `MECH_Monster_AI`, `MECH_Encounter_Resolution_System`. 경로와 최신 상태는 `PROJECT_INDEX` 및 각 문서에서 재확인한다.

## Approved Check / NPC Context

- 기본: `1d12 + Check Source Value + Modifiers >= Requirement`; 최종 Modifier는 `Clamp(Sum(raw modifiers), -3, +3)`.
- Difficulty: Very Easy 7, Easy 9, Normal 11, Hard 13, Very Hard 15, Impossible 17. Natural Critical은 없다.
- 불확실한 Check의 기본 성공 확률이 정확히 100% 또는 0%일 때만 Fate Override `1d100`을 굴린다. 1–2이면 각각 Failure 또는 Success로 반전하고 3–100이면 기본 결과를 유지한다. 그 밖의 확률에는 추가 Roll이 없으며 확정 상황은 Check를 생략할 수 있다.
- 기본 Composite: `Floor(Average(required Source Values))`, Equal Weight. Opposed Formula, Weighted Composite, Universal Great Success / Failure Threshold 및 Fractional Modifier는 미확정이다.
- 최신 Director 지시의 NPC Ability: Combat, Exploration, Dialogue, Care, Craft, Technique, Charm, Intelligence. Legacy `Search`, `Knowledge`를 Current 명칭으로 추정하지 않는다.

## Positioning / Action Runtime

- Positioning: `Close / Mid / Far` 추상 Combat Formation. Position Change ≠ Universal Dodge. 기본 Movement는 1 Action당 1 Band; 뒤로 이동할 때 이동 후 더 가까운 Band에 다른 유효 Survivor의 Frontline Anchor가 필요하다.
- Hostile Combat 중 Close가 비면 Survivor Formation의 Line Compression이 가능하며 최대 1 Band / Round다. Far는 영구 안전지대가 아니고 Cover는 Positioning v1 범위 밖이다.
- Cooldown N은 사용 후 N개의 완전한 Round 동안 재사용을 막는다. 일반 후보가 0일 때만 Cooldown을 제외한 모든 조건이 유효한 후보를 Fallback 대상으로 삼으며 가장 오래 사용하지 않은 후보를 복구한다. 해당 후보도 없을 때 최종 처리는 미정이다.
- Prepared는 선행 Action Resolution 성공과 Trigger 충족 후 생성된다. 기본적으로 Telegraph 하나가 Prepared Action 하나에 대응한다. 다음 유효 Activation에서 Target과 Requirement를 재검증하고 실행 또는 Fizzle한다. Fizzle은 Activation을 소비하고 기본 Full Cooldown을 적용한다(승인된 Action별 override 가능). Combat 종료 시 전투 전용 Runtime을 폐기한다.

## Monster AI / Status

Monster Activation → Hostile Context → Prepared Action 확인 → Available Action IDs → Eligibility → Target → Context → Profile → Weight → Weighted Random → Selected Action / Resolver. Prepared가 있으면 일반 선택보다 우선한다. Simple AI는 기본 평가 흐름, Advanced AI는 명시적 확장이다. AI는 Action Effect를 소유하지 않는다.

`MECH_Combat_Status_Effect_System`은 `CURRENT / APPROVED`, `DATA_Combat_Status_Effect_Catalog`는 `CURRENT_CANDIDATE / REVIEW`, `MECH_Status_Effect_DB`는 Legacy Migration Source다. NPC Stats의 Abnormality Susceptibility와 Combat Status Effect는 다르다.

## Monster Action Candidate

`DATA_Monster_Action_Catalog`는 `CURRENT_CANDIDATE / REVIEW / 1.0.0`이며 기존 Action 18개를 보존한다. Action별 Check는 `REBALANCE_REQUIRED`, Legacy Damage는 `LEGACY_BALANCE`, vNext Schema는 Candidate다.

- Required 후보: Action ID, Display Name, Role, Target Rule, Position 적용 여부 / Bands, Requirements, Effects.
- Optional 후보: Tier, Threat, Cooldown, Usage Limit, Telegraph, Prepared Trigger, Check, Status References, AI Tags, Presentation, Special Handler, Legacy Trace, Review Metadata. 미기재는 임의 기본값의 승인이 아니다.
- Role은 기능, Tier는 희소성 / 특수성, Threat는 플레이어 대응 필요 수준이다. Threat `Normal / Strong`은 미승인 후보이며 Damage Rank가 아니다.

### High-Risk Migration Notes

- `SK_Grab` / `SK_Bite` / `SK_LootEquip`: Bound 연계가 있으나 Prepared를 자동 확정하지 않는다.
- `SK_TailSwipe`: Action은 Migration 후보, Cover 부분만 `LEGACY_ONLY`다.
- `SK_WaryStep`: 조건부 후속 행동과 함정 정보의 Owner 및 Prepared 여부 검토.
- `SK_OminousPrayer`: Percentage Damage / Quirk Scaling 재검토.
- `SK_AimedShot`: 총기 설명과 Weapon Variant 책임 / 범위 충돌 검토.
- `SK_CallSupport`: `ST_Reinforce`는 Consumer Migration 전 Legacy Reference; Pending Reinforcement로의 이관 후보.
- `SK_StunGun`: `ST_Stun` / `ST_Paralysis` 선택 기준과 장비 조건 미확정.

## Do Not Reopen Without New Evidence

Owner와 최신 Director 지시를 확인하며 다음 승인 결정을 새 제안으로 되돌리지 않는다: 1d12 Check; Modifier Cap -3..+3; Difficulty 7/9/11/13/15/17; Natural Critical 없음; Fate Override; Equal Weight Composite `Floor(Average())`; Close / Mid / Far; Position Change ≠ Universal Dodge; 기본 1 Action = 1 Band; Frontline Anchor; Line Compression 최대 1 Band / Round; Cover는 Positioning v1 범위 밖; Core의 R18 의존 금지; Round Cooldown; Prepared Fizzle의 Activation 소비; Monster AI Weighted Random.

## Current Open Items

- Monster Action vNext Schema 최종 승인과 18개 Action 구조 Migration.
- Action별 Band, Role / Tier / Threat, Check Source / Requirement, Cooldown, Damage Balance.
- Weapon / Item Combat Owner, `SK_AimedShot` Weapon 관계, `SK_StunGun` Status 선택 규칙, `ST_Reinforce` 후속 Owner / Consumer Migration.
- Opposed Check Formula, Weighted Composite, Universal Great Success / Failure Threshold, Fractional Modifier.
- Action Runtime Schema와 Fallback Tie-break.

## Current Next Task

Monster Action vNext Schema 최종 승인 → 18개 Action 구조 Migration. 먼저 Structural / Semantic Migration을 검토하며 임의로 Action Balance를 확정하지 않는다.

## Update Rule / Handoff

신규 CURRENT / APPROVED Contract, 주요 Director 승인, Phase 변경, 주요 Blocker 생성 / 해결, Candidate Promotion 또는 Next Task 변경 시 이 현재 상태를 갱신한다. 단순 오탈자, 사소한 문구, Legacy Trace만의 변경이나 Gameplay 의미가 없는 정리는 갱신을 요구하지 않는다.

긴 작업의 handoff는 허용된 파일 범위 안에서 Current Phase, 완료 작업, 승인 결정, 변경 파일, 미해결 항목과 다음 작업을 기록한다. 작업 트리의 기존 변경 사항은 `git status`로 확인하고 보존한다. 과거 상세는 Owner, Git History 및 Migration 문서에 남긴다.
