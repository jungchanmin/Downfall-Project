---
id: TMPL_EVT_Notification
title: 통보형 이벤트 (Track A) 생성 양식 v2
type: template
status: complete
summary: 선택지 없는 단일 결과 이벤트의 v2 표준 양식. 셜리 잭슨 작법 유지 + Trigger DSL + 조사 슬롯 + Resolution Mode.
tags: [template, event, track_a, notification]
keywords: [이벤트, Track A, 통보형, 셜리잭슨]
depends_on: [SYS_Manifest, SYS_EVT_Template_v2_Spec, EVT_Conveyor_Belt]
emits: []
last_updated: 2026-05-12
---

# 📢 통보형 이벤트 템플릿 v2 (Track A)

> Track A는 *통보형* 이벤트입니다. 플레이어는 결과를 *받습니다* — 선택하지 않습니다.
> 그러나 v2 부터는 *결과가 캐릭터 스탯에 따라 달라질 수 있는* `stat_check` 모드를 허용합니다.

---

## 📋 0. 양식 사용법 (작성 전 필독)

1. 본 양식을 복사해 `/Wiki/05_Events/by_day/Day_XX/EVT_A{nnn}_{hash}.md` 로 저장
2. 모든 *필수 필드* 를 채움 — 빈 칸 ❌ / `TODO` ❌ / `...` ❌
3. 본 양식의 [작법 지침](#-3-셜리-잭슨-라이팅-디렉티브-rendering-directives) 을 *반드시 준수*
4. 완성 후 Gate A 자동 린트 통과 → Gate B 디렉터 검수

---

## ⚙️ 1. 프론트매터 + 메타데이터

### 1-1. 파일 프론트매터 (위키 자동화용)
```yaml
---
id: EVT_A{nnn}_{hash}                   # 예: EVT_A042_a1f3
title: (한국어 제목 — 시적이고 짧게)
type: event
status: draft | wip | complete
summary: 한두 문장 요약. AI 가 이 이벤트를 호출할지 판단하는 근거.
tags: [event, track_a, F{n}_{family}, day_XX, {actor}]
keywords: [등장 인물, 장소, 핵심 개념]
depends_on: [LORE_CHAR_{actor}, LORE_LOC_{loc}]
emits: [Flag_Memory_{...}]              # 이 이벤트가 발행 *가능* 한 모든 플래그
last_updated: YYYY-MM-DD
---
```

### 1-2. 이벤트 메타 (게임 시스템용)
```yaml
event_meta:
  id: EVT_A{nnn}_{hash}
  track: A
  family: F1_Resource | F2_Atmosphere | F3_Internal | F4_Encounter | F5_Cosmic
  phase: 새벽 | 아침 | 점심 | 저녁 | 밤
  location: Loc_{...}                   # 단일 장소 또는 "Any"
  weight: 1.0                           # 가중치 (0.1 ~ 3.0, 희소 이벤트일수록 낮음)
```

---

## 🎯 2. 발동 조건 (Trigger DSL)

> **v2 핵심 변경**: 평문 yaml 조건 ❌ → **재귀 술어 트리** ✅
> *"부적절한 맥락에서 발생하면 어떤 모습인가?" 를 먼저 떠올리고, 그 맥락을 `not` 으로 명시할 것.*

```yaml
trigger:
  all:
    - phase: "{발생 페이즈}"
    - day: { gte: 1, lte: 29 }          # 발생 가능 구간
    
    # ── 발생해야 하는 조건 (positive) ──
    - any:
        - resource: { food: { lt: 5 } }
        - stat: { actor: "*", 스트레스: { gte: 7 } }
    
    # ── 발생하면 안 되는 조건 (negative, 필수) ──
    - not: { flag: "Flag_Food_Abundant" }
    - not:
        any:
          - resource: { food: { gte: 10 } }
          - trait: { actor: "Leader", trait: "낙천적" }
    
    # ── 위치/엔티티 조건 ──
    - location: "Loc_{...}"
    - trait: { actor: "{actor_required}", trait: "{trait_id}" }  # 옵션
```

### DSL 문법 요약 (자세히는 `EVT_Template_v2_Spec.md` Section 2 참조)
- **논리**: `all` (AND) / `any` (OR) / `not` (NOT) — 무한 중첩 가능
- **비교**: `eq`, `neq`, `lt`, `lte`, `gt`, `gte`, `in`
- **와일드카드**: `actor: "*"` — 누구든 한 명이라도 만족하면 참

### 부적절한 맥락 차단 체크리스트 (작성 시 자가 점검)
- [ ] 정반대 상황(식량 풍부, 스트레스 낮음 등)에서 안 터지는가? → `not` 으로 명시
- [ ] 이미 같은 종류의 이벤트가 최근 발생했다면 안 터지는가? → `event_history` 활용
- [ ] 특정 기벽 보유 시 부적절한가? → `not: { trait: ... }`

---

## 🖋️ 3. 셜리 잭슨 라이팅 디렉티브 (Rendering Directives)

*이 이벤트를 작성하는 AI 는 셜리 잭슨의 페르소나를 유지합니다. 피와 괴물이 튀어나오는 천박한 공포를 배제하고, **'숨 막히는 고립감', '공간의 의인화', '인물의 피해망상'** 을 중심으로 아래의 흐름을 따라 장면을 직조하십시오.*

### 3-1. 6단계 작법 흐름 (필수)

1. **공간의 악의 (The Malice of the Room)**: 공간(집, 지하실, 숲)이 인물을 지켜보고 있거나 악의를 품고 기다리는 것처럼 의인화하여 묘사하며 시작한다.
2. **신경증적 투사 (Neurotic Projection)**: 인물의 신체적 약점이나 트라우마가 공간의 불길함과 맞물려 어떻게 발현되는지 보여준다.
3. **초대의 소음 (The Invitation)**: 고요함을 깨는 소음을 단순한 물리적 현상이 아닌, 공간이나 미지의 존재가 인물을 조롱하거나 부르는 '초대' 처럼 서술한다.
4. **발작적 방어 (Paranoid Defense)**: 인물이 극도로 신경질적이고 발작적인 반응을 보이며 경계하지만, 그 행동 자체가 오히려 인물의 나약함과 고립감을 강조하게 만든다.
5. **무력한 목소리 (Futile Voice)**: 인물이 허공에 대고 대사를 뱉지만, 벽에 부딪혀 흩어지는 것처럼 무의미하고 외롭게 들려야 한다.
6. **일상의 배신 (The Betrayal of Reality)**: 괴물이 등장하는 대신, 인물의 발밑이나 일상적인 사물(그림자, 문고리, 거울)이 인물을 배신하고 미쳐가는 듯한 서늘한 현상을 마지막에 배치한다.

### 3-2. 라이팅 통제 규칙 (위반 시 Gate B 회송)

#### 🚫 금지어 (Banned Words)
다음 단어를 *절대* 사용하지 마십시오:
> "코즈믹 호러", "기괴한", "초자연적인", "광기", "무서운", "환각"

오직 *물리적 현상* 과 *생리적 반응(식은땀, 떨림, 호흡)* 만 건조하게 나열하여, 유저가 *스스로* 기괴함을 느끼게 하십시오.

#### 🚫 단일 초점 묘사 (Single Point of Anomaly)
한 이벤트에서 *둘 이상* 의 사물·현상을 동시에 왜곡하지 마십시오.
**일상적이고 평범한 사물 *하나만*** 상식과 미세하게 어긋나도록 묘사하십시오.
> ❌ "물웅덩이가 끓고, 거울이 깨지고, 연기가 났다"
> ⭕ "물웅덩이에 비친 그녀의 표정만 현실의 그녀와 달랐다"

#### 🚫 페르소나 어휘의 자연스러운 체화
직업적 페르소나(예: 가빈의 투자자 성향)를 대사에 적용할 때, 전문 용어를 억지로 욱여넣지 마십시오. 대신 *태도와 행동* 으로 그것을 드러내십시오.
> ❌ "이건 매몰 비용이야"
> ⭕ 동료의 목숨을 *버려도 되는 물건* 처럼 다루는 행동 묘사

#### 🚫 노골적 몬스터·고어 금지
괴물의 찢어진 입, 쏟아지는 내장, 직접적 피의 묘사 ❌
*심리적 착각과 은유* 로 대체:
> ⭕ "녹아내린 촛농이 누군가 악의를 품고 발라놓은 핏자국처럼 보였다"

#### 🚫 영웅적 액션 묘사 금지
인물의 행동은 *언제나* '겁에 질린 자의 발작적 몸부림' 또는 '신경증적 반응' 으로.

---

## 📖 4. 내러티브 모듈 (Narrative Modules)

> **v2 핵심**: 본문 안의 모든 *고유명사* 는 변수 + 조사 슬롯으로 표기.
> `{actor}이` ❌  →  `{actor}{이/가}` ⭕

### 4-1. 기억 삽입구 (Micro-Interjection) — 옵션
*특정 플래그 보유 시* 기본 묘사 앞에 출력되는 한 문장. 인물의 트라우마·과거가 현재 장면에 *드리우는* 효과.

```yaml
interjection:
  condition: { flag: "Flag_Trauma_{...}" }
  text: |
    (예) 지난번처럼 누군가를 버려두고 도망쳐야 할지도 모른다는 공포가
    {actor}{의} 동공을 미세하게 흔든다.
```

### 4-2. 기본 상황 묘사 (Base Narration) — 필수
*Show, Don't Tell.* 6단계 작법 흐름을 *순서대로* 발현.

```yaml
narration: |
  (1단계 공간의 악의) ...
  (2단계 신경증적 투사) ...
  (3단계 초대의 소음) ...
  (4단계 발작적 방어) ...
  (5단계 무력한 목소리) ...
  (6단계 일상의 배신) ...
```

> ⚠️ 6단계를 명시적 라벨로 적지 마십시오 — 자연스러운 산문으로 흐르되, *내부적으로 점검* 만.

### 4-3. 대사 분기 (Dialogue Variants) — 옵션
같은 상황에 대한 *3가지 반응*. 인물의 지배적 기벽에 따라 선택됨.

```yaml
dialogue:
  - condition: { trait: { actor: "{actor}", trait: "감정적" } }
    text: "..."
  - condition: { trait: { actor: "{actor}", trait: "논리적" } }
    text: "..."
  - condition: { stat: { actor: "{actor}", 스트레스: { gte: 8 } } }
    label: 타락함 (Corrupted)
    text: "..."
```

→ 조건 만족 첫 분기 출력. 모두 미충족 시 dialogue 없이 narration 만 출력.

---

## ⚖️ 5. 결과 처리 (Resolution)

> **v2 핵심 변경**: Track A 도 *결정론적*(deterministic) 또는 *판정형*(stat_check) 두 모드 선택 가능.

### 5-1. Mode: deterministic (결과 고정)

대부분의 분위기·세계관 누설 이벤트가 여기에 해당.

```yaml
resolution:
  mode: deterministic
  
  outcome_text: |
    (마무리 문장 1~2개 — 6단계 작법의 *일상의 배신* 과 자연스럽게 연결)
    {actor}{은/는} 그 자리에 한참 서 있었다.
  
  effects:
    stat_delta:
      "{actor}.스트레스": +1
      "all.정신": -1                    # all = 아지트 전원
    resource_delta:
      food: -1
    flags_emit:
      - Flag_Memory_{actor}_Saw_The_Ledger
```

### 5-2. Mode: stat_check (캐릭터 스탯이 결과를 가른다)

캐릭터의 스탯·기벽·상태에 따라 *발견하는 것* 이 달라지는 이벤트.

```yaml
resolution:
  mode: stat_check
  
  check:
    actor: "{actor}"
    stat: 지능 | 인식 | 정신 | ...
    dc: 12                              # 기본 난이도 (8 = 쉬움, 16 = 어려움)
    modifiers:
      - condition: { trait: { actor: "{actor}", trait: "통제강박" } }
        bonus: +2
      - condition: { stat: { actor: "{actor}", 스트레스: { gte: 7 } } }
        penalty: -3
      - condition: { flag: "Flag_Memory_{actor}_Saw_Before" }
        bonus: +1
  
  on_success:
    text: |
      (성공 시 *서늘한 확인* — 안도가 아닌 *오만한 확신*)
      {actor}{은/는} 장부의 결산이 *틀려 있음* 을 알아차린다.
      누군가가 의도적으로 한 줄을 옮겨 적은 흔적이다.
    effects:
      stat_delta:
        "{actor}.정신": -1
        "{actor}.스트레스": +1
      flags_emit:
        - Flag_Memory_{actor}_Found_Forgery
  
  on_fail:
    text: |
      (실패 시 *놓친 무언가* — 명확한 패배가 아닌 *모호한 잔흔*)
      {actor}{은/는} 숫자들을 한참 들여다본 뒤 책상을 떠난다.
      무엇인가 어긋났다는 느낌만 남았다.
    effects:
      stat_delta:
        "{actor}.스트레스": +1
      flags_emit:
        - Flag_Memory_{actor}_Missed_Forgery
```

#### 🚫 stat_check 결과 작성 시 절대 금지
- on_success ≠ *완전한 해결*. 성공해도 톤은 *서늘한 확인* 까지만.
- on_fail ≠ *명확한 패배*. 실패해도 톤은 *놓친 무언가* 까지만.
- 두 결과의 *분량 차이* 가 5:1 이상 벌어지지 않도록 (성공만 길게 ❌)

---

## 🪶 6. 셜리 잭슨 발현 축 (Self-Audit)

작성 후 *반드시* 다음을 표시. Gate B 검수의 1차 근거.

```yaml
shirley_jackson_axes:
  primary: 공간의_악의 | 신경증적_투사 | 일상의_배신 | 무력한_목소리
  secondary: (동일 옵션 중 하나)
  notes: |
    (한 줄로 — 이 이벤트의 잭슨식 핵심이 *무엇* 인지)
```

---

## 📝 7. 예시 데이터 — 「제단의 시선」

기존 양식의 우수한 예시. v2 양식으로 *재포맷* 하면 다음과 같이 변환됩니다.

```yaml
---
id: EVT_A007_4d2a
title: 제단의 시선
type: event
status: complete
summary: 성당 지하실에서 레이첼이 자신의 그림자가 제단을 향해 기어가는 것을 목격하는 통보형 이벤트.
tags: [event, track_a, F2_Atmosphere, rachel, oebeng_cathedral]
keywords: [성당, 지하실, 제단, 그림자, 레이첼]
depends_on: [LORE_CHAR_Rachel, LORE_LOC_Oebeng_Cathedral]
emits: [Flag_Memory_Rachel_Shadow_Crawled]
last_updated: 2026-05-12
---

event_meta:
  id: EVT_A007_4d2a
  track: A
  family: F2_Atmosphere
  phase: 밤
  location: Loc_성당_지하실
  weight: 1.0

trigger:
  all:
    - phase: 밤
    - location: Loc_성당_지하실
    - any:
        - stat: { actor: Rachel, 스트레스: { gte: 5 } }
        - flag: Flag_Memory_Rachel_Visited_Altar_Before
    - not: { flag: Flag_Cathedral_Cleansed }
    - not: { trait: { actor: Rachel, trait: "초자연_무감각" } }

narration: |
  지하실은 언제나 그녀를 기다려온 것처럼 기분 나쁜 침묵으로 웅크리고 있었다.
  제단에 흘러내린 붉은 촛농은 누군가 악의를 품고 발라놓은 핏자국처럼 보였다.
  {actor}{은/는} 등불을 내려놓으며 발목을 감싸 쥐었다. 이 성당은 사람의
  약점을 기가 막히게 알아채는 구석이 있었다.

  챙그랑. 어둠 속에서 들려온 그 쇳소리는 단순한 소음이 아니라 명백한 초대의
  인사였다. {actor}{은/는} 발작적으로 돌아서며 부러진 검을 내밀었다.
  흔들리는 불빛 아래로 흩어진 묵주알과 부서진 의자 틈새에서, 아주 창백하고
  얌전한 손가락 하나가 그녀를 향해 내밀어져 있었다.

  "겁쟁이처럼 숨지 말고 기어나와."

  {actor}{은/는} 소리쳤지만 그 목소리는 벽에 부딪혀 무력하게 흩어졌다.
  불꽃은 고요했다. 하지만 {actor}{은/는} 자신의 발밑을 내려다보고는
  숨을 삼켰다. 그녀의 그림자가 천천히 몸을 비틀더니, 마치 제단이 부르는
  소리라도 들은 것처럼 스멀스멀 그곳을 향해 기어가고 있었다. 어둠이
  {actor}{의} 조각을 떼어내 삼키고 있었다.

resolution:
  mode: deterministic
  effects:
    stat_delta:
      "Rachel.정신": -2
      "Rachel.스트레스": +2
    flags_emit:
      - Flag_Memory_Rachel_Shadow_Crawled

shirley_jackson_axes:
  primary: 일상의_배신
  secondary: 공간의_악의
  notes: |
    그림자가 *주인을 배신* 하고 제단으로 기어가는 결말 —
    가장 일상적인 사물(자신의 그림자)이 어긋남.
```

---

## ✅ 8. 작성 완료 체크리스트 (Gate A 자동 린트와 일치)

작성자(AI) 는 출고 전 다음을 자가 점검:

- [ ] 모든 필수 필드가 채워져 있는가 (id, title, family, phase, trigger, narration, resolution, emits)
- [ ] `family` 가 F1~F5 중 하나로 지정되었는가
- [ ] 트리거에 *부적절한 맥락 차단* 의 `not` 조건이 포함되었는가
- [ ] 모든 변수 뒤에 *조사 슬롯* 이 사용되었는가 (`{actor}이` 같은 직접 표기 ❌)
- [ ] 금지어(코즈믹 호러, 기괴한, 초자연적인, 광기, 무서운, 환각)가 본문에 없는가
- [ ] 단일 초점 묘사 원칙 — 어긋난 사물이 *하나* 뿐인가
- [ ] 6단계 작법 흐름이 자연스럽게 발현되었는가
- [ ] stat_check 모드라면 on_success 도 *완전한 해결* 이 아닌가
- [ ] `emits` 에 본문에서 발행하는 모든 `Flag_*` 가 등재되었는가
- [ ] `shirley_jackson_axes` 가 명시되었는가
