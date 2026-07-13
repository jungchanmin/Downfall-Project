---
id: HIDEOUT_ROOM_PROFILE
title: 아지트 방 프로필 및 개조 분기
type: database
status: wip
summary: 아지트 고정 구역별 공간 규모, 기본 행동, 주 개조 분기, 설비 적합성과 손상 영향을 정의한다.
tags: [hideout, room, remodel, capacity, facility]
keywords: [아지트 방, 개조 분기, 수용 인원, 설비 슬롯, 방 상태]
depends_on:
  - LORE_LOC_Hideout
  - MECH_Hideout_System
emits:
  - HIDEOUT_FACILITY_DB
  - HIDEOUT_ACTION_PROFILE
last_updated: 2026-07-13
---

# 아지트 방 프로필 및 개조 분기

## 1. 목적

이 문서는 `MECH_Hideout_System`의 공통 규칙을 실제 아지트 고정 구역에 적용한다.

정확한 수용 인원, 설비 슬롯 수, 부품 비용과 판정 난이도는 테스트 단계에서 확정한다. 현재 단계에서는 방의 역할, 개조 선택과 상호 배타성을 정의한다.

## 2. 구조 결정

### 2.1 주 개조는 방마다 하나

각 방은 동시에 하나의 **주 개조**만 활성화한다.

- 기본 행동은 주 개조 후에도 유지될 수 있다.
- 주 개조는 방의 핵심 보너스와 특별 행동을 결정한다.
- 모든 분기를 동시에 활성화할 수 없다.
- 일부 보조 설비는 주 개조와 무관하게 설치할 수 있다.

이 규칙은 회차별 아지트 빌드 차이를 만든다.

### 2.2 주 개조는 회차 동안 영구 고정

주 개조가 완성되면 같은 회차에서 다른 분기로 변경할 수 없다.

- 시설 파괴 후에는 선택했던 동일 분기만 복구할 수 있다.
- 파괴를 이용해 다른 개조 분기로 전환할 수 없다.
- 전용 설비가 파괴돼도 주 개조 선택은 유지된다.
- 다음 회차에서는 다른 분기를 선택할 수 있다.

이 규칙은 플레이 도중 재배치 최적화에 집착하는 부담을 줄이고, 다회차 플레이에서 플레이어 경험과 빌드 지식을 보상한다.

### 2.3 수용 규모는 등급으로 관리

| 규모 | 의미 |
|---|---|
| 소형 | 개인 행동 또는 소수 전문 행동 |
| 중형 | 소규모 공동 행동 |
| 대형 | 다수 공동 행동·방어·집단 이벤트 |
| 실외 | 행동 종류와 이벤트에 따라 가변 |

실제 인원 수는 후속 밸런스 데이터가 소유한다.

### 2.4 설비 적합성

설비는 다음 적합도 중 하나를 가진다.

- `native`: 해당 방·개조에 가장 적합
- `compatible`: 설치 가능하지만 효율 또는 기능 제한 가능
- `forbidden`: 구조상 설치 불가

### 2.5 기본 행동과 전문 행동

- 기본 행동은 방이 정상 상태라면 개조 없이 수행 가능하다.
- 전문 행동은 특정 주 개조 또는 설비를 요구한다.
- 방이 손상되면 전문 행동부터 제한한다.

## 3. 실외 및 진입로

### 3.1 대문

```yaml
room_id: HIDEOUT_GATE
size: large
base_actions: [경계, 출입_통제, 침입_흔적_조사, 응급_보강]
primary_remodels: [강화_관문, 검문소, 함정_진입로]
facility_affinity: [방어, 경보, 검역, 함정]
combat_role: 첫_방어선
r18_extension: optional
```

| 개조 | 핵심 역할 | 대가·제약 |
|---|---|---|
| 강화 관문 | 침입 지연, 구조물 방어, 파괴 저항 | 외부 정보 획득에는 기여가 낮음 |
| 검문소 | 귀환자·방문자 검사, 오염·위험 조기 발견 | 직접 방어력은 낮음 |
| 함정 진입로 | 침입자 피해·경보·행동 지연 | 아군 출입과 복구 부담 증가 가능 |

### 3.2 정원

```yaml
room_id: HIDEOUT_GARDEN
size: exterior
base_actions: [침입_흔적_조사, 관측, 은신, 자재_정리]
primary_remodels: [정찰_정원, 훈련_마당, 완충_지대]
facility_affinity: [관측, 훈련, 장애물, 함정]
combat_role: 접근_탐지와_지연
r18_extension: optional
```

### 3.3 연못

