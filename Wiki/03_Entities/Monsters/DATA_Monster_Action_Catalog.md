---
id: DATA_Monster_Action_Catalog
title: Downfall Monster Action Catalog
type: data
authority: CURRENT_CANDIDATE
status: REVIEW
version: 1.0.0
parent:
  - MECH_Combat_Action_System
references:
  - MECH_Combat_System
  - MECH_Check_System
  - MECH_Combat_Action_Runtime_System
  - MECH_Combat_Positioning_System
  - MECH_Combat_Status_Effect_System
  - DATA_Combat_Status_Effect_Catalog
  - MECH_Status_Effect_DB
  - MONSTER_DB
  - MECH_Skill_Catalog
  - MECH_Monster_AI
summary: >
  Legacy Skill Catalog의 실행 Action 18개를 공통 계약에 맞게 구조화한 Migration 데이터.
  기존 수치와 미확정 판정을 분리하고 Monster 고유 행동 및 Passive의 후속 이관 목록을 기록한다.
last_updated: 2026-11-05
---

# Downfall Monster Action Catalog

## 1. Purpose

본 문서는 Mechanic Contract가 아니라 `MECH_Combat_Action_System`을 따르는 Monster Action Definition 데이터다.
현재 판정과 밸런스가 검증된 Runtime 데이터는 아니다. 기존 Source를 구조화하는 작업과 Gameplay 승인 상태를 구분한다.
현재 계약은 Action, Action Runtime, Positioning, Combat Status, Check와 Monster AI 각 Owner를 따른다.
`DATA_Combat_Status_Effect_Catalog`는 Status Data의 후보 문서이며 `CURRENT_CANDIDATE / REVIEW`다.
`MECH_Skill_Catalog`와 `MECH_Status_Effect_DB`는 현행 Owner가 아닌 Legacy Migration Source로 참조한다.

- 기존 `MECH_Skill_Catalog v1.3.0`은 `LEGACY ACTION ASSET SOURCE`로 보존한다.
- 모든 기존 SK_* 및 effect_id를 유지한다. 신규 ACT_* 또는 FX_*로 Rename하지 않는다.
- 알려지지 않은 Tier, Requirement, Effect 상세는 `REVIEW_REQUIRED`다. 기존 category를 Tier로 자동 변환하지 않는다.
- Batch 1 / 2 / 3의 해당 Check 필요 / 비적용 방향은 Director 승인됐다. Check가 필요한 Action의 미확정 설정은 `REBALANCE_REQUIRED`다. Difficulty, Requirement, Check Source를 임의 배정하지 않는다.
- 수치·비율·Gauge 및 수치를 포함한 Legacy Note는 `LEGACY_BALANCE`이며 현행 밸런스가 아니다.
- Role은 Source에 드러난 기능의 구조적 분류다. 복합 행동처럼 주 역할이 불명확하면 `REVIEW_REQUIRED`로 둔다.
- Range / Target은 기존 토큰을 보존한다. Range 의미와 Self Range 정규화는 Positioning Owner 검토 대상이다.
- 전투 상태효과는 Status DB ID만 참조하며 NPC의 `상태이상` Stat과 구분한다. Status DB 자체의 Legacy 효과를 승인하지 않는다.
- `special_effect`는 기존 Handler ID 참조다. 신규 Handler 구현이나 존재를 보장하지 않는다.
- Definition과 Cooldown / Usage Count 등 Runtime State는 분리한다.

## 2. Migration Data Shape

아래 YAML은 문서 Migration 표현이며 승인된 Runtime / Save Schema가 아니다. SECTION 3은 `definition` 후보와 `migration` Metadata를 논리적으로 분리한다.
`migration.previous_migration_record.legacy.source_record`는 원문 추적 자료로만 보존한다. Runtime에서 정의로 읽지 않는다.
`effects`는 원문에 명시된 단순 효과와 Director가 승인한 효과 방향을 구조화한다. Handler에만 존재하는 조건부 효과는 승인 없이 복제하거나 무조건 효과로 승격하지 않는다.
특히 스턴건의 기절/마비는 선택 조건이 미정인 후보이며 둘을 동시에 부여하는 효과가 아니다.

---

## 2.1 Priority Migration Examples

아래 3개는 동일한 공통 Schema로 검증한 우선 샘플이다. 실제 Definition은 SECTION 3에 한 번만 존재하며 예시는 해당 ID를 참조한다.

| Action ID | Role | Tier | Range / Target | 전투 상태효과 / Handler | 검토 상태 |
|---|---|---|---|---|---|
| SK_Bite | attack | basic | melee / single | ST_Bound / fx_bite_grip | Damage 1: LEGACY_BALANCE; Check: REBALANCE_REQUIRED |
| SK_Grab | control | basic | melee / single | ST_Bound / fx_grab_open_bind_gate | Check: REBALANCE_REQUIRED |
| SK_StunGun | control | REVIEW_REQUIRED | melee / single | ST_Stun 또는 ST_Paralysis 후보 / fx_stun_or_paralyze | 장비 Requirement: REVIEW_REQUIRED; Check: REBALANCE_REQUIRED |

Bite / Grab의 basic Tier는 기존 Migration 기록의 권장 해석이며 승인된 개별 Tier가 아니다. vNext에서는 검토 대상으로 보존한다. Legacy category를 Tier로 자동 변환하지 않는다.
스턴건에 장비 Requirement를 추가하는 제안은 NEW_PROPOSAL이며 현재 Definition에는 확정 조건으로 등록하지 않는다.

---

# 3. Shared Action Migration Records

각 기록의 `definition`은 미완료 정적 Definition 후보이며 `migration`은 이전 Migration Record와 검토 상태를 보존한다. 실행 데이터가 아니다. 필수 개념의 상태를 문서용 `status` / `value` / `items`로 명시한다. `SOURCE_SUPPORTED` / `SOURCE_EXPLICIT`은 Source 근거이지 Gameplay 승인이 아니다. `REVIEW_REQUIRED`와 `null`은 미확정이며 없음이나 비적용이 아니다. 명시된 빈 Requirement 목록은 Source의 Action별 조건 없음만 기록하며 다른 Owner의 Eligibility를 면제하지 않는다. Position의 `UNDEFINED`는 적용 여부 미정이며 빈 Band 목록이나 모든 Band 허용이 아니다. 이 표현은 Migration Document Shape이며 Runtime / Save Schema나 C# DTO가 아니다. Legacy Target / Range / Handler는 `migration.previous_migration_record`에 보존한다. `self`는 Source-supported Target 후보이며 Position Independent를 의미하지 않는다. Effect의 문서 순서는 Source Order 보존이며 Runtime 실행 우선순위가 아니다.

이 문서 표현에서 `NOT_APPLICABLE`은 명시적으로 비적용임을 나타내는 상태로, 미확정 `REVIEW_REQUIRED`와 구분한다. Position은 별도 검토 결과에 따라 비적용, 적용 및 Band 미정, 적용 및 Band 확인, 적용 여부 미정으로 구분할 수 있다. 이번 Cleanup에서는 어떤 Action에도 비적용이나 Band를 확정하지 않는다. `items: null`은 미확정이며, 확인된 조건 / 효과 없음은 근거가 있는 상태와 빈 목록을 함께 사용해 구분한다. Owner가 제공하는 Eligibility는 별도 참조 개념이며 비어 있는 Action별 조건 목록에 흡수하지 않는다.

## SK_Base_Strike — 맨손 타격

```yaml
{
  "definition": {
    "id": "SK_Base_Strike",
    "name": "맨손 타격",
    "role": {
      "status": "DIRECTOR_APPROVED",
      "value": "attack"
    },
    "target_rule": {
      "status": "DIRECTOR_APPROVED",
      "value": "single_enemy"
    },
    "position": {
      "status": "DIRECTOR_APPROVED",
      "applicability": "APPLICABLE",
      "actor_bands": {
        "status": "NO_ADDITIONAL_ACTION_SPECIFIC_RESTRICTION",
        "general_eligibility_applies": true
      },
      "target_bands": {
        "status": "DIRECTOR_APPROVED",
        "values": [
          "Close"
        ]
      }
    },
    "requirements": {
      "status": "DIRECTOR_APPROVED",
      "items": [
        {
          "type": "weapon_not_required"
        }
      ],
      "general_eligibility_applies": true
    },
    "effects": {
      "status": "DIRECTOR_APPROVED_DIRECTION",
      "items": [
        {
          "type": "damage"
        }
      ]
    },
    "check": {
      "status": "REQUIRED",
      "configuration_status": "REBALANCE_REQUIRED",
      "source": {
        "status": "DIRECTOR_APPROVED",
        "value": "Combat"
      }
    }
  },
  "migration": {
    "review": {
      "record_state": "INCOMPLETE_MIGRATION_RECORD",
      "role": "DIRECTOR_APPROVED",
      "tier": "REVIEW_REQUIRED",
      "target_rule": "DIRECTOR_APPROVED",
      "position_applicability": "DIRECTOR_APPROVED",
      "actor_bands": "NO_ADDITIONAL_ACTION_SPECIFIC_RESTRICTION",
      "target_bands": "DIRECTOR_APPROVED",
      "requirements": "DIRECTOR_APPROVED_DIRECTION",
      "effects": "DIRECTOR_APPROVED_DIRECTION",
      "check": "DIRECTOR_APPROVED_REQUIRED_AND_SOURCE_NUMERIC_CONFIGURATION_REBALANCE_REQUIRED",
      "cooldown": "REBALANCE_REQUIRED",
      "damage": "LEGACY_BALANCE",
      "source_order": "SOURCE_ORDER_PRESERVED_NO_RUNTIME_PRIORITY"
    },
    "previous_migration_record": {
      "id": "SK_Base_Strike",
      "type": "combat_action",
      "name": "맨손 타격",
      "role": "attack",
      "tier": "REVIEW_REQUIRED",
      "range": "melee",
      "target": "single",
      "requirements": {
        "status": "SOURCE_EXPLICIT",
        "constraints": [],
        "note": "SECTION 2-0: 무제약·맨몸, 무장 해제되어도 사용 가능."
      },
      "check": {
        "status": "REBALANCE_REQUIRED"
      },
      "effects": [
        {
          "type": "damage",
          "value": {
            "status": "LEGACY_BALANCE",
            "legacy_value": 1
          }
        }
      ],
      "special_effect": {
        "id": null
      },
      "presentation": {
        "legacy_log": "{ on_use: [\"놈이 주먹을 휘둘렀다.\"], on_hit: [\"둔한 충격이 스쳤다.\"] }"
      },
      "legacy": {
        "source": "MECH_Skill_Catalog v1.3.0 / SECTION 2",
        "category": "light",
        "balance_status": "LEGACY_BALANCE",
        "source_record": "- id: SK_Base_Strike\n  name: 맨손 타격\n  category: light\n  range: melee\n  target: single\n  damage: 1                            # 약함. 무기 무관(맨몸) — 무장 해제돼도 사용 가능\n  effect_id: null\n  log: { on_use: [\"놈이 주먹을 휘둘렀다.\"], on_hit: [\"둔한 충격이 스쳤다.\"] }\n",
        "mechanics_review_status": "REBALANCE_REQUIRED"
      }
    }
  }
}
```

## SK_Base_Threaten — 위협·조롱

```yaml
{
  "definition": {
    "id": "SK_Base_Threaten",
    "name": "위협·조롱",
    "role": {
      "status": "DIRECTOR_APPROVED",
      "value": "control"
    },
    "target_rule": {
      "status": "DIRECTOR_APPROVED",
      "value": "single_enemy"
    },
    "position": {
      "status": "DIRECTOR_APPROVED",
      "applicability": "APPLICABLE",
      "actor_bands": {
        "status": "NO_ADDITIONAL_ACTION_SPECIFIC_RESTRICTION",
        "general_eligibility_applies": true
      },
      "target_bands": {
        "status": "DIRECTOR_APPROVED",
        "values": [
          "Close",
          "Mid"
        ]
      }
    },
    "requirements": {
      "status": "DIRECTOR_APPROVED",
      "items": [
        {
          "type": "weapon_not_required"
        }
      ],
      "general_eligibility_applies": true
    },
    "effects": {
      "status": "DIRECTOR_APPROVED_DIRECTION",
      "items": [
        {
          "type": "apply_combat_status",
          "status_id": "ST_Cower",
          "resolution_condition": "check_success"
        }
      ]
    },
    "check": {
      "status": "REQUIRED",
      "configuration_status": "REBALANCE_REQUIRED",
      "source": {
        "status": "DIRECTOR_APPROVED",
        "value": "Dialogue"
      }
    }
  },
  "migration": {
    "review": {
      "record_state": "INCOMPLETE_MIGRATION_RECORD",
      "role": "DIRECTOR_APPROVED",
      "tier": "REVIEW_REQUIRED",
      "target_rule": "DIRECTOR_APPROVED",
      "position_applicability": "DIRECTOR_APPROVED",
      "actor_bands": "NO_ADDITIONAL_ACTION_SPECIFIC_RESTRICTION",
      "target_bands": "DIRECTOR_APPROVED",
      "requirements": "DIRECTOR_APPROVED_DIRECTION",
      "effects": "DIRECTOR_APPROVED_DIRECTION",
      "check": "DIRECTOR_APPROVED_REQUIRED_AND_SOURCE_NUMERIC_CONFIGURATION_REBALANCE_REQUIRED",
      "cooldown": "REBALANCE_REQUIRED",
      "damage": "LEGACY_BALANCE",
      "source_order": "SOURCE_ORDER_PRESERVED_NO_RUNTIME_PRIORITY"
    },
    "previous_migration_record": {
      "id": "SK_Base_Threaten",
      "type": "combat_action",
      "name": "위협·조롱",
      "role": "control",
      "tier": "REVIEW_REQUIRED",
      "range": "mid",
      "target": "single",
      "requirements": {
        "status": "SOURCE_EXPLICIT",
        "constraints": [],
        "note": "SECTION 2-0: 무제약·맨몸, 무장 해제되어도 사용 가능."
      },
      "check": {
        "status": "REBALANCE_REQUIRED"
      },
      "effects": [
        {
          "type": "apply_combat_status",
          "status_id": "ST_Cower"
        }
      ],
      "special_effect": {
        "id": null
      },
      "presentation": {
        "legacy_log": "{ on_use: [\"놈이 이죽거리며 위협했다.\"] }"
      },
      "legacy": {
        "source": "MECH_Skill_Catalog v1.3.0 / SECTION 2",
        "category": "light",
        "balance_status": "LEGACY_BALANCE",
        "source_record": "- id: SK_Base_Threaten\n  name: 위협·조롱\n  category: light\n  range: mid\n  target: single\n  status_inflict: [ST_Cower]           # 약한 움츠러듬 시도. 자원 소모 없음\n  effect_id: null\n  log: { on_use: [\"놈이 이죽거리며 위협했다.\"] }\n",
        "mechanics_review_status": "REBALANCE_REQUIRED"
      }
    }
  }
}
```

