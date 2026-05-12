---
id: SYS_EVT_Template_v2_Spec
title: 범용 이벤트 템플릿 v2 사양 — 4대 문제 해결안
type: system
status: draft
summary: EVT_Notification 의 콘텐츠 다양화·맥락 필터링·한국어 조사 처리·판정 구조를 통합한 v2 템플릿 사양.
tags: [system, template, event, schema]
keywords: [이벤트, 템플릿, 필터링, 조사, 판정, DC]
depends_on: [SYS_Manifest, TMPL_EVT_Notification, TMPL_EVT_Interactive]
last_updated: 2026-05-12
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
  - location:        # 어디서
      values: [Loc_거실, Loc_복도, Loc_지하실, Loc_창고, Loc_부엌]
  - sensory_axis:    # 어느 감각으로
      values: [시각, 청각, 후각, 촉각]
  - intensity:       # 얼마나
      values: [희미한, 분명한, 견딜 수 없는]
  - anomaly_type:    # 무엇이 어긋났는가
      values: [대칭의 어긋남, 시간의 반복, 사물의 위치, 그림자]
```

→ 이 한 패밀리에서 5 × 4 × 3 × 4 = **240개의 조합**. 그중 *적절한 조합* 만 추려도 50~80개 이벤트가 나옵니다. 디렉터가 "오늘 청각·지하실·견딜 수 없는·시간 반복 조합 만들어줘" 한 줄이면 컨베이어 벨트가 작동합니다.

### 1-4. 패밀리 분포 메트릭

PM 세션이 매주 점검:
```
F1 Resource:    ████████░░ 23개 / 50 목표  (46%)
F2 Atmosphere:  ██████████ 51개 / 50 목표  (102%) ⚠ 과잉
F3 Internal:    ████░░░░░░ 18개 / 50 목표  (36%) ← 우선
F4 Encounter:   ██████░░░░ 28개 / 30 목표  (93%)
F5 Cosmic:      ███░░░░░░░ 7개  / 20 목표  (35%) ← 우선
```

→ 다음 주 작업의 우선순위가 *자동으로 결정됩니다*.

---

## 2. 해법 ② — Trigger DSL (맥락 필터링)

### 2-1. 현재 트리거 시스템의 빈약함
지금까지 트리거는 *"이 조건이 충족되면 발생"* 의 단순 매칭이었습니다. 문제는:
- *"이 조건이면 발생하지 *말아야* 함"* 이 표현 불가
- *"이것 *또는* 저것이면 발생"* 이 표현 불가
- 수치 범위 (`5 ≤ X ≤ 10`) 가 표현 불가

식량 배급 이벤트가 풍족할 때 터지는 이유가 바로 이것 — 트리거가 *식량 부족* 을 positive 조건으로 검사하지 못함.

### 2-2. 트리거 DSL 도입

JSON 술어 트리(predicate tree)로 표현합니다. MongoDB 쿼리 문법과 비슷한 형태.

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

위 트리거가 의미하는 것:
- 아침 페이즈에
- Day 5 이상이고
- (식량이 5 미만 *또는* 누군가의 스트레스가 7 이상)
- *식량 풍부 플래그가 없고*
- *리더가 낙천적 기벽이 없을 때*

→ **negative 조건과 numeric 범위가 표현 가능해짐.** 식량 풍부 시 식량 부족 이벤트가 *기계적으로* 차단됩니다.

### 2-3. DSL 문법 명세

**논리 연산자 (재귀 가능)**:
- `all: [...]` — AND (전부 참)
- `any: [...]` — OR (하나라도 참)
- `not: {...}` — NOT (부정)

**리프 술어 (실제 검사)**:
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

**비교 연산자**: `eq`, `neq`, `lt`, `lte`, `gt`, `gte`, `in`

**와일드카드**: `"actor": "*"` 는 "아무 생존자라도" 의 의미. 한 명이라도 만족하면 참.

### 2-4. 평가 엔진 (Python 의사코드)

```python
def evaluate(predicate, state):
    if "all" in predicate:
        return all(evaluate(p, state) for p in predicate["all"])
    if "any" in predicate:
        return any(evaluate(p, state) for p in predicate["any"])
    if "not" in predicate:
        return not evaluate(predicate["not"], state)
    # 리프 술어로 위임
    return evaluate_leaf(predicate, state)
