---
id: EVT_A001_f2g7
title: 잠든 집이 셌다
type: event
status: complete
summary: >
  새벽 아지트 거실에서 {actor}가 창문 안쪽 유리면의 손자국을 발견하는
  통보형 이벤트. 닿을 수 없는 높이의 흔적.
tags: [event, track_a, F2_Atmosphere, day_any, hideout]
keywords: [아지트, 거실, 창문, 안개, 손자국, 새벽]
depends_on: [LORE_LOC_Oebeng]
emits: [Flag_Memory_{actor}_Saw_Fog_Marks]
last_updated: 2026-05-13
---

event_meta:
  id: EVT_A001_f2g7
  track: A
  family: F2_Atmosphere
  phase: 새벽
  location: Loc_아지트_거실
  weight: 1.2

trigger:
  all:
    - phase: "새벽"
    - day: { gte: 2, lte: 29 }
    - location: "Loc_아지트_거실"

    # ── positive ──
    - any:
        - stat: { actor: "*", 스트레스: { gte: 3 } }
        - day: { gte: 5 }

    # ── negative ──
    - not: { flag: "Flag_Window_Broken" }
    - not: { flag: "Flag_Hideout_Window_Explained" }
    - not: { event_history: { id: "EVT_A001_f2g7", within_days: 5 } }

narration: |
  {actor}{이/가} 거실에 들어섰을 때, 공기가 발소리를 먹었다.
  커튼 틈새로 스민 회색 빛이 창문 유리 위를 기었다. {actor}{은/는}
  부엌 쪽으로 한 걸음 옮기다 멈췄다.

  창문 안쪽 유리면에 손자국이 눌려 있었다.

  엄지와 네 손가락의 윤곽이 안개 속에 박혔다. {actor}{은/는} 창틀
  아래에서 위를 올려다보며 높이를 가늠했다. 창틀에서 세 뼘 위.
  {actor}{은/는} 천천히 뒤를 돌아 거실을 훑었다. 낮은 소파, 접힌
  의자, 닫힌 문. 그 높이에 무게를 실을 수 있는 것은 없었다.

  "누구야."

  목소리가 벽에 부딪혀 내려앉았다. {actor}{은/는} 다시 창문으로
  고개를 돌렸다. 안개가 유리를 타고 미세하게 흘러내렸다.
  손자국은 그 자리에 있었다.

resolution:
  mode: deterministic

  outcome_text: |
    {actor}{은/는} 잠시 그 자리에 서 있다가 부엌으로 걸어갔다.
    손자국은 뒤에 남았다.

  effects:
    stat_delta:
      "{actor}.스트레스": +1
    resource_delta: ~
    flags_emit:
      - Flag_Memory_{actor}_Saw_Fog_Marks

shirley_jackson_axes:
  primary: 공간의_악의
  secondary: 일상의_배신
  notes: |
    아지트가 밤새 생존자들을 헤아렸다는 뉘앙스.
    안쪽 유리면의 손자국 — 가장 물리적인 현상 하나가
    닿을 수 없는 위치에 있다는 사실만으로 공간의 의도를 암시.