## SK_Base_Brace — 경계

```yaml
{
  "definition": {
    "id": "SK_Base_Brace",
    "name": "경계",
    "role": {
      "status": "DIRECTOR_APPROVED",
      "value": "defense"
    },
    "target_rule": {
      "status": "DIRECTOR_APPROVED",
      "value": "self"
    },
    "position": {
      "status": "DIRECTOR_APPROVED",
      "applicability": "NOT_APPLICABLE",
      "general_eligibility_applies": true
    },
    "requirements": {
      "status": "DIRECTOR_APPROVED",
      "items": [],
      "scope": "NO_ACTION_SPECIFIC_REQUIREMENT",
      "general_eligibility_applies": true
    },
    "effects": {
      "status": "DIRECTOR_APPROVED_DIRECTION",
      "items": [
        {
          "type": "defensive_mitigation",
          "trigger": "subsequent_valid_hit",
          "details_status": "MITIGATION_AMOUNT_FORMULA_TIMING_AND_REFRESH_REVIEW_REQUIRED",
          "lifecycle": {
            "status": "DIRECTOR_APPROVED",
            "pending_until_first_of": [
              "next_valid_incoming_hit",
              "start_of_actors_next_activation"
            ],
            "on_first_valid_incoming_hit": "apply_mitigation_and_consume",
            "if_next_activation_begins_first": "expire_without_hit",
            "stacking": "NON_STACKING",
            "repeated_use_behavior": "UNDEFINED",
            "runtime_storage_model": "UNDEFINED"
          }
        }
      ]
    },
    "check": {
      "status": "NOT_APPLICABLE"
    }
  },
  "migration": {
    "review": {
      "record_state": "INCOMPLETE_MIGRATION_RECORD",
      "role": "DIRECTOR_APPROVED",
      "tier": "REVIEW_REQUIRED",
      "target_rule": "DIRECTOR_APPROVED",
      "position_applicability": "DIRECTOR_APPROVED",
      "actor_bands": "NOT_APPLICABLE",
      "target_bands": "NOT_APPLICABLE",
      "requirements": "DIRECTOR_APPROVED_DIRECTION",
      "effects": "DIRECTOR_APPROVED_DIRECTION",
      "check": "DIRECTOR_APPROVED_NOT_APPLICABLE",
      "cooldown": "REBALANCE_REQUIRED",
      "damage": "LEGACY_BALANCE",
      "source_order": "SOURCE_ORDER_PRESERVED_NO_RUNTIME_PRIORITY",
      "risk": "Legacy fx_base_brace gauge, next action and numeric mitigation remain LEGACY / REWORK_REQUIRED; approved lifecycle; mitigation value, runtime storage and repeated-use behavior UNDEFINED"
    },
    "previous_migration_record": {
      "id": "SK_Base_Brace",
      "type": "combat_action",
      "name": "경계",
      "role": "defense",
      "tier": "REVIEW_REQUIRED",
      "range": "self",
      "target": "self",
      "requirements": {
        "status": "SOURCE_EXPLICIT",
        "constraints": [],
        "note": "SECTION 2-0: 무제약·맨몸, 무장 해제되어도 사용 가능."
      },
      "check": {
        "status": "REBALANCE_REQUIRED"
      },
      "effects": [
        {
          "status": "REVIEW_REQUIRED",
          "note": "단순 효과 미기재. 기존 special_effect 참조 및 원문을 검토한다."
        }
      ],
      "special_effect": {
        "id": "fx_base_brace",
        "status": "REVIEW_REQUIRED",
        "note": "기존 ID 보존. Handler 구현 및 현행 Effect 분해는 후속 검토."
      },
      "presentation": {
        "legacy_log": "{ on_use: [\"놈이 자세를 낮추고 경계했다.\"] }"
      },
      "legacy": {
        "source": "MECH_Skill_Catalog v1.3.0 / SECTION 2",
        "category": "light",
        "balance_status": "LEGACY_BALANCE",
        "source_record": "- id: SK_Base_Brace\n  name: 경계\n  category: light\n  range: self\n  target: self\n  effect_id: fx_base_brace             # 피해 무효 아님 — 다음 피격 피해 감소 + 다음 행동/게이지 영향\n  log: { on_use: [\"놈이 자세를 낮추고 경계했다.\"] }\n",
        "mechanics_review_status": "REBALANCE_REQUIRED"
      },
      "balance_review": {
        "status": "REBALANCE_REQUIRED",
        "topics": [
          "damage_reduction",
          "gauge_interaction"
        ]
      }
    }
  }
}
```

## SK_Base_Backstep — 거리 벌리기

```yaml
{
  "definition": {
    "id": "SK_Base_Backstep",
    "name": "거리 벌리기",
    "role": {
      "status": "DIRECTOR_APPROVED",
      "value": "movement"
    },
    "target_rule": {
      "status": "DIRECTOR_APPROVED",
      "value": "self"
    },
    "position": {
      "status": "DIRECTOR_APPROVED",
      "applicability": "APPLICABLE",
      "mode": "movement_based",
      "actor_bands": "REVIEW_REQUIRED",
      "target_bands": "REVIEW_REQUIRED"
    },
    "requirements": {
      "status": "DIRECTOR_APPROVED_DIRECTION",
      "items": [
        {
          "type": "owner_provided_actor_action_capable_eligibility",
          "status": "DIRECTOR_APPROVED"
        },
        {
          "type": "owner_provided_movement_eligibility",
          "owners": [
            "MECH_Combat_Positioning_System",
            "MECH_Combat_Action_Runtime_System",
            "relevant Status / Runtime Owners"
          ],
          "status": "DIRECTOR_APPROVED",
          "meaning": "movement_available"
        },
        {
          "type": "backward_band_exists",
          "status": "DIRECTOR_APPROVED",
          "far": "ELIGIBILITY_FALSE_NOT_CHECK_FAILURE"
        }
      ],
      "survivor_frontline_anchor": "NOT_APPLICABLE_TO_MONSTER_BACKSTEP",
      "scope": "SK_Base_Backstep and monster basic backstep",
      "combination": "ALL_REQUIRED"
    },
    "effects": {
      "status": "DIRECTOR_APPROVED_DIRECTION",
      "items": [
        {
          "type": "move",
          "target": "self",
          "direction": "backward",
          "bands": 1,
          "transitions": [
            "Close to Mid",
            "Mid to Far"
          ],
          "far": "NO_BACKWARD_BAND",
          "universal_dodge": false
        }
      ]
    },
    "check": {
      "status": "NOT_APPLICABLE"
    }
  },
  "migration": {
    "review": {
      "record_state": "INCOMPLETE_MIGRATION_RECORD",
      "role": "DIRECTOR_APPROVED",
      "tier": "REVIEW_REQUIRED",
      "target_rule": "DIRECTOR_APPROVED",
      "position_applicability": "DIRECTOR_APPROVED",
      "actor_bands": "REVIEW_REQUIRED",
      "target_bands": "REVIEW_REQUIRED",
      "requirements": "DIRECTOR_APPROVED_DIRECTION",
      "effects": "DIRECTOR_APPROVED_DIRECTION",
      "check": "DIRECTOR_APPROVED_NOT_APPLICABLE",
      "cooldown": "REBALANCE_REQUIRED",
      "damage": "LEGACY_BALANCE",
      "source_order": "SOURCE_ORDER_PRESERVED_NO_RUNTIME_PRIORITY",
      "risk": "Approved actor action-capable, movement available and backward band exists use owner-provided eligibility; no Survivor Frontline Anchor for monster basic backstep; fx_base_backstep remains legacy; technical runtime implementation UNDEFINED"
    },
    "previous_migration_record": {
      "id": "SK_Base_Backstep",
      "type": "combat_action",
      "name": "거리 벌리기",
      "role": "movement",
      "tier": "REVIEW_REQUIRED",
      "range": "self",
      "target": "self",
      "requirements": {
        "status": "SOURCE_EXPLICIT",
        "constraints": [],
        "note": "SECTION 2-0: 무제약·맨몸, 무장 해제되어도 사용 가능."
      },
      "check": {
        "status": "REBALANCE_REQUIRED"
      },
      "effects": [
        {
          "status": "REVIEW_REQUIRED",
          "note": "단순 효과 미기재. 기존 special_effect 참조 및 원문을 검토한다."
        }
      ],
      "special_effect": {
        "id": "fx_base_backstep",
        "status": "REVIEW_REQUIRED",
        "note": "기존 ID 보존. Handler 구현 및 현행 Effect 분해는 후속 검토."
      },
      "presentation": {
        "legacy_log": "{ on_use: [\"놈이 한 걸음 물러섰다.\"] }"
      },
      "legacy": {
        "source": "MECH_Skill_Catalog v1.3.0 / SECTION 2",
        "category": "light",
        "balance_status": "LEGACY_BALANCE",
        "source_record": "- id: SK_Base_Backstep\n  name: 거리 벌리기\n  category: light\n  range: self\n  target: self\n  effect_id: fx_base_backstep          # 1밴드 후퇴(회피성) — 근접 피격 위험↓, 다음 접근 필요\n  log: { on_use: [\"놈이 한 걸음 물러섰다.\"] }",
        "mechanics_review_status": "REBALANCE_REQUIRED"
      },
      "balance_review": {
        "status": "REBALANCE_REQUIRED",
        "topics": [
          "position_band_change"
        ]
      }
    }
  }
}
```

## SK_Swing — 휘두르기

```yaml
{
  "definition": {
    "id": "SK_Swing",
    "name": "휘두르기",
    "role": {
      "status": "DIRECTOR_APPROVED",
      "value": "attack"
    },
    "target_rule": {
      "status": "DIRECTOR_APPROVED",
      "value": "single_enemy"
    },
    "position": {
      "status": "DIRECTOR_APPROVED",
      "applicability": "APPLICABLE",
      "actor_bands": {
        "status": "NO_ADDITIONAL_ACTION_SPECIFIC_RESTRICTION",
        "general_eligibility_applies": true
      },
      "target_bands": {
        "status": "DIRECTOR_APPROVED",
        "values": [
          "Close"
        ]
      }
    },
    "requirements": {
      "status": "DIRECTOR_APPROVED",
      "items": [
        {
          "type": "equipment_requirement",
          "condition": "weapon_held"
        }
      ],
      "scope": "WEAPON_HELD_REQUIRED",
      "general_eligibility_applies": true
    },
    "effects": {
      "status": "DIRECTOR_APPROVED_DIRECTION",
      "items": [
        {
          "type": "damage",
          "equipped_weapon_context": "MAY_BE_PROVIDED_TO_DAMAGE_RESOLVER",
          "weapon_properties_owner": "Weapon / Item Owner",
          "weapon_values": "PROVIDED_BY_OWNER_NOT_COPIED",
          "runtime_call_order": "TECH_SPEC_UNDEFINED"
        }
      ]
    },
    "check": {
      "status": "REQUIRED",
      "source": {
        "status": "DIRECTOR_APPROVED",
        "value": "Combat"
      },
      "configuration_status": "REBALANCE_REQUIRED"
    }
  },
  "migration": {
    "review": {
      "record_state": "INCOMPLETE_MIGRATION_RECORD",
      "role": "DIRECTOR_APPROVED",
      "tier": "REVIEW_REQUIRED",
      "target_rule": "DIRECTOR_APPROVED",
      "position_applicability": "DIRECTOR_APPROVED",
      "actor_bands": "NO_ADDITIONAL_ACTION_SPECIFIC_RESTRICTION",
      "target_bands": "DIRECTOR_APPROVED",
      "requirements": "DIRECTOR_APPROVED_DIRECTION",
      "effects": "DIRECTOR_APPROVED_DIRECTION",
      "check": "DIRECTOR_APPROVED_REQUIRED_AND_SOURCE_NUMERIC_CONFIGURATION_REBALANCE_REQUIRED",
      "cooldown": "REBALANCE_REQUIRED",
      "damage": "LEGACY_BALANCE",
      "source_order": "SOURCE_ORDER_PRESERVED_NO_RUNTIME_PRIORITY",
      "risk": "Weapon / Item Owner provides damage, properties and modifiers; weapon integration and numeric values pending; legacy damage LEGACY_BALANCE"
    },
    "previous_migration_record": {
      "id": "SK_Swing",
      "type": "combat_action",
      "name": "휘두르기",
      "role": "attack",
      "tier": "REVIEW_REQUIRED",
      "range": "melee",
      "target": "single",
      "requirements": {
        "status": "SOURCE_EXPLICIT",
        "conditions": [
          {
            "type": "equipment_requirement",
            "condition": "weapon_held"
          }
        ]
      },
      "check": {
        "status": "REBALANCE_REQUIRED"
      },
      "effects": [
        {
          "type": "damage",
          "value": {
            "status": "LEGACY_BALANCE",
            "legacy_value": 1
          }
        }
      ],
      "special_effect": {
        "id": null
      },
      "presentation": {
        "legacy_log": "{ on_use: [\"놈이 무기를 치켜들었다.\"], on_hit: [\"둔탁한 충격이 파고들었다.\"] }"
      },
      "legacy": {
        "source": "MECH_Skill_Catalog v1.3.0 / SECTION 2",
        "category": "light",
        "balance_status": "LEGACY_BALANCE",
        "source_record": "- id: SK_Swing\n  name: 휘두르기\n  category: light\n  range: melee\n  target: single\n  damage: 1\n  lock_condition: weapon_held        # 무장 시만 — 무장 해제 시 잠김\n  effect_id: null\n  log: { on_use: [\"놈이 무기를 치켜들었다.\"], on_hit: [\"둔탁한 충격이 파고들었다.\"] }\n",
        "mechanics_review_status": "REBALANCE_REQUIRED"
      }
    }
  }
}
```

