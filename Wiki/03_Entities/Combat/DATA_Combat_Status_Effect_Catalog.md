---
id: DATA_Combat_Status_Effect_Catalog
title: Downfall Combat Status Effect Catalog
type: data
authority: CURRENT_CANDIDATE
status: REVIEW
version: 1.0.0
parent:
  - MECH_Combat_Status_Effect_System
references:
  - MECH_Combat_System
  - MECH_Combat_Action_System
  - MECH_Check_System
  - MECH_NPC_Stats_System
  - MECH_Status_Effect_DB
  - DATA_Monster_Action_Catalog
summary: >
  Legacy Status DB의 general 전투 상태효과 13개를 공통 Status Contract에 맞게
  구조화한 검토용 Definition. 수치와 미확정 Owner는 승인 정본으로 승격하지 않는다.
last_updated: 2026-10-27
---

# Downfall Combat Status Effect Catalog

## 1. Purpose

Core Combat에서 사용하는 개별 Combat Status Effect Definition의 단일 데이터 출처 후보다.
상위 계약은 `MECH_Combat_Status_Effect_System`이다. Mechanic Contract나 Runtime / Save Schema가 아니다.
CURRENT_CANDIDATE / REVIEW 상태이며 개별 효과는 검토 완료 전 구현 승인값으로 사용하지 않는다.

이 문서는 general 계층 13개만 Migration한다. Optional R18 / Submission 데이터와 문서는 생성하지 않는다.
기존 `MECH_Status_Effect_DB v1.1.0`은 LEGACY STATUS ASSET SOURCE로 수정 없이 보존한다.
Consumer의 신규 Catalog 연결도 이번 작업에서 자동 변경하지 않는다.

## 2. Migration Data Shape

- 아래 YAML은 Migration Definition 표현이다. 객체와 배열의 Flow 표기는 간결한 문서 표현이며 Runtime Schema를 확정하지 않는다.
- SOURCE_EXPLICIT는 원문에 명시됐다는 추적 표기이며 현행 Gameplay 승인과 다르다.
- 명시된 Director 승인 방향과 미확정 세부값을 구분한다. effects.status는 세부 효과 검토 상태이며, 승인된 정체성·연계 흐름까지 미승인이라는 의미가 아니다. 그 외 모델과 effects 후보는 REVIEW_REQUIRED / REBALANCE_REQUIRED다.
- 기존 숫자·비율·Turn·Dice 효과는 legacy 안에서 LEGACY_BALANCE로만 보존한다.
- stacking은 Source에 명시된 ST_Bleed와 중첩 수가 언급된 ST_Brand만 후보를 기록한다. 그 외는 미확정이다.
- clear_conditions의 source_terms는 의미만 보존한다. Action / Item ID를 새로 만들지 않는다.
- application은 Consumer 참조이며 명중·저항·면역·Check Source / Requirement를 확정하지 않는다.
- persistence는 개별 Source 검증이 필요하므로 REVIEW_REQUIRED다. 영구 NPC State는 이 Catalog 소유가 아니다.
- special_effect.id의 null은 기존 Handler가 명시되지 않았다는 의미이며, 특수 로직 불필요를 확정하지 않는다.
- legacy.original_kind는 원문의 표시명을 보존한다. combat_quirk는 Legacy 추적 정보일 뿐 현행 kind가 아니다.

---

# 3. Core Status Migration Definitions

## ST_Bound — 속박됨

