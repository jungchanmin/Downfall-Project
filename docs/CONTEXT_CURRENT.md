# Downfall — Current Context Recovery

Last reviewed: 2026-11-05

이 문서는 세션 복구용 현재 상태 요약이다. **Gameplay Rule의 Authoritative Owner가 아니다.** 최신 Director 지시와 `PROJECT_INDEX`가 가리키는 실제 Owner를 확인하고 충돌은 보고한다. 이 요약으로 Candidate를 승인하거나 구현 요구사항을 새로 만들지 않는다.

역할: `AGENTS.md` = 운영 규칙; `PROJECT_CHARTER` = 프로젝트 방향; `PROJECT_INDEX` = Authority 경로; `CONTEXT_CURRENT` = 현재 상태 복구; Owner 문서 = 정본 규칙; Git History = 변경 이력.

## Current Phase

Director approval on 2026-11-12: `TECH_SPEC_DayCycle_Prototype` is APPROVED for the existing prototype scope, including no initialization events, isolated subscriber failures, scene-lifetime `DayCycleHost`, and no save or cross-scene persistence. `DownfallExternalRefresh` is approved as a shared development tool. Unity Assistant, Inference, Pipeline and other uncommitted environment settings remain outside that approval and require separate review. See `PROJECT_INDEX` for the specification path; `MECH_Time_System` remains the Gameplay Owner.

Combat System Refactor → Core Contract 정리 완료 단계 → Monster Action vNext Migration 준비. 다음 단계는 밸런스보다 구조 / 의미 Migration을 우선한다.

다음 Owner는 로컬에서 `CURRENT / APPROVED`다: `MECH_Combat_System`, `MECH_Check_System`, `MECH_Combat_Action_System`, `MECH_Combat_Action_Runtime_System`, `MECH_Combat_Positioning_System`, `MECH_Combat_Status_Effect_System`, `MECH_Monster_AI`, `MECH_Encounter_Resolution_System`. 경로와 최신 상태는 `PROJECT_INDEX` 및 각 문서에서 재확인한다.

## Approved Check / NPC Context

- 기본: `1d12 + Check Source Value + Modifiers >= Requirement`; 최종 Modifier는 `Clamp(Sum(raw modifiers), -3, +3)`.
- Difficulty: Very Easy 7, Easy 9, Normal 11, Hard 13, Very Hard 15, Impossible 17. Natural Critical은 없다.
- 불확실한 Check의 기본 성공 확률이 정확히 100% 또는 0%일 때만 Fate Override `1d100`을 굴린다. 1–2이면 각각 Failure 또는 Success로 반전하고 3–100이면 기본 결과를 유지한다. 그 밖의 확률에는 추가 Roll이 없으며 확정 상황은 Check를 생략할 수 있다.
- 기본 Composite: `Floor(Average(required Source Values))`, Equal Weight. Opposed Formula, Weighted Composite, Universal Great Success / Failure Threshold 및 Fractional Modifier는 미확정이다.
- 최신 Director 지시의 NPC Ability: Combat, Exploration, Dialogue, Care, Craft, Technique, Charm, Intelligence. Legacy `Search`, `Knowledge`를 Current 명칭으로 추정하지 않는다.

## Positioning / Action Runtime

