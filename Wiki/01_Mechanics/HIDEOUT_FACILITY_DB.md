---
id: HIDEOUT_FACILITY_DB
title: 아지트 설비 후보 데이터베이스
type: database
status: wip
summary: 아지트 개조 분기를 완성하는 설치형 설비의 역할, 설치 적합성, 행동 해금, 파괴·수리와 R18 확장 경계를 정의한다.
tags: [hideout, facility, equipment, upgrade, database]
keywords: [아지트 설비, 설치 장비, 행동 해금, 방 개조, 수리, 파괴]
depends_on:
  - MECH_Hideout_System
  - HIDEOUT_ROOM_PROFILE
  - HIDEOUT_ACTION_PROFILE
  - MECH_Loot_Distribution
  - ITEM_System_Overview
emits:
  - ITEM_Equipment_DB
  - HIDEOUT_ACTION_PROFILE
last_updated: 2026-07-13
---

# 아지트 설비 후보 데이터베이스

## 1. 목적

이 문서는 아지트 방에 설치하는 설비 후보를 정리한다.

설비는 단순한 수치 상승물이 아니라 다음 중 하나 이상의 역할을 가진다.

- 자율행동 또는 전문 행동 해금
- 기존 행동의 위험·자원 소모·실패 부작용 완화
- 방 개조의 정체성 강화
- 아지트 사건·전투·외출 준비 선택지 추가
- 특정 기벽·오염·부상 대응

정확한 수치, 획득 확률, 부품 비용과 내구도는 테스트 단계에서 확정한다.

## 2. 공통 원칙

- 설비는 아지트 전용 설치물이며 일반 휴대 장비와 구분한다.
- 주 개조를 대체하지 않고 선택한 분기를 완성한다.
- 하나의 설비가 모든 방과 빌드의 필수품이 되지 않게 한다.
- 같은 기능에는 가능하면 여러 대체 설비 또는 스탯 경로를 둔다.
- 설비가 없어도 기본 행동은 가능하며, 설비는 전문 행동·안전성·효율을 강화한다.
- 주 개조가 회차 영구 고정이므로 설치한 설비도 다른 개조 분기로 전용할 수 없다.
- 공용 태그 설비는 같은 개조 안에서 위치 조정이 가능할 수 있다.
- 방 파괴 시 설비는 정상 / 손상 / 파괴 / 회수 가능 상태 중 하나가 된다.
- R18 전용 효과는 공통 DB가 아니라 확장 DB가 소유한다.

## 3. 설비 데이터 구조

```yaml
facility_id:
name:
category:
facility_tags: []
native_rooms: []
compatible_rooms: []
required_remodels: []
unlocks_actions: []
modifies_actions: []
resource_mode:
condition:
repair_tags: []
loot_category: hideout_facility
rarity_tier:
r18_extension: none
status: candidate
```

## 4. 설비 분류

| 분류 | 역할 |
|---|---|
| 생활 | 휴식·위생·배식·관계 |
| 의료 | 치료·기벽·오염·회복 |
| 제작 | 제작·수리·개조·재료 회수 |
| 정보 | 지도·통신·관측·연구 |
| 방어 | 경보·함정·바리케이드·대피 |
| 저장 | 식량·위험물·설비·비상 자원 보호 |
| 훈련 | 전투·기술·전문 숙련 |
| 특수 | 이상현상·괴물 부산물·유물 대응 |

## 5. 생활·관계 설비

### 5.1 보강 침구 세트

```yaml
facility_id: HFAC_BEDDING_REINFORCED
category: 생활
facility_tags: [침구, 휴식]
native_rooms: [HIDEOUT_BIG_ROOM]
compatible_rooms: [HIDEOUT_SMALL_ROOM, HIDEOUT_LIVING_ROOM]
required_remodels: [공동_침실, 회복실, 공동생활실]
unlocks_actions: []
modifies_actions: [휴식]
resource_mode: passive
r18_extension: optional
status: candidate
```

- 피로·컨디션 회복 행동의 안정성을 높인다.
- 수면 방해 사건의 일부 부작용을 완화할 수 있다.
- 전문 치료나 정신 기벽 제거를 직접 수행하지 않는다.

### 5.2 오락 수납장