```

전체 엔진은 약 80~120 줄. 매 페이즈 시작 시 모든 이벤트의 트리거를 평가하여 *발현 후보 풀* 을 만들고, 가중치 기반 추첨.

### 2-5. AI 가 이 DSL 을 쓸 때의 지침

컨베이어 벨트 Step 3 (뼈대 설계) 에 다음을 추가:
> *"이 이벤트가 부적절한 맥락에서 터지면 어떤 모습인가?" 를 먼저 생각하고, 그 맥락을 `not` 으로 명시한다.*

예: 식량 부족 이벤트를 만들 때, *"식량 풍부할 때 터지면 이상하다"* → `{"not": {"resource": {"food": {"gte": 10}}}}` 를 자동 부착.

---

## 3. 해법 ③ — 한국어 조사 슬롯 시스템

### 3-1. 문제 재정의
변수 치환된 이름이 *받침 유무에 따라* 조사가 달라집니다:

| 받침 있음 (가빈) | 받침 없음 (레이첼) |
|---|---|
| 가빈**이** 들어왔다 | 레이첼**이**~~가~~ 들어왔다 |
| 가빈**을** 보았다 | 레이첼**을**~~를~~ 보았다 |
| 가빈**과** 함께 | 레이첼**과**~~와~~ 함께 |

템플릿 차원에서 *둘 다* 자연스럽게 작동해야 합니다.

### 3-2. 조사 슬롯 문법

이벤트 본문에 다음 형식으로 적습니다:

```
{actor}{이/가} 회계 장부를 들었다.
{target}{을/를} 노려보았다.
{actor}{은/는} 침묵했다.
{actor}{와/과} 함께였다.
{actor}{으로/로} 향했다.
```

→ 엔진이 `{변수}{A/B}` 패턴을 감지하면, 직전 변수의 마지막 글자 받침 유무에 따라 A 또는 B 를 선택.

### 3-3. 지원되는 조사 쌍

| 슬롯 | 받침 있음 | 받침 없음 | 용도 |
|---|---|---|---|
| `{이/가}` | 이 | 가 | 주격 |
| `{을/를}` | 을 | 를 | 목적격 |
| `{은/는}` | 은 | 는 | 주제 |
| `{와/과}` | 과 | 와 | 동반 (받침 있음 → **과**, 직관과 반대) |
| `{으로/로}` | 으로 | 로 | 방향/수단 (**ㄹ 받침은 예외**: 서울로, 레이첼로) |
| `{아/야}` | 아 | 야 | 호격 |
| `{이여/여}` | 이여 | 여 | 문어체 호격 |

→ **두 가지 특수 규칙** (엔진이 자동 처리, 작가가 외울 필요 없음):
1. **`{와/과}`** 는 받침 있을 때 *과*, 없을 때 *와* — 직관과 반대.
2. **`{으로/로}`** 는 받침 없거나 받침이 ㄹ 일 때 *로*, 그 외에는 *으로*.
   - `서울` (ㄹ 받침) → 서울**로** ✅
   - `부산` (ㄴ 받침) → 부산**으로** ✅
   - `레이첼` (ㄹ 받침) → 레이첼**로** ✅
   - `가빈` (ㄴ 받침) → 가빈**으로** ✅

### 3-4. 구현 함수 (Python)

```python
def has_jongseong(ch: str) -> bool:
    """한 글자가 받침을 가지는지 판정."""
    if not ch:
        return False
    code = ord(ch[-1]) - 0xAC00
    if 0 <= code <= 11171:
        return (code % 28) != 0
    return False  # 한글이 아니면 false 처리

