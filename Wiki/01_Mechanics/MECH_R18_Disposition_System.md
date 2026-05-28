---
id: MECH_R18_Disposition_System
title: 핵심 시스템 사양서 — R18 성향 5대 축 및 신체 오염 시스템
type: mechanic
status: complete
version: 1.0.0
summary: >
  생존자들의 심리적·성적 타락 단계를 추적하는 5대 성향 주축(Disposition Axes), 
  국소 부위별 성감 개발도(Anatomical Sensitivity), 육체 오염 및 도구 경험 기록 테이블의 
  데이터 아키텍처와 JRPG/미연시식 동적 트리거(Trigger DSL) 연동 규격을 정의한 마스터 문서.
tags: [mechanic, system, r18, core, framework]
last_updated: 2026-05-28
---

# 📊 DOWNFALL R18 핵심 메커닉: 성향 5대 축 및 신체 오염 시스템 (v1.0)

## 01. 아키텍처 개요 (Architecture Overview)

본 시스템은 '오뱅마을'이라는 악의적 공간과 리더(플레이어)의 가학적·지배적 행위가 생존자들의 신경계와 육체를 어떻게 단계적으로 파괴하고 영구 개조하는지 추적하는 백엔드 데이터 모델이다. 

- **정적 데이터(Blueprint)**: 본 문서 및 각 생존자 로어바이블(`LORE_CHAR_*`)에 초기 스탯셋으로 매립된다.
- **동적 데이터(Live State)**: 플레이어의 런타임 세이브 파일(`*_Live_Status.json`)에 컴포넌트 형태로 격리 수납되어 실시간 가감산 및 버전 관리가 이루어진다.

---

## 02. 성향 5대 주축 (The 5 Disposition Axes)

캐릭터의 심리적 성향과 성적 취향의 극단화를 추적하는 5대 핵심 지표다. 모든 지표는 `0`에서 `100` 사이의 정수(Integer) 값을 가진다.

```json
{
  "disposition_axes": {
    "dominance": 0,
    "submission": 0,
    "pleasure": 0,
    "benevolence": 0,
    "affection": 0
  }
}

```

### 1) 우월 (Dominance)

* **개념**: 고압 / 프라이드 / 가학증(새디즘) / 지배 통제권
* **작동**: 수치가 높을수록 타인을 신체적·언어적으로 제어하려 들며, 가학적 행위 및 상대의 패복에서 성적 카타르시스를 느낀다. 일반 대사 상태에서 가장 높은 권위를 유지하려는 속성이다.

### 2) 복종 (Submission)

* **개념**: 순종 / 수긍 / 피학증(마조키즘) / 종속 강박
* **작동**: 수치가 높을수록 지배당함과 학대에서 정신적 안도감을 느끼며, 굴욕적인 복종 명령에 대한 저항선(DC)이 무너진다. 극단에 달하면 명령이 없을 때 극심한 불안을 느낀다.

### 3) 쾌락 (Pleasure)

* **개념**: 욕정 / 발정 / 육체 오염 / 상시 음란
* **작동**: 수치가 높을수록 이성적 거부 반응이나 수치심보다 신체적 쾌락을 최우선시한다. 수치 임계점(50, 80) 돌파 시 일상 텍스트가 불수의적인 발정 상태 묘사로 강제 오버라이딩(Overriding)된다.

### 4) 호의 (Benevolence)

* **개념**: 친절 / 봉사 / 자기희생 / 헌신
* **작동**: 복종과 구별되는 스탯이다. 타인의 성적 만족과 해소를 위해 자기 자신을 기꺼이 '성적 도구'로 제공하는 것에 만족감을 느낀다. 가학을 수용하는 것이 아니라 봉사에 목적이 있다.

### 5) 애정 (Affection)

* **개념**: 사랑 / 연모 / 병적 집착 / 친밀도 연동
* **작동**: 대상(리더, 혹은 타인)에 대한 극단적인 독점욕이다. 이 수치가 높으면 미지의 공포나 극한의 위기 상황 속에서 대상의 품과 성적 결합만을 갈구하는 의존증이 발현된다.

---

## 03. 국소 부위별 성감 개발도 (Anatomical Sensitivity Profile)

인체를 6대 주요 구역으로 세분화하여 각 부위의 개발 단계(`Level 0 ~ 3`)와 누적 경험치(`EXP`)를 관리한다. 레벨이 상승할 때마다 캐릭터의 신체적 징후와 나레이션 렌더링에 영구 기벽(Trait)이 추가된다.

```yaml
body_development:
  sensitive_zones:
    mouth:    { level: 0, exp: 0, max_level: 3 } # 구강 및 설근
    breast:   { level: 0, exp: 0, max_level: 3 } # 가슴 및 유두
    clitoris: { level: 0, exp: 0, max_level: 3 } # 음핵 (외부 자극)
    vagina:   { level: 0, exp: 0, max_level: 3 } # 질 내벽 (내부 자극)
    anus:     { level: 0, exp: 0, max_level: 3 } # 항문 및 괄약근
    skin:     { level: 0, exp: 0, max_level: 3 } # 전신 피부 (구속/마찰)

```

### 🔓 부위별 레벨업 기벽(Trait) 풀 (Pool)

#### [구강 (Mouth)]

