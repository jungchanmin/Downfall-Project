---
id: MONSTER_DB
title: "핵심 시스템 사양서 — 괴물 데이터베이스"
type: mechanic
status: wip
version: 0.2.1
summary: >
  다운폴 괴물 DB. 위협 축(일반·네임드)×형태 축(인간형+비인간형 7) 2축 분류. 일반형은
  원형 8종 + 파라미터로 양산(swarm 규모×개체체력), 네임드는 개별 상세. 세력 회피 훅,
  보상 책정기 연계, r18_module/r18_weakness 필드. 첫 네임드 2종(거대이빨악어·잔혹한 살점포식자) 등재.
tags:
  - mechanic
  - monster
  - database
  - taxonomy
  - entity
keywords:
  - 괴물, 일반형, 네임드, 멸망, 원형, 파라미터, swarm, 규모, 적대적 생존자,
    인간형, 비인간형, 거대이빨악어, 살점포식자, r18 module
depends_on:
  - SYS_Manifest
  - MECH_NPC_Stats_System
  - MECH_Resource_System
  - MECH_Combat_System
  - MECH_Event_Reward_Appraisal
last_updated: 2026-06-05
---

# 👹 DOWNFALL 괴물 데이터베이스 (v0.2)

> 구조: 분류 2축 → 일반형 원형(8종)+파라미터 → swarm 규칙 → 네임드 상세 → R18 필드.

---

## SECTION 0 — 분류 2축 (직교)

### 0-1. 위협/지속성 축 (지도에 남는가)
| 등급 | 정의 |
|---|---|
| **일반괴물** | 일시 생성(탐색·세력교류·이벤트·지역특성). 즉시 전투. 도주·격퇴 시 소멸. 동종 다수 등장 기본. |
| **네임드괴물** | 매일 새벽 출현, 지역 상주, 처치까지 영향. 등장 시 즉시 전투 아님(SECTION 6, Combat). 다수 등장 드묾. |

네임드 하위: **표준형 / 돌연변이형 / 멸망의 괴물**.

### 0-2. 형태 축 (일반·네임드 공용)
인간형(적대적 생존자) + 비인간형 7: ①동물형 ②곤충형 ③심령체형 ④유사인간형 ⑤이상현상형 ⑥이계급괴이형 ⑦촉수·괴물형.

### 0-3. 식별자
`#Monster_{형태}_{이름}` (신규 태그 카테고리 — 승인 완료).

---

## SECTION 1 — 일반형 원형 (8종 + 파라미터)

> 일반형 규약: **약기술 2~3개**, **강기술은 대체로 없음**(절대 아님 — 형태·맥락상 필요 시
> *조건부 슬롯* 허용. 예: 인간형의 구속 조건부 준-강기술), **무기 타입 효과 없음**,
> 부여 상태이상은 **중앙 상태이상 표에서 차용**(신규 생성 금지), 개체별로 **체력·대사만 오버라이드**.
> 다수 등장은 swarm(SECTION 2)으로 처리.

### 원형 정의표

| 원형 ID | 형태축 | 기본 약기술(2~3) | 차용 상태이상 | swarm 경향 | 특이 훅 |
|---|---|---|---|---|---|
| `ARCH_Human_Armed` | 인간형 실체 | 협공 / 위협 / 날붙이질 | 고통·속박 | 다수, 개체 체력 2~3 | 세력 회피 훅 |
| `ARCH_Human_Anomaly` | 인간형 이상현상 | 익숙한 목소리 / 거짓 구조요청 / 표정 붕괴 | 공포·혼란 | 합창형 다수 | 일상의 배신 톤 |
| `ARCH_Beast_Pack` | 동물·곤충형 | 무리 포위 / 물어뜯기 | 고통·속박 | 다수, 개체 체력 1 | 떼 단위 |
| `ARCH_Undead_Horde` | 유사인간형 | 떼지어 물기 / 붙잡기 | 속박·고통 | 대규모 다수 | 느림·집요 |
| `ARCH_Spectre` | 심령체형 | 스며들기 / 속삭임 | 공포·움츠러듬 | 소수 | 물리 약·정신 압박 |
| `ARCH_Phenomenon` | 이상현상형 | 휘감기 / 끌어당기기 | 속박 | 단일~소수 | 사물 의인화 |
| `ARCH_Insect_Mimic` | 곤충형(참신) | 잘못된 목소리 / 군집 쇄도 | 혼란·공포 | 군집 다수 | 청각 교란 |
| `ARCH_Tendril_Fragment` | 촉수·괴물형 | 후려치기 / 감기 | 속박 | 소수 | 이계급 말단(본체 미등장)·R18 후보 |

