---
id: MECH_Skill_Catalog
title: "핵심 시스템 사양서 — 일반 전투 기술 카탈로그"
type: mechanic
status: wip
version: 1.1.0
summary: >
  괴물 일반 전투 기술(약기술·공유 준강기술)의 정의 단일 출처. 개체는 본 카탈로그를 기술 ID로
  참조만 한다(정의 복사 금지). 공유되는 약기술은 카탈로그 소유, 네임드 시그니처 강기술은 개체 잔류.
  단순 수치는 데이터로, 복잡한 조건부 로직은 effect_id로 코드 핸들러를 가리킨다. R18 기술은
  별도 MECH_R18_Skill_Catalog 가 소유.
tags:
  - mechanic
  - system
  - combat
  - skill
  - catalog
keywords:
  - 기술 카탈로그, 약기술, 강기술, 공유 풀, 기술 ID, 참조, effect_id, 정의,
    휘두르기, 외치기, 물기, 꼬리치기, 붙잡기, 텍스트 로그, 밸런스 패치
depends_on:
  - SYS_Manifest
  - MECH_Combat_System
  - MONSTER_DB
last_updated: 2026-06-07
---

# 🗂️ DOWNFALL 일반 전투 기술 카탈로그 (v1.0)

> **정의의 단일 출처.** 같은 기술을 여러 개체가 공유 → 카탈로그에 한 번만 정의, 개체는 ID 참조.
> 밸런스 패치 시 카탈로그 한 줄 수정으로 그 기술을 쓰는 모든 개체 동시 반영.

---

## SECTION 0 — 소유 규칙 (무엇이 여기 들어오나)

```
✅ 카탈로그 소유(공유):
   - 약기술 (2개 이상 개체가 공유하는 범용 기술)
   - 공유되는 조건부 준-강기술 (예: 인간형 실체의 '장비 약탈')
❌ 카탈로그 비소유(개체 잔류):
   - 네임드 시그니처 강기술 (데스롤·잔혹한 처형식 등 — 단일 개체 고유)
   - 개체 패시브 (살점포식자 재생 등)
R18 기술: 본 문서 아님 → MECH_R18_Skill_Catalog 소유.
```

> 기준: **2개 이상 공유하면 카탈로그 / 단일 고유면 개체.** 네임드 시그니처는 공유 안 함 → 개체.

---

## SECTION 1 — 기술 정의 스키마 (공통)

```yaml
SkillDef:
  id: str                    # 참조 키 (예: SK_Bite)
  name: str                  # 표시명 (물기)
  category: light | semi_heavy   # 약기술 / 공유 준-강기술
  range: melee | mid | ranged
  target: single | small_aoe | aoe | self
  damage: int | null         # 단순 수치 피해 (없으면 null)
  gauge_delta:               # 게이지 증감 (해당 시)
    opening: int | null      # 개방 게이지
  status_inflict: [상태이상]  # 중앙 상태이상 표에서 차용 (Combat SECTION 10)
  lock_condition: str | null # 사용 잠금 조건 (예: weapon_held / target_bound)
  effect_id: str | null      # ★ 복잡 조건부 로직은 코드 핸들러 ID로 위임
  log:                       # 텍스트 로그 (행동 주체 = 괴물)
    on_use: [str]
    on_hit: [str]
```

> **effect_id 원칙**: 피해·상태이상 부여 같은 단순 효과는 위 필드로 데이터 표현.
> "속박 보유 시에만 / 엄폐 시 피해↓" 같은 조건부는 effect_id 로 코드 함수에 위임(데이터에 미니 언어 금지).

---

## SECTION 2 — 공유 약기술 (범용 풀)