```yaml
id: "ST_Bound"
type: "combat_status_effect"
name: "속박됨"
allowed_target: "survivor"
duration: {"status": "REVIEW_REQUIRED", "model_candidates": ["Until Condition"]}
stacking: {"status": "REVIEW_REQUIRED"}
clear_conditions: {"status": "REVIEW_REQUIRED", "source_terms": ["탈출 판정"]}
effects: {"status": "REVIEW_REQUIRED", "candidates": ["Action Restriction", "Escape Restriction"]}
application: {"status": "REVIEW_REQUIRED", "source_giver": "붙잡기·물기", "consumer_references": [{"action_id": "SK_Grab", "reference": "declared_effect"}, {"action_id": "SK_Bite", "reference": "declared_effect"}]}
persistence: {"status": "REVIEW_REQUIRED"}
special_effect: {"id": null, "status": "REVIEW_REQUIRED"}
legacy: {"source": "MECH_Status_Effect_DB v1.1.0 / SECTION 1 general", "original_kind": "지속", "original_effect": "공격 불가, 탈출 시도만. 도주 불가", "original_clear": "탈출 판정", "balance_status": "LEGACY_BALANCE"}
review_note: "공격 제한·탈출 필요·도주 제한은 Legacy 정체성이다. 금지 Action 목록, Escape Check Source/Requirement와 도주 완전 금지는 REVIEW_REQUIRED."
```

## ST_Pain — 고통

```yaml
id: "ST_Pain"
type: "combat_status_effect"
name: "고통"
allowed_target: "survivor"
duration: {"status": "REVIEW_REQUIRED", "model_candidates": []}
stacking: {"status": "REVIEW_REQUIRED"}
clear_conditions: {"status": "REVIEW_REQUIRED", "source_terms": ["일시"]}
effects: {"status": "REBALANCE_REQUIRED", "candidates": ["Check Modifier Source"]}
application: {"status": "REVIEW_REQUIRED", "source_giver": "발톱치기", "consumer_references": [{"action_id": "SK_ClawLunge", "reference": "declared_effect"}]}
persistence: {"status": "REVIEW_REQUIRED"}
special_effect: {"id": null, "status": "REVIEW_REQUIRED"}
legacy: {"source": "MECH_Status_Effect_DB v1.1.0 / SECTION 1 general", "original_kind": "지속", "original_effect": "전투 주사위 −1", "original_clear": "일시", "balance_status": "LEGACY_BALANCE", "check_modifier": {"status": "REBALANCE_REQUIRED", "legacy_value": "전투 주사위 −1"}}
review_note: "전투 주사위 감소를 전역 Modifier로 변환하지 않는다. 적용 Check와 값은 REBALANCE_REQUIRED."
```

## ST_SeverePain — 심각한 고통

```yaml
id: "ST_SeverePain"
type: "combat_status_effect"
name: "심각한 고통"
allowed_target: "survivor"
duration: {"status": "REBALANCE_REQUIRED", "model_candidates": ["Encounter Duration", "Until Condition"]}
stacking: {"status": "REVIEW_REQUIRED"}
clear_conditions: {"status": "REVIEW_REQUIRED", "source_terms": ["전투 종료"]}
effects: {"status": "REBALANCE_REQUIRED", "candidates": ["Source Impairment"]}
application: {"status": "REVIEW_REQUIRED", "source_giver": "데스롤", "consumer_references": []}
persistence: {"status": "REVIEW_REQUIRED"}
special_effect: {"id": null, "status": "REVIEW_REQUIRED"}
legacy: {"source": "MECH_Status_Effect_DB v1.1.0 / SECTION 1 general", "original_kind": "지속", "original_effect": "전투 절반 — 이탈까지", "original_clear": "전투 종료", "balance_status": "LEGACY_BALANCE"}
review_note: "전투 절반의 Source·반감 계산·지속 범위는 REBALANCE_REQUIRED. 원문 효과의 이탈까지와 해제 열의 전투 종료 간 관계도 검토한다."
```

## ST_Fear — 공포

