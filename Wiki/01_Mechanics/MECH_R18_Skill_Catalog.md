---
id: MECH_R18_Skill_Catalog
title: "핵심 시스템 사양서 — R18 전투 기술 카탈로그"
type: mechanic
status: wip
version: 1.3.0
summary: >
  R18 전투 기술 정의의 단일 출처. 괴물 R18/굴복 커맨드(공유 풀)와 생존자 굴복 페이즈 기술
  5대분류(봉사·유혹·농락·흡수·저항)를 ID로 정의. 개체/NPC는 참조만. 파일 단위로 SFW 빌드에서
  제외(토글). 일반 기술 스키마(MECH_Skill_Catalog)를 확장해 R18 게이지·진척 필드를 추가.
tags:
  - mechanic
  - system
  - combat
  - skill
  - catalog
  - r18
keywords:
  - R18 기술, 굴복 기술, 굴복 페이즈, 봉사형, 유혹형, 농락형, 흡수형, 저항형,
    음담패설, 주무르기, 옷찢기, 주도권, 흥분, 성감, 진척 가속, 기술 ID
depends_on:
  - SYS_Manifest
  - MECH_Combat_System
  - MECH_Skill_Catalog
  - MECH_R18_Memory_Log
  - MECH_Quirk_R18_DB
  - MONSTER_DB
last_updated: 2026-06-07
---

# 🔞 DOWNFALL R18 전투 기술 카탈로그 (v1.0)

> **파일 단위 SFW 토글.** 본 파일을 로드하지 않으면 R18 기술 전체가 제거됨(빌드 무결성).
> 성인(18+) 캐릭터 한정. 정의 단일 출처 — 개체/NPC는 ID 참조만.

---

## SECTION 0 — 소유·연동 규칙

```
✅ 본 카탈로그 소유:
   - 괴물 R18/굴복 커맨드 (인간형 공유: 음담패설·주무르기·옷찢기 등 / 형태별 공유)
   - 생존자 굴복 페이즈 기술 5대분류 (공용 풀)
스키마: MECH_Skill_Catalog 의 SkillDef 확장 (R18 게이지·진척 필드 추가)
규칙 엔진: '어떻게 작동하나'는 MECH_Combat_System SECTION 11 (주도권·게이지·승패)
진척·해금: MECH_R18_Memory_Log (변질 축·부위 민감도)
기벽 강화: MECH_Quirk_R18_DB (보유 시 위력↑/해금)
참조: MONSTER_DB 개체 r18_skills:[ID] / 생존자 굴복 기술은 공용 풀(전원 사용 가능)
```

---

## SECTION 1 — R18 기술 정의 스키마 (확장)

```yaml
R18SkillDef:                  # SkillDef 확장
  id: str
  name: str
  side: monster | survivor    # 사용 주체
  phase: normal_r18 | submission   # 일반 R18 전투 / 굴복 페이즈 한정
  sub_category: null | service | tease | domination | absorption | defiance  # 생존자 5분류
  range / target: ...
  gauge_delta:                # R18 게이지 증감
    arousal_self: int | null      # 자기 성감/흥분
    arousal_target: int | null    # 상대(괴물 흥분 등)
    clothing: int | null          # 의복 게이지
  status_inflict: [상태이상]   # 일반 + 굴복 페이즈 전용(절정 여운·최면·구속)
  progress_axis: null | Contact | Penetration | Fluid | Mutation | Cognition | Subjugation
  progress_part: null | 입 | 가슴 | 하복부 | 후부 | 전신   # 부위 민감도 누적
  lock_condition: str | null  # 예: target_bound / submission_only / arousal_max
  scaling: null | erosion | quirk | sens_level   # 위력 의존(양날)
  # --- 자세 게이팅 (SECTION 8) ---
  required_parts: [입|가슴|하복부|후부|전신|손|하반신]  # 이 커맨드가 점유하는 부위
  valid_postures: [대치|정면|후배위|기승|구속]          # 가능 자세(불일치 시 봉쇄). null=무관
  posture_force: null | 정면 | 후배위 | 기승 | 구속      # 성공 시 강제하는 자세(주도권자용)
  bypass_gating: false        # true면 봉쇄 무시(저항형 = true)
  effect_id: str | null
  log: { on_use: [str], on_hit: [str] }
```

---