### 개체 오버라이드 스키마
```yaml
CommonMonster:
  id: "#Monster_{형태}_{이름}"
  archetype: ARCH_*          # 원형 참조 (약기술·상태이상 상속)
  unit_hp: int               # 개체 체력 (들개 1 / 자경단원 3 등)
  default_size: int          # 기본 등장 규모
  dialogue_override: {...}   # 1~2줄만 (나머지는 원형 공용 풀)
  faction: str | null        # 인간형 한정, 세력 회피 훅 연결
```

### 인간형 세력 회피 훅
```
세력 영향 구역 → 해당 세력 소속 적대 생존자 등장↑.
faction 태그 보유 시 전투 대신 [세력호감도] 소비/판정으로 회피·해결 가능.
DB는 전투 스탯만 저장. 세력 소속은 faction 태그로 FACTION_DB(미작성) 연결.
```

---

## SECTION 2 — Swarm (다수전)

```
swarm 유닛 = 규모 N × 개체 체력 H
공격 피해 → 맨 앞 개체 H 차감, 0 시 규모 −1. 규모 0 → 소멸.
규모 = 위협(공격력·피격·표적 수) 비례. 광역기 규모 −2~3, 단일기 −1.
개방 게이지: swarm 유닛엔 없음(약공 필중 피해로 직접). 분리 개체만 개방 적용.
분리 승격: 우두머리·특수 개체 → 별도 개체 유닛(개방·상태이상 개별).
```
> 상세 규칙: `MECH_Combat_System` SECTION 9.

---

## SECTION 2-B — 원형 상세: `ARCH_Human_Armed` (인간형 실체)

> 인간형 실체는 지능이 있어 **구속 후 약탈·유린** 행동이 자연스럽다.
> 따라서 일반형이지만 *구속 조건부 준-강기술* 슬롯을 예외로 가진다(규약 완화 적용).

### 2-B-1. 조건 게이트 (2종)
```
게이트 A — 무기 보유: [휘두르기]는 무장 시만. 무장 해제되면 잠김.
게이트 B — 대상 구속: 대상이 [속박]이면 그 대상에게 준-강기술(장비 약탈·강제 R18) 해금.
           일반형이라 전조 없이 즉발, 위력은 낮은 버전.
```

### 2-B-2. 무장 해제 (2경로)
```
① NPC 고유기술 "무기 떨어트리기" (판정: 기술) — 적중 시 무장 해제 확정.
② 기존 커맨드 부수효과 (확률):
   - 강공 적중 시 20~30% 무기 탈락 (강타가 손을 침)
   - 위압/교섭(대화) 성공 시 20~30% 위축되어 무기를 놓침
무장 해제 = 인간형 실체 공략의 핵심 약점(무기 약점이 없는 일반형의 대체 약점).
```
> `MECH_Combat_System` SECTION 6-B 동기화.

---

## SECTION 2-C — 일반형 개체 ① 약탈자