```yaml
room_id: HIDEOUT_POND
size: exterior
base_actions: [이상현상_조사, 투척_훈련]
primary_remodels: [관측_구역, 봉쇄_구역]
facility_affinity: [관측, 의식_연구, 봉쇄]
combat_role: 환경_위험
r18_extension: optional
```

연못은 안정적인 물 자원 생산지가 아니다.

### 3.4 텃밭

```yaml
room_id: HIDEOUT_GARDEN_PLOT
size: exterior
base_actions: [재배, 토양_조사, 음식물_처리]
primary_remodels: [생존_텃밭, 약초_재배지, 오염_연구지]
facility_affinity: [재배, 보존, 의료, 연구]
combat_role: 없음
r18_extension: optional
```

| 개조 | 핵심 역할 | 제한 |
|---|---|---|
| 생존 텃밭 | 식량 부족 완화 | 외출을 대체할 수준의 생산 금지 |
| 약초 재배지 | 의료품·상태치료 보조 | 전문 의료품 직접 생산 금지 |
| 오염 연구지 | 특수 재료·단서 | 오염 사건과 작업자 위험 증가 |

### 3.5 수영장

```yaml
room_id: HIDEOUT_POOL
size: large
base_actions: [대형_함정_준비, 야외_훈련, 이상현상_조사]
primary_remodels: [방어_함정구역, 집단_훈련장, 봉쇄_저장구역]
facility_affinity: [함정, 훈련, 대형_설비, 위험물]
combat_role: 지역_통제
r18_extension: optional
```

## 4. 1층 공용 구역

### 4.1 현관

```yaml
room_id: HIDEOUT_ENTRANCE
size: medium
base_actions: [장비_점검, 귀환_물자_정리, 부상_확인]
primary_remodels: [출정_준비실, 귀환_검역실, 전방_방어실]
facility_affinity: [장비, 검역, 방어, 인벤토리]
combat_role: 실내_첫_방어선
r18_extension: optional
```

### 4.2 거실

```yaml
room_id: HIDEOUT_LIVING_ROOM
size: large
base_actions: [집단_휴식, 회의, 대화, 집단_의사결정]
primary_remodels: [공동생활실, 작전실, 오락실, 집단_훈련실]
facility_affinity: [휴식, 지도, 통신, 오락, 훈련]
combat_role: 중앙_교전지
r18_extension: optional
```

| 개조 | 강화하는 빌드 |
|---|---|
| 공동생활실 | 관계 안정·갈등 완화·집단 회복 |
| 작전실 | 외출 정보·지도·단서·위험 회피 |
| 오락실 | 스트레스·취미·관계 이벤트 |
| 집단 훈련실 | 다수 생존자의 기초 숙련 |

거실의 네 분기는 상호 배타적이다.

### 4.3 식당

```yaml
room_id: HIDEOUT_DINING_ROOM
size: large
base_actions: [배식, 단체_식사, 대화]
primary_remodels: [공동_식당, 회의_식당, 긴급_배급소]
facility_affinity: [배식, 접대, 저장, 관계]
combat_role: 임시_집결지
r18_extension: optional
```

### 4.4 주방

```yaml
room_id: HIDEOUT_KITCHEN
size: medium
base_actions: [조리, 식품_정리, 간단_제작]
primary_remodels: [보존_주방, 대량_조리실, 응급_작업대]
facility_affinity: [조리, 식품_보존, 소비품_제작]
combat_role: 화재_위험
r18_extension: none
```

### 4.5 세탁실

```yaml
room_id: HIDEOUT_LAUNDRY
size: small
base_actions: [의복_수선, 천_세척, 오염_제거_보조]
primary_remodels: [위생_관리실, 의복_정비실, 재료_재생실]
facility_affinity: [위생, 의복, 필터, 붕대]
combat_role: 없음
r18_extension: required
```

### 4.6 복도

```yaml
room_id: HIDEOUT_CORRIDOR
size: medium
base_actions: [이동, 내부_경계, 매복, 순찰]
primary_remodels: [경보_복도, 방어_복도, 안전_동선]
facility_affinity: [경보, 조명, 장애물]
combat_role: 내부_이동과_병목
r18_extension: optional
```

복도는 생활 생산 방이 아니라 다른 방을 연결하고 침입을 통제하는 방이다.

### 4.7 작은방

```yaml
room_id: HIDEOUT_SMALL_ROOM
size: small
base_actions: [개인_휴식, 기억_정리, 은밀한_대화]
primary_remodels: [의무실, 상담실, 격리실, 개인_작업실]
facility_affinity: [의료, 상담, 격리, 연구, 제작]
combat_role: 보호_또는_봉쇄
r18_extension: required
```