```yaml
id: "ST_Fear"
type: "combat_status_effect"
name: "공포"
allowed_target: "survivor"
duration: {"status": "REVIEW_REQUIRED", "model_candidates": []}
stacking: {"status": "REVIEW_REQUIRED"}
clear_conditions: {"status": "REVIEW_REQUIRED", "source_terms": ["종료", "대기", "간호"]}
effects: {"status": "REVIEW_REQUIRED", "identity": "Combat Fear Runtime Status"}
application: {"status": "REVIEW_REQUIRED", "source_giver": "공포스러운 외침", "consumer_references": []}
persistence: {"status": "REVIEW_REQUIRED"}
special_effect: {"id": null, "status": "REVIEW_REQUIRED"}
legacy: {"source": "MECH_Status_Effect_DB v1.1.0 / SECTION 1 general", "original_kind": "전투기벽", "original_effect": "피격마다 영구 기벽 +1", "original_clear": "종료/대기/간호", "balance_status": "LEGACY_BALANCE", "kind": "combat_quirk"}
review_note: "Combat Status 유지와 Fear Runtime 정체성은 Director 승인 방향이다. Legacy 피격별 영구 기벽 증가는 현행 규칙이 아니다. Status는 Quirk 추가·Stack 증가·DB 수정·영구 기벽 직접 변경을 수행하지 않는다. 외부 평가 입력 후보만 전달하며 획득·변화 조건은 Quirk Owner가 결정한다. Fear Modifier·행동 제한·Check 영향은 REVIEW_REQUIRED."
quirk_boundary: {"direct_mutation": false, "transfer_candidate": "Combat Result / Event → Quirk System", "evaluation_owner": "Quirk System"}
```

## ST_Cower — 움츠러듬

```yaml
id: "ST_Cower"
type: "combat_status_effect"
name: "움츠러듬"
allowed_target: "survivor"
duration: {"status": "REBALANCE_REQUIRED", "model_candidates": ["Timed"]}
stacking: {"status": "REVIEW_REQUIRED"}
clear_conditions: {"status": "REVIEW_REQUIRED", "source_terms": ["1턴 후"]}
effects: {"status": "REVIEW_REQUIRED", "candidates": ["Action Restriction"]}
application: {"status": "REVIEW_REQUIRED", "source_giver": "외치기", "consumer_references": [{"action_id": "SK_Base_Threaten", "reference": "declared_effect"}, {"action_id": "SK_Shout", "reference": "declared_effect"}]}
persistence: {"status": "REVIEW_REQUIRED"}
special_effect: {"id": null, "status": "REVIEW_REQUIRED"}
legacy: {"source": "MECH_Status_Effect_DB v1.1.0 / SECTION 1 general", "original_kind": "지속", "original_effect": "1턴 해당 괴물 공격 불가", "original_clear": "1턴 후", "balance_status": "LEGACY_BALANCE", "duration": "1턴"}
review_note: "해당 괴물만 공격 불가라는 대상 제한, 다른 Action 허용 범위는 REVIEW_REQUIRED. 1턴은 LEGACY_BALANCE."
```

## ST_Stun — 기절

```yaml
id: "ST_Stun"
type: "combat_status_effect"
name: "기절"
allowed_target: "survivor"
duration: {"status": "REBALANCE_REQUIRED", "model_candidates": ["Timed"]}
stacking: {"status": "REVIEW_REQUIRED"}
clear_conditions: {"status": "REVIEW_REQUIRED", "source_terms": ["1턴 후"]}
effects: {"status": "REBALANCE_REQUIRED", "candidates": ["Action Availability Restriction"]}
application: {"status": "REVIEW_REQUIRED", "source_giver": "잔혹한 처형식", "consumer_references": [{"action_id": "SK_StunGun", "reference": "REVIEW_REQUIRED candidate"}]}
persistence: {"status": "REVIEW_REQUIRED"}
special_effect: {"id": null, "status": "REVIEW_REQUIRED"}
legacy: {"source": "MECH_Status_Effect_DB v1.1.0 / SECTION 1 general", "original_kind": "지속", "original_effect": "1턴 모든 행동 불가", "original_clear": "1턴 후", "balance_status": "LEGACY_BALANCE", "duration": "1턴"}
review_note: "행동 불가의 정체성을 보존하되 Action 범위는 검토한다. 1턴은 LEGACY_BALANCE이며 Duration은 REBALANCE_REQUIRED."
```

## ST_Bleed — 출혈

