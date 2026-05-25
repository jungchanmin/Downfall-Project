---
id: EVT_B004_SilentRequest
title: 삼켜진 말
type: event
status: complete
summary: >
  아침 작전 회의 직전 레이첼이 리더에게 무언가를
  말하려다 끝내 입을 열지 못하는 아지트 거실
  개입형 이벤트. 친밀도에 따라 말을 꺼내거나
  지나치는 선택이 분기되며, 친밀도 높음 시
  리더가 레이첼의 단어를 완성해주는 구조.
tags:
  - event
  - track_b
  - F3_Internal
  - day_any
  - Loc_아지트_거실_B2
keywords:
  - 거실
  - 레이첼
  - 리더
  - 침묵
  - 명령갈구
  - 삼켜진말
  - 친밀도
depends_on:
  - LORE_CHAR_Rachel_Lopez
  - SYS_EVT_Template_v2_Spec
emits:
  - Flag_Memory_Rachel_SilentRequest
  - Flag_Trace_Rachel_WordsUnspoken
  - Flag_Trace_Rachel_LeaderNoticed
  - Flag_Trace_Rachel_PassedBy
  - Rel_Rachel_Leader_Intimacy_Up
last_updated: 2026-05-21
---

event_meta:
  id: EVT_B004_SilentRequest
  track: B
  family: F3_Internal
  phase: 아침
  location: Loc_아지트_거실_B2
  weight: 1.0

trigger:
  all:
    - phase: 아침
    - location: Loc_아지트_거실_B2
    - day: { gte: 3 }
    - any:
        - stat: { actor: "Rachel", 친밀도: { gte: 1 } }
        - day: { gte: 6 }
    - not: { flag: Flag_Memory_Rachel_SilentRequest }
    - not: { event_history: { id: EVT_B004_SilentRequest,
        within_days: 5 } }

intro_narration: |
  아침 작전 회의 직전의 거실은 서늘한 정적으로
  가라앉아 있었다. 리더는 스프링이 튀어나온 낡은
  소파에 앉아 무릎 위에 커다란 지도를 펼쳐두고
  있었다. 거실 입구에 도착한 레이첼은 거실 안으로
  들어서지도, 그렇다고 복도로 물러서지도 않은 채
  문턱 위에 구두 끝을 걸치고 그대로 멈춰 섰다.
  긴장한 그녀는 오른손 손가락 마디마디가 검자루를 틀어쥔채로 단단히 고정하고 있었다.

  무릎 위의 지도를 짚고 있던 리더가 턱을 천천히
  들어 문턱에 멈춰 선 레이첼을 똑바로 응시했다.
  두 사람의 시선이 마주치는 순간, 레이첼이 무언가를 말하려는 듯 입술을 가볍게 벌렸다. 
  그러나 짓눌린 목구멍 너머로 호흡만 가쁘게 맴돌 뿐, 그녀의 어떤 말도 입밖으로 새어 나오지 못했다. 
  짧으면서도 긴 침묵이 이어졌고, 조용한 거실엔 소파 내부의 녹슨 스프링이 길게 삐걱거리는 마찰음만이 둔탁하게 울렸다. 
  벽면에 놓인 꺼진 TV 브라운관의 검은 표면 위로, 미동도 없이 대치한 두 사람의 흐릿한 실루엣이 마주 비춰지고 있었다.

  그녀의 목구멍에서는 단어 한자락조차 내뱉을 수 없었다. 
  레이첼은 오른손 손가락이 하얗게 질려 들어갈때까지, 검자루를 세게 틀어쥐었다. 
  문턱에 우두커니 선채로 대치할동안, 그녀의 어깨는 미세하게 떨렸다.
  분명히 하려고 했던 수많은 말들이 그녀의 가슴에서 맴돌뿐, 입으로는 튀어나오지 않았다.
  대사 한마디 없는 정적 속에서 오직 두 사람의 마주한 시선이 흐를 뿐이었다.