## SECTION 2 — 괴물 R18 기술 (공유 풀)

### 2-1. 인간형 공유 (미구속 대상 — 게이트 B 이전)
```yaml
- id: R18_DirtyTalk
  name: 음담패설
  side: monster
  phase: normal_r18
  target: single
  gauge_delta: { arousal_self: +1 }      # 대상 흥분 누적(정신 간섭, 약)
  progress_axis: Cognition
  log: { on_use: ["놈이 귓가에 추잡한 말을 흘렸다."], on_hit: ["말이 머릿속을 끈적하게 맴돌았다."] }

- id: R18_Grope
  name: 주무르기
  side: monster
  phase: normal_r18
  target: single
  gauge_delta: { arousal_self: +2, clothing: +1 }
  progress_axis: Contact
  progress_part: 가슴                      # 부위 민감도 누적 → 곱연산
  log: { on_use: ["놈의 손이 더듬어 왔다."], on_hit: ["억센 손길이 살갗을 짓눌렀다."] }

- id: R18_TearClothes
  name: 옷찢기
  side: monster
  phase: normal_r18
  target: single
  gauge_delta: { clothing: +3 }            # 의복 대량 → 노출 → 성감 배율 증폭
  progress_axis: Contact
  log: { on_use: ["놈이 옷자락을 거머쥐었다."], on_hit: ["천이 찢겨 나갔다."] }
```

### 2-2. 인간형 공유 (구속 대상 — 게이트 B 이후, 준-강기술)
```yaml
- id: R18_ForcedOral
  name: 강제 펠라치오
  side: monster
  phase: normal_r18
  target: single
  lock_condition: target_bound             # 대상 [속박] 시만
  gauge_delta: { arousal_self: +3 }
  progress_axis: Fluid
  progress_part: 입                         # Log_R18_입_괴롭혀짐 누적
  effect_id: fx_r18_bound_only
  log: { on_use: ["놈이 머리를 붙들어 끌어당겼다."], on_hit: ["숨이 막히고 비릿한 것이 입을 채웠다."] }
```

> 형태별 공유(촉수형 다중 속박 등)는 해당 형태 일반괴물 확충 시 추가.

---

## SECTION 3 — 괴물 굴복 페이즈 커맨드 (변질 6축)

> 굴복 페이즈에서 **괴물이 쓰는 공격 커맨드**. 변질 6축으로 분류 — 이 축은 동시에
> `MECH_R18_Memory_Log`의 진척 누적 축이다(공격 분류 = 진척 분류, 정합). 생존자 5분류 커맨드와
> 충돌(SECTION 5 상성표). 괴물은 사용 축 풀을 지정하고, 고정 시그니처 + 풀 추출 혼합으로 운용.

### 3-1. 괴물 커맨드 정의 + 풀 추출
```yaml
# 괴물별 지정 (MONSTER_DB):
r18_submission_draw:
  pools: [Cognition, Fluid]    # 사용할 변질 축 풀 (주력 + 보조)
  draw_count: 3                # 전투마다 풀에서 랜덤 추출 개수
  fixed: [SR_Cog_Whisper]      # 고정 시그니처(항상 보유) — 정체성 유지
```
> **고정+랜덤 혼합**: 완전 랜덤이면 정체성이 흐려짐. 고정 1~2 + 랜덤 2~3 = "정체성 일관 + 매번 변주".
> **풀 내 위력 균질화**: 같은 축 풀의 커맨드는 위력대를 맞춰 "운빨 즉사" 방지.

### 3-2. 축별 괴물 커맨드 풀 (대표 예시 — 추후 확충)
```yaml
# ⑤ 인지 (Cognition)
- id: SR_Cog_Whisper
  name: 잠식의 속삭임
  side: monster; phase: submission; progress_axis: Cognition
  gauge_delta: { arousal_self: +2 }        # 생존자 성감↑
  status_inflict: [ST_Trance]              # 홀림(굴복) — 행동 무작위화
  log: { on_use: ["귓속으로 낮은 음성이 비집고 들었다."] }

# ③ 체액 (Fluid)
- id: SR_Fluid_Feed
  name: 강제 섭취
  side: monster; phase: submission; progress_axis: Fluid; progress_part: 입
  gauge_delta: { arousal_self: +2 }
  effect_id: fx_sub_fluid_feed             # 흡수형으로 받으면 생존자 이득(상성 ◎)
  log: { on_use: ["비릿한 것이 입가로 밀려들었다."] }

# ① 접촉 (Contact)
- id: SR_Contact_Caress
  name: 농밀한 애무
  side: monster; phase: submission; progress_axis: Contact; progress_part: 가슴
  gauge_delta: { arousal_self: +2, clothing: +1 }
  log: { on_use: ["손길이 살갗 위를 느리게 훑었다."] }

# ② 침범 / ④ 변이 / ⑥ 함락 풀은 형태별 괴물 확충 시 추가(골격 예약).
```