```yaml
id: "ST_Bleed"
type: "combat_status_effect"
name: "출혈"
allowed_target: "survivor"
duration: {"status": "REVIEW_REQUIRED", "model_candidates": []}
stacking: {"status": "SOURCE_EXPLICIT", "model_candidate": "Stack Count", "source_meaning": "중첩 가능", "limits_and_formula_status": "REBALANCE_REQUIRED"}
clear_conditions: {"status": "REVIEW_REQUIRED", "source_terms": ["간호", "대기"]}
effects: {"status": "REBALANCE_REQUIRED", "candidates": ["Periodic Damage Request"]}
application: {"status": "REVIEW_REQUIRED", "source_giver": "찌르기", "consumer_references": [{"action_id": "SK_Stab", "reference": "declared_effect"}]}
persistence: {"status": "REVIEW_REQUIRED"}
special_effect: {"id": null, "status": "REVIEW_REQUIRED"}
legacy: {"source": "MECH_Status_Effect_DB v1.1.0 / SECTION 1 general", "original_kind": "전투기벽", "original_effect": "매 턴 고정 소량 피해. 중첩 가능(중첩 시 피해↑)", "original_clear": "간호/대기", "balance_status": "LEGACY_BALANCE", "kind": "combat_quirk"}
review_note: "출혈·지속 Damage·중첩 가능 개념을 보존한다. Damage, 발동 Timing, Stack당 증가량과 최대 Stack은 REBALANCE_REQUIRED."
```

## ST_Brand — 낙인

```yaml
id: "ST_Brand"
type: "combat_status_effect"
name: "낙인"
allowed_target: "survivor"
duration: {"status": "REVIEW_REQUIRED", "model_candidates": ["Encounter Duration", "Until Condition"]}
stacking: {"status": "SOURCE_EXPLICIT", "model_candidate": "Stack Count", "source_meaning": "중첩 수 언급; 구체 Stack 동작 검토", "limits_and_formula_status": "REBALANCE_REQUIRED"}
clear_conditions: {"status": "REVIEW_REQUIRED", "source_terms": ["피의 제사로 소비", "종료"]}
effects: {"status": "REVIEW_REQUIRED", "candidates": ["Status Marker"]}
application: {"status": "REVIEW_REQUIRED", "source_giver": "낙인새기기", "consumer_references": [{"action_id": "SK_Brandmark", "reference": "declared_effect"}]}
persistence: {"status": "REVIEW_REQUIRED"}
special_effect: {"id": null, "status": "REVIEW_REQUIRED"}
legacy: {"source": "MECH_Status_Effect_DB v1.1.0 / SECTION 1 general", "original_kind": "전투기벽", "original_effect": "자체 효과 미미(표식). 중첩 수 = '피의 제사' 위력·발동 연료", "original_clear": "피의 제사로 소비 / 종료", "balance_status": "LEGACY_BALANCE", "kind": "combat_quirk"}
review_note: "중첩 수와 소비 가능성은 Source 의미를 보존한다. 피의 제사 위력·발동 연료 연결은 Signature Migration 전까지 Legacy Reference이며 Damage 공식은 소유하지 않는다."
```

## ST_Exposed — 무방비

```yaml
id: "ST_Exposed"
type: "combat_status_effect"
name: "무방비"
allowed_target: "monster"
duration: {"status": "REVIEW_REQUIRED", "model_candidates": []}
stacking: {"status": "REVIEW_REQUIRED"}
clear_conditions: {"status": "REVIEW_REQUIRED", "source_terms": ["일시", "괴물 행동"]}
effects: {"status": "REVIEW_REQUIRED", "identity": "Vulnerability Marker", "possible_use": ["Action Requirement", "Additional Effect Gate"]}
application: {"status": "REVIEW_REQUIRED", "source_giver": "약공 누적", "consumer_references": [], "source_status": "LEGACY_REFERENCE_ONLY"}
persistence: {"status": "REVIEW_REQUIRED"}
special_effect: {"id": null, "status": "REVIEW_REQUIRED"}
legacy: {"source": "MECH_Status_Effect_DB v1.1.0 / SECTION 1 general", "original_kind": "지속", "original_effect": "회피 불가 → 개방. 강공 +2 보너스", "original_clear": "일시/괴물 행동", "balance_status": "LEGACY_BALANCE"}
review_note: "Combat Status 유지와 Vulnerability Marker 정체성은 Director 승인 방향이다. Target has ST_Exposed를 Action Requirement 또는 추가 Effect Gate로 참조할 수 있다. Light / Heavy, 강공 +2, 약공 누적, Opening Gauge 자동 적용과 회피 불가는 Legacy 전용이며 현행 규칙으로 사용하지 않는다. 사용·소비 Action, Modifier, 적용·해제, Duration은 REVIEW_REQUIRED / REBALANCE_REQUIRED."
```

