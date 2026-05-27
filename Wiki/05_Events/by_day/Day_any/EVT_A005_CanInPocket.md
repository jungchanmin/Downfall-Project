---
id: EVT_A005_CanInPocket
title: 품속의 통조림
type: event
status: complete
summary: >
  아침 배급 준비 중 레이첼이 어제 저녁 먹었다고
  확신하는 통조림이 개봉 흔적 없이 훈련복 품속에
  그대로 들어있음을 발견하는 아지트 주방 단독
  돌발 이벤트. 정신 판정에 따라 통조림을 확인하고
  서랍에 돌려놓거나, 확인하지 못하고 품속에
  은닉한 채 자신의 배급을 건너뜀.
tags:
  - event
  - track_a
  - F5_Cosmic
  - day_any
  - Loc_아지트_주방_B4
keywords:
  - 주방
  - 레이첼
  - 통조림
  - 기억붕괴
  - 배급
  - 식량
depends_on:
  - LORE_CHAR_Rachel_Lopez
  - SYS_EVT_Template_v2_Spec
  - MECH_Resource_System
emits:
  - Flag_Memory_Rachel_CanInPocket
  - Flag_Trace_Rachel_MemoryDoubt
  - Flag_Trace_Rachel_CanReturned
  - Flag_Trace_Rachel_CanKept
last_updated: 2026-05-21
---

event_meta:
  id: EVT_A005_CanInPocket
  track: A
  family: F5_Cosmic
  phase: 아침
  location: Loc_아지트_주방_B4
  weight: 1.0

trigger:
  all:
    - phase: 아침
    - location: Loc_아지트_주방_B4
    - day: { gte: 3 }
    - any:
        - stat: { actor: "Rachel", 스트레스: { gte: 1 } }
        - day: { gte: 5 }
    - flag: Flag_Daily_Ration_Received_Yesterday
    - flag: Flag_Daily_Ration_Phase_Active
    - not: { flag: Flag_Memory_Rachel_CanInPocket }
    - not: { event_history: { id: EVT_A005_CanInPocket,
        within_days: 99 } }

narration: |
  레이첼은 냉장고 옆에 비치된, 식량 보관 서랍 앞에 서서 상체를 숙였다. 
  조금 탄 냄비와 살짝 녹슨 주방용 칼 세트가 주방 선반 위에서 아침의 희미한 햇빛을 받아먹으며 약간의 거품과 함께 물속에 가라앉아 있었다. 그녀는 오른손 검지를 내밀어 리더가 배분하기로 결정한 서랍 속 통조림들의 윗면을 하나씩 누르며 개수를 세기 시작했다. 
  하나, 둘, 셋... 어제 저녁에 서랍을 닫으며 확인했던 개수와 오늘 아침의 숫자가 정확히 일치하는지 확인하기 위해 단순한 작업임에도, 신경을 기울였다. 
  매일 분배될 식량에 대한 확인 루틴은 그녀에게 하루를 시작할때 조금이나마 안심이 되곤 했다.

  네 번째 통조림을 향해 손가락을 뻗으려던 순간, 상체를 약간 비틀자 훈련복 안쪽 주머니가 아래로
  묵직하게 처지며 그녀의 가슴팍을 가볍게 때렸다. 
  평소보다 무거운 감각에 레이첼은 오른손을 훈련복 안으로
  밀어 넣었다. 
  손가락 끝에 딱딱하고 차가운 금속 표면이 닿았다.

  그녀는 주머니 속의 정체불명의 물건을 꺼내 손바닥 위에 올려놓았다.

  어제 저녁, 숟가락으로 내용물을 싹싹 긁어먹었던 바로 그 통조림이었다. 
  입안에 감돌던 맛과 온도, 숟가락이 철판을 긁던 감촉의 기억이 머릿속에 이토록 선명한데, 손 위에 놓인 통조림의 뚜껑은
  단 한 번도 개봉된 적이 없는 것처럼 매끄럽게 밀봉되어 있었다.

  통조림을 쥔 오른손 손가락이 하얗게 질릴 정도로 힘이 들어갔다. 
  생생한 기억과 눈앞에 실재하는 묵직한 통조림 중 어느 쪽이 진짜인지 알 수 없었다.
  그녀는 평생 자신의 기억을 의심한 적이 없었다. 
  그러나, 눈앞에 벌어진 현실은 이미 일어났던 사실을 정면으로 부인하고 있었다.
  그녀는 초조하게 입술을 깨물며, 방금 벌어진 이해할 수 없는 일을 이해하려고 애썼다.