```yaml
facility_id: HFAC_RECREATION_CABINET
category: 생활
facility_tags: [오락, 기호품, 취미]
native_rooms: [HIDEOUT_LIVING_ROOM]
compatible_rooms: [HIDEOUT_DINING_ROOM, HIDEOUT_SMALL_ROOM]
required_remodels: [오락실, 공동생활실, 개인_작업실]
unlocks_actions: [집단_취미, 기호품_교류]
modifies_actions: [취미, 대화_교류]
resource_mode: item_input
r18_extension: optional
status: candidate
```

- 기호품·책·게임·음악품을 활용한 취미 행동을 해금한다.
- 특정 NPC에게는 긍정적·부정적 반응이 다를 수 있다.

### 5.3 공동 게시판

```yaml
facility_id: HFAC_COMMUNITY_BOARD
category: 생활
facility_tags: [관계, 일정, 공지]
native_rooms: [HIDEOUT_LIVING_ROOM, HIDEOUT_DINING_ROOM]
compatible_rooms: [HIDEOUT_ENTRANCE]
required_remodels: [공동생활실, 공동_식당, 출정_준비실]
unlocks_actions: [행동_방침_공유]
modifies_actions: [자율행동_우선순위]
resource_mode: passive
r18_extension: none
status: candidate
```

- NPC 자율행동 방침을 집단에 전달하는 서사적 설비다.
- 명령 저항을 제거하지 않으며, 오해와 비효율만 줄인다.

## 6. 의료·위생 설비

### 6.1 기본 진료대

```yaml
facility_id: HFAC_MEDICAL_BED_BASIC
category: 의료
facility_tags: [의료, 치료]
native_rooms: [HIDEOUT_SMALL_ROOM]
compatible_rooms: [HIDEOUT_BIG_ROOM]
required_remodels: [의무실, 회복실]
unlocks_actions: [안정_치료]
modifies_actions: [간호]
resource_mode: passive
repair_tags: [REPAIR, TOOLKIT]
r18_extension: optional
status: candidate
```

- 일반 부상 치료와 상태 안정 행동을 강화한다.
- 전문적 기벽 치료에는 추가 설비가 필요하다.

### 6.2 전문 의료 장비 세트

```yaml
facility_id: HFAC_MEDICAL_SET_PRO
category: 의료
facility_tags: [전문_의료, 진단]
native_rooms: [HIDEOUT_SMALL_ROOM]
compatible_rooms: [HIDEOUT_BIG_ROOM]
required_remodels: [의무실, 회복실]
unlocks_actions: [전문_치료, 어려운_기벽_치료]
modifies_actions: [간호, 진단]
resource_mode: item_input
repair_tags: [REPAIR, TOOLKIT, HACK]
r18_extension: required
status: candidate
```

- 전문 의료품과 간호 판정을 결합하는 치료를 해금한다.
- 영구 변이·특수 기벽을 자동 제거하지 않는다.

### 6.3 상담 기록함

```yaml
facility_id: HFAC_COUNSEL_ARCHIVE
category: 의료
facility_tags: [상담, 기록, 정신]
native_rooms: [HIDEOUT_SMALL_ROOM]
compatible_rooms: [HIDEOUT_BIG_ROOM]
required_remodels: [상담실, 간부실]
unlocks_actions: [정신_기벽_상담, 트라우마_대화]
modifies_actions: [간호, 대화_교류]
resource_mode: passive
r18_extension: required
status: candidate
```

- 정신적 기벽과 트라우마의 적합한 치료 선택지를 구분한다.
- 상담 대상의 신뢰와 치료 동의 여부가 중요하다.

### 6.4 제독 샤워 장치

```yaml
facility_id: HFAC_DECON_SHOWER
category: 의료
facility_tags: [제독, 위생, 오염]
native_rooms: [HIDEOUT_SHOWER]
compatible_rooms: [HIDEOUT_LAUNDRY, HIDEOUT_ENTRANCE]
required_remodels: [제독실, 위생_관리실, 귀환_검역실]
unlocks_actions: [강한_오염_제거]
modifies_actions: [세척, 검역]
resource_mode: charge_or_filter
repair_tags: [REPAIR, TOOLKIT]
r18_extension: required
status: candidate
```

- 외출 귀환자의 오염·감염 위험을 줄인다.
- 필터나 소모재가 없으면 기본 세척만 가능하다.

### 6.5 격리 잠금장치

```yaml
facility_id: HFAC_ISOLATION_LOCK
category: 의료
facility_tags: [격리, 구금, 안전]
native_rooms: [HIDEOUT_SMALL_ROOM, HIDEOUT_BASEMENT]
compatible_rooms: [HIDEOUT_TOILET]
required_remodels: [격리실, 구금실, 봉쇄_구역]
unlocks_actions: [안전_격리]
modifies_actions: [간호, 경계]
resource_mode: passive
repair_tags: [REPAIR, PRY]
r18_extension: optional
status: candidate
```