PARTICLE_MAP = {
    ("이", "가"):   ("이", "가"),
    ("을", "를"):   ("을", "를"),
    ("은", "는"):   ("은", "는"),
    ("와", "과"):   ("과", "와"),   # 주의: 받침 있을 때 '과'
    ("으로", "로"): ("으로", "로"),
    ("아", "야"):   ("아", "야"),
    ("이여", "여"): ("이여", "여"),
}

def resolve_particles(text: str, variables: dict) -> str:
    import re
    # 변수 치환
    for k, v in variables.items():
        text = text.replace(f"{{{k}}}", v)
    # 조사 슬롯 처리: {A/B} 패턴
    def pick(match):
        a, b = match.group(1), match.group(2)
        # 직전 문자의 받침 유무로 결정
        idx = match.start()
        if idx == 0:
            return b
        prev_ch = text[idx - 1]
        if (a, b) in PARTICLE_MAP:
            has = has_jongseong(prev_ch)
            return PARTICLE_MAP[(a, b)][0 if has else 1]
        return a  # fallback
    return re.sub(r"\{([^/{}]+)/([^/{}]+)\}", pick, text)
```

→ 약 30줄. 게임 엔진에 한 번만 구현하면 모든 이벤트가 자동 처리.

### 3-5. 템플릿 작가 (AI) 를 위한 지침

컨베이어 벨트 Step 4 (지침 점검) 에 다음 추가:
> *모든 변수 뒤에 *반드시* 조사 슬롯을 사용한다. `{actor}이`, `{actor}는` 같은 직접 표기 ❌.*

예시:
```
❌ {actor}이 도착했다.
❌ {actor}는 침묵했다.
⭕ {actor}{이/가} 도착했다.
⭕ {actor}{은/는} 침묵했다.
```

이 규칙은 자동 린트로 잡을 수 있습니다 (Gate A 의 새 검사 항목).

---

## 4. 해법 ④ — Resolution Mode (판정 구조)

### 4-1. 현재 구조의 한계
Track A (통보형) 는 *결과 사전 확정*. Track B (개입형) 는 *플레이어 선택*. 그 사이가 비어 있습니다.

> 캐릭터의 스탯이 결과에 영향을 미치지만, 플레이어는 선택의 여지가 없는 이벤트

이 영역이 필요합니다. 가빈을 폐가에 보냈는데, 가빈의 지능이 *판정*되어 무엇을 발견하는지가 결정되는 식.

### 4-2. Resolution Mode 도입

기존 Track 위에 *해결 방식* 을 명시하는 필드를 얹습니다.

```yaml
resolution:
  mode: deterministic | stat_check | choice