```yaml
id: "#Monster_Humanoid_Looter"
name: 약탈자
threat: 일반
archetype: ARCH_Human_Armed
morphology: 인간형
unit_hp: 2                      # swarm 개체 체력
default_size: 3                 # 기본 규모 (다수 등장)
weapon: 둔기 | 칼               # 개체별 랜덤. 무기 타입 효과 없음(일반형)
faction: null | 가변            # 세력 영향 구역이면 소속 부여 → 세력 회피 훅

skills_basic:
  - 휘두르기: [게이트 A — 무장 시만] 근접 단일/소광역 피해. 무장 해제 시 잠김.
  - 외치기: swarm 규모 +1(동료 호출) 또는 일대 [움츠러듬].
  - 붙잡기: 대상 [속박] 시도. 회피 판정 실패 시 구속 → 게이트 B 개방.

conditional_signature:          # [게이트 B — 대상 속박 시만] 준-강기술, 전조 없음
  - 장비 약탈: 구속 대상 장비 1개 탈취. (SFW에서도 유효)

r18_module:                     # 토글 OFF면 무시
  arousal_attacks_unbound:      # 미구속 대상 대상
    - 음담패설: 흥분 게이지↑ (정신 간섭, 약)
    - 더듬기: 성감↑ + 의복 게이지 소량
    - 옷찢기: 의복 게이지 대량 (노출 → 성감 배율 증폭)
  arousal_attacks_bound:        # [게이트 B] 구속 대상 대상 — 준-강기술
    - 강제 펠라치오: 성감 대량 + 기록 Log_R18_입_괴롭혀짐 +1
  pin_condition: 붙잡기 적중 → 대상 [속박]
  r18_status_pool: [속박, 흥분]
  r18_weakness: [유혹 미끼]      # 표적 고정에 약함

flee_lock: { stats: [대화(위압·교섭), 매력], required: 3, note: 인간형이라 세력호감도/위압으로 해산 가능 }

dialogue_override:
  on_encounter: ["가진 거 다 내놔. 곱게 말할 때."]
  on_telegraph: ["놈이 거리를 좁히며 손을 뻗었다."]
  on_defeat: ["약탈자가 무기를 떨군 채 뒤로 쓰러졌다."]
survivor_reads:
  weakness: ["무기만 떨궈내면 별거 아냐. 손을 노려."]
  danger: ["붙잡히면 위험해 — 잡히기 전에 떼어내."]
```

> **공략 요약**: 붙잡기를 회피/방어로 막아 구속 회피 → 게이트 B 봉쇄 / 무장 해제로 휘두르기 봉쇄 /
> 구속된 아군은 선공 구출. swarm 다수면 "한 명이 붙잡고 다른 개체가 약탈·R18" 협공 성립.

---

## SECTION 3 — 네임드 상세 ① 거대이빨악어

```yaml
id: "#Monster_Beast_GiantTooth_Croc"
name: 거대이빨악어
threat: 네임드 (일반형 아님)
morphology: 동물형
stats: { hp: 6, defense: 0, attack: 3, mental_attack: 0, speed: 2 }
weaknesses:
  weapon_vuln: [둔기]            # 피해 +1
  weapon_resist: [검류]          # 무효 아님 — 약점 정밀타로만
  weak_points: [눈, 비늘없는 복부]
  sense_dependency: [청각, 진동] # 차단 시 탐색 급감
  behavioral: 시력 나쁨·지능 낮음 → 시야 이탈 시 포기
skills_basic:                    # 약기술
  - 물기: 근접 단일 → [속박됨]. 근접 밀착 시 취약. 속박 중 타 약기술 불가.
  - 꼬리치기: 근접 광역 → [비틀거림]. 구조물/엄폐 있으면 피해↓·비틀거림 불가.
  - 경계하며 뒷걸음질: 1턴 눈치보기. 공격받으면 물기 연계 / 비공격 시 발톱치기 연계. 함정 파악.
  - 달려들어 발톱치기: 근접 → [고통].
  - 사냥감 추적: 도주 시 1회. 물기 확정 적중.
skills_signature:                # 강기술
  - 데스롤 [전조형]: 속박 보유 시만. 장비 전부 떨굼 + [심각한 고통] + 고정 피해.
  - 강하게 물기 [전조형]: 2턴 준비. 엄폐 안 한 표적 돌진 물기 → [속박]+[고통]. 전조가 '경계하며 뒷걸음질'과 유사(마인드게임).
flee_lock: { stats: [제작(소음·진동 차단), 탐색(시야 이탈)], required: 4 }
dialogue_template:
  on_encounter: ["진흙 사이로 붉은 눈이 떠올랐다."]
  on_telegraph: ["거대한 턱이 크게 벌어지며 준비 자세에 들어갔다."]
  on_defeat: ["거대한 머리가 진흙 속으로 무겁게 꺾였다."]
survivor_reads:
  weakness: ["저 비늘, 칼은 안 박혀. 둔기로 부숴야 해."]
  danger: ["물리면 끝장이야. 데스롤로 뜯어낼 거라고."]
r18_module: null                 # (미적용)
```

---

## SECTION 4 — 네임드 상세 ② 잔혹한 살점포식자

