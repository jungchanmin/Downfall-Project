---
id: MECH_Status_Effect_DB
title: "핵심 시스템 사양서 — 상태이상·전투기벽 데이터베이스"
type: mechanic
status: wip
version: 1.0.0
summary: >
  모든 상태이상·전투기벽의 정의 단일 출처(single source of truth). 일반 전투·R18·굴복 페이즈
  전용을 ID 체계로 통합 관리. 기술 카탈로그·MONSTER_DB는 status_inflict 에 본 DB의 ID를 참조만 한다.
  신규 상태이상 도입은 본 DB 등록 + 디렉터 승인 게이트. 중복 정의(같은 이름 다른 효과)를 원천 차단.
tags:
  - mechanic
  - system
  - combat
  - status_effect
  - database
keywords:
  - 상태이상, 전투기벽, 속박, 고통, 공포, 출혈, 낙인, 최면, 홀림, 광분, 타락욕망,
    무방비, 비틀거림, 은신, 절정 여운, 굴복 페이즈, 단일 출처, ID 참조
depends_on:
  - SYS_Manifest
  - MECH_Combat_System
  - MECH_Quirk_R18_DB
last_updated: 2026-06-08
---

# 🩹 DOWNFALL 상태이상·전투기벽 데이터베이스 (v1.0)

> **정의의 단일 출처.** 모든 상태이상·전투기벽은 여기 한 번만 정의. 기술/괴물은 ID로 참조만.
> 신규 도입 = 본 DB 등록 + 디렉터 승인. **같은 이름 다른 효과(중복 정의) 금지** — 등록 전 대조 필수.

---

## SECTION 0 — 분류 & ID 규약

```
ID 규약: ST_{이름}
구분:
  지속형(transient)  : 전투 중 일시. 턴/조건으로 만료.
  전투기벽(combat_quirk): 전투 중 누적·발현. 전투 종료 시 해제(일부는 영구 기벽 전환).
대상: survivor / monster
계층: general(일반 전투) / r18(R18 토글) / submission(굴복 페이즈 한정)
신규 등록 시 필수: id / 대상 / 계층 / 효과 / 해제 / 부여처(어떤 기술이 거는가)
```

> R18·submission 계층은 SFW 빌드에서 비활성. 본 DB 안에서 `layer` 필드로 구분.

---

## SECTION 1 — 일반 전투 (general)

| ID | 이름 | 대상 | 구분 | 효과 | 해제 | 부여처(예) |
|---|---|---|---|---|---|---|
| `ST_Bound` | 속박됨 | survivor | 지속 | 공격 불가, 탈출 시도만. 도주 불가 | 탈출 판정 | 붙잡기·물기 |
| `ST_Pain` | 고통 | survivor | 지속 | 전투 주사위 −1 | 일시 | 발톱치기 |
| `ST_SeverePain` | 심각한 고통 | survivor | 지속 | 전투 절반 — 이탈까지 | 전투 종료 | 데스롤 |
| `ST_Fear` | 공포 | survivor | 전투기벽 | 피격마다 영구 기벽 +1 | 종료/대기/간호 | 공포스러운 외침 |
| `ST_Cower` | 움츠러듬 | survivor | 지속 | 1턴 해당 괴물 공격 불가 | 1턴 후 | 외치기 |
| `ST_Stun` | 기절 | survivor | 지속 | 1턴 모든 행동 불가 | 1턴 후 | 잔혹한 처형식 |
| `ST_Bleed` | 출혈 | survivor | 전투기벽 | 매 턴 고정 소량 피해. 중첩 가능(중첩 시 피해↑) | 간호/대기 | 찌르기 |
| `ST_Brand` | 낙인 | survivor | 전투기벽 | 자체 효과 미미(표식). 중첩 수 = '피의 제사' 위력·발동 연료 | 피의 제사로 소비 / 종료 | 낙인새기기 |
| `ST_Exposed` | 무방비 | monster | 지속 | 회피 불가 → 개방. 강공 +2 보너스 | 일시/괴물 행동 | 약공 누적 |
| `ST_Stagger` | 비틀거림 | survivor | 지속 | 다음 행동 주사위 −1 | 1행동 후 | 꼬리치기 |
| `ST_Stealth` | 은신 | monster | 지속 | 공격받지 않음. 공격 시 해제+1턴 공격력 2배 | 피격/탐색 | 은밀한 잠복자 |

---

## SECTION 2 — R18 (r18) — 토글 시 활성