- Positioning: `Close / Mid / Far` 추상 Combat Formation. Position Change ≠ Universal Dodge. 기본 Movement는 1 Action당 1 Band; Survivor 후퇴에는 이동 후 더 가까운 Band에 다른 유효 Survivor의 Frontline Anchor가 필요하다. Director 승인에 따라 `SK_Base_Backstep` 및 Monster 기본 Backstep에는 Survivor Frontline Anchor를 적용하지 않는다. Positioning Owner의 표현은 이 결정과 후속 정합화가 필요하다.
- Hostile Combat 중 Close가 비면 Survivor Formation의 Line Compression이 가능하며 최대 1 Band / Round다. Far는 영구 안전지대가 아니고 Cover는 Positioning v1 범위 밖이다.
- Cooldown N은 사용 후 N개의 완전한 Round 동안 재사용을 막는다. 일반 후보가 0일 때만 Cooldown을 제외한 모든 조건이 유효한 후보를 Fallback 대상으로 삼으며 가장 오래 사용하지 않은 후보를 복구한다. 해당 후보도 없을 때 최종 처리는 미정이다.
- Prepared는 선행 Action Resolution 성공과 Trigger 충족 후 생성된다. 기본적으로 Telegraph 하나가 Prepared Action 하나에 대응한다. 다음 유효 Activation에서 Target과 Requirement를 재검증하고 실행 또는 Fizzle한다. Fizzle은 Activation을 소비하고 기본 Full Cooldown을 적용한다(승인된 Action별 override 가능). Combat 종료 시 전투 전용 Runtime을 폐기한다.
- Reactive State는 Prepared와 별개다. 유효한 상대 Attack Attempt에서 Trigger를 소비 / 예약하고 원 Action을 먼저 해결한 뒤 Owner / Attacker / Position Eligibility를 재검증해 Counter를 실행 또는 취소한다. 원 공격의 Miss는 반격을 자동 취소하지 않는다. Combat 종료 시 Reactive 상태와 예약을 폐기한다.

## Monster AI / Status

Monster Activation → Hostile Context → Prepared Action 확인 → Available Action IDs → Eligibility → Target → Context → Profile → Weight → Weighted Random → Selected Action / Resolver. Prepared가 있으면 일반 선택보다 우선한다. Simple AI는 기본 평가 흐름, Advanced AI는 명시적 확장이다. AI는 Action Effect를 소유하지 않는다.

`MECH_Combat_Status_Effect_System`은 `CURRENT / APPROVED`, `DATA_Combat_Status_Effect_Catalog`는 `CURRENT_CANDIDATE / REVIEW`, `MECH_Status_Effect_DB`는 Legacy Migration Source다. NPC Stats의 Abnormality Susceptibility와 Combat Status Effect는 다르다.

## Monster Action Candidate

Catalog 자체는 `CURRENT_CANDIDATE / REVIEW`다. vNext Schema 방향은 Director 승인 완료이며 §8 문서 반영도 완료됐다.

`DATA_Monster_Action_Catalog`의 Version은 `1.0.0`이며 기존 Action 18개를 보존한다. Batch 1 / 2 / 3의 Check 방향은 승인됐고 필요한 Check의 미확정 설정은 `REBALANCE_REQUIRED`, Legacy Damage는 `LEGACY_BALANCE`다.

**BATCH 3 CORE ACTION DIRECTIONS AND COUNTER / REACTIVE RUNTIME MINIMUM CONTRACT APPROVED AND DOCUMENTED → READY FOR CLAWLUNGE RECENT ACTION CONTEXT REVIEW.** 18개 기록의 필수 개념과 미확정 상태를 명시하고 Migration Metadata와 원문을 보존했다. Balance Pass는 아직 시작하지 않았으며 각 기록은 미완료이고 Catalog는 승격되지 않았다.