## SK_Shout — 외치기

```yaml
{
  "definition": {
    "id": "SK_Shout",
    "name": "외치기",
    "role": {
      "status": "DIRECTOR_APPROVED",
      "value": "control"
    },
    "target_rule": {
      "status": "DIRECTOR_APPROVED",
      "value": "multiple_enemies_aoe"
    },
    "position": {
      "status": "DIRECTOR_APPROVED",
      "applicability": "APPLICABLE",
      "actor_bands": {
        "status": "NO_ADDITIONAL_ACTION_SPECIFIC_RESTRICTION",
        "general_eligibility_applies": true
      },
      "target_bands": {
        "status": "DIRECTOR_APPROVED",
        "values": [
          "Close",
          "Mid"
        ]
      }
    },
    "requirements": {
      "status": "DIRECTOR_APPROVED",
      "items": [],
      "scope": "NO_ACTION_SPECIFIC_REQUIREMENT",
      "general_eligibility_applies": true
    },
    "effects": {
      "status": "DIRECTOR_APPROVED_DIRECTION",
      "items": [
        {
          "type": "apply_combat_status",
          "status_id": "ST_Cower",
          "resolution_condition": "check_success",
          "targets": "ALL_VALID_CLOSE_MID_ENEMIES",
          "application_owner": "MECH_Combat_Status_Effect_System",
          "actual_application": "STATUS_OWNER_DETERMINES_APPLICABILITY",
          "check_failure": "NO_STATUS_APPLICATION_REQUESTS"
        }
      ]
    },
    "check": {
      "status": "REQUIRED",
      "source": {
        "status": "DIRECTOR_APPROVED",
        "value": "Dialogue"
      },
      "configuration_status": "REBALANCE_REQUIRED",
      "roll_scope": "ONE_ACTION_CHECK_NOT_PER_TARGET"
    }
  },
  "migration": {
    "review": {
      "record_state": "INCOMPLETE_MIGRATION_RECORD",
      "role": "DIRECTOR_APPROVED",
      "tier": "REVIEW_REQUIRED",
      "target_rule": "DIRECTOR_APPROVED",
      "position_applicability": "DIRECTOR_APPROVED",
      "actor_bands": "NO_ADDITIONAL_ACTION_SPECIFIC_RESTRICTION",
      "target_bands": "DIRECTOR_APPROVED",
      "requirements": "DIRECTOR_APPROVED_DIRECTION",
      "effects": "DIRECTOR_APPROVED_DIRECTION",
      "check": "DIRECTOR_APPROVED_REQUIRED_AND_SOURCE_NUMERIC_CONFIGURATION_REBALANCE_REQUIRED",
      "cooldown": "REBALANCE_REQUIRED",
      "damage": "LEGACY_BALANCE",
      "source_order": "SOURCE_ORDER_PRESERVED_NO_RUNTIME_PRIORITY",
      "risk": "Legacy fx_shout_summon_or_cower reinforcement branch REWORK_REQUIRED; separate future Action / Encounter / Swarm ownership review; max target count, ordering, falloff and status resistance remain UNDEFINED"
    },
    "previous_migration_record": {
      "id": "SK_Shout",
      "type": "combat_action",
      "name": "외치기",
      "role": "REVIEW_REQUIRED",
      "tier": "REVIEW_REQUIRED",
      "range": "mid",
      "target": "aoe",
      "requirements": {
        "status": "REVIEW_REQUIRED",
        "reason": "Source에 사용 조건이 명시되지 않음. 장비 등 추가 조건을 추론하지 않는다."
      },
      "check": {
        "status": "REBALANCE_REQUIRED"
      },
      "effects": [
        {
          "type": "apply_combat_status",
          "status_id": "ST_Cower"
        }
      ],
      "special_effect": {
        "id": "fx_shout_summon_or_cower",
        "status": "REVIEW_REQUIRED",
        "note": "기존 ID 보존. Handler 구현 및 현행 Effect 분해는 후속 검토."
      },
      "presentation": {
        "legacy_log": "{ on_use: [\"놈이 목청껏 동료를 불렀다.\"], on_hit: [\"고함이 신경을 긁었다.\"] }"
      },
      "legacy": {
        "source": "MECH_Skill_Catalog v1.3.0 / SECTION 2",
        "category": "light",
        "balance_status": "LEGACY_BALANCE",
        "source_record": "- id: SK_Shout\n  name: 외치기\n  category: light\n  range: mid\n  target: aoe\n  status_inflict: [움츠러듬]\n  effect_id: fx_shout_summon_or_cower  # swarm 규모+1(동료 호출) 또는 일대 움츠러듬 — 조건부\n  log: { on_use: [\"놈이 목청껏 동료를 불렀다.\"], on_hit: [\"고함이 신경을 긁었다.\"] }\n",
        "mechanics_review_status": "REBALANCE_REQUIRED"
      },
      "balance_review": {
        "status": "REBALANCE_REQUIRED",
        "topics": [
          "swarm_size_change"
        ]
      }
    }
  }
}
```

## SK_Grab — 붙잡기

```yaml
{
  "definition": {
    "id": "SK_Grab",
    "name": "붙잡기",
    "role": {
      "status": "DIRECTOR_APPROVED",
      "value": "control"
    },
    "target_rule": {
      "status": "DIRECTOR_APPROVED",
      "value": "single_enemy"
    },
    "position": {
      "status": "DIRECTOR_APPROVED",
      "applicability": "APPLICABLE",
      "actor_bands": {
        "status": "NO_ADDITIONAL_ACTION_SPECIFIC_RESTRICTION",
        "general_eligibility_applies": true
      },
      "target_bands": {
        "status": "DIRECTOR_APPROVED",
        "values": [
          "Close"
        ]
      }
    },
    "requirements": {
      "status": "DIRECTOR_APPROVED",
      "items": [
        {
          "type": "action_specific_equipment_not_required"
        }
      ],
      "scope": "NO_ACTION_SPECIFIC_EQUIPMENT_REQUIREMENT",
      "general_eligibility_applies": true
    },
    "effects": {
      "status": "DIRECTOR_APPROVED_DIRECTION",
      "items": [
        {
          "type": "apply_combat_status",
          "status_id": "ST_Bound",
          "resolution_condition": "check_success",
          "follow_up": "ACTION_ENDS_NO_AUTOMATIC_PREPARED_TELEGRAPH_OR_FOLLOW_UP",
          "later_bound_relationship": "MAY_ENABLE_LATER_ACTIONS_THROUGH_NORMAL_ELIGIBILITY_AND_AI_SELECTION"
        }
      ]
    },
    "check": {
      "status": "REQUIRED",
      "source": {
        "status": "DIRECTOR_APPROVED",
        "value": "Combat"
      },
      "configuration_status": "REBALANCE_REQUIRED"
    }
  },
  "migration": {
    "review": {
      "record_state": "INCOMPLETE_MIGRATION_RECORD",
      "role": "DIRECTOR_APPROVED",
      "tier": "REVIEW_REQUIRED",
      "target_rule": "DIRECTOR_APPROVED",
      "position_applicability": "DIRECTOR_APPROVED",
      "actor_bands": "NO_ADDITIONAL_ACTION_SPECIFIC_RESTRICTION",
      "target_bands": "DIRECTOR_APPROVED",
      "requirements": "DIRECTOR_APPROVED_DIRECTION",
      "effects": "DIRECTOR_APPROVED_DIRECTION",
      "check": "DIRECTOR_APPROVED_REQUIRED_AND_SOURCE_NUMERIC_CONFIGURATION_REBALANCE_REQUIRED",
      "cooldown": "REBALANCE_REQUIRED",
      "damage": "LEGACY_BALANCE",
      "source_order": "SOURCE_ORDER_PRESERVED_NO_RUNTIME_PRIORITY",
      "risk": "Legacy Gate B remains legacy / REWORK_REQUIRED; Grab applies ST_Bound only and does not automatically create Prepared, telegraph, reserved follow-up or guaranteed combo"
    },
    "previous_migration_record": {
      "id": "SK_Grab",
      "type": "combat_action",
      "name": "붙잡기",
      "role": "control",
      "tier": "basic",
      "range": "melee",
      "target": "single",
      "requirements": {
        "status": "REVIEW_REQUIRED",
        "reason": "Source에 사용 조건이 명시되지 않음. 장비 등 추가 조건을 추론하지 않는다."
      },
      "check": {
        "status": "REBALANCE_REQUIRED"
      },
      "effects": [
        {
          "type": "apply_combat_status",
          "status_id": "ST_Bound"
        }
      ],
      "special_effect": {
        "id": "fx_grab_open_bind_gate",
        "status": "REVIEW_REQUIRED",
        "note": "기존 ID 보존. Handler 구현 및 현행 Effect 분해는 후속 검토."
      },
      "presentation": {
        "legacy_log": "{ on_use: [\"놈이 손을 뻗어 붙들려 했다.\"], on_hit: [\"억센 손아귀가 팔을 옭아맸다.\"] }"
      },
      "legacy": {
        "source": "MECH_Skill_Catalog v1.3.0 / SECTION 2",
        "category": "light",
        "balance_status": "LEGACY_BALANCE",
        "source_record": "- id: SK_Grab\n  name: 붙잡기\n  category: light\n  range: melee\n  target: single\n  status_inflict: [속박됨]\n  effect_id: fx_grab_open_bind_gate    # 회피 실패 시 [속박] → 게이트 B 개방\n  log: { on_use: [\"놈이 손을 뻗어 붙들려 했다.\"], on_hit: [\"억센 손아귀가 팔을 옭아맸다.\"] }\n",
        "mechanics_review_status": "REBALANCE_REQUIRED"
      },
      "balance_review": {
        "status": "REBALANCE_REQUIRED",
        "topics": [
          "opening_gate_interaction"
        ]
      }
    }
  }
}
```

## SK_LootEquip — 장비 약탈