* **Lvl 1. 타액 과다분비**: 대사 출력 시 파찰음이 섞이거나 침을 삼키는 목줄기의 꿀렁임이 묘사됨.
* **Lvl 2. 미각 왜곡**: 가학적인 체액이나 오염 물질에서 뇌내 보상 메커니즘에 의해 단맛과 안도를 인지함.
* **Lvl 3. 구강 동화**: 언어적 소통 기능이 퇴화하고, 오직 리더를 받아들이고 핥는 성적 도구로 고착됨.

#### [가슴 (Breast)]

* **Lvl 1. 마찰 예민**: 헐렁한 옷자락이 유두에 스치는 물리적 마찰만으로도 호흡이 가빠짐.
* **Lvl 2. 자발적 노출 강박**: 리더 앞이나 특정 공간에서 상의를 가리는 행위 자체를 거부하거나 잊어버림.
* **Lvl 3. 유즙 분비 전조**: 신체 호르몬계가 리더의 사디즘에 완전 정렬되어 인공적 분비 전조 징후가 발현됨.

#### [비부 및 내벽 (Vagina)]

* **Lvl 1. 상시 윤활**: 공포나 긴장감을 느낄 때 뇌의 명령보다 비부의 애액 분출이 먼저 작동함.
* **Lvl 2. 불수의적 수축**: 리더의 가학적 목소리나 특정 최면 패턴 목격 시 자궁벽이 스스로 경련함.
* **Lvl 3. 인공 발정 완성**: 외부의 물리적 삽입이나 문지름이 없으면 정신 수용체가 붕괴하는 중독 상태.

---

## 04. 경험 및 도구 장착 기록 테이블 (The Ledger of Flesh)

플레이어가 게임 플레이 중 달성한 성적 업적과 누적 횟수를 추적하는 다차원 메트릭스(Metrics)다. 이 데이터는 업적 해금 및 특수 기벽 진화의 인덱스로 활용된다.

```yaml
flesh_ledger:
  positions:
    masturbation: 0       # 자위 행위 횟수
    oral_sex: 0           # 구강 성교 횟수
    missionary: 0         # 정상위 횟수
    cowgirl: 0            # 상위 횟수
    doggy_style: 0        # 후배위 횟수
    
  tools_and_toys:
    vibrator_used: 0      # 바이브레이터 자극 횟수
    ropes_bound: 0        # 로프 및 구속구 구속 경험 횟수
    anal_plug_hours: 0    # 아날 플러그 상시 장착 누적 시간 (Hour)
    
  records:
    total_orgasms: 0            # 총 절정/사정 횟수
    creampie_count: 0           # 질내 사정 수용 횟수
    public_exposure_count: 0    # 외부 및 공공장소(거실, 야외 등) 노출 횟수
    total_swallowed_semen_ml: 0 # 총 정액 흡수량 (ml)

```

---

## 05. JRPG / 미연시식 동적 트리거 연동 규격 (Trigger DSL)

이벤트 파일(`.md`) 생성 시, 본 시스템의 스탯을 파서(Parser)가 인식하여 선택지를 해금하거나 감추는 구체적인 문법 사양이다.

### 1) 프리컨디션 명시 (trigger_requirement)

특정 선택지가 활성화되기 위한 성향 축 및 부위 레벨 조건을 논리 연산자(`all`, `any`, `not`)와 비교 연산자(`gte`, `lte`, `eq`)로 결착한다.

```yaml
# 예시: 복종 수치와 구강 개발도가 일치할 때만 오픈되는 선택지 구조
choices:
  - id: ch_exclusive_oral_01
    label: "[복종 50 / 구강 2레벨] 구두 끝에 묻은 먼지를 혀로 핥아 청소한다."
    trigger_requirement:
      all:
        - stat: { actor: "Rachel", "disposition_axes.submission": { gte: 50 } }
        - stat: { actor: "Rachel", "body_development.sensitive_zones.mouth.level": { gte: 2 } }

```

### 2) 포스트 콘sequence 명시 (resolution.stat_delta)

선택지 결과나 확률 판정(`on_success`, `on_fail`) 종료 시, 수치 변동과 경험치 지급을 명확한 데이터 주소로 입력한다.

```yaml
    resolution:
      mode: auto_success
      stat_delta:
        "Rachel.disposition_axes.submission": +3
        "Rachel.disposition_axes.pleasure": +1
        "Rachel.body_development.sensitive_zones.mouth.exp": +25
        "Rachel.flesh_ledger.positions.oral_sex": +1

```

### 3) 런타임 플레이스홀더 변수 관리 (`local_variables`)

JRPG식 연속 탐색이나 루프형 대화 이벤트를 설계할 때, 해당 이벤트 세션 내부에서만 한시적으로 작동하는 흥분/조교 스택 변수를 생성하여 클라이맥스 R18 씬으로 강제 전환하는 구조를 지원한다.

```yaml
trigger_mechanism:
  type: "Iterative_Exploration"
  local_variables:
    session_excitation_stack: 0 # 세션 내 누적 흥분 스택
  climax_condition:
    - if: { "local.session_excitation_stack": { gte: 3 } }
      trigger_event: "EVT_B022_VaginalExplosion" # 스택 3 도달 시 클라이맥스 강제 기화

```