## ST_Stagger — 비틀거림

```yaml
id: "ST_Stagger"
type: "combat_status_effect"
name: "비틀거림"
allowed_target: "survivor"
duration: {"status": "REBALANCE_REQUIRED", "model_candidates": ["Until Action"]}
stacking: {"status": "REVIEW_REQUIRED"}
clear_conditions: {"status": "REVIEW_REQUIRED", "source_terms": ["1행동 후"]}
effects: {"status": "REBALANCE_REQUIRED", "candidates": ["Next Action Impairment", "Check Modifier Source", "Action Quality Penalty"]}
application: {"status": "REVIEW_REQUIRED", "source_giver": "꼬리치기", "consumer_references": [{"action_id": "SK_TailSwipe", "reference": "declared_effect"}]}
persistence: {"status": "REVIEW_REQUIRED"}
special_effect: {"id": null, "status": "REVIEW_REQUIRED"}
legacy: {"source": "MECH_Status_Effect_DB v1.1.0 / SECTION 1 general", "original_kind": "지속", "original_effect": "다음 행동 주사위 −1", "original_clear": "1행동 후", "balance_status": "LEGACY_BALANCE", "duration": "1행동", "check_modifier": {"status": "REBALANCE_REQUIRED", "legacy_value": "다음 행동 주사위 −1"}}
review_note: "후보 의미만 기록한다. 다음 행동의 적용 범위·효과와 값은 REBALANCE_REQUIRED."
```

## ST_Paralysis — 마비

```yaml
id: "ST_Paralysis"
type: "combat_status_effect"
name: "마비"
allowed_target: "survivor"
duration: {"status": "REBALANCE_REQUIRED", "model_candidates": ["Timed", "Until Condition"]}
stacking: {"status": "REVIEW_REQUIRED"}
clear_conditions: {"status": "REVIEW_REQUIRED", "source_terms": ["턴 경과", "판정"]}
effects: {"status": "REVIEW_REQUIRED", "identity": "Unstable Action Execution"}
application: {"status": "REVIEW_REQUIRED", "source_giver": "스턴건", "consumer_references": [{"action_id": "SK_StunGun", "reference": "REVIEW_REQUIRED candidate"}]}
persistence: {"status": "REVIEW_REQUIRED"}
special_effect: {"id": null, "status": "REVIEW_REQUIRED"}
legacy: {"source": "MECH_Status_Effect_DB v1.1.0 / SECTION 1 general", "original_kind": "지속", "original_effect": "행동 시 일정 확률로 실패(불발). 여러 턴 잔존", "original_clear": "턴 경과/판정", "balance_status": "LEGACY_BALANCE", "duration": "여러 턴"}
review_note: "Combat Status로 유지한다. Stun은 짧은 기간의 강한 Action Availability 제한 중심이며 Paralysis는 행동 시도가 가능하지만 수행이 불안정한 Action Execution Check 중심이다. Legacy 단순 확률 RNG는 사용하지 않는다. 저항 Check 흐름은 승인 방향이며 Check Source·Requirement·Difficulty, 대상 Action, 실패 시 취소/약화, Duration·재시도는 REVIEW_REQUIRED. Check 공식은 Check System만 소유한다."
resolution_candidate: {"direction_status": "DIRECTOR_APPROVED", "flow": ["Action Attempt", "Paralysis Resistance Check", "Success → continue Action", "Failure → interrupt or cancel Action"]}
check: {"status": "REVIEW_REQUIRED", "source": "UNDEFINED", "requirement": "UNDEFINED", "difficulty": "UNDEFINED", "scope": "REVIEW_REQUIRED", "failure_outcome": "REVIEW_REQUIRED", "retry_rule": "REVIEW_REQUIRED", "formula_owner": "MECH_Check_System"}
```