```

세 가지 모드:

| 모드 | 의미 | 사용 처 |
|---|---|---|
| `deterministic` | 결과 고정 | 분위기 누설, 환경 이벤트, 통보 |
| `stat_check` | 캐릭터 스탯 판정으로 분기 | 자동 해결되지만 결과 가변 |
| `choice` | 플레이어 선택 | Track B 의 본질 |

### 4-3. 트랙과 모드의 매트릭스

| Track | 허용 모드 | 비중 (권장) |
|---|---|---|
| A | `deterministic`, `stat_check` | 70% / 30% |
| B | `choice` (선택 내부에 `stat_check` 중첩 가능) | 100% |

→ Track A 의 30% 가 stat_check 모드로 만들어지면, 캐릭터 스탯이 *생존자별로 다른 결과* 를 만들어내는 영역이 생깁니다.

### 4-4. stat_check 모드의 스키마

```json
{
  "id": "EVT_A042_xyz",
  "track": "A",
  "family": "F4_Encounter",
  "trigger": { ... },
  "narrative": {
    "setup": "{actor}{이/가} 폐가의 회계실로 들어섰다. 책상 위에 낯선 장부가 놓여 있었다."
  },
  "resolution": {
    "mode": "stat_check",
    "check": {
      "actor": "{assigned_actor}",
      "stat": "지능",
      "dc": 12,
      "modifiers": [
        { "if": { "trait": { "actor": "{assigned_actor}", "trait": "통제강박" } },
          "bonus": 2 },
        { "if": { "stat": { "actor": "{assigned_actor}", "stress": { "gte": 7 } } },
          "penalty": 3 }
      ]
    },
    "on_success": {
      "narrative": "그러나 {actor}{은/는} 장부의 결산이 *틀려 있음* 을 알아차렸다. 누군가가 의도적으로 한 줄을 옮겨 적은 흔적이다.",
      "effects": {
        "stat_delta": { "{actor}.정신": -1, "{actor}.스트레스": +1 },
        "flags_emit": ["Flag_Memory_Ledger_Forged"]
      }
    },
    "on_fail": {
      "narrative": "{actor}{은/는} 숫자들을 한참 들여다본 뒤 책상을 떠났다. 무엇인가 어긋났다는 느낌만 남았다.",
      "effects": {
        "stat_delta": { "{actor}.스트레스": +1 },
        "flags_emit": ["Flag_Memory_Ledger_Missed"]
      }
    }
  }
}
```

→ *결과는 캐릭터에 따라 다르고*, *플레이어는 선택하지 않으며*, *둘 다 셜리 잭슨 톤을 유지함* (성공해도 안도가 아닌 *서늘한 확인*).

### 4-5. 변동 요소 (Modifier) 시스템

`modifiers` 는 캐릭터의 상태에 따라 DC 를 가감합니다:
- 기벽 보유 시 보너스/페널티
- 스트레스 임계점 초과 시 페널티
- 특정 플래그 보유 시 보너스

→ 같은 이벤트라도 *누가 보내졌는지* 와 *그 시점 상태* 에 따라 결과 확률이 달라집니다. 이게 다운폴의 *"리더의 명령이 비용을 만든다"* 를 시스템적으로 강화합니다.

### 4-6. on_success / on_fail 의 본문 작성 원칙

셜리 잭슨 톤을 유지하기 위해:
- **on_success 도 *완전한 해결* 이 아니어야 함** — 안도는 *오만한 확신* 으로, 발견은 *더 큰 불확실성* 으로
- **on_fail 도 *명확한 패배* 가 아니어야 함** — 실패는 *놓친 것* 으로, 잃은 것은 *모호한 무언가* 로
- 본문은 1~2문장으로 짧게, *주관적 감각* 으로 마무리

---

## 5. 통합 — v2 템플릿의 최종 모습

```yaml
# Track A v2 (Resolution Mode 포함)

id: EVT_A{nnn}_{hash}
title: (한국어 제목)
track: A
family: F1_Resource | F2_Atmosphere | F3_Internal | F4_Encounter | F5_Cosmic
status: complete

trigger:
  # Trigger DSL (재귀 술어 트리)
  all:
    - phase: "..."
    - any:
      - resource: { food: { lt: 5 } }
      - ...
    - not:
      - flag: "Flag_..."

slots:
  # 패밀리별 파라메트릭 슬롯 (선택)
  location: Loc_지하실
  sensory_axis: 청각
  intensity: 견딜 수 없는

narrative:
  setup: |
    (시네마틱 8단계 도입부, {actor} 등 변수 사용, 조사 슬롯 {이/가} 포함)
  
resolution:
  mode: deterministic | stat_check   # Track A 는 둘 중 하나
  
  # deterministic 일 때만:
  effects:
    stat_delta: { ... }
    flags_emit: [ ... ]
  
  # stat_check 일 때만:
  check:
    actor: "{assigned_actor}"
    stat: "지능"
    dc: 12
    modifiers: [ ... ]
  on_success:
    narrative: "..."
    effects: { ... }
  on_fail:
    narrative: "..."
    effects: { ... }

emits:
  # 이 이벤트가 발행 *가능* 한 모든 플래그 (Gate C 무결성 검사용)
  - Flag_Memory_X
  - Flag_Memory_Y

