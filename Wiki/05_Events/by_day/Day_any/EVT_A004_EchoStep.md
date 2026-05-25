---
id: EVT_A004_EchoStep
title: 한 박자 늦은 발소리
type: event
status: complete
summary: >
  아침 순찰 중 레이첼이 복도에서 자신의 발소리를
  정확히 한 박자 늦게 따라오는 정체불명의 소리를
  감지하는 아지트 단독 돌발 이벤트.
  탐색 판정에 따라 소리의 규칙을 읽어내거나
  끝내 잡지 못하고 불안을 안은 채 순찰을 마침.
tags:
  - event
  - track_a
  - F2_Atmosphere
  - day_any
  - Loc_아지트_복도_B6
keywords:
  - 복도
  - 레이첼
  - 발소리
  - 순찰
  - 마룻바닥
  - 엇박자
depends_on:
  - LORE_CHAR_Rachel_Lopez
  - SYS_EVT_Template_v2_Spec
emits:
  - Flag_Memory_Rachel_EchoStep
  - Flag_Trace_Rachel_CorridorUnease
  - Flag_Trace_Rachel_EchoAnalysis
  - Flag_Trace_Rachel_EchoMissed
last_updated: 2026-05-21
---

event_meta:
  id: EVT_A004_EchoStep
  track: A
  family: F2_Atmosphere
  phase: 아침
  location: Loc_아지트_복도_B6
  weight: 1.0

trigger:
  all:
    - phase: 아침
    - location: Loc_아지트_복도_B6
    - day: { gte: 2 }
    - any:
        - stat: { actor: "Rachel", 스트레스: { gte: 1 } }
        - day: { gte: 4 }
    - not: { flag: Flag_Memory_Rachel_EchoStep }
    - not: { event_history: { id: EVT_A004_EchoStep,
        within_days: 7 } }

narration: |
  복도를 걸을 때마다 발밑에서 삐걱, 삐걱하는 낡은 마룻바닥 소리가났다. 
  일정한 간격으로 켜진 촛대 불빛을 지나칠 때마다 벽에 비친 레이첼의 그림자도 보폭에 맞춰 길어졌다 짧아졌다를 반복했다.
  레이첼은 습관처럼 검을 늘어뜨리고 바닥을 툭툭, 건드리며 걸음을 이어갔다.
  그때까지는, 여느덧 반복하던 평범한 아침 순찰과 다를바가 없었다.

  세 걸음쯤 걸었을 때였다.

  탁.

  레이첼이 왼쪽 발을 내딛는 순간, 바로 뒤에서 정확히 한 박자 늦게 똑같은 발소리가 났다. 
  메아리같은 벽에 부딪혀서 반사된 소리가 아니었다. 
  그 소리는 그녀의 발뒤꿈치 바로 뒤에서 마룻바닥을 짓누르는 생생한 마찰음이 분명했다.

  레이첼은 서늘한 감각을 느끼며 의도적으로 뚝, 걸음을 멈췄다. 
  그러자 등 뒤의 소리도 거짓말처럼 동시에 딱 멈췄다. 
  레이첼은 고개를 휙 돌려 그녀의 뒤를 매섭게 노려보면서 누가 장난치는건지 확인하려 했으나,
  그녀의 눈앞에는 굳게 닫힌 문들과 텅 빈 어두운 복도 외에는 아무것도 보이지 않았다.

  그녀는 대충 늘어뜨렸던 검자루를 고쳐쥐었다. 
  손목에 힘이 들어가며 검 날이 수평으로 곧게 섰다. 
  적이 당장이라도 튀어나올것 같은 불길한 감각이 스쳐지나가며, 그녀는 목덜미에 식은땀을 흘렸다.
  본능적으로 왼발을 내딛으며 자세를 취할 때, 예전에 다쳤던 왼쪽 발목이 시큰거리며 통증을 뱉었다. 
  습관처럼 거리를 재려 검 끝을 정면으로 겨누었지만, 겨눌 대상 자체가 없으니 거리를 얼마나 둬야 할지조차 계산할 수가 없었다. 
  레이첼은 쿵쾅거리는 심장 소리를 들키지 않기 위해 턱을 당긴 채로
  숨을 길게 들이쉬고 내뱉었다. 
  "후우, 하아." 
  복도에는 다시 지독한 고요만 남았다.