```yaml
{
  "definition": {
    "id": "SK_LootEquip",
    "name": "장비 약탈",
    "role": {
      "status": "DIRECTOR_APPROVED",
      "value": "control"
    },
    "target_rule": {
      "status": "DIRECTOR_APPROVED",
      "value": "single_enemy"
    },
    "position": {
      "status": "DIRECTOR_APPROVED",
      "applicability": "APPLICABLE",
      "actor_bands": {
        "status": "NO_ADDITIONAL_ACTION_SPECIFIC_RESTRICTION",
        "general_eligibility_applies": true
      },
      "target_bands": {
        "status": "DIRECTOR_APPROVED",
        "values": [
          "Close"
        ]
      }
    },
    "requirements": {
      "status": "DIRECTOR_APPROVED",
      "items": [
        {
          "type": "target_requirement",
          "combat_status_id": "ST_Bound"
        },
        {
          "type": "target_has_removable_equipment",
          "owner": "Item / Equipment Owner",
          "evaluation": "OWNER_PROVIDED_REMOVABLE_EQUIPMENT_ELIGIBILITY"
        }
      ],
      "scope": "ALL_REQUIRED",
      "general_eligibility_applies": true,
      "failure": "ELIGIBILITY_FALSE_NOT_CHECK_FAILURE",
      "inventory_inspection": "ITEM_EQUIPMENT_OWNER_RESPONSIBILITY"
    },
    "effects": {
      "status": "DIRECTOR_APPROVED_DIRECTION",
      "items": [
        {
          "type": "equipment_removal_or_transfer_request",
          "resolution_condition": "check_success",
          "owner": "Item / Equipment Owner"
        }
      ]
    },
    "check": {
      "status": "REQUIRED",
      "source": {
        "status": "DIRECTOR_APPROVED",
        "value": "Technique"
      },
      "configuration_status": "REBALANCE_REQUIRED"
    }
  },
  "migration": {
    "review": {
      "record_state": "INCOMPLETE_MIGRATION_RECORD",
      "role": "DIRECTOR_APPROVED",
      "tier": "REVIEW_REQUIRED",
      "target_rule": "DIRECTOR_APPROVED",
      "position_applicability": "DIRECTOR_APPROVED",
      "actor_bands": "NO_ADDITIONAL_ACTION_SPECIFIC_RESTRICTION",
      "target_bands": "DIRECTOR_APPROVED",
      "requirements": "DIRECTOR_APPROVED_DIRECTION",
      "effects": "DIRECTOR_APPROVED_DIRECTION",
      "check": "DIRECTOR_APPROVED_REQUIRED_AND_SOURCE_NUMERIC_CONFIGURATION_REBALANCE_REQUIRED",
      "cooldown": "REBALANCE_REQUIRED",
      "damage": "LEGACY_BALANCE",
      "source_order": "SOURCE_ORDER_PRESERVED_NO_RUNTIME_PRIORITY",
      "risk": "Item / Equipment Owner provides removable-equipment eligibility and resolves actual removal / transfer; item selection, inventory details and destination UNDEFINED; legacy handler retained"
    },
    "previous_migration_record": {
      "id": "SK_LootEquip",
      "type": "combat_action",
      "name": "장비 약탈",
      "role": "control",
      "tier": "REVIEW_REQUIRED",
      "range": "melee",
      "target": "single",
      "requirements": {
        "status": "SOURCE_EXPLICIT",
        "conditions": [
          {
            "type": "target_requirement",
            "combat_status_id": "ST_Bound"
          }
        ]
      },
      "check": {
        "status": "REBALANCE_REQUIRED"
      },
      "effects": [
        {
          "status": "REVIEW_REQUIRED",
          "note": "단순 효과 미기재. 기존 special_effect 참조 및 원문을 검토한다."
        }
      ],
      "special_effect": {
        "id": "fx_loot_bound_target",
        "status": "REVIEW_REQUIRED",
        "note": "기존 ID 보존. Handler 구현 및 현행 Effect 분해는 후속 검토."
      },
      "presentation": {
        "legacy_log": "{ on_use: [\"놈의 손이 장비를 더듬었다.\"], on_hit: [\"장비 하나가 뜯겨 나갔다.\"] }"
      },
      "legacy": {
        "source": "MECH_Skill_Catalog v1.3.0 / SECTION 2",
        "category": "semi_heavy",
        "balance_status": "LEGACY_BALANCE",
        "source_record": "- id: SK_LootEquip\n  name: 장비 약탈\n  category: semi_heavy                 # 공유 준-강기술\n  range: melee\n  target: single\n  lock_condition: target_bound         # 대상 [속박] 시만 (게이트 B)\n  effect_id: fx_loot_bound_target      # 구속 대상 장비 1개 탈취\n  log: { on_use: [\"놈의 손이 장비를 더듬었다.\"], on_hit: [\"장비 하나가 뜯겨 나갔다.\"] }",
        "mechanics_review_status": "REBALANCE_REQUIRED"
      },
      "balance_review": {
        "status": "REBALANCE_REQUIRED",
        "topics": [
          "conditional_item_transfer"
        ]
      }
    }
  }
}
```

## SK_Bite — 물기

```yaml
{
  "definition": {
    "id": "SK_Bite",
    "name": "물기",
    "role": {
      "status": "DIRECTOR_APPROVED",
      "value": "attack"
    },
    "target_rule": {
      "status": "DIRECTOR_APPROVED",
      "value": "single_enemy"
    },
    "position": {
      "status": "DIRECTOR_APPROVED",
      "applicability": "APPLICABLE",
      "actor_bands": {
        "status": "NO_ADDITIONAL_ACTION_SPECIFIC_RESTRICTION",
        "general_eligibility_applies": true
      },
      "target_bands": {
        "status": "DIRECTOR_APPROVED",
        "values": [
          "Close"
        ]
      }
    },
    "requirements": {
      "status": "DIRECTOR_APPROVED",
      "items": [],
      "scope": "NO_ADDITIONAL_ACTION_SPECIFIC_REQUIREMENT",
      "general_eligibility_applies": true
    },
    "effects": {
      "status": "DIRECTOR_APPROVED_DIRECTION",
      "items": [
        {
          "type": "damage",
          "resolution_condition": "check_success"
        },
        {
          "type": "apply_combat_status",
          "status_id": "ST_Bound",
          "resolution_condition": "check_success",
          "application_owner": "MECH_Combat_Status_Effect_System"
        }
      ],
      "follow_up": "NO_AUTOMATIC_PREPARED_RESERVED_ACTION_OR_FORCED_COMBO_NORMAL_AI_ELIGIBILITY"
    },
    "check": {
      "status": "REQUIRED",
      "source": {
        "status": "DIRECTOR_APPROVED",
        "value": "Combat"
      },
      "configuration_status": "REBALANCE_REQUIRED"
    }
  },
  "migration": {
    "review": {
      "record_state": "INCOMPLETE_MIGRATION_RECORD",
      "role": "DIRECTOR_APPROVED",
      "tier": "REVIEW_REQUIRED",
      "target_rule": "DIRECTOR_APPROVED",
      "position_applicability": "DIRECTOR_APPROVED",
      "actor_bands": "NO_ADDITIONAL_ACTION_SPECIFIC_RESTRICTION",
      "target_bands": "DIRECTOR_APPROVED",
      "requirements": "DIRECTOR_APPROVED_DIRECTION",
      "effects": "DIRECTOR_APPROVED_DIRECTION",
      "check": "DIRECTOR_APPROVED_REQUIRED_AND_SOURCE_NUMERIC_CONFIGURATION_REBALANCE_REQUIRED",
      "cooldown": "REBALANCE_REQUIRED",
      "damage": "LEGACY_BALANCE",
      "source_order": "SOURCE_ORDER_PRESERVED_NO_RUNTIME_PRIORITY",
      "risk": "fx_bite_grip legacy action lock not promoted; Bound status rules owned by Status / Eligibility; no automatic Prepared or follow-up"
    },
    "previous_migration_record": {
      "id": "SK_Bite",
      "type": "combat_action",
      "name": "물기",
      "role": "attack",
      "tier": "basic",
      "range": "melee",
      "target": "single",
      "requirements": {
        "status": "REVIEW_REQUIRED",
        "reason": "Source에 사용 조건이 명시되지 않음. 장비 등 추가 조건을 추론하지 않는다."
      },
      "check": {
        "status": "REBALANCE_REQUIRED"
      },
      "effects": [
        {
          "type": "damage",
          "value": {
            "status": "LEGACY_BALANCE",
            "legacy_value": 1
          }
        },
        {
          "type": "apply_combat_status",
          "status_id": "ST_Bound"
        }
      ],
      "special_effect": {
        "id": "fx_bite_grip",
        "status": "REVIEW_REQUIRED",
        "note": "기존 ID 보존. Handler 구현 및 현행 Effect 분해는 후속 검토."
      },
      "presentation": {
        "legacy_log": "{ on_use: [\"턱이 벌어졌다.\"], on_hit: [\"이빨이 살을 파고들며 붙들었다.\"] }"
      },
      "legacy": {
        "source": "MECH_Skill_Catalog v1.3.0 / SECTION 2",
        "category": "light",
        "balance_status": "LEGACY_BALANCE",
        "source_record": "- id: SK_Bite\n  name: 물기\n  category: light\n  range: melee\n  target: single\n  damage: 1\n  status_inflict: [속박됨]\n  effect_id: fx_bite_grip              # 밀착 시 취약, 속박 중 타 약기술 불가\n  log: { on_use: [\"턱이 벌어졌다.\"], on_hit: [\"이빨이 살을 파고들며 붙들었다.\"] }\n",
        "mechanics_review_status": "REBALANCE_REQUIRED"
      }
    }
  }
}
```

## SK_TailSwipe — 꼬리치기

```yaml
{
  "definition": {
    "id": "SK_TailSwipe",
    "name": "꼬리치기",
    "role": {
      "status": "DIRECTOR_APPROVED",
      "value": "attack"
    },
    "target_rule": {
      "status": "DIRECTOR_APPROVED",
      "value": "multiple_enemies_small_aoe"
    },
    "position": {
      "status": "DIRECTOR_APPROVED",
      "applicability": "APPLICABLE",
      "actor_bands": {
        "status": "NO_ADDITIONAL_ACTION_SPECIFIC_RESTRICTION",
        "general_eligibility_applies": true
      },
      "target_bands": {
        "status": "DIRECTOR_APPROVED",
        "values": [
          "Close"
        ]
      }
    },
    "requirements": {
      "status": "DIRECTOR_APPROVED",
      "items": [],
      "scope": "NO_ADDITIONAL_ACTION_SPECIFIC_REQUIREMENT",
      "general_eligibility_applies": true
    },
    "effects": {
      "status": "DIRECTOR_APPROVED_DIRECTION",
      "items": [
        {
          "type": "damage",
          "resolution_condition": "check_success"
        },
        {
          "type": "apply_combat_status",
          "status_id": "ST_Stagger",
          "resolution_condition": "check_success",
          "application_owner": "MECH_Combat_Status_Effect_System"
        }
      ],
      "targets": "VALID_SMALL_AOE_TARGETS_MAX_COUNT_UNDEFINED"
    },
    "check": {
      "status": "REQUIRED",
      "source": {
        "status": "DIRECTOR_APPROVED",
        "value": "Combat"
      },
      "configuration_status": "REBALANCE_REQUIRED",
      "roll_scope": "ONE_ACTION_CHECK_NOT_PER_TARGET"
    }
  },
  "migration": {
    "review": {
      "record_state": "INCOMPLETE_MIGRATION_RECORD",
      "role": "DIRECTOR_APPROVED",
      "tier": "REVIEW_REQUIRED",
      "target_rule": "DIRECTOR_APPROVED",
      "position_applicability": "DIRECTOR_APPROVED",
      "actor_bands": "NO_ADDITIONAL_ACTION_SPECIFIC_RESTRICTION",
      "target_bands": "DIRECTOR_APPROVED",
      "requirements": "DIRECTOR_APPROVED_DIRECTION",
      "effects": "DIRECTOR_APPROVED_DIRECTION",
      "check": "DIRECTOR_APPROVED_REQUIRED_AND_SOURCE_NUMERIC_CONFIGURATION_REBALANCE_REQUIRED",
      "cooldown": "REBALANCE_REQUIRED",
      "damage": "LEGACY_BALANCE",
      "source_order": "SOURCE_ORDER_PRESERVED_NO_RUNTIME_PRIORITY",
      "risk": "fx_cover_reduces cover effect LEGACY_ONLY; Small AoE maximum target count UNDEFINED"
    },
    "previous_migration_record": {
      "id": "SK_TailSwipe",
      "type": "combat_action",
      "name": "꼬리치기",
      "role": "attack",
      "tier": "REVIEW_REQUIRED",
      "range": "melee",
      "target": "small_aoe",
      "requirements": {
        "status": "REVIEW_REQUIRED",
        "reason": "Source에 사용 조건이 명시되지 않음. 장비 등 추가 조건을 추론하지 않는다."
      },
      "check": {
        "status": "REBALANCE_REQUIRED"
      },
      "effects": [
        {
          "type": "damage",
          "value": {
            "status": "LEGACY_BALANCE",
            "legacy_value": 1
          }
        },
        {
          "type": "apply_combat_status",
          "status_id": "ST_Stagger"
        }
      ],
      "special_effect": {
        "id": "fx_cover_reduces",
        "status": "REVIEW_REQUIRED",
        "note": "기존 ID 보존. Handler 구현 및 현행 Effect 분해는 후속 검토."
      },
      "presentation": {
        "legacy_log": "{ on_use: [\"거대한 꼬리가 휘둘러졌다.\"], on_hit: [\"휩쓸린 발밑이 흔들렸다.\"] }"
      },
      "legacy": {
        "source": "MECH_Skill_Catalog v1.3.0 / SECTION 2",
        "category": "light",
        "balance_status": "LEGACY_BALANCE",
        "source_record": "- id: SK_TailSwipe\n  name: 꼬리치기\n  category: light\n  range: melee\n  target: small_aoe\n  damage: 1\n  status_inflict: [비틀거림]\n  effect_id: fx_cover_reduces          # 구조물/엄폐 있으면 피해↓·비틀거림 불가\n  log: { on_use: [\"거대한 꼬리가 휘둘러졌다.\"], on_hit: [\"휩쓸린 발밑이 흔들렸다.\"] }\n",
        "mechanics_review_status": "REBALANCE_REQUIRED"
      },
      "balance_review": {
        "status": "REBALANCE_REQUIRED",
        "topics": [
          "cover_dependent_effect"
        ]
      }
    }
  }
}
```

## SK_ClawLunge — 달려들어 발톱치기