### 3-3. 광신도 굴복 커맨드 풀 (인지 + 함락 — 직관적 신체 행위)
> 광신도 사용 축 = **인지 + 함락**. 행위는 직관적 신체 행위로, 효과로 축 정체성 유지.
> 광신의 색(교리·구원)은 연출 텍스트(Gemini)로 입힘 — 메커니즘은 직관 신체.
```yaml
# ⑤ 인지 (Cognition) — 정신을 흔드는 직관 신체 행위
- id: SR_Cog_ForcedKiss
  name: 강제 입맞춤
  side: monster; phase: submission; progress_axis: Cognition; progress_part: 입
  gauge_delta: { arousal_self: +2 }
  status_inflict: [ST_Trance]              # 깊은 키스로 의식을 흐림
  required_parts: [입]; valid_postures: [정면]
  log: { on_use: ["놈이 입술을 틀어막듯 밀어붙였다."] }

- id: SR_Cog_EarLick
  name: 귓속 애무
  side: monster; phase: submission; progress_axis: Cognition; progress_part: 입
  gauge_delta: { arousal_self: +2 }
  status_inflict: [ST_Enthrall]            # 귓가 자극 → 기벽저항↓·성감 가속
  required_parts: [입]
  log: { on_use: ["축축한 숨결이 귓가를 핥았다."] }

- id: SR_Cog_Caress
  name: 농밀한 더듬기
  side: monster; phase: submission; progress_axis: Cognition; progress_part: 가슴
  gauge_delta: { arousal_self: +2, clothing: +1 }
  required_parts: [손]
  log: { on_use: ["손바닥이 온몸을 어지럽게 더듬었다."] }

# ⑥ 함락 (Subjugation) — 의지를 꺾는 직관 신체 행위
- id: SR_Sub_Pin
  name: 짓누르기
  side: monster; phase: submission; progress_axis: Subjugation; progress_part: 전신
  effect_id: fx_sub_will_break             # 짓눌러 굴복도 직접 삭감
  required_parts: [전신]; posture_force: 구속
  log: { on_use: ["체중으로 짓눌러 바닥에 고정했다."] }

- id: SR_Sub_Gag
  name: 입 틀어막기
  side: monster; phase: submission; progress_axis: Subjugation; progress_part: 입
  gauge_delta: { arousal_self: +2 }
  effect_id: fx_sub_offering               # 굴복도 낮을수록 위력↑
  required_parts: [입]; valid_postures: [후배위, 구속]
  log: { on_use: ["입을 틀어막아 봉사를 강요했다."] }

- id: SR_Sub_Thrust
  name: 깊숙이 박기
  side: monster; phase: submission; progress_axis: Subjugation; progress_part: 하복부
  gauge_delta: { arousal_self: +3 }
  status_inflict: [ST_Afterglow]           # 결착 직전 절정 여운 유도
  required_parts: [하복부]; valid_postures: [정면, 후배위]; lock_condition: 굴복도 임계 이하
  log: { on_use: ["끝을 보려는 듯 깊숙이 밀어붙였다."] }
```
> 운용: 인지(흔들기)로 성감·홀림 누적 → 함락(꺾기)으로 굴복도 직접 삭감 → 결착(깊숙이 박기, 임계 이하 피니셔).
> 고정 시그니처 = `SR_Cog_ForcedKiss` + 풀에서 랜덤 2~3 추출.
> 상성: 인지·함락 둘 다 농락(◎)에 약함 → 농락형 역공이 정공법(단 침식·진척 비례).

---

## SECTION 4 — 생존자 굴복 페이즈 기술 (5대분류·공용 풀)