- Batch 1: Strike는 Single Enemy / Target Close / Damage / Check Required, Source Combat이다. Threaten은 Single Enemy / Target Close + Mid / Check Required, 단일 Source Dialogue이며 성공 시 ST_Cower 적용을 요청한다. 둘 다 무기가 필요 없으며 추가 Actor Band 제한 없이 일반 Eligibility를 따른다.
- Brace는 Self / Position Not Applicable / Defensive Mitigation / Check Not Applicable이다. 첫 유효 피격 시 완화를 적용하고 소비하며, 피격이 먼저 없으면 사용자 다음 Activation 시작 시 만료한다. 중첩하지 않으며 재사용 시 처리와 Runtime 저장 방식은 미정이다.
- Backstep은 Self / 후방 1 Band 이동 / Check Not Applicable이다. Actor Action 가능, Movement 가능, 뒤쪽 Band 존재를 Owner 제공 Eligibility로 확인한다. Far에는 뒤쪽 Band가 없어 Eligibility false다. Monster 기본 Backstep에 Survivor Anchor를 적용하지 않고 범용 회피를 부여하지 않는다.
- Batch 2: Swing은 Single Enemy / Target Close / Weapon Held / Damage / Combat Check, Shout은 Multiple Enemies AoE / Target Close + Mid / ST_Cower / Dialogue Check다. Shout의 Legacy 증원 분기는 현재 Effect에서 분리했다.
- Grab은 Single Enemy / Target Close / ST_Bound / Combat Check이며 Gate B나 Prepared 후속 행동을 자동 생성하지 않는다. LootEquip은 Single Enemy / Target Close / Bound와 제거 가능한 장비 요구 / Technique Check 후 Item / Equipment Owner에게 제거·이전을 요청한다.
- Shout은 Action당 Dialogue Check 한 번을 굴리고 성공 시 유효한 Close / Mid 적 모두에게 ST_Cower 적용을 요청한다. 실제 적용 가능 여부는 Status Owner가 결정한다. Grab의 Bound는 이후 일반 Eligibility / AI 선택을 통해 후속 Action을 가능하게 할 수 있다.
- LootEquip의 제거 가능한 장비 존재 여부는 Item / Equipment Owner가 제공한다. Swing은 Weapon Held와 Damage 요청을 소유하며 필요한 장착 무기 Context는 Resolver에 제공될 수 있다. 무기 수치·속성은 Weapon / Item Owner 영역이며 구체 Owner 계약은 후속 작업이다.
- Batch 3: Bite는 Close 단일 대상 Combat Check 후 Damage / ST_Bound 요청이며 자동 후속 행동이 없다. TailSwipe는 Close Small AoE에 Combat Action Check 한 번 후 Damage / ST_Stagger 요청을 한다. 대상 수는 미정이고 Cover 효과는 Legacy다.
- ClawLunge는 정상 Monster Activation에서 선택하며, 직전 Player Action 전 유효한 Close 교전 대상이 그 Action 중 Close → Mid로 이동한 경우 해당 대상에 한해 추격 Eligibility가 유지된다. Reaction이 아니며 양측 Position을 이동하지 않는다. 정확한 최근 교전 / 이동 Context 소유와 Runtime Schema는 후속 검토다.
- WaryStep은 이동 없는 Self Defense setup이며 Counter Ready ≠ Prepared다. 다음 Monster Activation 직전까지 Close의 Survivor가 이 Monster에 유효한 Hostile Attack을 시도하면 Hit / Miss와 무관하게 Trigger를 소비 / 예약한다. 원 공격 해결 후 재검증하여 Counter를 실행 또는 취소하며 다음 Activation은 정상 진행한다. Catalog의 Resolution Order는 Runtime Owner에 정합화됐다.

- 최종 Definition은 Action ID, Display Name, Role, Target Rule, Position Container, Requirements와 Effects를 필수로 한다. 미확정 기록은 Migration 상태로 보류하며 빈 조건으로 확정하지 않는다.
- Position Container는 적용 여부를 구분한다. Actor / Target Bands는 Position 적용 시 조건부다. Threat Field는 Optional이며 enum은 보류한다.
- Tier는 희소성 / 특수성이며 `MECH_Combat_Action_System` §10과 정합화됐다.
- Effect의 Source Order를 보존하되 Runtime 실행 의미는 보류한다. Legacy Handler는 Migration Metadata에 유지하고 승인된 Special Handler의 Optional Definition 참조를 허용한다.
- Definition과 Migration Metadata는 논리적으로 분리하고 Runtime State는 Definition에서 제외한다. 개별 Action 값과 Optional 필드 미기재의 Gameplay 기본값은 이 결정으로 승인되지 않는다.

### High-Risk Migration Notes