```yaml
{
  "definition": {
    "id": "SK_ClawLunge",
    "name": "달려들어 발톱치기",
    "role": {
      "status": "DIRECTOR_APPROVED",
      "value": "attack"
    },
    "target_rule": {
      "status": "DIRECTOR_APPROVED",
      "value": "single_enemy"
    },
    "position": {
      "status": "DIRECTOR_APPROVED",
      "applicability": "APPLICABLE",
      "actor_bands": "REVIEW_REQUIRED",
      "target_bands": {
        "status": "DIRECTOR_APPROVED",
        "values": [
          "Close"
        ],
        "scope": "NORMAL_TARGET_CONTEXT_ONLY"
      },
      "special_target_eligibility": {
        "status": "DIRECTOR_APPROVED",
        "target": "survivor",
        "prior_context": "valid_close_engagement_target_of_this_monster_before_immediately_preceding_player_action",
        "transition": "Close_to_Mid_during_immediately_preceding_player_action",
        "effect": "target_remains_eligible_for_this_action_only",
        "ordinary_mid_target": "NOT_ELIGIBLE_BY_EXCEPTION",
        "runtime_history_schema": "UNDEFINED"
      }
    },
    "requirements": {
      "status": "REVIEW_REQUIRED",
      "items": null
    },
    "effects": {
      "status": "DIRECTOR_APPROVED_DIRECTION",
      "items": [
        {
          "type": "damage",
          "resolution_condition": "check_success"
        },
        {
          "type": "apply_combat_status",
          "status_id": "ST_Pain",
          "resolution_condition": "check_success",
          "application_owner": "MECH_Combat_Status_Effect_System"
        }
      ]
    },
    "activation_timing": {
      "status": "DIRECTOR_APPROVED",
      "selection": "NORMAL_MONSTER_ACTIVATION_AI_SELECTION",
      "reaction_to_player_movement": false
    },
    "position_change": {
      "monster": "NONE",
      "target": "NONE"
    },
    "check": {
      "status": "REQUIRED",
      "source": {
        "status": "DIRECTOR_APPROVED",
        "value": "Combat"
      },
      "configuration_status": "REBALANCE_REQUIRED"
    }
  },
  "migration": {
    "review": {
      "record_state": "INCOMPLETE_MIGRATION_RECORD",
      "role": "DIRECTOR_APPROVED",
      "tier": "REVIEW_REQUIRED",
      "target_rule": "DIRECTOR_APPROVED",
      "position_applicability": "DIRECTOR_APPROVED",
      "actor_bands": "REVIEW_REQUIRED",
      "target_bands": "DIRECTOR_APPROVED_NORMAL_CLOSE_WITH_CHASE_EXCEPTION",
      "requirements": "REVIEW_REQUIRED",
      "effects": "DIRECTOR_APPROVED_DIRECTION",
      "check": "DIRECTOR_APPROVED_REQUIRED_AND_SOURCE_NUMERIC_CONFIGURATION_REBALANCE_REQUIRED",
      "cooldown": "REBALANCE_REQUIRED",
      "damage": "LEGACY_BALANCE",
      "source_order": "SOURCE_ORDER_PRESERVED_NO_RUNTIME_PRIORITY",
      "risk": "Recent valid close engagement and immediately preceding Player Action movement context FOLLOW_UP_REQUIRED; exact runtime fields and AI weight / priority UNDEFINED"
    },
    "previous_migration_record": {
      "id": "SK_ClawLunge",
      "type": "combat_action",
      "name": "달려들어 발톱치기",
      "role": "attack",
      "tier": "REVIEW_REQUIRED",
      "range": "melee",
      "target": "single",
      "requirements": {
        "status": "REVIEW_REQUIRED",
        "reason": "Source에 사용 조건이 명시되지 않음. 장비 등 추가 조건을 추론하지 않는다."
      },
      "check": {
        "status": "REBALANCE_REQUIRED"
      },
      "effects": [
        {
          "type": "damage",
          "value": {
            "status": "LEGACY_BALANCE",
            "legacy_value": 1
          }
        },
        {
          "type": "apply_combat_status",
          "status_id": "ST_Pain"
        }
      ],
      "special_effect": {
        "id": null
      },
      "presentation": {
        "legacy_log": "{ on_use: [\"놈이 몸을 낮췄다.\"], on_hit: [\"발톱이 살갗을 갈랐다.\"] }"
      },
      "legacy": {
        "source": "MECH_Skill_Catalog v1.3.0 / SECTION 2",
        "category": "light",
        "balance_status": "LEGACY_BALANCE",
        "source_record": "- id: SK_ClawLunge\n  name: 달려들어 발톱치기\n  category: light\n  range: melee\n  target: single\n  damage: 1\n  status_inflict: [고통]\n  effect_id: null\n  log: { on_use: [\"놈이 몸을 낮췄다.\"], on_hit: [\"발톱이 살갗을 갈랐다.\"] }\n",
        "mechanics_review_status": "REBALANCE_REQUIRED"
      }
    }
  }
}
```

## SK_WaryStep — 경계하며 뒷걸음질

```yaml
{
  "definition": {
    "id": "SK_WaryStep",
    "name": "경계하며 뒷걸음질",
    "role": {
      "status": "DIRECTOR_APPROVED",
      "value": "defense"
    },
    "target_rule": {
      "status": "DIRECTOR_APPROVED",
      "value": "self"
    },
    "position": {
      "status": "REVIEW_REQUIRED",
      "applicability": "UNDEFINED",
      "actor_bands": "REVIEW_REQUIRED",
      "target_bands": "REVIEW_REQUIRED"
    },
    "requirements": {
      "status": "REVIEW_REQUIRED",
      "items": null
    },
    "effects": {
      "status": "DIRECTOR_APPROVED_DIRECTION",
      "items": [
        {
          "type": "counter_ready_setup",
          "starts": "IMMEDIATELY_AFTER_SUCCESSFUL_SETUP",
          "ends": "IMMEDIATELY_BEFORE_ACTORS_NEXT_ACTIVATION",
          "trigger": {
            "attacker": "SURVIVOR",
            "attempt": "HOSTILE_ATTACK_AGAINST_THIS_MONSTER",
            "attacker_band_at_attempt": "Close",
            "trigger_on": "ATTACK_ATTEMPT_HIT_OR_MISS"
          },
          "counter": {
            "target": "TRIGGERING_ATTACKER",
            "timing": "TRIGGER_CONSUMED_AND_RESERVED_THEN_ORIGINAL_ACTION_RESOLVES_THEN_REVALIDATE_THEN_COUNTER_RESOLVES_OR_CANCELS_NOT_PREEMPTIVE_INTERRUPT",
            "effect_direction": "COUNTER_ATTACK_DAMAGE",
            "damage": "UNDEFINED",
            "check": "UNDEFINED",
            "hit_rule": "UNDEFINED",
            "internal_bite_call": "NOT_APPROVED"
          },
          "consumption": "ONE_TRIGGER_THEN_CONSUMED",
          "next_monster_activation": "NOT_CONSUMED",
          "is_prepared_action": false,
          "runtime_contract": "MINIMUM_REACTIVE_CONTRACT_APPROVED_DETAIL_FOLLOW_UP_REQUIRED"
        }
      ]
    },
    "check": {
      "status": "NOT_APPLICABLE"
    },
    "position_change": {
      "monster": "NONE",
      "target": "NONE"
    }
  },
  "migration": {
    "review": {
      "record_state": "INCOMPLETE_MIGRATION_RECORD",
      "role": "DIRECTOR_APPROVED",
      "tier": "REVIEW_REQUIRED",
      "target_rule": "DIRECTOR_APPROVED",
      "position_applicability": "REVIEW_REQUIRED",
      "actor_bands": "REVIEW_REQUIRED",
      "target_bands": "REVIEW_REQUIRED",
      "requirements": "REVIEW_REQUIRED",
      "effects": "DIRECTOR_APPROVED_DIRECTION",
      "check": "DIRECTOR_APPROVED_NOT_APPLICABLE",
      "cooldown": "REBALANCE_REQUIRED",
      "damage": "LEGACY_BALANCE",
      "source_order": "SOURCE_ORDER_PRESERVED_NO_RUNTIME_PRIORITY",
      "risk": "Earlier review left original attack / counter order UNDEFINED; current approved Runtime contract resolves original Action first, then revalidates and resolves or cancels Counter. Per-action counter damage / check / status and detailed eligibility remain UNDEFINED; legacy fx_wary_branch retained, automatic Bite / Claw / trap detection not promoted"
    },
    "previous_migration_record": {
      "id": "SK_WaryStep",
      "type": "combat_action",
      "name": "경계하며 뒷걸음질",
      "role": "REVIEW_REQUIRED",
      "tier": "REVIEW_REQUIRED",
      "range": "melee",
      "target": "self",
      "requirements": {
        "status": "REVIEW_REQUIRED",
        "reason": "Source에 사용 조건이 명시되지 않음. 장비 등 추가 조건을 추론하지 않는다."
      },
      "check": {
        "status": "REBALANCE_REQUIRED"
      },
      "effects": [
        {
          "status": "REVIEW_REQUIRED",
          "note": "단순 효과 미기재. 기존 special_effect 참조 및 원문을 검토한다."
        }
      ],
      "special_effect": {
        "id": "fx_wary_branch",
        "status": "REVIEW_REQUIRED",
        "note": "기존 ID 보존. Handler 구현 및 현행 Effect 분해는 후속 검토."
      },
      "presentation": {
        "legacy_log": "{ on_use: [\"놈이 거리를 재며 물러섰다.\"] }"
      },
      "legacy": {
        "source": "MECH_Skill_Catalog v1.3.0 / SECTION 2",
        "category": "light",
        "balance_status": "LEGACY_BALANCE",
        "source_record": "- id: SK_WaryStep\n  name: 경계하며 뒷걸음질\n  category: light\n  range: melee\n  target: self\n  effect_id: fx_wary_branch            # 공격받으면 물기 연계 / 비공격 시 발톱 연계 + 함정 파악\n  log: { on_use: [\"놈이 거리를 재며 물러섰다.\"] }",
        "mechanics_review_status": "REBALANCE_REQUIRED"
      },
      "balance_review": {
        "status": "REBALANCE_REQUIRED",
        "topics": [
          "conditional_action_branch"
        ]
      }
    }
  }
}
```

## SK_Stab — 찌르기

```yaml
{
  "definition": {
    "id": "SK_Stab",
    "name": "찌르기",
    "role": {
      "status": "SOURCE_SUPPORTED",
      "value": "attack"
    },
    "target_rule": {
      "status": "REVIEW_REQUIRED",
      "value": null
    },
    "position": {
      "status": "REVIEW_REQUIRED",
      "applicability": "UNDEFINED",
      "actor_bands": "REVIEW_REQUIRED",
      "target_bands": "REVIEW_REQUIRED"
    },
    "requirements": {
      "status": "SOURCE_EXPLICIT",
      "items": [
        {
          "type": "equipment_requirement",
          "condition": "weapon_held"
        }
      ]
    },
    "effects": {
      "status": "REVIEW_REQUIRED",
      "items": [
        {
          "type": "damage"
        },
        {
          "type": "apply_combat_status",
          "status_id": "ST_Bleed"
        }
      ]
    }
  },
  "migration": {
    "review": {
      "record_state": "INCOMPLETE_MIGRATION_RECORD",
      "role": "SOURCE_EXPLICIT",
      "tier": "REVIEW_REQUIRED",
      "target_rule": "REVIEW_REQUIRED",
      "position_applicability": "REVIEW_REQUIRED",
      "actor_bands": "REVIEW_REQUIRED",
      "target_bands": "REVIEW_REQUIRED",
      "requirements": "SOURCE_EXPLICIT",
      "effects": "REVIEW_REQUIRED",
      "check": "REBALANCE_REQUIRED",
      "cooldown": "REBALANCE_REQUIRED",
      "damage": "LEGACY_BALANCE",
      "source_order": "SOURCE_ORDER_PRESERVED_NO_RUNTIME_PRIORITY"
    },
    "previous_migration_record": {
      "id": "SK_Stab",
      "type": "combat_action",
      "name": "찌르기",
      "role": "attack",
      "tier": "REVIEW_REQUIRED",
      "range": "melee",
      "target": "single",
      "requirements": {
        "status": "SOURCE_EXPLICIT",
        "conditions": [
          {
            "type": "equipment_requirement",
            "condition": "weapon_held"
          }
        ]
      },
      "check": {
        "status": "REBALANCE_REQUIRED"
      },
      "effects": [
        {
          "type": "damage",
          "value": {
            "status": "LEGACY_BALANCE",
            "legacy_value": 1
          }
        },
        {
          "type": "apply_combat_status",
          "status_id": "ST_Bleed"
        }
      ],
      "special_effect": {
        "id": null
      },
      "presentation": {
        "legacy_log": "{ on_use: [\"놈이 단검 끝을 겨눴다.\"], on_hit: [\"날이 살을 얕게 갈랐다.\"] }"
      },
      "legacy": {
        "source": "MECH_Skill_Catalog v1.3.0 / SECTION 2",
        "category": "light",
        "balance_status": "LEGACY_BALANCE",
        "source_record": "- id: SK_Stab\n  name: 찌르기\n  category: light\n  range: melee\n  target: single\n  damage: 1                            # 휘두르기보다 약하나\n  status_inflict: [ST_Bleed]           # 출혈 부여\n  lock_condition: weapon_held          # 단검 필요 — 무장 해제 시 잠김\n  effect_id: null\n  log: { on_use: [\"놈이 단검 끝을 겨눴다.\"], on_hit: [\"날이 살을 얕게 갈랐다.\"] }\n",
        "mechanics_review_status": "REBALANCE_REQUIRED"
      }
    }
  }
}
```