choices:
  - id: ch1
    label: "말을 꺼내려 한다"
    resolution:
      - condition: { stat: { actor: "Rachel",
          친밀도: { lt: 3 } } }
        narration: |
          레이첼은 벌어졌던 입술을 다시 꾹 닫았다. 
          단 한 마디도 하지 못하고, 그녀는 고개를 아주 약간 아래로 숙여 인사하는 것으로 긴 침묵을 끝냈다. 
          리더는 발길을 돌려 멀어지는 그녀에게 말을 걸거나 불러세우지 않았고, 시선을 다시 펼쳐진 지도 위로 떨어뜨렸다. 
          지도가 거칠게 바스락거리는 소리가 거실을 채우는 동안,
          복도의 어둠 속으로 레이첼의 뚜벅뚜벅 걸어가는 소리가 울려퍼졌다.
        stat_delta:
          "Rachel.스트레스": +1
        flags_emit:
          - Flag_Memory_Rachel_SilentRequest
          - Flag_Trace_Rachel_WordsUnspoken

      - condition: { stat: { actor: "Rachel",
          친밀도: { gte: 3 } } }
        narration: |
          레이첼은 침묵을 유지한채로, 리더의 무릎 위에 펼쳐진 종이지도를 향해 시선을 던졌다. 
          그녀는 애절한 눈빛으로, 리더가 다시 자신을 바라봐 주기를 기다렸다. 
          그러나 리더의 시선은 이제 그녀에게서 멀어져 묵묵히 지도 위의 검은 표시선만을 좇고 있을 뿐이었다.
          두 사람의 시선이 철저하게 엇갈리는 정적 속에서 레이첼의 오른손 손가락이 검자루를 한 번 더 굳게 움켜쥐었다.

          그녀가 마른침을 삼키며 간신히 숨을 밀어내면서, 조각난 단어 하나가 그녀의 입술사이로 힘겹게 흘러나왔다.
          "……보내줘."

          짧은 단어가 거실 공기 중으로 흩어질 때, 지도만을 내려다보던 리더의 시선이 다시 그녀에게 향했다. 
          마침내 두 사람의 눈이 똑바로 마주쳤을때, 리더는 그녀에게 답변했다.
          "여기로 널 보내달라고?"

          레이첼은 더 이상 대답하지 않았다. 
          그럴 필요가 없었다.
          굳게 다문 입술과 긴장한 표정사이에 걸친 희미한 미소는 그녀의 복종의 뜻이자 애원이나 다름 없었다. 
          리더는 손가락으로 지도 위의 좌표를 짚어가며 진행해야할 토벌 임무, 자원탐색과 지역탐험 임무에 대해서 자신의 생각을 풀어놓기 시작했다.
          그것을 리더의 명령으로 알아듣고, 레이첼은 비로소 문턱을 넘어 거실에 성큼성큼 들어와 유심히 리더의 말을 경청했다.
        stat_delta:
          "Rachel.스트레스": +1
          "Rachel.친밀도": +1
        flags_emit:
          - Flag_Memory_Rachel_SilentRequest
          - Flag_Trace_Rachel_WordsUnspoken
          - Flag_Trace_Rachel_LeaderNoticed
          - Rel_Rachel_Leader_Intimacy_Up

  - id: ch2
    label: "그냥 지나친다"
    resolution:
      - condition: { stat: { actor: "Rachel",
          친밀도: { lt: 3 } } }
        narration: |
          레이첼은 거실의 문턱을 넘지 않고 그대로 고개를 돌려 어두운 복도 방향으로 발걸음을 옮겼다. 
          소파에 앉은 리더는 지도의 경계선으로 시선을 던진 뒤에 끝내 그녀를 보지 않았고, 두 사람
          사이에는 더이상 시선 교환이 일어나지 않았다. 
          규칙적으로 삐걱거리는 낡은 마룻바닥 소리만이 복도를 걸어 나가는 레이첼의 보폭에
          맞춰 점점 작아지며 사라졌다. 
          아침 순찰을 계속하며 어두운 1층 복도를 길게
          걸어가는 내내, 목구멍 깊은 곳에 딱딱하고
          차가운 쇠붙이가 꽉 걸려 있는 듯한 찝찝하고
          서늘한 압박감이 그녀의 호흡을 아침 내내
          무겁게 짓눌렀다.
        stat_delta:
          "Rachel.스트레스": +1
        flags_emit:
          - Flag_Memory_Rachel_SilentRequest
          - Flag_Trace_Rachel_WordsUnspoken
          - Flag_Trace_Rachel_PassedBy

      - condition: { stat: { actor: "Rachel",
          친밀도: { gte: 3 } } }
        narration: |
          거실 입구를 지나치려던 레이첼의 구두 끝이
          문턱 바로 앞에서 무겁게 멈춰 섰다. 그녀는
          차마 거실 안으로 발을 들이지도 못한 채,
          문틀 옆에 우두커니 서서 소파 위의 리더를
          애타게 바라보았다. 고개를 들어 단 한 번만이라도
          자신을 봐 주기를, 이쪽을 향해 무언가 한마디라도
          던져 주기를 바라는 절박한 시선이었다. 그러나
          리더의 눈길은 굳건하게 무릎 위 지도의 검은
          표시선들에만 고정되어 있었다. 지도를 누른
          가죽 장갑의 미동조차 없는 서늘함 속에서,
          두 사람의 구도는 마치 등을 돌린 채 마주 보지
          못하는 짝사랑하는 연인의 모습처럼 철저하게
          어긋나 있었다.

          레이첼은 검자루를 쥔 손가락 마디가 하얗게
          질리도록 악력만을 쥐어짜다가, 이내 포기한 듯
          나직하게 숨을 뱉으며 어두운 복도를 향해 다시
          발걸음을 내디뎠다. 모퉁이를 돌아 리더의
          실루엣이 시야에서 완전히 가려질 때까지, 등
          뒤에서는 그 어떤 기척도, 불러 세우는 목소리도
          들려오지 않았다. 끝내 시선 한 자락 받지 못했다는
          지독한 허무함과 목구멍을 꽉 죄어오는 압박감이
          복도를 걸어가는 그녀의 호흡을 아침 내내
          서늘하게 짓눌렀다.
        stat_delta:
          "Rachel.스트레스": +2
        flags_emit:
          - Flag_Memory_Rachel_SilentRequest
          - Flag_Trace_Rachel_WordsUnspoken
          - Flag_Trace_Rachel_PassedBy

shirley_jackson_axes:
  primary: 무력한_목소리
  secondary: 신경증적_투사