```yaml
id: "#Monster_Tendril_FleshEater"
name: 잔혹한 살점포식자
threat: 네임드 (멸망의 괴물)
morphology: 촉수·괴물형
stats: { hp: 8, defense: 1, attack: 2, mental_attack: 2, speed: 2 }
weaknesses:
  behavioral: 은밀 이동·추적형. 식사로 재생 → 시체 소각/먹이 차단으로 재생 봉쇄.
  control: 화력 집중 필요 (시간 끌수록 강해짐)
skills_basic:
  - 할퀴며 피핥기: 적중 시 체력 3 회복.
  - 은밀한 잠복자: 3턴 [은신](매턴 체력 +2). 탐색 4 판정으로 해제.
  - 공포스러운 외침: 일대 전원 [움츠러듬]+[공포].
  - 잔혹한 처형식: 기벽 3+ 또는 체력 임계 시 사망. 아니면 기벽 +1 + [기절].
  - 공중덮치기: 원거리 표적 돌입. 2배 피해 + [속박됨].
skills_signature:                # 전부 [패시브형]
  - 은밀한 움직임 [패시브]: 지도 미표시. 최다 방문/전일 방문 지역으로 거리 무시 이동.
  - 살점포식자 [패시브]: 전투 종료 시 타 희생양 포식 → 체력 전회복. 추격당하면 불가. 지역 체류 시 최대 3회 재전투.
  - 사냥본능 [패시브]: 매턴 속도 +1. 속도 5+ 시 속도 대신 매턴 피해량만큼 회복(정신 피해 제외).
flee_lock: { stats: [제작(이동수단 봉쇄)], required: 5, note: 추격 패시브로 도주 불완전 — 봉쇄/소각 강제 }
dialogue_template:
  on_encounter: ["살점 사이로 수백 개의 이빨이 소리 없이 드러났다."]
  on_telegraph: ["턱이 벌어지며 처형의 자세를 잡았다."]
  on_defeat: ["연체동물 같은 몸이 마침내 늘어졌다."]
survivor_reads:
  weakness: ["저거 먹으면서 회복해. 시체를 태워서 못 먹게 막아."]
  danger: ["기벽 많이 쌓인 사람부터 노려. 물리면 통째로 뜯겨."]
  morale_low: ["...저런 걸 어떻게 이겨."]
r18_module:                      # 멸망급 R18 후보 (촉수형) — 콘텐츠 [미정], 훅만
  clothing_attacks: [미정]
  arousal_attacks: [미정]
  pin_condition: 다중 촉수 [속박] 2회 누적
  r18_status_pool: [속박, 흥분, 황홀]
  r18_weakness: [미정]
```

---

## SECTION 5 — 보상 책정기 연계

```
패널티 강도 → 일반(낮음, 즉시 전투) / 네임드(높음, 등장만) 스폰 분기.
일반: 즉시 전투, 도주·격퇴 시 종료.  네임드: 등장(지도 상주 추가), 즉시 전투 아님.
격파 트랙 → 전리품 + 제물 진척. (MECH_Event_Reward_Appraisal SECTION 8 훅)
```

---

## SECTION 6 — 미작성 의존성 (훅)

```
FACTION_DB.md       : 세력 목록·호감도 변동표. faction 태그로 연결. (미작성)
MECH_Day_Type_System: 고요/전조/멸망의 날 → 네임드 출현 풀. Time_System 편입 예정. (보류)
R18 콘텐츠          : 살점포식자 등 r18_module 세부. MECH_Combat_System SECTION 11 + MECH_R18_Memory_Log 연동. (미정)
```

---

## SECTION 7 — 버전 관리

- **문서 위치**: `03_Entities/Monsters/MONSTER_DB.md`
- **커밋 메시지**: `feat(entity): monster archetypes + swarm + named details (croc, flesh-eater) + r18 fields`
- **Wiki_Index.md 갱신 필요 여부**: **필요 (YES)**

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v0.1.0 | 2026-06-02 | 2축 분류·훅. |
| v0.2.0 | 2026-06-05 | **일반형 원형 8종 + 파라미터 / swarm(규모×개체체력·분리승격) / 네임드 상세 2종(거대이빨악어·잔혹한 살점포식자) / r18_module·r18_weakness 필드 / 세력 회피 훅 구체화.** |
| v0.2.1 | 2026-06-05 | 일반형 강기술 규약 완화(절대→대체로, 조건부 슬롯 허용). `ARCH_Human_Armed` 상세(2게이트·무장 해제 2경로). 일반형 개체 ① **약탈자** 등재(구속 게이트 R18 포함). |

**갱신 기준**: 개체 다수 등재 후 status `complete`. FACTION_DB·Day_Type·R18 콘텐츠 작성 시 연동.
