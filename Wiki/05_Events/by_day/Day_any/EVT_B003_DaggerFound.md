---
id: EVT_B003_DaggerFound
title: 먼지 없는 단검
type: event
status: complete
summary: >
  아침 장비 점검 중 레이첼이 작은 다락방 잡동사니 속에서
  먼지 없이 깨끗한 이계의 단검을 발견하고, 리더에게
  보고할지 숨길지 선택하는 아지트 단독 돌발 이벤트.
  숨기면 유물 귀속·패널티 활성화, 보고하면 단검과
  기억이 동시에 소멸하는 분기.
tags:
  - event
  - track_b
  - F5_Cosmic
  - day_any
  - Loc_아지트_작은다락방_C5
keywords:
  - 작은다락방
  - 레이첼
  - 단검
  - 유물
  - 대제사장
  - 기억소멸
  - 이계
depends_on:
  - LORE_CHAR_Rachel_Lopez
  - SYS_EVT_Template_v2_Spec
  - ITEM_Relic_DB
emits:
  - Flag_Memory_Rachel_DaggerFound
  - Flag_Item_HighPriestDagger_Owned
  - Flag_Item_HighPriestDagger_Reported
  - Flag_Trace_Rachel_DaggerObsession
  - Rel_Rachel_Leader_Trust_Up
last_updated: 2026-05-21
---

event_meta:
  id: EVT_B003_DaggerFound
  track: B
  family: F5_Cosmic
  phase: 아침
  location: Loc_아지트_작은다락방_C5
  weight: 1.0

trigger:
  all:
    - phase: 아침
    - location: Loc_아지트_작은다락방_C5
    - day: { gte: 2 }
    - any:
        - stat: { actor: "Rachel", 스트레스: { gte: 1 } }
        - day: { gte: 5 }
    - not: { flag: Flag_Memory_Rachel_DaggerFound }
    - not: { flag: Flag_Item_HighPriestDagger_Owned }
    - not: { event_history: { id: EVT_B003_DaggerFound,
        within_days: 99 } }

intro_narration: |
  낮은 천장 아래로 뽀얗게 가라앉은 아침 먼지가
  다락방의 희박한 햇빛 속에서 유령처럼 떠돌고
  있었다. 레이첼은 허리를 잔뜩 숙인 채 구석에
  쌓인 잡동사니들을 뒤적거리고 있었다. 그녀는
  흩뿌려지는 먼지에 연신 콜록대면서도, 쉬지 않고
  낡은 철제 상자들을 계속 열어젖혔다.

  구석의 천 덮개를 거칠게 들어 올렸을 때,
  엉망진창인 먼지 더미 속에서 기이하게 깨끗한
  단검 한 자루가 모습을 드러냈다. 방금 닦아낸 듯
  투명한 광택을 내는 칼날 위에는 시계 부품의
  정밀한 부속품들처럼 정교하게 맞물린 기하학적
  무늬들이 새겨져 있었다. 주변의 온갖 고물들에
  두껍게 먼지가 앉은 것과 대조적으로, 오직 그
  단검만이 먼지나 더러운 자국 없이 매끄럽고 신비한 광택을 뿜어냈다.

  레이첼은 손을 뻗어 단검의 손잡이를 움켜쥐었다.
  손바닥으로 차가운 금속의 냉기가 묵직하게
  배어들었다. 그녀는 멍하니 입을 벌린 채로,
  뚫어져라 단검을 한참이나 응시했다. 
  그녀의 단검을 쥐고 있는 손가락 끝에서부터, 묘한 만족감과 기쁨이 솟아올랐다.  
  그녀의 뇌리에는 리더에게 보고하고 싶지 않다, 이 단검을 가져야만 한다라는 충동이 폭발하고 있었다. 
  단검을 누군가 다른 사람에게 들키기라도 하면 큰일이 날것처럼, 그녀는 소중하게 단검을 감싸쥐고 훈련복
  안쪽 깊은곳에 숨겼다. 단검을 쥔 손끝이 바들바들 떨렸다.