## SK_Brandmark — 낙인새기기

```yaml
{
  "definition": {
    "id": "SK_Brandmark",
    "name": "낙인새기기",
    "role": {
      "status": "SOURCE_SUPPORTED",
      "value": "control"
    },
    "target_rule": {
      "status": "REVIEW_REQUIRED",
      "value": null
    },
    "position": {
      "status": "REVIEW_REQUIRED",
      "applicability": "UNDEFINED",
      "actor_bands": "REVIEW_REQUIRED",
      "target_bands": "REVIEW_REQUIRED"
    },
    "requirements": {
      "status": "SOURCE_EXPLICIT",
      "items": [
        {
          "type": "equipment_requirement",
          "condition": "weapon_held"
        }
      ]
    },
    "effects": {
      "status": "REVIEW_REQUIRED",
      "items": [
        {
          "type": "apply_combat_status",
          "status_id": "ST_Brand"
        }
      ]
    }
  },
  "migration": {
    "review": {
      "record_state": "INCOMPLETE_MIGRATION_RECORD",
      "role": "SOURCE_EXPLICIT",
      "tier": "REVIEW_REQUIRED",
      "target_rule": "REVIEW_REQUIRED",
      "position_applicability": "REVIEW_REQUIRED",
      "actor_bands": "REVIEW_REQUIRED",
      "target_bands": "REVIEW_REQUIRED",
      "requirements": "SOURCE_EXPLICIT",
      "effects": "REVIEW_REQUIRED",
      "check": "REBALANCE_REQUIRED",
      "cooldown": "REBALANCE_REQUIRED",
      "damage": "LEGACY_BALANCE",
      "source_order": "SOURCE_ORDER_PRESERVED_NO_RUNTIME_PRIORITY"
    },
    "previous_migration_record": {
      "id": "SK_Brandmark",
      "type": "combat_action",
      "name": "낙인새기기",
      "role": "control",
      "tier": "REVIEW_REQUIRED",
      "range": "melee",
      "target": "single",
      "requirements": {
        "status": "SOURCE_EXPLICIT",
        "conditions": [
          {
            "type": "equipment_requirement",
            "condition": "weapon_held"
          }
        ]
      },
      "check": {
        "status": "REBALANCE_REQUIRED"
      },
      "effects": [
        {
          "type": "apply_combat_status",
          "status_id": "ST_Brand"
        }
      ],
      "special_effect": {
        "id": null
      },
      "presentation": {
        "legacy_log": "{ on_use: [\"놈이 칼끝으로 표식을 그었다.\"], on_hit: [\"살갗에 낙인이 새겨졌다.\"] }"
      },
      "legacy": {
        "source": "MECH_Skill_Catalog v1.3.0 / SECTION 2",
        "category": "light",
        "balance_status": "LEGACY_BALANCE",
        "source_record": "- id: SK_Brandmark\n  name: 낙인새기기\n  category: light\n  range: melee\n  target: single\n  status_inflict: [ST_Brand]           # 낙인 적립 (피의 제사 연료)\n  lock_condition: weapon_held          # 단검 필요\n  effect_id: null\n  log: { on_use: [\"놈이 칼끝으로 표식을 그었다.\"], on_hit: [\"살갗에 낙인이 새겨졌다.\"] }\n",
        "mechanics_review_status": "REBALANCE_REQUIRED"
      }
    }
  }
}
```

## SK_OminousPrayer — 불길한 기도

```yaml
{
  "definition": {
    "id": "SK_OminousPrayer",
    "name": "불길한 기도",
    "role": {
      "status": "SOURCE_SUPPORTED",
      "value": "attack"
    },
    "target_rule": {
      "status": "REVIEW_REQUIRED",
      "value": null
    },
    "position": {
      "status": "REVIEW_REQUIRED",
      "applicability": "UNDEFINED",
      "actor_bands": "REVIEW_REQUIRED",
      "target_bands": "REVIEW_REQUIRED"
    },
    "requirements": {
      "status": "REVIEW_REQUIRED",
      "items": null
    },
    "effects": {
      "status": "REVIEW_REQUIRED",
      "items": null
    }
  },
  "migration": {
    "review": {
      "record_state": "INCOMPLETE_MIGRATION_RECORD",
      "role": "SOURCE_EXPLICIT",
      "tier": "REVIEW_REQUIRED",
      "target_rule": "REVIEW_REQUIRED",
      "position_applicability": "REVIEW_REQUIRED",
      "actor_bands": "REVIEW_REQUIRED",
      "target_bands": "REVIEW_REQUIRED",
      "requirements": "REVIEW_REQUIRED",
      "effects": "REVIEW_REQUIRED",
      "check": "REBALANCE_REQUIRED",
      "cooldown": "REBALANCE_REQUIRED",
      "damage": "LEGACY_BALANCE",
      "source_order": "SOURCE_ORDER_PRESERVED_NO_RUNTIME_PRIORITY",
      "risk": "percentage damage and quirk scaling REWORK_REQUIRED / REBALANCE_REQUIRED"
    },
    "previous_migration_record": {
      "id": "SK_OminousPrayer",
      "type": "combat_action",
      "name": "불길한 기도",
      "role": "attack",
      "tier": "REVIEW_REQUIRED",
      "range": "mid",
      "target": "single",
      "requirements": {
        "status": "REVIEW_REQUIRED",
        "reason": "Source에 사용 조건이 명시되지 않음. 장비 등 추가 조건을 추론하지 않는다."
      },
      "check": {
        "status": "REBALANCE_REQUIRED"
      },
      "effects": [
        {
          "status": "REVIEW_REQUIRED",
          "note": "단순 효과 미기재. 기존 special_effect 참조 및 원문을 검토한다."
        }
      ],
      "special_effect": {
        "id": "fx_prayer_quirk_scaling",
        "status": "REVIEW_REQUIRED",
        "note": "기존 ID 보존. Handler 구현 및 현행 Effect 분해는 후속 검토."
      },
      "presentation": {
        "legacy_log": "{ on_use: [\"놈이 알 수 없는 기도를 읊었다.\"], on_hit: [\"머릿속이 송곳에 찔린 듯 울렸다.\"] }"
      },
      "legacy": {
        "source": "MECH_Skill_Catalog v1.3.0 / SECTION 2",
        "category": "semi_heavy",
        "balance_status": "LEGACY_BALANCE",
        "source_record": "- id: SK_OminousPrayer\n  name: 불길한 기도\n  category: semi_heavy                  # 공유 준-강기술\n  range: mid\n  target: single\n  effect_id: fx_prayer_quirk_scaling    # 대상 기벽 수 비례 정신피해(100%+개당10%, 최대200%)\n  log: { on_use: [\"놈이 알 수 없는 기도를 읊었다.\"], on_hit: [\"머릿속이 송곳에 찔린 듯 울렸다.\"] }",
        "mechanics_review_status": "REBALANCE_REQUIRED"
      },
      "balance_review": {
        "status": "REBALANCE_REQUIRED",
        "topics": [
          "percentage_damage",
          "quirk_count_scaling"
        ]
      }
    }
  }
}
```

## SK_AimedShot — 정조준 격발

```yaml
{
  "definition": {
    "id": "SK_AimedShot",
    "name": "정조준 격발",
    "role": {
      "status": "SOURCE_SUPPORTED",
      "value": "attack"
    },
    "target_rule": {
      "status": "REVIEW_REQUIRED",
      "value": null
    },
    "position": {
      "status": "REVIEW_REQUIRED",
      "applicability": "UNDEFINED",
      "actor_bands": "REVIEW_REQUIRED",
      "target_bands": "REVIEW_REQUIRED"
    },
    "requirements": {
      "status": "SOURCE_EXPLICIT",
      "items": [
        {
          "type": "equipment_requirement",
          "condition": "weapon_held"
        }
      ]
    },
    "effects": {
      "status": "REVIEW_REQUIRED",
      "items": [
        {
          "type": "damage"
        }
      ]
    }
  },
  "migration": {
    "review": {
      "record_state": "INCOMPLETE_MIGRATION_RECORD",
      "role": "SOURCE_EXPLICIT",
      "tier": "REVIEW_REQUIRED",
      "target_rule": "REVIEW_REQUIRED",
      "position_applicability": "REVIEW_REQUIRED",
      "actor_bands": "REVIEW_REQUIRED",
      "target_bands": "REVIEW_REQUIRED",
      "requirements": "SOURCE_EXPLICIT",
      "effects": "REVIEW_REQUIRED",
      "check": "REBALANCE_REQUIRED",
      "cooldown": "REBALANCE_REQUIRED",
      "damage": "LEGACY_BALANCE",
      "source_order": "SOURCE_ORDER_PRESERVED_NO_RUNTIME_PRIORITY",
      "risk": "firearm description versus weapon variant ownership conflict REVIEW_REQUIRED"
    },
    "previous_migration_record": {
      "id": "SK_AimedShot",
      "type": "combat_action",
      "name": "정조준 격발",
      "role": "attack",
      "tier": "REVIEW_REQUIRED",
      "range": "ranged",
      "target": "single",
      "requirements": {
        "status": "SOURCE_EXPLICIT",
        "conditions": [
          {
            "type": "equipment_requirement",
            "condition": "weapon_held"
          }
        ]
      },
      "check": {
        "status": "REBALANCE_REQUIRED"
      },
      "effects": [
        {
          "type": "damage",
          "value": {
            "status": "LEGACY_BALANCE",
            "legacy_value": 2
          }
        }
      ],
      "special_effect": {
        "id": "fx_weapon_type_variant",
        "status": "REVIEW_REQUIRED",
        "note": "기존 ID 보존. Handler 구현 및 현행 Effect 분해는 후속 검토."
      },
      "presentation": {
        "legacy_log": "{ on_use: [\"놈이 총구를 겨눴다.\"], on_hit: [\"총성과 함께 충격이 박혔다.\"] }"
      },
      "legacy": {
        "source": "MECH_Skill_Catalog v1.3.0 / SECTION 2",
        "category": "light",
        "balance_status": "LEGACY_BALANCE",
        "source_record": "- id: SK_AimedShot\n  name: 정조준 격발\n  category: light\n  range: ranged                        # 총기 보유 개체 — 거리 시스템 원거리 특화\n  target: single\n  damage: 2\n  lock_condition: weapon_held          # 무기(총기) 필요 — 무장 해제 시 잠김\n  effect_id: fx_weapon_type_variant     # 무기 타입에 따라 근접(둔기)/원거리(총) 분기\n  log: { on_use: [\"놈이 총구를 겨눴다.\"], on_hit: [\"총성과 함께 충격이 박혔다.\"] }\n",
        "mechanics_review_status": "REBALANCE_REQUIRED"
      },
      "balance_review": {
        "status": "REBALANCE_REQUIRED",
        "topics": [
          "weapon_dependent_effect"
        ]
      }
    }
  }
}
```

## SK_CallSupport — 지원 요청

```yaml
{
  "definition": {
    "id": "SK_CallSupport",
    "name": "지원 요청",
    "role": {
      "status": "SOURCE_SUPPORTED",
      "value": "support"
    },
    "target_rule": {
      "status": "REVIEW_REQUIRED",
      "value": null,
      "source_supported_candidate": "self"
    },
    "position": {
      "status": "REVIEW_REQUIRED",
      "applicability": "UNDEFINED",
      "actor_bands": "REVIEW_REQUIRED",
      "target_bands": "REVIEW_REQUIRED"
    },
    "requirements": {
      "status": "REVIEW_REQUIRED",
      "items": null
    },
    "effects": {
      "status": "REVIEW_REQUIRED",
      "items": null
    }
  },
  "migration": {
    "review": {
      "record_state": "INCOMPLETE_MIGRATION_RECORD",
      "role": "SOURCE_EXPLICIT",
      "tier": "REVIEW_REQUIRED",
      "target_rule": "REVIEW_REQUIRED",
      "position_applicability": "REVIEW_REQUIRED",
      "actor_bands": "REVIEW_REQUIRED",
      "target_bands": "REVIEW_REQUIRED",
      "requirements": "REVIEW_REQUIRED",
      "effects": "REVIEW_REQUIRED",
      "check": "REBALANCE_REQUIRED",
      "cooldown": "REBALANCE_REQUIRED",
      "damage": "LEGACY_BALANCE",
      "source_order": "SOURCE_ORDER_PRESERVED_NO_RUNTIME_PRIORITY",
      "risk": "ST_Reinforce legacy reference only; Pending Reinforcement / Delayed Encounter Effect owner REVIEW_REQUIRED"
    },
    "previous_migration_record": {
      "id": "SK_CallSupport",
      "type": "combat_action",
      "name": "지원 요청",
      "role": "support",
      "tier": "REVIEW_REQUIRED",
      "range": "mid",
      "target": "self",
      "requirements": {
        "status": "REVIEW_REQUIRED",
        "reason": "Source에 사용 조건이 명시되지 않음. 장비 등 추가 조건을 추론하지 않는다."
      },
      "check": {
        "status": "REBALANCE_REQUIRED"
      },
      "effects": [
        {
          "type": "apply_combat_status",
          "status_id": "ST_Reinforce"
        }
      ],
      "special_effect": {
        "id": null
      },
      "presentation": {
        "legacy_log": "{ on_use: [\"놈이 무전으로 지원을 요청했다.\"] }"
      },
      "legacy": {
        "source": "MECH_Skill_Catalog v1.3.0 / SECTION 2",
        "category": "light",
        "balance_status": "LEGACY_BALANCE",
        "source_record": "- id: SK_CallSupport\n  name: 지원 요청\n  category: light\n  range: mid\n  target: self\n  status_inflict: [ST_Reinforce]       # 일정 턴 후 swarm 규모 +1 (지연 자버프)\n  effect_id: null\n  log: { on_use: [\"놈이 무전으로 지원을 요청했다.\"] }\n",
        "mechanics_review_status": "REBALANCE_REQUIRED"
      },
      "balance_review": {
        "status": "REBALANCE_REQUIRED",
        "topics": [
          "delayed_swarm_size_change"
        ]
      }
    }
  }
}
```