- 감염자·침식자·적대 인물을 안전하게 분리한다.
- 격리 대상의 자유행동과 관계에 부정적 영향을 줄 수 있다.

## 7. 제작·수리 설비

### 7.1 공구 작업대

```yaml
facility_id: HFAC_TOOL_BENCH
category: 제작
facility_tags: [공구, 제작, 수리]
native_rooms: [HIDEOUT_SMALL_ROOM, HIDEOUT_KITCHEN]
compatible_rooms: [HIDEOUT_STORAGE, HIDEOUT_LAUNDRY]
required_remodels: [개인_작업실, 응급_작업대, 설비_보관소, 의복_정비실]
unlocks_actions: [장비_수리, 소비품_제작]
modifies_actions: [제작_수리, 시설_강화_보수]
resource_mode: item_input
repair_tags: [REPAIR, TOOLKIT]
r18_extension: optional
status: candidate
```

- 제작·수리 행동의 중심 설비다.
- 모든 제작법을 자동 해금하지 않으며 레시피·능력 조건은 유지한다.

### 7.2 재료 분해대

```yaml
facility_id: HFAC_SALVAGE_TABLE
category: 제작
facility_tags: [해체, 부품, 재활용]
native_rooms: [HIDEOUT_STORAGE, HIDEOUT_LAUNDRY]
compatible_rooms: [HIDEOUT_POOL]
required_remodels: [정리_창고, 재료_재생실, 봉쇄_저장구역]
unlocks_actions: [장비_해체, 재료_회수]
modifies_actions: [제작_수리]
resource_mode: item_input
repair_tags: [REPAIR]
r18_extension: none
status: candidate
```

- 불필요하거나 파손된 장비에서 부품·천·필터류를 회수한다.
- 무한 증식 방지를 위해 회수량은 원재료보다 낮아야 한다.

### 7.3 의복 정비대

```yaml
facility_id: HFAC_CLOTHING_STATION
category: 제작
facility_tags: [의복, 방어구, 수선]
native_rooms: [HIDEOUT_LAUNDRY]
compatible_rooms: [HIDEOUT_STORAGE, HIDEOUT_SMALL_ROOM]
required_remodels: [의복_정비실, 설비_보관소, 개인_작업실]
unlocks_actions: [보호장비_수선]
modifies_actions: [제작_수리, 세척]
resource_mode: item_input
repair_tags: [REPAIR, TOOLKIT]
r18_extension: required
status: candidate
```

- 실제 장비 내구도를 수리한다.
- R18 의복 게이지는 전투별 진행값이며 직접 영구 수리 대상으로 취급하지 않는다.

## 8. 정보·통신 설비

### 8.1 지도·작전판

```yaml
facility_id: HFAC_TACTICAL_MAP_BOARD
category: 정보
facility_tags: [지도, 작전, 단서]
native_rooms: [HIDEOUT_LIVING_ROOM]
compatible_rooms: [HIDEOUT_BIG_ROOM]
required_remodels: [작전실, 간부실]
unlocks_actions: [경로_분석, 지역_정보_정리]
modifies_actions: [조사_연구, 외출_준비]
resource_mode: clue_input
r18_extension: none
status: candidate
```

- 발견한 지도와 단서를 외출 선택지로 전환한다.
- 미발견 지역 정보까지 자동 공개하지 않는다.

### 8.2 고정 무전기

```yaml
facility_id: HFAC_RADIO_STATION
category: 정보
facility_tags: [통신, 신호, 세력]
native_rooms: [HIDEOUT_VERANDA]
compatible_rooms: [HIDEOUT_LIVING_ROOM, HIDEOUT_ENTRANCE]
required_remodels: [통신소, 작전실, 출정_준비실]
unlocks_actions: [외부_교신, 구조_신호]
modifies_actions: [조사_연구, 경계]
resource_mode: charge
repair_tags: [REPAIR, HACK]
r18_extension: optional
status: candidate
```

- 세력·생존자·세계 이벤트의 통신 선택지를 연다.
- 연락 결과가 항상 우호적이거나 안전하지는 않다.

### 8.3 장거리 관측경