choices:
  - id: ch1
    label: "챙긴다"
    resolution:
      mode: deterministic
      narration: |
        무의식적으로 손가락의 근육들이 먼저 움직여 결정을
        내렸다. 레이첼은 단검의 차가운 칼날을 속옷
        안감 사이, 맨 가슴에 닿을때까지 더더욱 깊숙히 밀어 넣었다. 
        살갗에 직접 닿아오는 금속의 냉기가 서늘하게 그녀의 가슴에 퍼져나갔다.
        다락방을 빠져나가기 위해 발걸음을 옮기는 순간, 마치 경고라도 하는 것처럼 왼쪽 발목에서 시큼한 통증이
        찌르듯 밀려왔다. 레이첼은 한 손으로 먼지 묻은 벽을 짚으며 평소보다 극도로 조심스럽고 부자연스러운
        템포로 발걸음을 옮겼다. 
        다락방 문을 열고 나갈때, 그녀는 가슴의 연한 살갗을 단검이 베어낸 것을 전혀 눈치채지 못했다.
        다만 가슴팍 안쪽에서 자신의 피와 체온을 마시며 기이하게 달아오르는 단검의 감촉과 거기서 쏟아지는 열락과 정체모를 희열감에 혼미해질 정도로 취해있었다.
      stat_delta:
        "Rachel.탐색": +1
        "Rachel.기술": +1
        "Rachel.매력": +1
        "Rachel.지능": +1
      relic_acquire:
        id: RELIC_HighPriestDagger
        bound_to: "Rachel"
        daily_penalty_active: true
      flags_emit:
        - Flag_Memory_Rachel_DaggerFound
        - Flag_Item_HighPriestDagger_Owned
        - Flag_Trace_Rachel_DaggerObsession

  - id: ch2
    label: "보고한다"
    resolution:
      mode: deterministic
      narration: |
        레이첼은 결심을 굳히고, 단검을 쥔 채 다락방을 내려와 리더의 방 문을 열었다. 
        그녀는 잠깐 망설이다가, 말없이 팔을 뻗어 단검을 리더의 눈앞에 내밀었다. 
        리더는 당황했지만, 곧 리더는 손을 내밀고 단검의 자루를 건네받았다. 
        그리고 두 사람 사이에 지독한 침묵이 내려앉았다.
        레이첼은 리더를 응시하며 입술을 가볍게 벌렸으나, 
        무슨 말을 하려 했는지 기억이 전혀 나지 않았다. 뭔가 여기 왔던 중요한 이유가 있었던 것같은데, 라고 생각하며 리더의 말을 기다렸다. 
        리더 역시 자신의 구부러진 손바닥에 무언가를 쥐고 있었던 것 같은데,
        손안에는 아무것도 없이, 텅비어있음을 눈치채고 고개를 갸웃거렸다.
        두 사람은 아무런 말도 하지 못한 채 서로의 말을 기다리며 초점을 잃은 눈동자로 서로를 멀뚱히 마주 보았다. 
        방 안 어디에도 중요했던 무언가는 존재하지 않았다. 이제와서는, 왜 여기 있는지도 몰랐다.
        "리더."
        침묵을 깨는 그녀의 작은 말에, 리더는 연신 주먹을 쥐었다 피던 것을 멈추고 그녀의 입술을 응시했다.
        "무슨 일이야? 아니. 언제부터 와있었어? 뭔가 중요한 용건이 있었던 것 같은데."
        "아니에요. 아무 일도 없었어요."
        레이첼은 여전히 혼란스러워하며 돌아섰고, 리더는 헛웃음을 터뜨리며 그녀를 배웅했다.
      stat_delta:
        "Rachel.스트레스": -1
        "Rachel.친밀도": +1
      flags_emit:
        - Flag_Memory_Rachel_DaggerFound
        - Flag_Item_HighPriestDagger_Reported
        - Rel_Rachel_Leader_Trust_Up

shirley_jackson_axes:
  primary: 일상의_배신
  secondary: 신경증적_투사