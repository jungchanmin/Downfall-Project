---
id: SYS_EVT_Template_v2_Spec
title: 범용 이벤트 템플릿 v2 사양 — 4대 문제 해결안
type: system
status: draft
version: 2.1
summary: EVT_Notification 의 콘텐츠 다양화·맥락 필터링·한국어 조사 처리·판정 구조를 통합한 v2 템플릿 사양. v2.1: 아이템·유물 획득 블록 확장.
tags: [system, template, event, schema]
keywords: [이벤트, 템플릿, 필터링, 조사, 판정, DC, 유물, 아이템, relic_acquire, item_acquire]
depends_on: [SYS_Manifest, TMPL_EVT_Notification, TMPL_EVT_Interactive, MECH_Resource_System, ITEM_Relic_DB]
last_updated: 2026-05-21
---

# 🧩 EVT Template v2 — 4대 문제 통합 해결안

> **요약**: 범용 이벤트(주로 Track A)의 콘텐츠 분량·맥락 정합성·언어 자연스러움·판정 구조 문제를 *단일한 스키마 확장* 으로 해결한다.

---

## 0. 문제 진단 (요약)

| # | 문제 | 본질 |
|---|---|---|
| 1 | 범용 이벤트의 종류 부족 | 단일 템플릿 → 단일 톤. *템플릿이 패밀리 단위로 갈라지지 않음.* |
| 2 | 부적절한 맥락에서 발생 | 트리거 조건이 *positive 조건만* 검사하고 *negative/numeric* 검사가 빈약. |
| 3 | 생존자 이름에 따른 조사 오류 | 한국어 받침 유무에 따른 조사 변형이 *템플릿 차원에서 미해결*. |
| 4 | 결과가 사전 확정됨 | Track A 가 *결정론적* 으로 끝남. 캐릭터 스탯이 결과에 개입할 자리가 없음. |

→ 네 문제 모두 **이벤트 스키마의 표현력 부족** 이라는 같은 뿌리에서 나온다. 한 번에 풀어야 한다.

---

## 1. 해법 ① — 이벤트 패밀리(Event Family) 분류

### 1-1. 단일 "범용 템플릿" 의 함정
지금까지 *범용 이벤트* 라고 부르던 것은 사실 *분류되지 않은* 이벤트였습니다. 분류가 없으면:
- 같은 패턴이 무한 반복됨 (AI 가 익숙한 형태만 양산)
- 비어 있는 영역이 보이지 않음
- 디렉터가 *오늘 무엇을 더 만들어야 하는지* 판단 불가

### 1-2. 5대 이벤트 패밀리

| 패밀리 | 정의 | 비중 (권장) | 셜리 잭슨 발현 축 |
|---|---|---|---|
| **F1. Resource** | 자원의 유입·유출·발견·부패 | 25% | 굴복하는 공간 / 차가운 안도 |
| **F2. Atmosphere** | 환경·날씨·공간·전조 | 25% | 공간의 악의 / 일상의 배신 |
| **F3. Internal** | 아지트 내부 인간 관계·기벽 발현 | 25% | 신경증적 투사 / 무력한 목소리 |
| **F4. Encounter** | 외부 존재·접촉·관찰 | 15% | 일상의 배신 (노골 ❌) |
| **F5. Cosmic** | 이해 불가능성의 누설 | 10% | 4지침 전부 미세하게 |

→ 매주 산출되는 이벤트의 패밀리 분포를 추적하면, *어떤 영역이 부족한지* 자동으로 드러납니다 (Gate C 의 분포 점검과 연동).

### 1-3. 패밀리별 슬롯 변수 (Parametric Templates)

각 패밀리는 *변수 슬롯* 을 가집니다. 같은 템플릿에서 *N개의 변형* 이 생성됩니다.

**예시 — F2 Atmosphere 의 슬롯:**
```yaml
family: F2_Atmosphere
slots:
  - location:
      values: [Loc_거실, Loc_복도, Loc_지하실, Loc_창고, Loc_부엌]
  - sensory_axis:
      values: [시각, 청각, 후각, 촉각]
  - intensity:
      values: [희미한, 분명한, 견딜 수 없는]
  - anomaly_type:
      values: [대칭의 어긋남, 시간의 반복, 사물의 위치, 그림자]
```

→ 이 한 패밀리에서 5 × 4 × 3 × 4 = **240개의 조합**.

### 1-4. 패밀리 분포 메트릭

PM 세션이 매주 점검:
```
F1 Resource:    ████████░░ 23개 / 50 목표  (46%)
F2 Atmosphere:  ██████████ 51개 / 50 목표  (102%) ⚠ 과잉
F3 Internal:    ████░░░░░░ 18개 / 50 목표  (36%) ← 우선
F4 Encounter:   ██████░░░░ 28개 / 30 목표  (93%)
F5 Cosmic:      ███░░░░░░░ 7개  / 20 목표  (35%) ← 우선
```

---

## 2. 해법 ② — Trigger DSL (맥락 필터링)

### 2-1. 트리거 DSL 도입

JSON 술어 트리(predicate tree)로 표현합니다.