| 개조 | 핵심 기능 | 상호 배타 이유 |
|---|---|---|
| 의무실 | 육체 치료·전문 의료 | 위생·의료 설비 전용 |
| 상담실 | 정신 기벽·트라우마·관계 안정 | 조용하고 비공개인 환경 요구 |
| 격리실 | 감염·침식·위험 인물 통제 | 수용자의 자유행동 제한 |
| 개인 작업실 | 집중 제작·연구·취미 | 의료·격리 기능과 공간 충돌 |

### 4.8 창고

```yaml
room_id: HIDEOUT_STORAGE
size: large
base_actions: [물자_보관, 출정_물품_정리, 부품_분류]
primary_remodels: [정리_창고, 보존_창고, 위험물_창고, 설비_보관소]
facility_affinity: [저장, 보존, 위험물, 설비]
combat_role: 자원_보호_목표
r18_extension: optional
```

### 4.9 지하실

```yaml
room_id: HIDEOUT_BASEMENT
size: large
base_actions: [비상_보관, 구금, 대피]
primary_remodels: [비상_대피소, 구금실, 격리_연구실, 비상_창고]
facility_affinity: [대피, 구금, 위험_연구, 비상_저장]
combat_role: 최후_방어선
r18_extension: optional
```

## 5. 2층 및 사적 공간

### 5.1 큰방

```yaml
room_id: HIDEOUT_BIG_ROOM
size: large
base_actions: [숙면, 개인_대화, 수면_경계]
primary_remodels: [공동_침실, 회복실, 간부실, 고급_훈련실]
facility_affinity: [침구, 회복, 지휘, 전문_훈련]
combat_role: 보호_대상_집결
r18_extension: required
```

| 개조 | 핵심 기능 |
|---|---|
| 공동 침실 | 다수 휴식과 피로 회복 |
| 회복실 | 중상자 안정·치료 후 회복 |
| 간부실 | 지휘·개별 명령·핵심 인물 교류 |
| 고급 훈련실 | 소수 정예 훈련·고유 능력 해금 |

### 5.2 베란다

```yaml
room_id: HIDEOUT_VERANDA
size: medium
base_actions: [외부_감시, 신호_교환, 개인_휴식]
primary_remodels: [감시초소, 통신소, 저격_관측지점]
facility_affinity: [관측, 통신, 원거리_지원]
combat_role: 감시와_원거리_지원
r18_extension: optional
```

### 5.3 샤워실

```yaml
room_id: HIDEOUT_SHOWER
size: small
base_actions: [세척, 오염_제거, 상처_세척]
primary_remodels: [제독실, 회복_목욕실, 응급_세척실]
facility_affinity: [제독, 위생, 회복, 응급_처치]
combat_role: 없음
r18_extension: required
```

### 5.4 화장실

```yaml
room_id: HIDEOUT_TOILET
size: small
base_actions: [위생_관리, 단독_휴식, 신체_이상_확인]
primary_remodels: [위생실, 검사실, 봉쇄_구역]
facility_affinity: [위생, 검사, 봉쇄]
combat_role: 이상현상_차단
r18_extension: optional
```

## 6. 개조 단계

공통 단계는 다음 네 상태를 사용한다.

| 단계 | 의미 |
|---|---|
| 미개조 | 방의 기본 행동만 사용 |
| 임시 | 주 개조의 핵심 행동 해금, 불안정 |
| 정비됨 | 표준 기능과 설비 운용 |
| 강화됨 | 전문 행동·사건 저항·설비 효율 강화 |

`강화됨`은 무조건 수치가 높은 단계가 아니다. 개조 방향에 맞는 전문 기능이 강화된다.

## 7. 개조 영구 선택과 복구

- 주 개조가 완성되면 회차 동안 다른 분기로 변경할 수 없다.
- 시설 단계 향상은 선택한 동일 분기 안에서만 가능하다.
- 전용 설비의 설치·파괴·교체는 주 개조 선택을 바꾸지 않는다.
- 파괴 상태에서는 선택한 동일 분기를 복구한다.
- 다음 회차에서만 다른 주 개조를 선택할 수 있다.

## 8. 손상 우선순위

방이 손상되면 다음 순서로 기능이 제한된다.

```text
전문 행동
→ 설치 설비 효과
→ 개조 보정
→ 기본 행동
```

경미한 손상으로 방 전체가 즉시 무용지물이 되지 않도록 한다.

## 9. 확정 전 검토 항목

다음은 후속 밸런스 또는 구현 단계에서 결정한다.

- 소형·중형·대형의 실제 수용 인원
- 단계별 설비 슬롯
- 방별 개조 비용
- 손상 단계 수와 기능 감소량
- 동시에 진행 가능한 개조 공사 수
- 공사 중 방 사용 가능 여부
- R18 확장 데이터의 실제 필드