> 굴복 페이즈(흥분 先MAX 진입) 한정. 전원 사용 가능(공용). 위력은 침식·진척·기벽 의존(양날).
> 주도권(Tempo) 작동은 Combat SECTION 11-4.

### ① 봉사형 (Service) — 안정 누적·양날 기본기
```yaml
- id: SB_Service_Kiss
  name: 입맞춤
  side: survivor; phase: submission; sub_category: service
  gauge_delta: { arousal_target: +2, arousal_self: +1 }   # 괴물↑ + 자기↑(양날)
  progress_axis: Contact; progress_part: 입
  log: { on_use: ["떨리는 입술을 가져다 댔다."], on_hit: ["맞닿은 곳에서 열이 옮아왔다."] }
```

### ② 유혹형 (Tease) — 느림·안전·견제
```yaml
- id: SB_Tease_Caress
  name: 애무 지연
  side: survivor; phase: submission; sub_category: tease
  gauge_delta: { arousal_target: +1 }
  status_inflict: [최면]                     # 괴물 다음 행동 약화/교란
  effect_id: fx_sub_weaken_next
  log: { on_use: ["손끝으로 천천히 윤곽을 그렸다."], on_hit: ["놈의 움직임이 한 박자 늦춰졌다."] }
```

### ③ 농락형 (Domination) — 고위력·역전 마무리
```yaml
- id: SB_Dom_Ride
  name: 역제압
  side: survivor; phase: submission; sub_category: domination
  gauge_delta: { arousal_target: +4 }        # 괴물 흥분 폭증
  scaling: erosion                            # 침식·진척 높을수록 강함
  status_inflict: [절정 여운]                  # 성공 시 괴물에 부여 = 주도권 굳히기
  effect_id: fx_sub_dom_scaling
  log: { on_use: ["몸을 일으켜 흐름을 뒤집었다."], on_hit: ["놈의 호흡이 거칠게 무너졌다."] }
```

### ④ 흡수형 (Absorption) — 회복 ↔ 변질 가속(능동)
```yaml
- id: SB_Absorb_Drink
  name: 동화 섭취
  side: survivor; phase: submission; sub_category: absorption
  gauge_delta: { arousal_target: +2 }
  progress_axis: Fluid                        # 체액 축 진척 능동 가속(Memory_Log 연동)
  progress_part: 입
  effect_id: fx_sub_absorb_recover            # 자기 게이지(굴복도/성감 완화) 회복 + 진척↑
  log: { on_use: ["흘러나온 것을 받아 삼켰다."], on_hit: ["몸 안쪽이 뜨겁게 채워졌다."] }
```

### ⑤ 저항형 (Defiance) — 안전판·후퇴
```yaml
- id: SB_Defiance_Focus
  name: 정신 집중
  side: survivor; phase: submission; sub_category: defiance
  effect_id: fx_sub_defiance                  # 굴복도 손실 완화 / 상태이상 해제 / 이탈 시도
  status_inflict: []
  log: { on_use: ["이를 악물고 의식을 붙들었다."], on_hit: ["흐려지던 시야가 잠시 또렷해졌다."] }
```

> 각 분류 개별 기술은 추후 확충(부위·연출별 변종). 현재는 분류당 대표 1종.

---

## SECTION 5 — 축 vs 분류 상성표 (충돌 판정)

> 굴복 페이즈는 **괴물 6축 커맨드 vs 생존자 5분류 커맨드가 합(合) 단위로 충돌**하는 미니게임.
> 한 표를 양방향으로 사용(생존자 대응 / 괴물 주도 모두 커버).

| 괴물 축 ↓ \ 생존자 분류 → | 봉사 | 유혹 | 농락 | 흡수 | 저항 |
|---|---|---|---|---|---|
| **① 접촉** | ○ | ◎ | △ | ○ | ○ |
| **② 침범** | △ | ○ | ○ | △ | ◎ |
| **③ 체액** | ○ | △ | ○ | ◎ | ○ |
| **④ 변이** | △ | ○ | ○ | ○ | ◎ |
| **⑤ 인지** | △ | ○ | ◎ | ○ | ○ |
| **⑥ 함락** | ○ | △ | ◎ | ○ | △ |

(◎ 강한 상성 / ○ 보통 / △ 불리)