## SK_StunGun — 스턴건

```yaml
{
  "definition": {
    "id": "SK_StunGun",
    "name": "스턴건",
    "role": {
      "status": "SOURCE_SUPPORTED",
      "value": "control"
    },
    "target_rule": {
      "status": "REVIEW_REQUIRED",
      "value": null
    },
    "position": {
      "status": "REVIEW_REQUIRED",
      "applicability": "UNDEFINED",
      "actor_bands": "REVIEW_REQUIRED",
      "target_bands": "REVIEW_REQUIRED"
    },
    "requirements": {
      "status": "REVIEW_REQUIRED",
      "items": null
    },
    "effects": {
      "status": "REVIEW_REQUIRED",
      "items": null
    }
  },
  "migration": {
    "review": {
      "record_state": "INCOMPLETE_MIGRATION_RECORD",
      "role": "SOURCE_EXPLICIT",
      "tier": "REVIEW_REQUIRED",
      "target_rule": "REVIEW_REQUIRED",
      "position_applicability": "REVIEW_REQUIRED",
      "actor_bands": "REVIEW_REQUIRED",
      "target_bands": "REVIEW_REQUIRED",
      "requirements": "REVIEW_REQUIRED",
      "effects": "REVIEW_REQUIRED",
      "check": "REBALANCE_REQUIRED",
      "cooldown": "REBALANCE_REQUIRED",
      "damage": "LEGACY_BALANCE",
      "source_order": "SOURCE_ORDER_PRESERVED_NO_RUNTIME_PRIORITY",
      "risk": "ST_Stun or ST_Paralysis selection REVIEW_REQUIRED; equipment requirement REVIEW_REQUIRED"
    },
    "previous_migration_record": {
      "id": "SK_StunGun",
      "type": "combat_action",
      "name": "스턴건",
      "role": "control",
      "tier": "REVIEW_REQUIRED",
      "range": "melee",
      "target": "single",
      "requirements": {
        "status": "REVIEW_REQUIRED",
        "reason": "Source에 사용 조건이 명시되지 않음. 장비 등 추가 조건을 추론하지 않는다."
      },
      "check": {
        "status": "REBALANCE_REQUIRED"
      },
      "effects": [
        {
          "status": "REVIEW_REQUIRED",
          "note": "단순 효과 미기재. 기존 special_effect 참조 및 원문을 검토한다."
        }
      ],
      "special_effect": {
        "id": "fx_stun_or_paralyze",
        "status": "REVIEW_REQUIRED",
        "note": "기존 ID 보존. Handler 구현 및 현행 Effect 분해는 후속 검토.",
        "combat_status_candidates": [
          "ST_Stun",
          "ST_Paralysis"
        ]
      },
      "presentation": {
        "legacy_log": "{ on_use: [\"놈이 전류가 흐르는 도구를 들이댔다.\"], on_hit: [\"몸이 경직되며 감각이 끊겼다.\"] }"
      },
      "legacy": {
        "source": "MECH_Skill_Catalog v1.3.0 / SECTION 2",
        "category": "light",
        "balance_status": "LEGACY_BALANCE",
        "source_record": "- id: SK_StunGun\n  name: 스턴건\n  category: light\n  range: melee\n  target: single\n  effect_id: fx_stun_or_paralyze        # 적중 시 [기절] 또는 [마비] 중 하나\n  log: { on_use: [\"놈이 전류가 흐르는 도구를 들이댔다.\"], on_hit: [\"몸이 경직되며 감각이 끊겼다.\"] }",
        "mechanics_review_status": "REBALANCE_REQUIRED"
      },
      "balance_review": {
        "status": "REBALANCE_REQUIRED",
        "topics": [
          "status_selection_rule"
        ]
      }
    }
  }
}
```

---

# 4. Legacy Handler Notes

아래는 원문 SECTION 5의 추적 자료다. 모두 Legacy 설명이며 숫자·비율·Gauge는 `LEGACY_BALANCE`다.
C# 로직을 본 문서에서 새로 정의하거나 구현하지 않는다.

| effect_id | 동작 |
|---|---|
| `fx_shout_summon_or_cower` | swarm이면 규모+1, 아니면 일대 [움츠러듬] |
| `fx_grab_open_bind_gate` | 회피 실패 시 [속박] 부여 + 게이트 B 개방 |
| `fx_loot_bound_target` | 대상 [속박] 확인 후 장비 1개 탈취 |
| `fx_bite_grip` | 밀착 취약 + 속박 중 타 약기술 잠금 |
| `fx_cover_reduces` | 엄폐/구조물 존재 시 피해↓·[비틀거림] 무효 |
| `fx_wary_branch` | 피격 여부로 다음 연계 분기 + 함정 파악 |
| `fx_prayer_quirk_scaling` | 대상 기벽 수 비례 정신피해(기본 100% + 기벽당 10%, 상한 200%) |
| `fx_weapon_type_variant` | 무기 타입에 따라 근접(둔기)/원거리(총) 사거리·보정 분기 |
| `fx_stun_or_paralyze` | 적중 시 [기절](ST_Stun) 또는 [마비](ST_Paralysis) 중 하나 부여 |
| `fx_base_brace` | 피해 무효 아님 — 다음 피격 피해 감소 + 다음 행동/게이지 영향 |
| `fx_base_backstep` | 1밴드 후퇴(회피성) — 근접 피격 위험↓ |

---

# 5. Signature / Unique Action Inventory

다음 항목은 조사 목록이며 이번 데이터 Migration 대상 18개에 포함하지 않는다.
현재 소유 문서는 모두 `MONSTER_DB`다. 새 ID는 실제 등록이나 참조 변경이 아닌 `NEW_PROPOSAL`이다.
명시된 자동 반응과 능동 행동의 구분이 불명확하면 후속 검토한다.

| 원문 위치 | 사용 Monster | 행동 | Action 여부 | Passive 여부 | 권장 ID (NEW_PROPOSAL) |
|---|---|---|---|---|---|
| SECTION 2-D | 광신도 | 피의 제사 | 예 | 아니오 | ACT_BloodRitual |
| SECTION 3 | 거대이빨악어 | 데스롤 | 예 | 아니오 | ACT_DeathRoll |
| SECTION 3 | 거대이빨악어 | 강하게 물기 | 예 | 아니오 | ACT_PowerfulBite |
| SECTION 3 | 거대이빨악어 | 사냥감 추적 | REVIEW_REQUIRED: 도주 시 반응 | REVIEW_REQUIRED | ACT_PreyPursuit |
| SECTION 4 | 잔혹한 살점포식자 | 할퀴며 피핥기 | 예 | 아니오 | ACT_ClawAndLick |
| SECTION 4 | 잔혹한 살점포식자 | 은밀한 잠복자 | 예 (skills_basic) | 지속 회복과의 분리 REVIEW_REQUIRED | ACT_HiddenAmbusher |
| SECTION 4 | 잔혹한 살점포식자 | 공포스러운 외침 | 예 | 아니오 | ACT_TerrifyingCry |
| SECTION 4 | 잔혹한 살점포식자 | 잔혹한 처형식 | 예 | 아니오 | ACT_CruelExecution |
| SECTION 4 | 잔혹한 살점포식자 | 공중덮치기 | 예 | 아니오 | ACT_AerialPounce |

원형 표의 이름만 있는 행동(SECTION 1)은 개체별 Signature 정의가 아니며 이번 작업에서 새 Action ID로 등록하지 않는다.
R18 전용 Action은 Optional Module 소유이므로 이번 일반 Action Catalog로 이관하지 않는다.

---

# 6. Passive Exclusion Inventory

다음은 `MONSTER_DB` SECTION 4에서 명시적으로 Passive로 정의되어 있다.
Action Definition에 포함하지 않으며 별도 Passive 문서는 생성하지 않는다.

| 사용 Monster | 항목 | Action 여부 | Passive 여부 | 상태 | 권장 ID |
|---|---|---|---|---|---|
| 잔혹한 살점포식자 | 은밀한 움직임 | 아니오 | 예 | PASSIVE_MIGRATION_REQUIRED | NEW_PROPOSAL: TRAIT_HiddenMovement |
| 잔혹한 살점포식자 | 살점포식자 | 아니오 | 예 | PASSIVE_MIGRATION_REQUIRED | NEW_PROPOSAL: TRAIT_FleshEater |
| 잔혹한 살점포식자 | 사냥본능 | 아니오 | 예 | PASSIVE_MIGRATION_REQUIRED | NEW_PROPOSAL: TRAIT_PredatorInstinct |

---

# 7. Review / Migration Notes

- 신규 문서와 원본의 중복은 Migration 추적을 위한 것이다. 기존 Consumer는 자동으로 신규 문서를 사용하지 않는다.
- Status 정규화: 움츠러듬 → ST_Cower, 속박됨 → ST_Bound, 비틀거림 → ST_Stagger, 고통 → ST_Pain.
- ST_Bleed / ST_Brand / ST_Reinforce는 기존 ID를 유지한다. 스턴건 후보는 Status DB의 ST_Stun / ST_Paralysis다.
- Source의 `self` Range, 무장 변형과 Ranged 선언(SK_AimedShot), 분기 효과(SK_Shout / SK_WaryStep)는 REVIEW_REQUIRED다.
- Source에 없는 장비 Requirement를 추가하지 않는다. 특히 SK_StunGun의 장비 조건은 REVIEW_REQUIRED다.
- `MECH_Combat_Status_Effect_System`은 CURRENT / APPROVED다. `DATA_Combat_Status_Effect_Catalog`는 CURRENT_CANDIDATE / REVIEW이므로 개별 Status Data를 자동 승인하지 않는다. `MECH_Status_Effect_DB`는 Legacy Migration Source이며 MONSTER_DB는 REFERENCE다.
- 추가 전달된 17~22항을 반영했다. 우선 샘플 3개와 전체 18개는 동일 Schema로 검증했다.
- 향후 Check / Positioning / Status / Balance 검토와 데이터 승인 후 Runtime Schema 및 Consumer Migration을 진행한다.


## 7.1 Balance Review Queue

SK_OminousPrayer의 비율 Damage·기벽 개수 Scaling은 REBALANCE_REQUIRED다.
Opening Gauge / Gate 영향(SK_Base_Brace, SK_Grab), Swarm 증감(SK_Shout, SK_CallSupport),
조건부 효과와 상태 선택(SK_WaryStep, SK_StunGun 등)도 기존 수치를 승인하지 않고 후속 검토한다.
기존 Dice Modifier와 확률 기반 효과가 관련 Owner 또는 Handler 검토에서 발견되면 REBALANCE_REQUIRED로 유지한다.
Source에 없는 확률, Damage 공식, Check Requirement는 신규로 생성하지 않았다.

## 7.2 Validation Summary

- 실행 Action 18개: 기존 SK_* ID의 완전한 집합을 유지하고 중복 없음.
- 우선 샘플 3개: 동일 필드 구조, 기존 Range / Target / Handler와 전투 상태효과 참조 보존.
- 전투 상태효과 ID 및 Handler의 상태 후보는 기존 Status DB에 존재한다.
- Passive는 실행 Definition에서 제외하고 SECTION 6 조사 목록으로 분리.
- Damage 수치는 LEGACY_BALANCE, 미확정 Check 설정은 REBALANCE_REQUIRED. Batch 1의 Check 필요 / 비적용은 별도 Director 승인 방향이며 신규 Difficulty / Requirement 배정은 없다.
- 원문 Action 레코드는 migration.previous_migration_record.legacy.source_record에 그대로 유지한다.

---

# 8. vNext Schema / Migration Contract

이 절의 vNext Schema 방향은 Director 승인 완료다. 이는 개념적 Definition / Migration 경계에 대한 승인으로, 구체적인 직렬화 Schema나 개별 Action 데이터의 승인이 아니다. 기존 18개 Migration Record와 원문 추적은 Migration Metadata에 보존한다. 본 Catalog는 `CURRENT_CANDIDATE / REVIEW`를 유지한다. Batch 1 / 2 / 3의 해당 Check 필요 / 비적용 방향은 Director 승인됐다. Check 설정, 개별 Cooldown, Damage와 세부 밸런스는 별도 승인 전 `REBALANCE_REQUIRED`다.