| ID | 이름 | 대상 | 구분 | 효과 | 해제 | 부여처(예) |
|---|---|---|---|---|---|---|
| `ST_R18_Bound` | R18 속박 | survivor | 지속 | [속박] + 탈출 요구치↑ + 흥분 누적 | 탈출 판정 | 촉수 다중속박 |
| `ST_Arousal` | 흥분 | survivor | 전투기벽 | 성감 누적 시 발현. 일부 커맨드 봉인 | 종료/대기/간호 | R18 피격 |
| `ST_Hypnosis` | 최면 | survivor | 전투기벽 | 공격 표적 무작위화/아군 오인 | 종료/대기/간호 | (R18 표적 교란계) |
| `ST_Enthrall` | 홀림 | survivor | 전투기벽 | 기벽저항↓ + 성감 누적 가속 | 종료/대기/간호 | 광신도 '최면(정신착란)' |
| `ST_Frenzy` | 광분 | survivor | 전투기벽 | 전투 커맨드 위력↑ + 괴물 분노 게이지↓ (흥분 경로 유도) | 종료/대기/간호 | 광신도 '광란' |
| `ST_CorruptDesire` | 타락욕망 | survivor | 전투기벽 | 전투 커맨드 효과 크게↓ + (흥분 先MAX 시) 강제 굴복 전환 | 종료/대기/간호 | 광신도 '끔찍한 환상' |
| `ST_Submission` | 굴종 | survivor | 전투기벽 | [공포]의 R18 변종 — 저항→순응, 도주 트랙 잠금 | 종료 | (공포 R18 변종) |

> **충돌 해소 명시**: `ST_Hypnosis`(최면 = 표적 무작위화)와 `ST_Enthrall`(홀림 = 기벽저항↓·성감 가속)은
> **별개의 상태이상**이다. 이름·효과 혼용 금지. (광신도 기획 충돌 정정 반영)

---

## SECTION 3 — 굴복 페이즈 전용 (submission)

| ID | 이름 | 대상 | 구분 | 효과 | 해제 | 주도권 작용 |
|---|---|---|---|---|---|---|
| `ST_Afterglow` | 절정 여운 | both | 지속 | 1~2턴 행동 불가 | 턴 경과 | 상대 주도권 굳히기 |
| `ST_Trance` | 홀림(굴복) | survivor | 지속 | 행동 무작위화/의지 흐려짐 | 해제 판정 | 주도권 쥔 채 교란 |
| `ST_Restraint` | 구속(굴복) | survivor | 지속 | 행동 선택지 제한(저항·특정 기술만) | 탈출 시도 | 탈출 성공 = 주도권 탈환 |
| `ST_Ecstasy` | 황홀 | survivor | 전투기벽 | [기절]의 R18 변종 — 행동 불가 + 제압 전환 가속 | 종료/대기 | 제압 가속 |

> 주도권(Tempo) 메커니즘 본문은 `MECH_Combat_System` SECTION 11-4.

---

## SECTION 4 — 데이터 구조 (참조 방식)

```yaml
StatusEffectDef:               # 본 DB가 소유하는 정의
  id: str                      # ST_*
  name: str
  target: survivor | monster | both
  kind: transient | combat_quirk
  layer: general | r18 | submission
  effect: str
  clear: str
  effect_id: str | null        # 복잡 로직은 코드 핸들러 위임
  permanent_convert: bool      # 전투기벽 → 영구 기벽 전환 가능 여부(예 공포)

# 기술 카탈로그·MONSTER_DB:
status_inflict: [ST_Bleed, ST_Brand]   # 본 DB ID 참조만
```

---

## SECTION 5 — 신규 등록 프로토콜 (정합성 방지책)

```
신규 상태이상이 기획에 등장하면:
  1. 본 DB와 대조 → "기존에 X 있음 / 신규임" 먼저 보고
  2. 신규면: 같은 이름 다른 효과(중복 정의) 아닌지 확인 → 디렉터 승인
  3. 승인 후 본 DB 등록 → 기술 카탈로그가 ID 참조
빌드 검증(코드 단계):
  - 모든 status_inflict ID가 본 DB에 존재하는가
  - 중복 정의(동일 id 2회 / 동일 name 다른 효과)가 없는가
  → 사람이 놓쳐도 기계가 차단.
```

---

## SECTION 6 — 버전 관리

- **문서 위치**: `01_Mechanics/MECH_Status_Effect_DB.md`
- **커밋 메시지**: `feat(mechanic): status effect DB — single source of truth (general/r18/submission), resolve 최면/홀림 conflict`
- **Wiki_Index.md 갱신 필요 여부**: **필요 (YES)**

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.0.0 | 2026-06-08 | 최초. Combat SECTION 10 표 이전 + ID 체계화. 일반 11종 / R18 7종 / 굴복 전용 4종. 신규(출혈·낙인·홀림·광분·타락욕망) 등록. **최면≠홀림 충돌 해소.** 신규 등록 프로토콜·빌드 검증 규약. |

**갱신 기준**: 네임드 기벽 50+종·R18 추가분 순차 등록. `layer`별 SFW 토글. 신규는 SECTION 5 프로토콜 준수.