```
상성 보정(판정): ◎ +2 주사위 / ○ 0 / △ −1 주사위  (밸런스 시 조정)
충돌 판정 = (발동측 위력 + 상성) vs (대응측 위력 + 상성)
  → 우세측이 차이만큼 이득 + 상태이상 부여 + 주도권 선취/유지
  → 양측 모두 게이지 변동(차등) — 비기는 합 없음
```

상성 설계 의도:
```
접촉←유혹 : 느림의 결을 맞받아 흐름을 끊음
침범·변이←저항 : 돌이킬 수 없는 '수용'을 거부 — 저항이 가장 직접적
체액←흡수 : 받아 흡수하면 오히려 자기 게이지 회복(양날: 체액 축 진척 가속)
인지·함락←농락 : 정신전을 되받아침 — 침식·진척 비례라 '타락한 NPC가 주역'
```

> 운용 함의: 저항형은 침범·변이 방어 특화(만능 아님). 농락형은 인지·함락 역전 특화이나
> 침식·진척 비례 → 순결한 NPC는 못 살림. **타락 정도가 굴복 페이즈 운용을 가른다.**

---

## SECTION 6 — effect_id 핸들러 (R18 위임분)

| effect_id | 동작 |
|---|---|
| `fx_r18_bound_only` | 대상 [속박] 확인 후 발동 (게이트 B) |
| `fx_sub_weaken_next` | 괴물 다음 행동 위력/명중 약화 |
| `fx_sub_dom_scaling` | 침식·부위 민감도·축 진척으로 위력 가산. 절정 여운 부여 |
| `fx_sub_absorb_recover` | 자기 게이지 회복 + Fluid 축 진척 가속(양날) |
| `fx_sub_defiance` | 굴복도 손실 완화 / 상태이상 1개 해제 / 이탈 시도 판정 |
| `fx_sub_fluid_feed` | 흡수형 대응 시 생존자 게이지 회복 + Fluid 진척↑(상성 ◎ 처리) |
| `fx_sub_will_break` | 굴복도 직접 삭감(함락축 — 성감 아닌 의지) + [구속] 자세 강제 |
| `fx_sub_offering` | 굴복도 낮을수록 위력↑(막판 가속) |

---

## SECTION 7 — 참조 방식 & 콘텐츠 경계

```yaml
# MONSTER_DB 개체:
약탈자:
  r18_skills: [R18_DirtyTalk, R18_Grope, R18_TearClothes, R18_ForcedOral]   # 본 카탈로그 참조
# 생존자 굴복 기술: 공용 풀 — 전원 사용 가능(개체 참조 불필요). 기벽 보유 시 위력↑/해금.
```
```
콘텐츠 경계: 성인(18+) 한정. 미성년 캐릭터 일절 미적용(토글 불가). SFW 빌드 = 본 파일 미로드.
신규 Log_/기술 카테고리는 태그 스키마 락 — 디렉터 승인 후 사용.
```

---

## SECTION 8 — 자세 게이팅 (부위 점유 + 자세 정합)

> 상성과 **별개 차원**의 전략 레이어. 상대의 강축 커맨드를 *원천봉쇄*하는 것이 핵심.
> 규칙 작동(가능 커맨드 계산·해제)은 `MECH_Combat_System` SECTION 11-4-8.

### 9-1. 점유 부위
```
[피점유 부위] (메모리 로그 부위와 일치 — 점유 시 그 부위 민감도도 누적):
  입 / 가슴 / 하복부 / 후부 / 전신
  - 커맨드가 점유 → 같은 부위 쓰는 '상대' 커맨드 봉쇄(자원 경합·동적)
  - '전신' 점유(구속류)는 광역 봉쇄 → 강력하나 지속 짧음/저항으로 풀기 쉬움(안전장치)
[행위 부위] (시전에 쓰는 자기 신체 — 그 커맨드에 묶임):
  입 / 손 / 하반신
```

### 9-2. 자세 5종
| 자세 | 성격 | 가능/봉쇄 |
|---|---|---|
| **대치** | 중립(전투 시작 기본) | 대부분 가능, 특화 봉쇄 없음 |
| **정면** | 정면 밀착 | 입·가슴·하복부 접근 ○ / 후부 커맨드 ✕ |
| **후배위** | 등 뒤 제압 | 후부·하복부 ○ / 정면(키스 등) ✕ |
| **기승** | 생존자 상위 주도 | 생존자 농락 일부 해금 / 괴물 주도 제약 (생존자 유리 자세) |
| **구속** | 전신 결박 | 생존자 행위 부위 대폭 제약 → 저항·입 커맨드만 / 강력하나 풀기 쉬움 |

