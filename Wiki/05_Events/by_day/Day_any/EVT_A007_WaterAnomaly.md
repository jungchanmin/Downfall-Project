---
id: EVT_A007_WaterAnomaly
title: 삼켜진 질감
type: event
status: complete
summary: >
  레이첼이 아침 루틴 중 주방에서 물을 마시다가 끈적하고 시큼한 
  이상 질감을 인지하고 강박적으로 삼켜낸 뒤, 잔을 내려놓자 
  다시 평범한 물로 돌아와 있는 것을 목격하는 아지트 단독 돌발 이벤트.
tags:
  - event
  - track_a
  - F3_Internal
  - day_any
  - Loc_아지트_주방
keywords:
  - 주방
  - 레이첼
  - 물
  - 이상질감
  - 헛구역질
depends_on:
  - LORE_CHAR_Rachel_Lopez
  - SYS_EVT_Template_v2_Spec
emits:
  - Flag_Memory_Rachel_WaterAnomaly
  - Flag_Trace_Rachel_TasteDistortion
  - Flag_Trace_Rachel_Nausea_Morning
last_updated: 2026-05-27
---

event_meta:
  id: EVT_A007_WaterAnomaly
  track: A
  family: F3_Internal
  phase: 아침
  location: Loc_아지트_주방
  weight: 1.0

trigger:
  all:
    - phase: 아침
    - location: Loc_아지트_주방
    - day: { gte: 1 }
    - any:
        - stat: { actor: "Rachel", 스트레스: { gte: 1 } }
        - day: { gte: 3 }
    - not: { flag: Flag_Memory_Rachel_WaterAnomaly }

narration: |
  싱크대 상판의 스테인리스 표면 위로 아침의 날선 성에가 얇게 가라앉아 있었다. 레이첼은 주방 안쪽의 한기를 느끼며 수도꼭지의 레버를 왼쪽으로 돌렸다. 배관을 타고 올라온 물줄기가 투명한 유리잔 바닥을 때리며 빠르게 차올랐다. 거실 쪽에서 다른 생존자들이 서성이는 발소리와 낮은 대화 소리가 문틈으로 가깝게 흘러들었다. 

  레이첼은 잔을 들어 올려 목구멍 안쪽으로 물을 밀어 넣었다.

  입술에 닿아 식도를 타고 흘러드는 순간, 레이첼의 미간이 좁아졌다. 눈으로 확인했던 투명함과 달리, 혀끝을 비틀며 밀려든 것은 찐득하게 뭉쳐진 젤리 형태의 점액질이었다. 덩어리진 질감이 목구멍을 꽉 압착해 들어왔고, 뒤이어 비강을 타고 썩은 과일 같은 시큼한 체취와 비릿한 맛이 훅 끼쳤다. 

  "읍,"

  당황한 그녀의 손가락이 순간적으로 느슨해지며 유리잔이 미끄러졌다. 잔이 바닥으로 떨어지기 직전, 레이첼은 본능적으로 손가락에 힘을 주어 컵을 낚아챘다. 왈칵 쏟아질 뻔한 액체가 잔 가장자리까지 출렁였다. 

  그녀는 숨을 멈췄다. 뱉어내야 마땅한 상황이었지만, 레이첼은 이를 악물고 턱근육을 굳혔다. 거부 반응으로 위장이 뒤틀리는 것을 억누르며, 그녀는 컵을 쥔 오른손 손가락 마디가 하얗게 질릴 정도로 유리잔을 움켜쥐었다. 그리고는 끈적이는 덩어리를 목구멍 뒤로 억지로 삼켜내기 시작했다. 목줄기가 기괴하게 꿀렁였다. 그녀는 마지막 한 방울의 점액이 식도를 완전히 통과할 때까지 턱을 멈추지 않았다.

resolution:
  mode: stat_check
  check:
    stat: 정신력
    dc: 12
    modifiers:
      - condition: { trait: { actor: "Rachel", trait: "Trait_비정상적_침착함" } }
        bonus: +2

  on_success:
    narration: |
      마지막 목 넘김이 끝나는 순간, 레이첼은 격렬한 헛구역질을 하며 싱크대 모서리를 거칠게 붙잡았다. 위장이 뒤틀리는 압박감에 다친 왼쪽 발목으로 순간 체중이 쏠졌고, 둔탁한 통증이 척추를 찔렀다. 

      그녀가 거친 호흡을 고르며 잔을 내려놓았을 때, 유리잔 바닥에 남은 액체는 투명하고 평범한 물이었다. 싱크대 상판을 짚은 손가락의 미세한 떨림을 움켜쥔 레이첼은 입술을 거칠게 닦아낸 뒤, 아무 일도 없었다는 듯 주방 문을 열고 걸어 나갔다.
    stat_delta:
      "Rachel.스트레스": +1
      "Rachel.허기": -1
    flags_emit:
      - Flag_Memory_Rachel_WaterAnomaly
      - Flag_Trace_Rachel_Nausea_Morning

  on_fail:
    narration: |
      잔을 겨우 비워냈음에도 목구멍 안쪽에 달라붙은 끈적한 느낌은 사라지지 않았다. 레이첼은 타액을 연거푸 삼켜보았지만, 비강을 메운 시큼한 냄새는 오히려 혀뿌리를 타고 더 깊숙이 번져 나갔다. 이미 정체 모를 덩어리가 신체 내부로 파고들었다는 감각이 불쾌한 닻처럼 뇌리에 박혔다. 

      허탈하게 내려놓은 유리잔 바닥에는 정상적인 물방울만이 고여 있었지만, 그 투명한 수면 위로 초점을 잃고 기괴하게 일렁이는 자신의 눈동자가 반사되어 있었다. 레이첼은 한참 동안 그 잔을 바라보며 움직이지 못했다.
    stat_delta:
      "Rachel.스트레스": +2
      "Rachel.정신력": -2
      "Rachel.허기": -1
    flags_emit:
      - Flag_Memory_Rachel_WaterAnomaly
      - Flag_Trace_Rachel_TasteDistortion

shirley_jackson_axes:
  primary: 신경증적_투사
  secondary: 일상의_배신