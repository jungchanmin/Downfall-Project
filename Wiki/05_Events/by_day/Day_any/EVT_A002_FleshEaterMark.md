---
id: EVT_A002_FleshEaterMark
title: 놈은 아침을 알았다
type: event
status: complete
summary: >
  아침 훈련 루틴 중 레이첼이 자신의 보폭과 정확히
  일치하는 간격으로 훈련 동선 위에 새겨진 U.H-028의
  표식을 발견하고, 사냥감으로 지목되었음을 인지하는
  아지트 수영장 인근 단독 돌발 이벤트.
  정신 판정에 따라 투지 발현 또는 강박 균열로 분기.
tags:
  - event
  - track_a
  - F4_Encounter
  - day_any
  - Loc_아지트_수영장_A5
keywords:
  - 수영장
  - 레이첼
  - 표식
  - 살점포식자
  - UH028
  - 선공권
  - 훈련동선
depends_on:
  - LORE_CHAR_Rachel_Lopez
  - SYS_EVT_Template_v2_Spec
  - BESTIARY_UH028
emits:
  - Flag_Memory_Rachel_FleshEaterMark
  - Flag_Lore_UH028_Rachel_Targeted
  - Flag_Trace_Rachel_HuntingInstinct
  - Flag_Trace_Rachel_PatternAnxiety
last_updated: 2026-05-21
---

event_meta:
  id: EVT_A002_FleshEaterMark
  track: A
  family: F4_Encounter
  phase: 아침
  location: Loc_아지트_수영장_A5
  weight: 1.0

trigger:
  all:
    - phase: 아침
    - location: Loc_아지트_수영장_A5
    - day: { gte: 3 }
    - any:
        - stat: { actor: "Rachel", 스트레스: { gte: 2 } }
        - day: { gte: 7 }
    - not: { flag: Flag_Memory_Rachel_FleshEaterMark }
    - not: { flag: Flag_Encounter_UH028_Active }
    - not: { event_history: { id: EVT_A002_FleshEaterMark, within_days: 99 } }

narration: |
  아지트 수영장 인근의 축축한 석판 위로 서늘한 아침
  안개가 무겁게 깔려 있었다. 밤새 잠들지 못해 피로가
  고인 눈을 치켜뜬 레이첼은 손에 익숙한 펜싱 검을
  쥔 채, 피스트의 선을 그리듯 매일 반복하던 훈련
  동선 위에 섰다. 그녀의 시선은 정면의 빈 허공을
  응시했고, 호흡은 어느새 냉정하고 침착하게 가라앉아 있었다.

  첫 번째 마르셰(Marcher) 스텝을 밟기 위해 오른발
  구두 끝을 앞으로 길게 미끄러뜨린 순간, 무언가 이상함을 눈치챈 레이첼의
  시선이 바닥을 스쳐서 지나갔다. 정확히 구두
  굽이 내려앉으려는 석판 정중앙에 기하학적으로
  정밀하면서도, 거칠게 깎여 나간 문양이 새겨져 있었다. 단순한
  괴물이나 짐승이 우연히 냈을 법한 발톱 자국이 아니었다. 날카로운 도구로 정확한
  각도를 계산해 파내려간 무언가의 서명과도 비슷했다. 연이어 한 걸음
  더 나아가 롱제(Fente) 자세를 취하려던 그녀의
  발끝이 다시 멈췄다. 두 번째 스텝 위치에도, 세 번째
  스텝 위치에도, 그녀만이 알고 있는 아침 훈련 동선의
  궤적을 정확히 따라 문양들이 완전히 같은 방식으로 새겨져
  있었다.

  레이첼은 더 이상 훈련을 지속할 수 없었다. 그녀는 무릎을 굽혀 바닥에 새겨진 표식과 자신의
  보폭 간격을 수평으로 비교했다. 정확히 일치했다.
  1밀리미터의 오차도 없이 그녀의 보폭을 그대로
  복제해 둔 정밀한 무언가의 사인을 보았더니, 왼쪽 발목에서 익숙한 통증이 다시금 느껴졌다.
  어떠한, 자신을 음침하게 지켜본 놈이 먼저 거리를 재고 선공권
  (Right of way)을 가져갔다는 인식이 뇌리에 난폭하게
  파고들었다. 이 아지트, 깊숙한 안전가옥까지 들어와 그녀의
  아침을 관찰하고, 보폭을 측정하고, 오직 혼자 남은
  이 타이밍을 계산해 둔 존재가 프레임 바깥의 어둠
  속에 도사리고 있다는 본능적 경고였다. 레이첼은
  입술을 꽉 깨물면서, 폭발할 것 같은 심장소리를 강제로
  낮추기 위해 연신 숨을 들이켜고 내쉬며 침착하려고 애썼다.
  펜싱검 날의 단면은 아침 햇빛을 받아 차갑게 번뜩였다.