```yaml
facility_id: HFAC_LONG_RANGE_SCOPE
category: 정보
facility_tags: [관측, 괴물, 경계]
native_rooms: [HIDEOUT_VERANDA, HIDEOUT_GARDEN]
compatible_rooms: [HIDEOUT_GATE]
required_remodels: [감시초소, 저격_관측지점, 정찰_정원]
unlocks_actions: [원거리_관측]
modifies_actions: [경계, 조사_연구]
resource_mode: passive
repair_tags: [REPAIR]
r18_extension: optional
status: candidate
```

- 새벽 맵 배치 괴물·세력 이동의 일부 정보를 조기 공개할 수 있다.
- 완전한 위치·약점 공개를 보장하지 않는다.

### 8.4 구형 분석 단말기

```yaml
facility_id: HFAC_ANALYSIS_TERMINAL
category: 정보
facility_tags: [기술, 기록, 분석]
native_rooms: [HIDEOUT_SMALL_ROOM, HIDEOUT_BASEMENT]
compatible_rooms: [HIDEOUT_LIVING_ROOM]
required_remodels: [개인_작업실, 격리_연구실, 작전실]
unlocks_actions: [데이터_복구, 기록_해독]
modifies_actions: [조사_연구]
resource_mode: charge
repair_tags: [HACK, REPAIR]
r18_extension: optional
status: candidate
```

- 전자 기록·암호화 저장장치·괴물 연구 자료를 해석한다.
- 지능·기술 판정을 대체하지 않는다.

## 9. 방어·경계 설비

### 9.1 기계식 경보망

```yaml
facility_id: HFAC_ALARM_NETWORK
category: 방어
facility_tags: [경보, 침입, 순찰]
native_rooms: [HIDEOUT_GATE, HIDEOUT_CORRIDOR]
compatible_rooms: [HIDEOUT_GARDEN, HIDEOUT_ENTRANCE]
required_remodels: [강화_관문, 경보_복도, 정찰_정원, 전방_방어실]
unlocks_actions: [침입_조기경보]
modifies_actions: [경계, 불침번]
resource_mode: passive_or_charge
repair_tags: [REPAIR, TOOLKIT]
r18_extension: optional
status: candidate
```

- 침입을 막기보다 조기에 알린다.
- 오작동·이상현상 사건의 대상이 될 수 있다.

### 9.2 모듈식 바리케이드

```yaml
facility_id: HFAC_BARRICADE_MODULE
category: 방어
facility_tags: [방어, 병목, 지연]
native_rooms: [HIDEOUT_GATE, HIDEOUT_ENTRANCE, HIDEOUT_CORRIDOR]
compatible_rooms: [HIDEOUT_GARDEN, HIDEOUT_BASEMENT]
required_remodels: [강화_관문, 전방_방어실, 방어_복도, 완충_지대, 비상_대피소]
unlocks_actions: [방어선_구축]
modifies_actions: [아지트_전투, 시설_강화_보수]
resource_mode: durability
repair_tags: [REPAIR, TOOLKIT]
r18_extension: none
status: candidate
```

- 아지트 전투의 이동·침입을 지연한다.
- 일상 이동이나 귀환 동선에 불편을 줄 수 있다.

### 9.3 함정 제어판

```yaml
facility_id: HFAC_TRAP_CONTROL
category: 방어
facility_tags: [함정, 지역_통제]
native_rooms: [HIDEOUT_GATE, HIDEOUT_POOL, HIDEOUT_GARDEN]
compatible_rooms: [HIDEOUT_CORRIDOR]
required_remodels: [함정_진입로, 방어_함정구역, 완충_지대, 방어_복도]
unlocks_actions: [함정_배치, 함정_재설정]
modifies_actions: [경계, 아지트_전투]
resource_mode: item_input
repair_tags: [REPAIR, TOOLKIT]
r18_extension: optional
status: candidate
```

- 전술품·부품을 아지트 방어 선택지로 전환한다.
- 아군 오작동 위험과 재설정 비용이 존재한다.

### 9.4 비상 대피 캐비닛

```yaml
facility_id: HFAC_EMERGENCY_CACHE
category: 방어
facility_tags: [대피, 비상, 생존]
native_rooms: [HIDEOUT_BASEMENT]
compatible_rooms: [HIDEOUT_STORAGE, HIDEOUT_BIG_ROOM]
required_remodels: [비상_대피소, 비상_창고, 공동_침실]
unlocks_actions: [비상_대피_준비]
modifies_actions: [아지트_전투, 재난_이벤트]
resource_mode: item_input
r18_extension: none
status: candidate
```