resolution:
  mode: stat_check
  check:
    stat: 탐색
    dc: 11
    modifiers:
      - condition: { trait: { actor: "Rachel",
          trait: "Trait_변형된_펜싱_룰" } }
        bonus: +3
      - condition: { trait: { actor: "Rachel",
          trait: "Trait_비정상적_침착함" } }
        bonus: +1
      - condition: { stat: { actor: "Rachel",
          피로도: { gte: 5 } } }
        bonus: -2

  on_success:
    narration: |
      레이첼은 자세를 낮춘 채 한참 동안 복도를 집어삼킨 어둠 속을 노려보며 대치했지만, 여전히 아무런 움직임도 포착되지않았다. 
      그녀는 마른침을 삼키고 다시 고개를 돌려 앞으로 발걸음을 옮겼다.

      삐걱. 그녀가 발을 옮긴 반 박자 뒤에, 등 뒤에서 아까와 똑같은 발소리가 찰거머리처럼 따라붙었다.

      레이첼은 이 정체 모를 소리의 정체를 알아내기 위해 일부러 걷는 속도를 확 올렸다. 타다닥,
      마루를 거칠게 디디며 뛰다시피 나아가자 등 뒤의 발소리도 가속도가 붙으며 똑같이 빨라졌다.
      이번에는 가던 걸음을 강제로 멈추고 아주 느릿하게 발을 길게 끌었다. 
      스으윽. 
      그러자 뒤에 있는 무언가도 귀신같이 타이밍을 맞춰 똑같이 비죽하게 발을 끌었다. 
      정확히 반 박자 늦은 엇박자로. 
      철저하게 그녀의 걸음의 템포를 관음하며 장난을 치고 있었다.

      레이첼은 더 이상 뒤를 돌아보지 않기로 했다. 
      보이지 않는 소리를 이해할 수 없는 이상현상으로 규정하고, 앞으로 나아갔다.
      온 신경을 곤두세우고 등 뒤에서 쫓아오는 발소리의 섬뜩한 울림을 하나하나 귀로 새기면서, 복도 끝을 향해 흔들림 없이 걸어 나갔다. 
      마침내 복도 끝 문턱을 넘어 완전히 빠져나오는 순간, 질척하게 쫓아오던 발소리가 단칼에 잘린 듯 뚝 끊겼다.

      레이첼은 복도 입구에 멈춰 서서 지나온 길을 다시 한번 돌아보았다. 
      촛대 불빛만 번뜩이며 깜빡일 뿐, 여전히 텅 빈 통로가 덩그러니 놓여있었다. 
      그녀는 어느덧 차갑게 식은 옷깃을 손으로 여미며 나직하게 숨을 뱉었다.
    stat_delta:
      "Rachel.스트레스": +1
    flags_emit:
      - Flag_Memory_Rachel_EchoStep
      - Flag_Trace_Rachel_CorridorUnease
      - Flag_Trace_Rachel_EchoAnalysis

  on_fail:
    narration: |
      레이첼은 뚝 걸음을 멈추고 휙 뒤를 돌아보았다.

      복도 양옆의 문들을 하나하나 짚어가며 범인을 찾으려 눈을 부릅떴지만, 흔들리는 촛대 그림자 외에는 복도에 개미 한 마리 보이지 않았다.
      레이첼은 소리라도 지르고 싶은 심정이었지만, 아랫입술을 지그시 깨물고 다시 앞을 향해 힘차게 발을 내디뎠다.

      하지만 이번에는 아무리 귀를 기울여도 등 뒤에서 아무 소리도 나지 않았다. 
      평소와 똑같이 혼자서 걷을때 났던 마룻바닥 소리만 복도에 둔탁하게 울릴뿐이었다. 
      이상한 발소리가 완전히 사라지자, 오히려 발소리의 주인이 언제 어디서 덮칠지 모른다는 생각에 신경이 날카롭게 곤두섰다.

      소리가 완전히 멈춘 것인지, 아니면 놈이 소리만 죽인 채 바로 뒤통수까지 바짝 따라붙은 것인지 도무지 판별할 방법이 없었다. 
      결국 순찰을 마치고 복도를 완전히 빠져나왔지만, 보이지 않는 눈이 아침 내내 그녀의 등 뒤를 뚫어져라 쳐다보는
      것 같은 서늘한 한기가 가시질 않았다. 
      레이첼은 연신 느껴지는 불길하고 오싹한 시선이 느껴졌지만, 마주보기가 두려워서 차마 고개를 돌려서 뒤를 확인할 수가 없었다. 
      차가운 아침 안개가 그녀의 떨리는 어깨 위로 비정하게 들이치고 있었다.
    stat_delta:
      "Rachel.스트레스": +2
    flags_emit:
      - Flag_Memory_Rachel_EchoStep
      - Flag_Trace_Rachel_CorridorUnease
      - Flag_Trace_Rachel_EchoMissed

shirley_jackson_axes:
  primary: 공간의_악의
  secondary: 신경증적_투사