```
주도권자가 자세 강제(posture_force). 자세 되돌리려면 주도권 탈취 필요.
[기승]만 생존자 유리 — 공격형 NPC가 주도권 쥐고 기승 만들어 농락 퍼붓는 구도.
```

### 9-3. 봉쇄 안전장치 (좌절 방지)
```
① 저항형 = bypass_gating: true → 봉쇄 무시 항상 사용 가능(탈출 보루).
② 주도권 탈취 성공 시 점유·자세 해제.
③ 전 부위 동시 봉쇄 불가(점유는 부위 수 한정). 전신 점유는 약점 동반.
```

### 9-4. 유혹형 패링 (봉쇄 탈출 — 고위험 범용 카운터)
```
유혹형은 모든 괴물 공격(자세 게이팅·상태이상 강제 포함)에 패링 시도 가능(범용).
  성공률: 상성 무관 동등(범용성 보존).
  성공 → 적 공격 무력화 + 주도권 탈취.  역상성(◎ 정확히 찌름) = 대성공 보상(흥분 가산/자세 해제).
  실패 → 괴물 흥분 가산 + 제압. 약상성(△)일수록 패널티 증폭 — 생존자의 시도가 '역이용'됨.
        예) 괴물 침범 시도에 유혹+손애무 패링 실패 → 강제 '자위 행위' 전환 → 심각한 성감 피해.
  (역이용 연출은 축별로 다양 — Gemini 분업. 메커니즘은 성감 증폭 공통.)
```
> 유혹(능동 받아치기·주도권 탈취·실패 시 손해) ↔ 저항(수동 버티기·손해 없음·주도권 못 가져옴) 역할 분리.
> 봉쇄 시 탈출구 = 유혹(고위험 역전) / 저항(안전 정비). 둘 다 열려 있어 봉쇄가 좌절이 아닌 역전 무대.

---

## SECTION 9 — 버전 관리

- **문서 위치**: `01_Mechanics/MECH_R18_Skill_Catalog.md`
- **커밋 메시지**: `feat(mechanic): R18 skill catalog (monster shared + survivor submission 5-category, file-level SFW toggle)`
- **Wiki_Index.md 갱신 필요 여부**: **필요 (YES)**

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.0.0 | 2026-06-07 | 최초. R18 스키마 확장(게이지·진척 필드) / 괴물 공유 R18 기술(인간형 미구속·구속) / 생존자 굴복 기술 5대분류 대표 1종씩 / effect_id 핸들러 / 참조 방식 / 파일 단위 SFW 토글. 약탈자 r18_skills ID 추출. |
| v1.1.0 | 2026-06-08 | **괴물 굴복 페이즈 커맨드(변질 6축) 섹션 신설** — 풀 추출(고정+랜덤 혼합)·축별 대표 커맨드. **축 vs 분류 상성표** 추가(충돌 판정 보정). effect_id `fx_sub_fluid_feed` 추가. 섹션 재번호(상성표 5 / effect_id 6 / 참조 7 / 버전 8). |
| v1.2.0 | 2026-06-08 | **자세 게이팅 SECTION 8 신설**: 점유 부위(피점유 5·행위 3)·자세 5종(대치/정면/후배위/기승/구속)·봉쇄 안전장치(저항 면역·주도권 해제·전부위 동시봉쇄 불가)·유혹형 패링(범용·고위험, 약상성 실패 시 역이용 증폭). 스키마에 게이팅 4필드 추가. 버전 섹션 9로. |
| v1.3.0 | 2026-06-08 | **광신도 굴복 커맨드 풀(3-3) 추가**: 인지+함락 6종, 직관적 신체 행위(강제 입맞춤·귓속 애무·농밀한 더듬기 / 짓누르기·입 틀어막기·깊숙이 박기). 부위·자세 명확 → 자세 게이팅·티키타카 작동. effect_id `fx_sub_will_break`·`fx_sub_offering` 추가. |

**갱신 기준**: 분류별 개별 기술 변종 확충. 형태별 괴물 R18 기술 추가. effect_id 코드 동기화.