### 2-1. 인간형 실체 계열 (`ARCH_Human_Armed` 등 공유)
```yaml
- id: SK_Swing
  name: 휘두르기
  category: light
  range: melee
  target: single
  damage: 1
  lock_condition: weapon_held        # 무장 시만 — 무장 해제 시 잠김
  effect_id: null
  log: { on_use: ["놈이 무기를 치켜들었다."], on_hit: ["둔탁한 충격이 파고들었다."] }

- id: SK_Shout
  name: 외치기
  category: light
  range: mid
  target: aoe
  status_inflict: [움츠러듬]
  effect_id: fx_shout_summon_or_cower  # swarm 규모+1(동료 호출) 또는 일대 움츠러듬 — 조건부
  log: { on_use: ["놈이 목청껏 동료를 불렀다."], on_hit: ["고함이 신경을 긁었다."] }

- id: SK_Grab
  name: 붙잡기
  category: light
  range: melee
  target: single
  status_inflict: [속박됨]
  effect_id: fx_grab_open_bind_gate    # 회피 실패 시 [속박] → 게이트 B 개방
  log: { on_use: ["놈이 손을 뻗어 붙들려 했다."], on_hit: ["억센 손아귀가 팔을 옭아맸다."] }

- id: SK_LootEquip
  name: 장비 약탈
  category: semi_heavy                 # 공유 준-강기술
  range: melee
  target: single
  lock_condition: target_bound         # 대상 [속박] 시만 (게이트 B)
  effect_id: fx_loot_bound_target      # 구속 대상 장비 1개 탈취
  log: { on_use: ["놈의 손이 장비를 더듬었다."], on_hit: ["장비 하나가 뜯겨 나갔다."] }
```

### 2-2. 동물형 계열 (`ARCH_Beast_Pack` / 네임드 동물 공유 가능)
```yaml
- id: SK_Bite
  name: 물기
  category: light
  range: melee
  target: single
  damage: 1
  status_inflict: [속박됨]
  effect_id: fx_bite_grip              # 밀착 시 취약, 속박 중 타 약기술 불가
  log: { on_use: ["턱이 벌어졌다."], on_hit: ["이빨이 살을 파고들며 붙들었다."] }

- id: SK_TailSwipe
  name: 꼬리치기
  category: light
  range: melee
  target: small_aoe
  damage: 1
  status_inflict: [비틀거림]
  effect_id: fx_cover_reduces          # 구조물/엄폐 있으면 피해↓·비틀거림 불가
  log: { on_use: ["거대한 꼬리가 휘둘러졌다."], on_hit: ["휩쓸린 발밑이 흔들렸다."] }

- id: SK_ClawLunge
  name: 달려들어 발톱치기
  category: light
  range: melee
  target: single
  damage: 1
  status_inflict: [고통]
  effect_id: null
  log: { on_use: ["놈이 몸을 낮췄다."], on_hit: ["발톱이 살갗을 갈랐다."] }

- id: SK_WaryStep
  name: 경계하며 뒷걸음질
  category: light
  range: melee
  target: self
  effect_id: fx_wary_branch            # 공격받으면 물기 연계 / 비공격 시 발톱 연계 + 함정 파악
  log: { on_use: ["놈이 거리를 재며 물러섰다."] }
```

> 위 동물형 약기술은 거대이빨악어(네임드)가 현재 사용 중이나, 동물형 일반괴물과 **공유 가능**하므로 카탈로그 소유.
> 네임드 고유 강기술(데스롤·강하게 물기)은 공유 안 함 → MONSTER_DB 개체 잔류.

### 2-3. 광신도 계열 (정신공격형 인간형 — 공유 가능)
```yaml
- id: SK_Stab
  name: 찌르기
  category: light
  range: melee
  target: single
  damage: 1                            # 휘두르기보다 약하나
  status_inflict: [ST_Bleed]           # 출혈 부여
  lock_condition: weapon_held          # 단검 필요 — 무장 해제 시 잠김
  effect_id: null
  log: { on_use: ["놈이 단검 끝을 겨눴다."], on_hit: ["날이 살을 얕게 갈랐다."] }

- id: SK_Brandmark
  name: 낙인새기기
  category: light
  range: melee
  target: single
  status_inflict: [ST_Brand]           # 낙인 적립 (피의 제사 연료)
  lock_condition: weapon_held          # 단검 필요
  effect_id: null
  log: { on_use: ["놈이 칼끝으로 표식을 그었다."], on_hit: ["살갗에 낙인이 새겨졌다."] }

- id: SK_OminousPrayer
  name: 불길한 기도
  category: semi_heavy                  # 공유 준-강기술
  range: mid
  target: single
  effect_id: fx_prayer_quirk_scaling    # 대상 기벽 수 비례 정신피해(100%+개당10%, 최대200%)
  log: { on_use: ["놈이 알 수 없는 기도를 읊었다."], on_hit: ["머릿속이 송곳에 찔린 듯 울렸다."] }
```
> 정신공격형 인간형(광신도 등)이 공유. 출혈·낙인은 `ST_Bleed`·`ST_Brand`(Status DB).
> 시그니처 강기술 '피의 제사'(낙인 소비 → 피해 + 영구 기벽)는 공유 안 함 → 개체 잔류.