## ST_Reinforce — 지원

```yaml
id: "ST_Reinforce"
type: "combat_status_effect"
name: "지원"
allowed_target: "monster"
duration: {"status": "REBALANCE_REQUIRED", "model_candidates": ["Timed", "Instant / Triggered"]}
stacking: {"status": "REVIEW_REQUIRED"}
clear_conditions: {"status": "REVIEW_REQUIRED", "source_terms": ["발동 후 소멸"]}
effects: {"status": "REVIEW_REQUIRED", "candidates": ["Delayed Encounter Effect", "Pending Reinforcement"]}
application: {"status": "REVIEW_REQUIRED", "source_giver": "지원 요청", "consumer_references": [{"action_id": "SK_CallSupport", "reference": "declared_effect"}], "reference_note": "Consumer Migration 전까지 유지되는 Legacy Reference"}
persistence: {"status": "REVIEW_REQUIRED"}
special_effect: {"id": null, "status": "REVIEW_REQUIRED"}
legacy: {"source": "MECH_Status_Effect_DB v1.1.0 / SECTION 1 general", "original_kind": "지속", "original_effect": "일정 턴 후 swarm 규모 +1 (지연 발동 자버프)", "original_clear": "발동 후 소멸", "balance_status": "LEGACY_BALANCE", "duration": "일정 턴"}
review_note: "장기적으로 Combat Status에서 제거하는 방향이 Director 승인됐다. 현행 Status Owner로 승인하지 않는다. SK_CallSupport가 ST_Reinforce를 참조하고 Encounter / Swarm Owner가 정본화되지 않아 ID와 임시 레코드를 유지한다. Consumer Migration 후 이동 여부를 반영하며 신규 Encounter ID나 지연 조건·증원 수치를 만들지 않는다."
ownership_status: "REVIEW_REQUIRED"
migration_status: "MOVE_OUT_OF_STATUS_CANDIDATE"
record_role: "Migration Stub"
target_concept: ["Pending Reinforcement", "Delayed Encounter Effect"]
migration_flow: ["SK_CallSupport", "Pending Reinforcement 생성", "Encounter Runtime 지연 처리", "조건/시간 충족", "지원군 등장"]
```

## ST_Stealth — 은신

```yaml
id: "ST_Stealth"
type: "combat_status_effect"
name: "은신"
allowed_target: "monster"
duration: {"status": "REBALANCE_REQUIRED", "model_candidates": ["Until Condition"]}
stacking: {"status": "REVIEW_REQUIRED"}
clear_conditions: {"status": "REVIEW_REQUIRED", "source_terms": ["피격", "탐색"]}
effects: {"status": "REVIEW_REQUIRED", "candidates": ["Visibility / Targetability Change"]}
application: {"status": "REVIEW_REQUIRED", "source_giver": "은밀한 잠복자", "consumer_references": []}
persistence: {"status": "REVIEW_REQUIRED"}
special_effect: {"id": null, "status": "REVIEW_REQUIRED"}
legacy: {"source": "MECH_Status_Effect_DB v1.1.0 / SECTION 1 general", "original_kind": "지속", "original_effect": "공격받지 않음. 공격 시 해제+1턴 공격력 2배", "original_clear": "피격/탐색", "balance_status": "LEGACY_BALANCE", "duration": "공격 시 해제 후 1턴 보너스"}
review_note: "은신·Targetability/Detection 정체성과 공격 시 해제 가능성을 보존한다. 원문 효과의 공격 시 해제와 해제 열의 피격/탐색 관계는 REVIEW_REQUIRED. 공격 배율은 승인하지 않는다."
```

---

# 4. Review Queue