- 아지트 공격·화재·오염 사건 중 일부 자원과 생존자를 보호한다.
- 평상시 전투력을 직접 높이지 않는다.

## 10. 저장·보존 설비

### 10.1 밀폐 식품 보관함

```yaml
facility_id: HFAC_FOOD_STORAGE_SEALED
category: 저장
facility_tags: [식량, 보존]
native_rooms: [HIDEOUT_KITCHEN, HIDEOUT_STORAGE]
compatible_rooms: [HIDEOUT_BASEMENT]
required_remodels: [보존_주방, 보존_창고, 비상_창고]
unlocks_actions: []
modifies_actions: [식량_정리, 배식]
resource_mode: passive
repair_tags: [REPAIR]
r18_extension: none
status: candidate
```

- 식량 변질·도난·사건 손실을 완화한다.
- 식량을 생산하거나 배급 비용을 제거하지 않는다.

### 10.2 위험물 격납함

```yaml
facility_id: HFAC_HAZARD_LOCKER
category: 저장
facility_tags: [위험물, 유물, 오염]
native_rooms: [HIDEOUT_STORAGE, HIDEOUT_BASEMENT]
compatible_rooms: [HIDEOUT_POOL]
required_remodels: [위험물_창고, 격리_연구실, 봉쇄_저장구역]
unlocks_actions: [위험물_보관]
modifies_actions: [조사_연구, 경계]
resource_mode: passive
repair_tags: [REPAIR, PRY]
r18_extension: optional
status: candidate
```

- 폭발물·오염물·괴물 부산물·위험 유물의 사건 위험을 낮춘다.
- 내용물 자체의 저주나 특수 이벤트까지 무효화하지 않는다.

### 10.3 설비 운반대

```yaml
facility_id: HFAC_FACILITY_RACK
category: 저장
facility_tags: [설비, 운반, 보관]
native_rooms: [HIDEOUT_STORAGE]
compatible_rooms: [HIDEOUT_POOL, HIDEOUT_BASEMENT]
required_remodels: [설비_보관소, 봉쇄_저장구역, 비상_창고]
unlocks_actions: [설비_보관, 설비_수리_준비]
modifies_actions: [시설_강화_보수]
resource_mode: passive
r18_extension: none
status: candidate
```

- 아직 설치하지 않은 설비와 회수한 파손 설비를 보관한다.
- 영구 선택된 개조와 맞지 않는 설비를 다른 분기로 전환하는 기능은 없다.

## 11. 훈련 설비

### 11.1 기초 훈련 세트

```yaml
facility_id: HFAC_TRAINING_BASIC
category: 훈련
facility_tags: [훈련, 전투, 기초]
native_rooms: [HIDEOUT_LIVING_ROOM, HIDEOUT_GARDEN, HIDEOUT_POOL]
compatible_rooms: [HIDEOUT_BIG_ROOM]
required_remodels: [집단_훈련실, 훈련_마당, 집단_훈련장, 고급_훈련실]
unlocks_actions: [기초_훈련]
modifies_actions: [훈련]
resource_mode: passive
r18_extension: optional
status: candidate
```

- 반복 가능한 경험·숙련 행동을 지원한다.
- 무제한 영구 스탯 상승을 제공하지 않는다.

### 11.2 전문 훈련 장비

```yaml
facility_id: HFAC_TRAINING_SPECIALIST
category: 훈련
facility_tags: [전문_훈련, 고유_능력]
native_rooms: [HIDEOUT_BIG_ROOM]
compatible_rooms: [HIDEOUT_LIVING_ROOM, HIDEOUT_POOL]
required_remodels: [고급_훈련실, 집단_훈련실, 집단_훈련장]
unlocks_actions: [전문_훈련, 고유_능력_연습]
modifies_actions: [훈련]
resource_mode: item_input
r18_extension: optional
status: candidate
```

- NPC 직업·고유기술과 맞는 전문 훈련을 제공한다.
- 모든 생존자에게 같은 효과를 주지 않는다.

## 12. 특수 연구 설비

### 12.1 봉인 관측함

```yaml
facility_id: HFAC_ANOMALY_OBSERVATION_BOX
category: 특수
facility_tags: [이상현상, 봉인, 연구]
native_rooms: [HIDEOUT_BASEMENT, HIDEOUT_POND]
compatible_rooms: [HIDEOUT_STORAGE]
required_remodels: [격리_연구실, 관측_구역, 위험물_창고]
unlocks_actions: [이상현상_관찰, 안전_표본_분석]
modifies_actions: [조사_연구]
resource_mode: item_input
repair_tags: [REPAIR, TOOLKIT]
r18_extension: optional
status: experimental
```