- `SK_Grab` / `SK_Bite` / `SK_LootEquip`: Bound 연계가 있으나 Prepared를 자동 확정하지 않는다. Grab Gate B는 Legacy이며 LootEquip의 장비 이관은 Item / Equipment Owner가 담당한다.
- `SK_Shout`: Legacy 증원 분기는 Encounter / Swarm 또는 별도 Action의 후속 Owner 검토 대상이다.
- `SK_TailSwipe`: Cover 부분은 `LEGACY_ONLY`이며 Small AoE 최대 대상 수는 미정이다.
- `SK_WaryStep`: 최소 Reactive Runtime Contract는 승인됐으며 Catalog Resolution Order와 정합화됐다. Legacy 자동 Bite / Claw 및 함정 정보는 승격하지 않는다.
- `SK_OminousPrayer`: Percentage Damage / Quirk Scaling 재검토.
- `SK_AimedShot`: 총기 설명과 Weapon Variant 책임 / 범위 충돌 검토.
- `SK_CallSupport`: `ST_Reinforce`는 Consumer Migration 전 Legacy Reference; Pending Reinforcement로의 이관 후보.
- `SK_StunGun`: `ST_Stun` / `ST_Paralysis` 선택 기준과 장비 조건 미확정.

## Do Not Reopen Without New Evidence

Owner와 최신 Director 지시를 확인하며 다음 승인 결정을 새 제안으로 되돌리지 않는다: 1d12 Check; Modifier Cap -3..+3; Difficulty 7/9/11/13/15/17; Natural Critical 없음; Fate Override; Equal Weight Composite `Floor(Average())`; Close / Mid / Far; Position Change ≠ Universal Dodge; 기본 1 Action = 1 Band; Frontline Anchor; Line Compression 최대 1 Band / Round; Cover는 Positioning v1 범위 밖; Core의 R18 의존 금지; Round Cooldown; Prepared Fizzle의 Activation 소비; Monster AI Weighted Random.

## Current Open Items

- 18개 Monster Action별 구조 / 의미 검토와 미확정 항목 해소.
- 나머지 Action별 Band, Role / Tier / Threat와 Check Source 및 Action별 Check Requirement / Difficulty, Cooldown, Damage Balance. Batch 1 / 2의 승인된 Check Source는 Catalog를 따른다.
- Brace 완화량 / 공식 / 반복 사용 처리 / Runtime 저장 방식, ST_Cower 상세 데이터, Backstep의 Status별 판정은 관련 Owner와 후속 검토한다.
- Weapon / Item Combat Owner, `SK_AimedShot` Weapon 관계, `SK_StunGun` Status 선택 규칙, `ST_Reinforce` 후속 Owner / Consumer Migration.
- Opposed Check Formula, Weighted Composite, Universal Great Success / Failure Threshold, Fractional Modifier.
- Action Runtime Schema와 Fallback Tie-break.
- WaryStep Counter Damage / Check / Status 및 개별 Effect, Reactive Runtime 정확한 DTO / Event / Sync Schema와 Action별 상세 Eligibility.
- ClawLunge의 최근 유효 Close 교전 대상 및 직전 Player Action의 이동 Context: Source of Truth와 Runtime Schema 미정.

## Current Next Task

READY FOR CLAWLUNGE RECENT ACTION CONTEXT REVIEW → 최근 유효 Close 교전 대상과 직전 Player Action의 이동 Context / Source of Truth를 검토한 뒤 Batch 3 Detail Review를 진행한다. 수치 Balance는 아직 시작하지 않았다.

## Update Rule / Handoff

신규 CURRENT / APPROVED Contract, 주요 Director 승인, Phase 변경, 주요 Blocker 생성 / 해결, Candidate Promotion 또는 Next Task 변경 시 이 현재 상태를 갱신한다. 단순 오탈자, 사소한 문구, Legacy Trace만의 변경이나 Gameplay 의미가 없는 정리는 갱신을 요구하지 않는다.

긴 작업의 handoff는 허용된 파일 범위 안에서 Current Phase, 완료 작업, 승인 결정, 변경 파일, 미해결 항목과 다음 작업을 기록한다. 작업 트리의 기존 변경 사항은 `git status`로 확인하고 보존한다. 과거 상세는 Owner, Git History 및 Migration 문서에 남긴다.