| Status | 문제 | 필요한 Owner | 다음 결정 |
|---|---|---|---|
| ST_Fear | Runtime 유지·외부 Quirk 평가 경계 승인 | Status / Quirk / Combat Result | Modifier·행동 제한·Check 영향 및 외부 평가 입력 상세 결정; 직접 Quirk 변경 금지 |
| ST_Exposed | Vulnerability Marker 방향 승인; Legacy Light / Heavy 미사용 | Action / Status | 사용·소비 Action, Modifier, 적용·해제·Duration 결정 |
| ST_Paralysis | Action Attempt → Resistance Check 흐름 승인 | Action / Check / Status | Check Source·Requirement·Difficulty, 대상 Action, 실패 결과·Duration·재시도 결정 |
| ST_Reinforce | Status에서 Pending Reinforcement로 장기 이관 방향 승인 | Encounter / Swarm | Owner 정본화와 지연 처리 상세·Consumer Migration 결정; Stub 유지 |
| ST_Bound | 탈출·도주 제한 상세 미정 | Action / Check / Positioning | 금지 Action과 Escape Check 계약 검토 |
| ST_Pain / ST_SeverePain / ST_Stagger | Legacy Dice·Source 반감 | Check / Status | Source, 적용 범위, 수치와 지속 범위 검토 |
| ST_Cower / ST_Stun | 대상 제한과 Turn 기준 | Action / Status / Combat Runtime | 제한 범위와 Duration 확정 |
| ST_Bleed / ST_Brand | Stack·Damage·소비 연계 미정 | Damage / Status / Signature Action | Stack 규칙, Timing, 소비 계약 검토 |
| ST_Stealth | 은신 해제 조건과 공격 배율 | Detection / Check / Damage / Status | 공격·피격·탐색 해제 관계와 보너스 재검토 |

---

# 5. Action Reference Validation

DATA_Monster_Action_Catalog의 구조화 effects.status_id 및 special_effect의 상태 후보를 대조했다.
다음 9개 ID는 모두 본 Catalog의 13개 Migration Definition 안에 존재한다.

| Status ID | Action Consumer | 참조 상태 |
|---|---|---|
| ST_Bleed | SK_Stab | Definition ID 존재 확인 |
| ST_Bound | SK_Grab, SK_Bite | Definition ID 존재 확인 |
| ST_Brand | SK_Brandmark | Definition ID 존재 확인 |
| ST_Cower | SK_Base_Threaten, SK_Shout | Definition ID 존재 확인 |
| ST_Pain | SK_ClawLunge | Definition ID 존재 확인 |
| ST_Paralysis | SK_StunGun | 선택 후보; 동시 부여 규칙 아님 |
| ST_Reinforce | SK_CallSupport | Definition ID 존재 확인 |
| ST_Stagger | SK_TailSwipe | Definition ID 존재 확인 |
| ST_Stun | SK_StunGun | 선택 후보; 동시 부여 규칙 아님 |

ID가 일치한다는 검증은 개별 효과나 수치의 승인과 다르다. 신규 Consumer를 생성하지 않았다.
원문 부여처에 이름만 있는 Signature Action은 기존 명칭만 source_giver로 보존했다.

---

# 6. Optional / Legacy Boundaries

R18 / Submission Status는 이번 Definition 목록에서 제외했다.
Legacy DB가 Optional 데이터를 포함하더라도 원문 추적 목적의 참조이며 Core Runtime 의존성이 아니다.
Optional 문서나 전용 Status ID를 신규 Core 의존 관계로 등록하지 않는다.

기존 Status DB의 효과·해제 열과 전체 원문은 원본이 보존한다. 본 문서는 필요한 필드만 추적한다.
원본·Monster Action Catalog·Combat Contract·Check·Monster·Quirk·R18 문서 및 코드는 수정하지 않는다.

---

# 7. Migration Validation Summary

13개 general ID, Target, Legacy 효과·해제와 표시 분류를 원본과 대조했다.
ID 중복, Optional Status 혼입, 현행 combat_quirk 분류, 신규 Check Requirement·확률·Handler 생성은 없다.
ST_Fear Runtime·외부 평가 경계, ST_Exposed Marker, ST_Paralysis 저항 Check 흐름과
ST_Reinforce 장기 이관 방향은 승인됐다. 세부값과 Reinforce Owner·Consumer Migration은 검토 상태다.
Definition과 Runtime State를 혼합하지 않으며 본 문서는 밸런스 승인이나 Migration verification 완료 선언이 아니다.