- 이상현상·괴물 부산물을 제한적으로 연구한다.
- 실패 시 오염·침식·사건 위험이 존재한다.

### 12.2 의식 흔적 분석대

```yaml
facility_id: HFAC_RITUAL_ANALYSIS_TABLE
category: 특수
facility_tags: [의식, 단서, 유물]
native_rooms: [HIDEOUT_LIVING_ROOM, HIDEOUT_BASEMENT]
compatible_rooms: [HIDEOUT_SMALL_ROOM, HIDEOUT_POND]
required_remodels: [작전실, 격리_연구실, 개인_작업실, 관측_구역]
unlocks_actions: [의식_단서_분석]
modifies_actions: [조사_연구]
resource_mode: clue_input
r18_extension: optional
status: experimental
```

- 일반 단서와 고유 단서를 분류해 장소·세계 이벤트 선택지로 연결한다.
- 의식 중단이나 세계 구원을 직접 가능하게 하지 않는다.

## 13. 설비 획득과 설치

설비는 다음 경로로 획득할 수 있다.

- 지역 탐색의 `아지트 설비` 카테고리
- 지역 필수 이벤트 보상
- 맵 배치 괴물 해결 후 봉쇄 구역 접근
- 세력 거래·보상
- 제작 또는 파손 설비 복구

설치 과정:

```text
설비 확보
→ 설치 가능한 주 개조 확인
→ 방 상태 확인
→ 시설 강화·보수 행동
→ 제작/기술 판정
→ 설비 설치
```

주 개조와 맞지 않는 설비는 설치할 수 없다.

## 14. 설비 손상·파괴·회수

| 상태 | 처리 |
|---|---|
| 정상 | 전체 기능 사용 |
| 손상 | 전문 기능 또는 보정 일부 제한 |
| 파괴 | 기능 정지, 수리 또는 해체 필요 |
| 회수 가능 | 다른 위치가 아니라 선택된 동일 개조 내 재설치 가능 |
| 소실 | 이벤트가 명시할 때만 완전 제거 |

- 방이 파괴돼도 설비가 자동 소실되지는 않는다.
- 영구 개조 규칙 때문에 회수 설비를 다른 주 개조에 전용할 수 없다.
- 공통 기반 설비는 같은 개조 분기의 복구에 재사용할 수 있다.

## 15. R18 확장 경계

- 공통 설비는 R18 OFF에서도 완전하게 작동한다.
- `required`는 공통 기능이 불완전하다는 뜻이 아니라 확장 데이터가 필요하다는 뜻이다.
- R18 전용 설비는 별도 `R18_HIDEOUT_FACILITY_DB`가 소유한다.
- 공통 설비의 R18 효과는 item/facility ID 참조 방식으로 추가한다.

확장 후보:

- 전문 의료 장비: R18 기벽 치료 조건
- 상담 기록함: 성벽·상식개변·욕구 기벽 상담
- 의복 정비대: R18 의복 손상 프로파일 연결
- 제독 샤워 장치: R18 전용 신체 상태 완화
- 보강 침구·오락 수납장: 사적 관계 이벤트 추가

## 16. 우선 구현 후보

### 권장 1차

- 공구 작업대
- 기본 진료대
- 지도·작전판
- 고정 무전기
- 장거리 관측경
- 기계식 경보망
- 모듈식 바리케이드
- 밀폐 식품 보관함
- 오락 수납장
- 보강 침구 세트

### 권장 2차

- 전문 의료 장비 세트
- 상담 기록함
- 제독 샤워 장치
- 재료 분해대
- 의복 정비대
- 함정 제어판
- 위험물 격납함
- 기초 훈련 세트

### 실험

- 구형 분석 단말기
- 봉인 관측함
- 의식 흔적 분석대
- 전문 훈련 장비

## 17. 미확정 항목

- 설비별 실제 크기와 슬롯 비용
- 설치·수리 부품 비용
- 능력 판정 난이도
- 설비 내구도 단계
- 소모재·충전량
- 장소별 실제 획득 후보
- 설비 중복 설치 허용 여부
- 사건 저항·행동 보정 수치
- R18 전용 설비 후보 목록