## 8.1 Approved Definition Schema Direction

**최종 실행 Definition의 필수 개념:** `id`, `name`, `role`, `target_rule`, `position`, `requirements`, `effects`. `id`는 실행 Action의 안정적인 고유 ID이며 기존 `SK_*` ID를 유지한다. `name`은 사람이 읽는 Display Name이다. Localization System은 범위 밖이다. `role`은 Action의 기능이고, `target_rule`은 대상의 종류와 선택 범위다.

`position` Container는 필수이며 적용 / 적용 없음을 구분한다. 적용 시 `actor_bands`와 `target_bands`는 조건부로 독립 표현한다. Target과 Position은 별개다. 빈 배열, 적용 없음, 미확정을 혼동하지 않으며 빈 배열의 Runtime 의미는 확정하지 않는다. Band는 Positioning Owner의 `Close / Mid / Far`를 따른다. Legacy `melee / mid / ranged / self`는 자동 변환하지 않는다.

`requirements`는 사용 조건을 표현한다. 조건 없음이 확인된 경우와 조건이 미확정인 경우는 다르며, 불명확한 Source를 빈 조건으로 확정하지 않는다. `effects`는 Resolution 이후 각 Owner에 전달할 결과 요청 / 참조를 복수로 표현한다. 미확정 Migration Record는 Complete Runtime-ready Definition이 아니며 미정 값을 억지로 채우지 않는다.

**Optional Definition 개념:** `tier`, `threat`, `check`, `cooldown_rounds`, `usage_limit`, `telegraph`, `prepared_trigger`, `ai_tags`, `presentation`, 승인된 `special_handler_ref`. 누락은 특정 Gameplay 기본값을 뜻하지 않는다. 구체 타입, 직렬화 형식과 Runtime Schema는 후속 Data / TECH_SPEC에서 정한다.

- Role은 기능, Tier는 희소성 / 특수성, Threat는 플레이어 대응 필요 수준이며 독립적이다. Role의 Attack / Defense / Movement / Control / Support / Recovery / Information / Escape / Special과 Tier의 Basic / Advanced / Signature는 예시이며 닫힌 Runtime enum을 확정하지 않는다. Basic이 반드시 약하거나 Signature가 반드시 Strong인 것은 아니다. Legacy 약기술 / 강기술을 자동 매핑하지 않는다.
- Threat Field는 Optional로 승인됐으나 `Normal / Strong` enum과 개별 값은 미승인이다. Threat 누락은 Normal을 의미하지 않으며 Threat는 Damage Rank가 아니다.
- Check는 요청 / 설정 참조다. 1d12 공식, Difficulty Mapping, Modifier Cap, Composite, Fate Override는 Check Owner 소유다. 개별 Source / Requirement / Modifier는 후속 검토한다.
- 정적 Cooldown은 Runtime Owner의 Round 계약을 따른다. Usage Limit도 정적 설정 후보이며 현재 사용 횟수는 Runtime이다. Threat, Telegraph, Prepared는 독립적이다. Telegraph와 Prepared의 기본 관계 및 생성 조건은 Runtime Owner를 따른다.
- Status는 ID로 참조하며 효과 정의를 복제하지 않는다. Status Catalog는 `CURRENT_CANDIDATE / REVIEW`이고 ID 참조는 개별 효과의 승인이 아니다. AI Profile, Context 평가, Weight 계산, Weighted Random, Target 선호 및 선택은 Monster AI 소유다. Weight의 저장 위치는 여기서 확정하지 않는다.

**Definition / Migration / Runtime 경계:** Definition은 정적 Gameplay 구조를 보유한다. Migration / Review Metadata는 Legacy Source, 원문, category, `effect_id`, `SOURCE_EXPLICIT`, `REVIEW_REQUIRED`, `REBALANCE_REQUIRED`, `LEGACY_BALANCE`, `NEW_PROPOSAL` 및 Owner 이관 메모를 보존하며 Runtime Gameplay 값으로 읽지 않는다. 별도 YAML Wrapper를 강제하지 않는다.

Remaining Cooldown, Last Used Round, Current Usage Count, Prepared State / Target, Temporary Lock, Runtime Eligibility Result, Current Combat Position, 계산된 AI Weight 및 Selected Action은 Definition에서 제외하고 각 Runtime Owner가 관리한다.

**Effect Order:** Source에 존재하는 Effect 순서는 Migration에서 보존한다. Source / Authoring Order는 Runtime Execution Priority가 아니며 실행 순서의 Gameplay 의미는 후속 Effect Resolution / TECH_SPEC에서 결정한다.

**Special Handler:** 단순한 Effect는 구조화된 Data를 우선하고 복잡한 예외에만 승인된 `special_handler_ref`를 Optional Definition 참조로 허용한다. Legacy `fx_*`는 Migration Metadata에 보존한다. Legacy Handler ID는 승인된 Special Handler가 아니며 자동 승격하지 않는다. `fx_cover_reduces`의 Cover 부분은 `LEGACY_ONLY`다.

## 8.2 Action Migration Matrix

표의 Role / Tier는 기존 Catalog의 분류이며 Gameplay 확정 판정이 아니다. `R`은 `REVIEW_REQUIRED`, `RB`는 `REBALANCE_REQUIRED`다. 이 표는 이전 Migration 감사 이력이며 Batch 1 / 2 / 3 최신 승인 방향은 SECTION 3의 해당 Definition을 따른다. 모든 행에서 Cooldown은 미제공 / RB, Telegraph와 Prepared는 근거 불충분 / R이다. Legacy Range는 괄호 안에 보존하며 Band는 모두 R이다. Verdict는 이관 후보이지 승인된 새 행동 정의가 아니다.

| Action ID | Role | Tier | Threat | Position / Target | Status / Effect 및 판정 |
|---|---|---|---|---|---|
| SK_Base_Strike | attack | R | R | melee / single → Band R | Damage 1 LEGACY_BALANCE; 일반 Action 이관 후보 |
| SK_Base_Threaten | control | R | R | mid / single → Band R | ST_Cower; 일반 Action 이관 후보 |
| SK_Base_Brace | defense | R | R | self / self → 적용 범위 R | fx_base_brace; 피해 감소 / Gauge 재설계 |
| SK_Base_Backstep | movement | R | R | self / self → 이동 Band R | fx_base_backstep; Position Owner 연계 검토 |
| SK_Swing | attack | R | R | melee / single → Band R | weapon_held, Damage 1 LEGACY_BALANCE; 일반 Action 이관 후보 |
| SK_Shout | R | R | R | mid / aoe → 대상 Band R | ST_Cower / fx_shout_summon_or_cower; 조건부 Swarm 분기 REWORK_REQUIRED |
| SK_Grab | control | basic | R | melee / single → Band R | ST_Bound / fx_grab_open_bind_gate; Gate 재설계, 후속 Trigger 가능성 R |
| SK_LootEquip | control | R | R | melee / single → Band R | ST_Bound 조건 / fx_loot_bound_target; 장비 이전 Owner와 조건 검토 |
| SK_Bite | attack | basic | R | melee / single → Band R | ST_Bound / fx_bite_grip, Damage 1 LEGACY_BALANCE; 속박 중 제한 재검토 |
| SK_TailSwipe | attack | R | R | melee / small_aoe → 대상 Band R | Action 이관 후보; ST_Stagger / Damage 검토, fx_cover_reduces의 Cover 부분은 LEGACY_ONLY |
| SK_ClawLunge | attack | R | R | melee / single → Band R | ST_Pain, Damage 1 LEGACY_BALANCE; 돌진이 이동을 뜻하는지 R |
| SK_WaryStep | R | R | R | melee / self → Band R | fx_wary_branch; 조건부 후속 행동 / 함정 확인 REWORK_REQUIRED |
| SK_Stab | attack | R | R | melee / single → Band R | weapon_held, ST_Bleed, Damage 1 LEGACY_BALANCE; 무기 범위 R |
| SK_Brandmark | control | R | R | melee / single → Band R | weapon_held, ST_Brand; 후속 소비 조건 R |
| SK_OminousPrayer | attack | R | R | mid / single → Band R | fx_prayer_quirk_scaling; 비율 Damage / Quirk Scaling REWORK_REQUIRED / RB |
| SK_AimedShot | attack | R | R | ranged / single → Band R | weapon_held / fx_weapon_type_variant, Damage 2 LEGACY_BALANCE; 총기와 무기 분기 충돌 검토 |
| SK_CallSupport | support | R | R | mid / self → 적용 범위 R | ST_Reinforce Legacy 참조; Pending Reinforcement Owner로 MOVE_OUT 후보 |
| SK_StunGun | control | R | R | melee / single → Band R | fx_stun_or_paralyze; ST_Stun 또는 ST_Paralysis 선택 / 장비 조건 R |

`SK_Grab` / `SK_Bite`의 Bound와 `SK_LootEquip`의 Bound 조건은 선행–후속 관계 검토 근거지만, 이들만으로 Telegraph나 Prepared를 확정할 수 없다. `SK_WaryStep`의 Legacy 분기 역시 Prepared Trigger로 자동 승격하지 않는다. `MONSTER_DB`의 데스롤 등 고유 기술은 별도 조사 대상이며 이 18개에 추가하지 않는다.

## 8.3 Legacy effect_id 판정

분류는 후속 이관 권고이며 Handler의 현행 구현이나 효과를 승인하지 않는다. 복합 Handler는 분해 후 둘 이상의 Owner가 필요할 수 있다.

| effect_id | 권고 | 근거 / 후속 Owner |
|---|---|---|
| fx_shout_summon_or_cower | REWORK_REQUIRED | 조건부 Cower / Swarm 분기; Status 및 Encounter / Swarm 검토 |
| fx_grab_open_bind_gate | REWORK_REQUIRED | Bound 요청은 Status ID, Legacy Gate는 별도 재검토 |
| fx_loot_bound_target | MOVE_TO_OTHER_OWNER | Bound Requirement와 장비 이전은 Requirement / Item Owner 연계 후보 |
| fx_bite_grip | REWORK_REQUIRED | Bound 참조와 Legacy 행동 제한 분리 |
| fx_cover_reduces | LEGACY_ONLY | Cover는 Positioning v1 범위 밖이며 현재 Core Owner가 없다. 향후 별도 Cover System 도입 시 재감사한다. |
| fx_wary_branch | KEEP_AS_SPECIAL_HANDLER_REF | 복합 분기 후보; Action / AI / 정보 Owner 분해 검토 |
| fx_prayer_quirk_scaling | REWORK_REQUIRED | Quirk 입력 및 Damage Owner, 비율 / Scaling 재검토 |
| fx_weapon_type_variant | MOVE_TO_OTHER_OWNER | Weapon Data / Position 분기 후보; 기존 총기 설명과 분기 충돌 검토 |
| fx_stun_or_paralyze | REWORK_REQUIRED | Status ID 중 선택 기준 미정; 두 효과 동시 적용 아님 |
| fx_base_brace | REWORK_REQUIRED | 피해 감소와 Legacy Gauge 상호작용 분리 |
| fx_base_backstep | MIGRATE_TO_DATA_EFFECT | Position 이동 요청 후보; 구체 결과와 회피성 재검토 |

단순 Damage, Status 적용, 이동 요청은 Data Effect 후보이고 복잡한 예외만 Handler 참조를 검토한다. Legacy ID는 보존하며 신규 Handler 구현을 가정하지 않는다. 기벽 변화는 Combat Result / Event를 통한 Quirk Owner 평가 후보로 남기며 Action의 직접 mutation으로 승인하지 않는다. 명시적 Passive 3개는 기존 SECTION 6에만 남기고 실행 Action에서 제외한다.

## 8.4 Review / Promotion Gate

- Close / Mid / Far의 Action별 Actor / Target Band와 Self / AoE 의미, 무기별 범위 및 장비 Owner를 검토한다. `SK_AimedShot`의 총기 전용 설명과 둔기 분기, `SK_StunGun`의 미명시 장비 조건은 별도 결정이 필요하다.
- `SK_CallSupport → ST_Reinforce`는 Consumer Migration 전 Legacy 참조다. Status Catalog의 해당 ID는 Pending Reinforcement / Delayed Encounter Effect로 이동할 후보이며 새로운 Owner나 ID는 아직 확정되지 않았다.
- 구체 Check Source / Requirement, Action별 Cooldown, Role / Tier / Threat, Damage 및 Status 효과, Prepared / Telegraph의 실제 적용 대상은 모두 검토한다. Status Catalog도 `CURRENT_CANDIDATE / REVIEW`다.
- Check Owner는 승인된 Difficulty별 Requirement, Fate Override와 기본 Equal Weight Composite 규칙을 소유한다. 개별 Action의 Check Source / Requirement / Difficulty는 여전히 REBALANCE_REQUIRED이며 Opposed Check Formula는 UNDEFINED다.
- MONSTER_DB에 남은 고유 Action 정의와 기존 공유 / 고유 소유 규칙은 독립 Action ID 원칙으로 후속 Migration이 필요하다. 자동 반응인 사냥감 추적 등은 Passive / Action 분류도 검토한다.
- 향후 승인 전 `legacy.source_record`를 별도 Appendix / Migration Archive로 분리하는 방안을 권장한다. 원본 및 추적 가능성을 보존하고 이번에는 Split하지 않는다.