```json
{
  "trigger": {
    "all": [
      { "phase": "아침" },
      { "day": { "gte": 5 } },
      {
        "any": [
          { "resource": { "food": { "lt": 5 } } },
          { "stat": { "actor": "*", "stress": { "gte": 7 } } }
        ]
      },
      { "not": { "flag": "Flag_Food_Abundant" } },
      { "not": { "trait": { "actor": "Leader", "trait": "낙천적" } } }
    ]
  }
}
```

### 2-2. DSL 문법 명세

**논리 연산자 (재귀 가능)**:
- `all: [...]` — AND
- `any: [...]` — OR
- `not: {...}` — NOT

**리프 술어**:
| 술어 | 의미 | 예시 |
|---|---|---|
| `phase` | 현재 페이즈 일치 | `{"phase": "밤"}` |
| `day` | 일자 비교 | `{"day": {"gte": 10, "lt": 20}}` |
| `location` | 현재 장소 | `{"location": "Loc_성당"}` |
| `resource` | 자원 수치 | `{"resource": {"food": {"lt": 3}}}` |
| `stat` | 캐릭터 스탯 | `{"stat": {"actor": "Gavin", "stress": {"gte": 5}}}` |
| `trait` | 기벽 보유 | `{"trait": {"actor": "*", "trait": "통제강박"}}` |
| `flag` | 플래그 존재 | `{"flag": "Flag_Memory_Gavin_X"}` |
| `relation` | 관계 수치 | `{"relation": {"a": "Gavin", "b": "Rachel", "gte": 3}}` |
| `event_history` | 과거 발생 이력 | `{"event_history": {"id": "EVT_A001", "occurred": false}}` |
| `relic` | 유물 소지 여부 | `{"relic": {"actor": "*", "id": "RELIC_HighPriestDagger"}}` |

**비교 연산자**: `eq`, `neq`, `lt`, `lte`, `gt`, `gte`, `in`

---

## 3. 해법 ③ — 한국어 조사 슬롯 시스템

### 3-1. 조사 슬롯 문법

```
{actor}{이/가} 회계 장부를 들었다.
{target}{을/를} 노려보았다.
{actor}{은/는} 침묵했다.
{actor}{와/과} 함께였다.
{actor}{으로/로} 향했다.
```

### 3-2. 지원되는 조사 쌍

| 슬롯 | 받침 있음 | 받침 없음 |
|---|---|---|
| `{이/가}` | 이 | 가 |
| `{을/를}` | 을 | 를 |
| `{은/는}` | 은 | 는 |
| `{와/과}` | 과 | 와 |
| `{으로/로}` | 으로 | 로 |
| `{아/야}` | 아 | 야 |
| `{이여/여}` | 이여 | 여 |

---

## 4. 해법 ④ — Resolution Mode (판정 구조)

### 4-1. Resolution Mode 도입

```yaml
resolution:
  mode: deterministic | stat_check | choice
```

| 모드 | 의미 | 사용 처 |
|---|---|---|
| `deterministic` | 결과 고정 | 분위기 누설, 환경 이벤트, 통보 |
| `stat_check` | 캐릭터 스탯 판정으로 분기 | 자동 해결되지만 결과 가변 |
| `choice` | 플레이어 선택 | Track B 의 본질 |

### 4-2. 트랙과 모드의 매트릭스

| Track | 허용 모드 | 비중 (권장) |
|---|---|---|
| A | `deterministic`, `stat_check` | 70% / 30% |
| B | `choice` (선택 내부에 `stat_check` 중첩 가능) | 100% |

---

## 5. v2.1 확장 — 아이템·유물 획득 블록

> **v2.1 신규 추가 (2026-05-21)**
> 이벤트 결과로 아이템 또는 유물을 획득하는 경우를 처리하기 위한
> `item_acquire` 및 `relic_acquire` 블록을 공식 스키마에 추가한다.

### 5-1. relic_acquire 블록

유물 획득 시 사용. `ITEM_Relic_DB.md` 에 등재된 유물만 참조 가능.

```yaml
resolution:
  mode: deterministic | stat_check
  on_success:  # 또는 choice 선택지 내부
    narration: |
      [텍스트]
    stat_delta:
      "{actor}.스탯명": +N
    relic_acquire:
      id: RELIC_{유물식별자}        # ITEM_Relic_DB 등재 ID
      bound_to: "{actor}"           # 귀속 대상
      daily_penalty_active: true    # 일일 패널티 활성화 여부
    flags_emit:
      - Flag_Item_{유물명}_Owned
```

**처리 규칙**:
- `relic_acquire` 실행 시 해당 유물의 `stat_bonus` 가 즉시 적용
- `daily_penalty_active: true` 이면 매일 밤 행동계산 페이즈에
  `ITEM_Relic_DB` 의 `daily_penalty` 가 자동 실행
- 귀속된 유물은 `Flag_Item_{유물명}_Owned` 플래그로 소지 추적
- 동일 유물 중복 획득 불가 (트리거 `not: { flag: Flag_Item_{유물명}_Owned }` 로 차단)