shirley_jackson_axes:
  # 4지침 중 *주력* 으로 발현되는 축 명시 (자가 점검용)
  primary: 공간의_악의
  secondary: 일상의_배신
```

---

## 6. 컨베이어 벨트 v2.2 변경 사항

이 사양을 반영하기 위해 `EVT_Conveyor_Belt_Master_Prompt.md` 를 다음과 같이 갱신:

### Step 2 (브레인스토밍) 갱신
키워드 제안 시 **반드시 패밀리(F1~F5)를 명시**. 다음 형식:
```
패밀리: F2_Atmosphere
슬롯 후보:
  - location: Loc_지하실
  - sensory_axis: 청각
  - anomaly_type: 시간의 반복
```

### Step 3 (뼈대 설계) 갱신
다음 5가지를 *반드시* 명시:
1. 트리거 DSL (positive + negative + numeric)
2. Resolution mode (Track A 는 deterministic / stat_check 중 택일)
3. stat_check 일 경우 DC 와 modifier
4. on_success / on_fail 의 효과 차이
5. 발행 가능한 모든 `Flag_Memory_*` (emits 필드)

### Step 4 (지침 점검) 신규 항목
- [ ] 모든 변수에 조사 슬롯 부착했는가 (`{actor}이` 같은 직접 표기 없음)
- [ ] 트리거에 *부적절한 맥락 차단* 의 `not` 조건이 포함되었는가
- [ ] stat_check 모드라면 on_success 도 *완전한 해결* 이 아닌가 (오만한 확신·서늘한 확인)
- [ ] 패밀리 분류가 자료로 명시되었는가

---

## 7. Gate A 자동 린트 확장

이 사양에 맞춰 새 린트 추가:

| 린트 | 검사 내용 |
|---|---|
| `lint_particle_slot` | 변수 뒤에 조사 슬롯 없는 직접 표기 검출 (예: `{actor}이`) |
| `lint_trigger_negation` | 트리거가 `all` 만 있고 `not` 이 없으면 경고 (필수는 아님) |
| `lint_resolution_mode` | Track A 인데 mode 필드 누락 시 에러 |
| `lint_check_modifier` | stat_check 인데 modifiers 가 빈 배열이면 경고 |
| `lint_family_required` | family 필드 누락 시 에러 |
| `lint_emits_completeness` | narrative 에 등장하는 모든 `Flag_*` 가 `emits` 에 등재되어 있는지 |

---

## 8. 도입 로드맵

| 주차 | 작업 | 비고 |
|---|---|---|
| 1주 | 본 사양 디렉터 검토 + 합의 | |
| 2주 | `EVT_Notification.md` / `EVT_Interactive.md` 의 v2 양식 갱신 | Phase 1 의 일부 |
| 2주 | 컨베이어 벨트 v2.2 프롬프트 갱신 | |
| 3주 | 조사 슬롯 처리 함수 + 트리거 DSL 엔진 구현 | 약 200줄 |
| 3주 | Gate A 새 린트 6종 구현 | |
| 4주 | 파일럿 이벤트 10개 v2 양식으로 양산 + 검수 | Phase 6 의 첫 사이클 |
| 5주+ | 본격 양산 (패밀리 분포 추적하면서) | Phase 7 |

---

## 9. 한 줄 요약

> **범용 이벤트의 4대 문제는 모두 *스키마 표현력 부족* 이라는 한 뿌리에서 나온다.**
> **패밀리 분류(다양화) + 트리거 DSL(필터링) + 조사 슬롯(언어) + Resolution Mode(판정) 의 4가지 확장을 한 번에 도입하면, 같은 비용으로 *질·양·정합성* 이 동시에 올라간다.**

각 확장은 *독립적으로 도입 가능* 하지만, 함께 도입할 때 시너지가 가장 큽니다. 4주 안에 v2 로 전환 가능합니다.