resolution:
  mode: stat_check
  check:
    stat: 정신력
    dc: 12
    modifiers:
      - condition: { trait: { actor: "Rachel",
          trait: "Trait_비정상적_침착함" } }
        bonus: +2
      - condition: { trait: { actor: "Rachel",
          trait: "Trait_변형된_펜싱_룰" } }
        bonus: +1
      - condition: { flag: { actor: "Rachel",
          flag: "Flag_Past_Rachel_Career_Broken" } }
        bonus: -1
      - condition: { stat: { actor: "Rachel",
          스트레스: { gte: 4 } } }
        bonus: -2

  on_success:
    narration: |
      레이첼은 손바닥 위의 통조림을 창문으로 들어오는 아침 빛 쪽으로 바짝 가져갔다. 
      뚜껑의 접합부를 손톱 끝으로 한 바퀴 돌려가며 확인했으나, 찌그러지거나 틈이 벌어진 흔적은
      전혀 없었다. 
      하단에 찍힌 제조일자 조차도 어제 저녁 자신이 먹었던 제품의 날짜와 정확히 일치했다.

      원통형 몸체를 한 바퀴 돌려 쥐었을 때, 측면에 날카로운 칼끝으로 긁어둔 작은 십자 모양의 표식이 빛에 반사되어 눈에 들어왔다. 
      그녀는 통조림을 먹을때, 강박적으로 이러한 표시를 남겨두는 버릇이 있었고, 이건 기억상 어제 오후에 직접 새겨 넣은 흔적이었다.

      다른 통조림일 가능성은 없었다.
      내 손으로 새긴 표식이 선명하게 살아있는데도 철판은 뜯겨지지 않았고, 통조림은 묵직했다.

      레이첼은 통조림을 서랍 안쪽 구석에 천천히 내려놓았다. 
      다시 작업을 재개한 그녀는 서랍 속 다른 식량들을 개수를 맞추어 꺼내며 생존자들을 위한 아침 배급 체크를 차분하게 이어 나갔다.
      그녀는 아무런 망설임 없이 자신의 몫으로 배당된 통조림 한 통도 정상적으로 챙겨 들었다. 
      주방을 나가기 직전, 레이첼은 문턱 앞에서 발걸음을 망설이다 돌아서서 그 통조림이 들어있는 식량 보관 서랍을 다시 한번
      스으윽 열었다. 
      그러나 곧 그녀는 서랍 안을 확인하지 않고 재빨리
      쾅 밀어 닫았다. 
      굳게 닫힌 철제 서랍의 모습은 지극히도 평온했다.
    stat_delta:
      "Rachel.스트레스": +2
      "Rachel.정신력": -1
    flags_emit:
      - Flag_Memory_Rachel_CanInPocket
      - Flag_Trace_Rachel_MemoryDoubt
      - Flag_Trace_Rachel_CanReturned

  on_fail:
    narration: |
      레이첼은 꺼내 든 통조림을 거머쥔 채 먼지가 가라앉은 주방 바닥 위에 한참 동안 서 있었다.
      빛이 드는 쪽으로 손을 뻗어 그 통조림의 상태를 제대로 확인하려다가, 그녀는 손을 허공에서 뚝, 멈췄다.

      확인하는 순간 어느 쪽이 거짓말을 하고 있는지 확실해질게 자명했다. 
      만약 통조림이 완벽한 상태이고, 어제 먹었다고 착각했다는 사실을 확신한다면.
      그녀는 더 이상 자신의 기억을 믿을 수 없게 될지도 몰랐다.

      레이첼은 고개를 살짝 젓고는, 통조림을 훈련복 안쪽 주머니 깊숙한 곳에 다시 밀어 넣었다.

      그녀는 서랍을 뒤적여 다른 생존자들의 몫을 정량대로 꺼내기 시작했다. 
      주방 서랍에서 배급용의 식량을 정리하는 동안, 자신의 이름 앞으로 가야 할 몫은 다시 집어넣었다. 
      다른 이들의 식량이 도마 위에 질서정연하게 정렬되는 동안
      그녀의 몫이 있어야 할 자리는 공백으로 남았다.
      모든 할 일을 마친 레이첼이 식량 상자를 들어올리고, 주방을 빠져나갔다. 
      방을 나서서 걸어가는 그녀의 뒷모습은 살짝 비틀거렸다.
      그녀가 걸음을 옮길 때마다 훈련복 안감에 부딪히며 가슴팍을 무겁게 짓누르는 통조림의 무게감이 선명하게 따라붙었다.
    stat_delta:
      "Rachel.스트레스": +1
      "Rachel.정신력": -1
      "Rachel.허기": -1
    flags_emit:
      - Flag_Memory_Rachel_CanInPocket
      - Flag_Trace_Rachel_MemoryDoubt
      - Flag_Trace_Rachel_CanKept

shirley_jackson_axes:
  primary: 일상의_배신
  secondary: 신경증적_투사