---

## SECTION 3 — 개체 잔류 (카탈로그 비소유) — 참조용 목록

> 아래는 본 카탈로그가 소유하지 않음. MONSTER_DB 개체에 정의가 잔류함을 명시(중복 방지).

```
거대이빨악어 시그니처 강기술: 데스롤 [전조형], 강하게 물기 [전조형]
거대이빨악어 도주 시: 사냥감 추적
잔혹한 살점포식자: 할퀴며 피핥기, 은밀한 잠복자, 공포스러운 외침, 잔혹한 처형식, 공중덮치기,
                  + 패시브(은밀한 움직임·살점포식자·사냥본능)
```

---

## SECTION 4 — 개체 참조 방식 (MONSTER_DB 연동)

```yaml
# MONSTER_DB 개체는 기술 '내용'이 아니라 'ID 목록'만 보유:
약탈자:
  skills: [SK_Swing, SK_Shout, SK_Grab, SK_LootEquip]   # 카탈로그 참조
  # r18_skills: [...]  → MECH_R18_Skill_Catalog 참조 (별도)
거대이빨악어:
  skills: [SK_Bite, SK_TailSwipe, SK_ClawLunge, SK_WaryStep]   # 공유 약기술 참조
  signature_skills: [데스롤, 강하게 물기, 사냥감 추적]          # 개체 잔류(고유)
```

> 실행 시: 개체가 `SK_Bite` 사용 → 카탈로그에서 정의 조회 → 효과 적용.
> 정의는 읽기 전용(공유). 변하는 상태(쿨다운·사용 횟수)는 개체 인스턴스에.

---

## SECTION 5 — effect_id 핸들러 목록 (코드 위임분)

> 데이터로 표현 못 하는 조건부 로직. 코드에 동명 핸들러 구현 필요. 빌드 시 ID 존재 검증.

| effect_id | 동작 |
|---|---|
| `fx_shout_summon_or_cower` | swarm이면 규모+1, 아니면 일대 [움츠러듬] |
| `fx_grab_open_bind_gate` | 회피 실패 시 [속박] 부여 + 게이트 B 개방 |
| `fx_loot_bound_target` | 대상 [속박] 확인 후 장비 1개 탈취 |
| `fx_bite_grip` | 밀착 취약 + 속박 중 타 약기술 잠금 |
| `fx_cover_reduces` | 엄폐/구조물 존재 시 피해↓·[비틀거림] 무효 |
| `fx_wary_branch` | 피격 여부로 다음 연계 분기 + 함정 파악 |
| `fx_prayer_quirk_scaling` | 대상 기벽 수 비례 정신피해(기본 100% + 기벽당 10%, 상한 200%) |

---

## SECTION 6 — 버전 관리

- **문서 위치**: `01_Mechanics/MECH_Skill_Catalog.md`
- **커밋 메시지**: `feat(mechanic): general combat skill catalog (shared defs + effect_id schema, ID-reference)`
- **Wiki_Index.md 갱신 필요 여부**: **필요 (YES)**

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.0.0 | 2026-06-07 | 최초. 소유 규칙(약기술 공유=카탈로그 / 네임드 강기술=개체) / 기술 정의 스키마 + effect_id / 공유 약기술 풀(인간형·동물형) / 개체 참조 방식 / effect_id 핸들러 목록. 악어·약탈자 약기술 ID 추출. |
| v1.1.0 | 2026-06-08 | 광신도 계열 공유 약기술 추가(2-3): 찌르기(ST_Bleed)·낙인새기기(ST_Brand)·불길한 기도(준-강기술, 기벽 비례). effect_id `fx_prayer_quirk_scaling` 추가. 피의 제사는 개체 시그니처로 잔류. |

**갱신 기준**: 일반형 개체 확충 시 공유 약기술 추가. effect_id 핸들러는 코드와 동기화. R18 기술은 본 문서 아님.