**엔진 구현 요구사항**:
```python
def apply_relic_acquire(actor, relic_id, state):
    relic = load_relic(relic_id)           # ITEM_Relic_DB 참조
    state.apply_stat_bonus(actor, relic.stat_bonus)
    state.bind_relic(actor, relic_id)
    if relic.daily_penalty_active:
        state.register_daily_effect(actor, relic.daily_penalty)
    state.emit_flag(f"Flag_Item_{relic_id}_Owned")
```

---

### 5-2. item_acquire 블록

일반 장비·소모품 획득 시 사용. 유물과 달리 귀속되지 않으며
수량으로 관리.

```yaml
resolution:
  mode: deterministic | stat_check
  on_success:
    narration: |
      [텍스트]
    item_acquire:
      - id: ITEM_{아이템식별자}
        quantity: N
        category: 의약품 | 무기류 | 일회용품 | 사치품
    flags_emit:
      - Flag_Memory_{actor}_{이벤트명}
```

**처리 규칙**:
- `item_acquire` 실행 시 인벤토리에 수량 추가
- 장비 카테고리에 따라 저장 위치 자동 분류
- 수량 상한은 `MECH_Resource_System` 의 1회 변동 상한 ±3 이내 권장

---

### 5-3. 두 블록의 공존

하나의 이벤트 결과에서 `relic_acquire` 와 `item_acquire` 가
동시에 존재할 수 있다.

```yaml
on_success:
  narration: |
    [텍스트]
  stat_delta:
    "{actor}.스트레스": -1
  relic_acquire:
    id: RELIC_HighPriestDagger
    bound_to: "{actor}"
    daily_penalty_active: true
  item_acquire:
    - id: ITEM_OldBandage
      quantity: 2
      category: 의약품
  flags_emit:
    - Flag_Item_HighPriestDagger_Owned
```

---

### 5-4. relic_acquire 사용 시 Gate C 추가 검사

이벤트 파일에 `relic_acquire` 블록이 있는 경우:

- [ ] `ITEM_Relic_DB.md` 에 해당 `id` 가 등재되어 있는가
- [ ] `trigger` 에 `not: { flag: Flag_Item_{유물명}_Owned }` 가 포함되어 있는가
- [ ] `flags_emit` 에 `Flag_Item_{유물명}_Owned` 가 등재되어 있는가
- [ ] `daily_penalty_active: true` 라면 `ITEM_Relic_DB` 의
      `daily_penalty` 블록이 정의되어 있는가

---

## 6. 통합 — v2.1 템플릿의 최종 모습

```yaml
# Track B v2.1 (relic_acquire 포함 예시)

id: EVT_B{nnn}_{hash}
title: (한국어 제목)
track: B
family: F1_Resource | F2_Atmosphere | F3_Internal | F4_Encounter | F5_Cosmic
status: complete

trigger:
  all:
    - phase: "..."
    - not: { flag: "Flag_Item_{유물명}_Owned" }  # 유물 소지 시 차단

intro_narration: |
  (시네마틱 도입부)

choices:
  - id: ch1
    label: "선택지 라벨"
    resolution:
      mode: deterministic
      narration: |
        (결과 텍스트)
      stat_delta: { ... }
      relic_acquire:                          # ← v2.1 신규
        id: RELIC_{유물식별자}
        bound_to: "{actor}"
        daily_penalty_active: true
      item_acquire:                           # ← v2.1 신규
        - id: ITEM_{아이템식별자}
          quantity: N
          category: 의약품
      flags_emit:
        - Flag_Item_{유물명}_Owned

  - id: ch2
    label: "선택지 라벨"
    resolution:
      mode: deterministic
      narration: |
        (결과 텍스트)
      stat_delta: { ... }
      flags_emit:
        - Flag_Memory_{actor}_{이벤트명}

emits:
  - Flag_Item_{유물명}_Owned
  - Flag_Memory_{actor}_{이벤트명}

shirley_jackson_axes:
  primary: 공간의_악의 | 신경증적_투사 | 일상의_배신 | 무력한_목소리
  secondary: ...
```

---

## 7. Gate A 자동 린트 (v2.1 추가)

기존 린트에 다음 추가:

| 린트 | 검사 내용 |
|---|---|
| `lint_relic_db_ref` | `relic_acquire.id` 가 `ITEM_Relic_DB` 에 존재하는가 |
| `lint_relic_trigger` | `relic_acquire` 사용 시 트리거에 소지 차단 `not` 조건이 있는가 |
| `lint_relic_flag` | `relic_acquire` 사용 시 `flags_emit` 에 소지 플래그가 있는가 |
| `lint_item_quantity` | `item_acquire.quantity` 가 1회 변동 상한 ±3 을 초과하는가 |

---

## 8. 버전 관리

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v2.0 | 2026-05-12 | 최초 작성. 4대 문제 해결안 통합. |
| v2.1 | 2026-05-21 | SECTION 5 추가. `relic_acquire` / `item_acquire` 블록 공식화. Gate A 린트 4종 추가. `relic` 트리거 술어 추가. |
