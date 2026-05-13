---
id: TMPL_EVT_Interactive
title: 개입형 이벤트 (Track B) 생성 양식 v2
type: template
status: complete
summary: 2~3 선택지를 가진 개입형 이벤트의 v2 표준 양식. 내러티브 모듈 분리 + Trigger DSL + 조사 슬롯 + 선택지 내부 stat_check.
tags: [template, event, track_b, interactive]
keywords: [이벤트, Track B, 개입형, 선택지, 판정]
depends_on: [SYS_Manifest, SYS_EVT_Template_v2_Spec, EVT_Conveyor_Belt]
emits: []
last_updated: 2026-05-12
---

# 🎲 개입형 이벤트 템플릿 v2 (Track B)

> Track B는 *개입형* 이벤트입니다. 플레이어는 *선택* 합니다. 그 선택은 *대가* 를 동반합니다.
> v2 부터는 각 선택지 내부에 *캐릭터 스탯·상태에 따른 modifier* 가 적용되는 stat_check 구조를 표준화합니다.

---

## 📋 0. 양식 사용법 (작성 전 필독)

1. 본 양식을 복사해 `/Wiki/05_Events/by_day/Day_XX/EVT_B{nnn}_{hash}.md` 로 저장
2. 모든 *필수 필드* 를 채움
3. **선택지는 2~3개**. 한쪽이 명백히 우월하면 더미 선택지 → *Gate B 회송*
4. 본 양식의 [작법 지침](#-3-라이팅-디렉티브) 을 *반드시 준수*

---

## ⚙️ 1. 프론트매터 + 메타데이터

### 1-1. 파일 프론트매터 (위키 자동화용)
```yaml
---
id: EVT_B{nnn}_{hash}                   # 예: EVT_B007_a1f3
title: (한국어 제목)
type: event
status: draft | wip | complete
summary: 한두 문장 요약 — 이 이벤트의 딜레마 본질.
tags: [event, track_b, F{n}_{family}, day_XX, {actor}]
keywords: [등장 인물, 장소, 핵심 딜레마]
depends_on: [LORE_CHAR_{actor}, LORE_LOC_{loc}]
emits: [Flag_Memory_{...}]
last_updated: YYYY-MM-DD
---
```

### 1-2. 이벤트 메타 (게임 시스템용)
```yaml
event_meta:
  id: EVT_B{nnn}_{hash}
  track: B
  family: F1_Resource | F2_Atmosphere | F3_Internal | F4_Encounter | F5_Cosmic
  category: 탐색_조우 | 거점_방어 | 세력_거래 | 내부_중재
  phase: 새벽 | 아침 | 점심 | 저녁 | 밤
  location: Loc_{...}
  weight: 1.0
```

---

## 🎯 2. 발동 조건 (Trigger DSL)

> *"부적절한 맥락에서 발생하면 어떤 모습인가?" 를 먼저 떠올리고, 그 맥락을 `not` 으로 명시.*

```yaml
trigger:
  all:
    - phase: "{발생 페이즈}"
    - location: "Loc_{...}"
    
    # ── 참여 엔티티 조건 ──
    - trait: { actor: "{actor_required}", trait: "파견조" }
    - stat: { actor: "{actor_required}", 탐색: { gte: 3 } }
    
    # ── 지배적 상태 ──
    - any:
        - stat: { actor: "*", 스트레스: { gte: 8 } }
        - flag: "Flag_Crisis_{...}"
    
    # ── 환경 조건 ──
    - flag: "Flag_Env_안개"               # 예시
    
    # ── 부적절한 맥락 차단 (필수) ──
    - not: { flag: "Flag_Cathedral_Cleansed" }
    - not: { event_history: { id: "EVT_B007_a1f3", occurred: true } }
```

DSL 문법은 `EVT_Notification.md` 와 동일. 자세히는 `EVT_Template_v2_Spec.md` Section 2 참조.

---

## 🖋️ 3. 라이팅 디렉티브 (Rendering Directives)

### 3-1. Downfall Voice
- 하드보일드 문체. 과장된 수식어 금지.
- 본문은 짧은 문장의 누적으로 *긴장* 을 만든다.

### 3-2. 코즈믹 호러 3원칙
1. **설명 금지**: 위협의 정체나 기원을 *구체적으로* 묘사하지 말 것.
2. **감각의 왜곡**: 시각/청각/후각 중 *하나만* 기괴하게 비틀 것.
   (예: 피비린내 대신 *역겨울 정도로 달콤한 꽃향기*)
3. **보상 속의 저주**: 이득을 취하는 선택지라도 *반드시* 찝찝한 심리적/시각적 대가가 따르도록.

### 3-3. 성격과 타락(Corruption) 모델
선택지 전 상황 묘사와 [대사 분기](#4-3-대사-분기-dialogue-variants) 작성 시:
- 캐스팅된 NPC 의 *로어 바이블 (Bot_Universal_Template) 데이터* 에 맞춰 대사 출력
- *지배적 상태 발동 중* (예: 극심한 스트레스) 이라면 → *타락한 대사* 출력

### 3-4. 라이팅 통제 규칙 (Track A 와 공유)

#### 🚫 금지어 (Banned Words)
> "코즈믹 호러", "기괴한", "초자연적인", "광기", "무서운", "환각"
물리적 현상과 생리적 반응(식은땀, 떨림)만 건조하게 나열.

#### 🚫 단일 초점 묘사 (Single Point of Anomaly)
*하나의 사물·현상만* 상식과 미세하게 어긋나도록.

#### 🚫 페르소나 어휘의 자연스러운 체화
직업적 페르소나를 *전문 용어* 가 아닌 *태도와 행동* 으로.

#### 🚫 노골적 몬스터·고어 / 영웅적 액션 금지

---

## 📖 4. 내러티브 모듈 (Narrative Modules)

> **v2 핵심**: 기존 양식의 *3 모듈 분리(기억 / 기본묘사 / 대사분기) 설계는 그대로 유지.* 변수 처리만 보강.

### 4-1. 기억 삽입구 (Micro-Interjection) — 옵션
특정 플래그 보유 시, 기본 묘사 *앞에* 출력되는 한 문장.

```yaml
interjection:
  condition: { flag: "Flag_Trauma_Cowardice" }
  text: |
    지난번처럼 누군가를 버려두고 도망쳐야 할지도 모른다는 공포가
    {actor}{의} 동공을 미세하게 흔든다.
```

여러 개 가능. 첫 조건 만족분만 출력.

### 4-2. 기본 상황 묘사 (Base Narration) — 필수
*Show, Don't Tell.* 다음 슬롯을 채움:

```yaml
narration: |
  (감각 진입 — 시각·청각·후각 중 *하나만* 왜곡)
  ...
  
  (공간 또는 사물의 묘사 — 일상적인 것의 미세한 어긋남)
  ...
  
  (보상의 가시화 — 무엇을 노릴 수 있는지 *간접적* 제시)
  ...
  
  (저주의 암시 — 보상을 취할 때 따라올 *대가의 그림자*)
  ...
```

> ⚠️ 위 슬롯 라벨을 본문에 적지 마십시오. 자연스러운 산문으로 흐르되 *내부적으로* 점검.

### 4-3. 대사 분기 (Dialogue Variants)
같은 상황에 대한 인물 반응. 보유 기벽·지배적 상태로 분기.

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

평가 순서: 위에서 아래로, 첫 조건 만족분 출력. 모두 미충족 시 dialogue 생략.

---

## ⚖️ 5. 선택지 (Choices) — Track B 의 핵심

### 5-1. 선택지 작성 원칙

| 항목 | 규칙 |
|---|---|
| 개수 | 2 또는 3 (선택지 4개 이상 ❌ — 분기 폭발) |
| 균형 | 한쪽이 *명백히 우월* 하면 안 됨. 각 선택지는 *다른 비용* 을 동반 |
| 기회비용 명시 | 각 선택지마다 *무엇을 포기하는가* 가 분명해야 함 |
| 비도덕 옵션 | 동료를 미끼로 삼는 등 비인간적 선택지 *환영*. 단 *결과로 대가* 부과 |
| 도주 옵션 | "도망친다" 류는 안전하지만 *자원·진척의 손실* 동반 |

### 5-2. 선택지 스키마

```yaml
choices:
  - id: ch1
    label: (행동을 짧고 명확하게 — 예: "렌치를 휘둘러 안구들을 짓이기고 구급상자를 뺏는다")
    cost: { time: 1 }                    # 즉시 비용 (옵션)
    
    resolution:
      mode: stat_check                   # stat_check | deterministic
      
      check:
        actor: "{assigned_actor}"
        stat: 전투 | 인식 | 적응도 | 지능 | ...
        dc: 12
        modifiers:
          - condition: { trait: { actor: "{assigned_actor}", trait: "통제강박" } }
            bonus: +2
          - condition: { stat: { actor: "{assigned_actor}", 정신: { lt: 30 } } }
            penalty: -3
      
      on_success:
        text: |
          (보상 + *반드시* 찝찝한 대가의 그림자)
          둔탁한 타격음과 함께 젤리 같은 안구들이 터져 나간다. 그것이
          기괴한 비명을 지르며 물러서는 틈을 타 {actor}{이/가} 구급상자를
          낚아챈다. 하지만 터져 나온 체액이 {actor}{의} 팔에 눌어붙는다.
        effects:
          stat_delta:
            "{actor}.체력": -1
          resource_delta:
            의약품: +1
          flags_emit:
            - Flag_Trace_시선이_박힌_흉터    # 상태창 흔적
            - Flag_Memory_{actor}_Took_Medkit
      
      on_fail:
        text: |
          (실패의 모호함 — 명확한 패배 ❌, *놓친 무언가*)
          타격은 미끄러진다. 터진 안구 속에서 뻗어 나온 촉수가 
          {actor}{의} 손목을 휘감는다. 살이 타들어 가는 냄새가 진동한다.
        effects:
          stat_delta:
            "{actor}.체력": -2
          flags_emit:
            - Flag_강제전투_돌입
            - Flag_Trace_환지통과_속삭임

  - id: ch2
    label: "{ally}{을/를} 미끼로 삼아 시선을 끈 사이 물건을 훔친다"
    cost: { relation_risk: high }
    
    resolution:
      mode: stat_check
      check:
        actor: "{actor}"
        stat: 적응도
        dc: 14
        modifiers:
          - condition: { trait: { actor: "{actor}", trait: "냉혹함" } }
            bonus: +3
      
      on_success:
        text: |
          {actor}{이/가} 등을 떠밀자 {ally}{이/가} 비명을 지르며 넘어진다.
          괴물의 모든 안구가 그를 향한 사이, {actor}{은/는} 쥐새끼처럼
          구급상자를 챙겨 빠져나온다. {ally}{은/는} 간신히 살아 돌아오지만,
          그 눈빛은 예전과 다르다.
        effects:
          resource_delta: { 의약품: +1 }
          relation_delta:
            "{actor},{ally}": -4
          flags_emit:
            - Flag_Trauma_{ally}_Betrayed_By_{actor}    # 후속 타락 이벤트 씨앗
            - Flag_Memory_{actor}_Used_Ally_As_Bait
      
      on_fail:
        text: |
          (생략 — 작가가 채움)
        effects: { ... }

  - id: ch3
    label: "문을 닫고 도망친다"
    cost: { time: 1 }
    
    resolution:
      mode: deterministic                 # 도주는 판정 없이 고정
      
      outcome_text: |
        우주적 공포 앞에서 이성은 도주를 명한다. 덜덜 떨리는 손으로
        문을 닫고 폐가를 빠져나오지만, 등 뒤에서 문을 긁는 소리가
        아지트까지 환청처럼 따라붙는다.
      effects:
        stat_delta:
          "all.스트레스": +1
        flags_emit:
          - Flag_Memory_{actor}_Fled_Abandoned_House
```

### 5-3. 상태창 흔적 (Status Trace) — `Flag_Trace_*`
선택지 결과로 *캐릭터의 상태창에 영구히 남는 흉터*. 단순 텍스트가 아니라 *재호출 가능한 플래그*.

> 예: `Flag_Trace_시선이_박힌_흉터` →
> 향후 이벤트에서 `{ if: flag: Flag_Trace_시선이_박힌_흉터 }` 로 트리거 가능.

이러한 흔적은 *반드시* `emits` 필드에 등재.

---

## 🪶 6. 셜리 잭슨 발현 축 (Self-Audit)

```yaml
shirley_jackson_axes:
  primary: 일상의_배신 | 공간의_악의 | 신경증적_투사 | 무력한_목소리
  secondary: (동일 옵션)
  notes: |
    이 이벤트의 잭슨식 핵심은 *무엇* 인지 한 줄.
```

---

## ✅ 7. 작성 완료 체크리스트 (Gate A 자동 린트와 일치)

- [ ] 모든 필수 필드 채워짐 (id, title, family, phase, location, trigger, narration, choices, emits)
- [ ] `family` 가 F1~F5 중 하나로 지정
- [ ] 트리거에 *부적절한 맥락 차단* 의 `not` 조건 포함
- [ ] 모든 변수에 *조사 슬롯* 사용 (`{actor}이` 같은 직접 표기 ❌)
- [ ] 금지어가 본문에 없음
- [ ] 단일 초점 묘사 — 어긋난 사물이 *하나* 뿐
- [ ] 선택지 2~3 개, 한쪽이 명백히 우월하지 *않음*
- [ ] 각 선택지의 *기회비용* 이 명확함
- [ ] 성공 결과에 *반드시* 찝찝한 대가의 그림자 있음 (보상 속의 저주)
- [ ] 실패 결과가 *명확한 패배* 가 아닌 *모호한 잔흔*
- [ ] 모든 발행 가능한 `Flag_*` 가 `emits` 에 등재됨
- [ ] `shirley_jackson_axes` 명시됨