resolution:
  mode: stat_check
  check:
    stat: 정신
    dc: 10
    modifiers:
      - condition: { trait: { actor: "Rachel",
          trait: "Trait_비정상적_침착함" } }
        bonus: +3
      - condition: { trait: { actor: "Rachel",
          trait: "Trait_변형된_펜싱_룰" } }
        bonus: +2
      - condition:
          all:
            - trait: { actor: "Rachel",
                trait: "Trait_동적_자기파멸욕" }
            - stat: { actor: "Rachel", 스트레스: { gte: 3 } }
        bonus: -2

  on_success:
    narration: |
      검자루를 쥔 레이첼은 오른손 가죽 장갑이 터질 듯이 검을 꽉 감싸 쥐었다.
      놈이 그녀를 관찰하고 분석했다면, 이제부터는
      그녀가 그 궤적을 역추적해 사냥할 차례였다.
      패턴이 읽혔다는 사실은 더 이상 수치심이 아닌,
      전력으로 짓밟아버려야 할 선공권의 탈환으로
      전환되었다. 사냥개를 사냥하려는 맹수도, 그 목을 물어뜯길 준비는 해야했다.
      레이첼은 표식을 짓밟으며 어딘가에서 지켜보고 있을 괴물을 향해 검 끝을 정확한 직선으로
      겨누었다. 검자루를 틀어쥔 손가락 마디마디에
      핏줄이 붉게 융기하며 익숙한 파괴의 감각이
      파괴적으로 끌어올랐다.
    stat_delta:
      "Rachel.스트레스": -1
      "Rachel.전투력": +1
    flags_emit:
      - Flag_Memory_Rachel_FleshEaterMark
      - Flag_Lore_UH028_Rachel_Targeted
      - Flag_Trace_Rachel_HuntingInstinct

  on_fail:
    narration: |
      검자루를 쥐려던 레이첼의 손가락 끝이
      크게 떨렸다. 완벽하게 통제하고 있다고
      믿었던 자신만의 요새와 아침의 루틴이 이미
      놈의 사냥 데이터로 전용되었다는 사실이 인지되는
      순간, 이미 그녀는 패닉에 빠져있었다.
      선공권을 완전히 빼앗겼으며, 그녀의 신체는 정지
      명령을 받은 것처럼 굳어가고 있었다. 도망칠 수도,
      거리를 잴 틈도없이 압도적인 사냥꾼 앞에서는 이미 모든 동작이 계산되어
      있다는 절대적인 절망감이 그녀의 척추를 타고
      흘러내렸다. 레이첼은 검을 손에서 떨어뜨리지
      않기 위해 안간힘을 썼으나, 이내 검자루를 쥔 손목과 손가락이 제어 불능의 상태로
      사정없이 덜덜 떨리기 시작했다.
    stat_delta:
      "Rachel.스트레스": +2
      "Rachel.정신": -1
    flags_emit:
      - Flag_Memory_Rachel_FleshEaterMark
      - Flag_Lore_UH028_Rachel_Targeted
      - Flag_Trace_Rachel_PatternAnxiety

shirley_jackson_axes:
  primary: 공간의_악의
  secondary: 신경증적_투사