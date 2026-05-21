---
id: EVT_B001_ShowerHair
title: 물소리가 잦아드는 순간
type: event
status: complete
summary: >
  아침 샤워 루틴 중 리더가 샤워실에 진입해 레이첼의
  젖은 머리카락을 씻기고 수건으로 말려주는 과정에서
  스킨십이 발생하는 아지트 샤워실 개입형 이벤트.
  침식도에 따라 레이첼의 반응이 절제된 수용 또는
  강박 붕괴로 분기됨.
tags:
  - event
  - track_b
  - F3_Internal
  - day_any
  - Loc_아지트_샤워실_C3
  - R18
keywords:
  - 샤워실
  - 레이첼
  - 머리카락
  - 수건
  - 깨진_거울
  - 침식도_분기
depends_on:
  - LORE_CHAR_Rachel_Lopez
  - SYS_EVT_Template_v2_Spec
emits:
  - Flag_Memory_Rachel_ShowerHair
  - Flag_Trace_Rachel_LeaderTouchAllowed
  - Flag_Trace_Rachel_CrackingEdge
  - Flag_Trace_Rachel_DistanceReset
  - Flag_Trace_Rachel_CollapseShame
  - Rel_Rachel_Leader_Intimacy_Up
last_updated: 2026-05-20
---

event_meta:
  id: EVT_B001_ShowerHair
  track: B
  family: F3_Internal
  phase: 아침
  location: Loc_아지트_샤워실_C3
  weight: 1.0

trigger:
  all:
    - phase: 아침
    - location: Loc_아지트_샤워실_C3
    - day: { gte: 2 }
    - any:
        - stat: { actor: "Rachel", 스트레스: { gte: 2 } }
        - day: { gte: 5 }
    - not: { flag: Flag_Memory_Rachel_ShowerHair }
    - not: { event_history: { id: EVT_B001_ShowerHair, within_days: 7 } }

intro_narration: |
  샤워실 타일에 끊임없이 물줄기가 배수구를 향해 흘러내렸고, 레이첼은
작은 소리로 노래를 흥얼거리며 몸을 씻었다. 이내 그녀는 샤워기를 잠그고, 자신의 물기어린 나신을 가만히 응시했다.
다소 금이 갔지만, 사용하는데 큰 문제없는 거울 면 위에 그녀의 아름답게 굴곡진 몸이 비춰졌다.
거울의 쪼개진 조각들은, 각자 다른 각도에서 비추며 물기어린 모습의 그녀를 응시했다.

그때, 갑작스럽게 샤워실 문이 소리 없이 열리며 짙은 실루엣 하나가
등 뒤로 예고없이 등장했다. 깜짝 놀라서 손을 치켜들었던 레이첼은 곧 거울에 비친 그 실루엣을 확인하고 다시
손을 내렸다. 가만히 거울을 통해 서로를 응시하는 두 사람의 형상은 맞닿았고, 거실에서
들려오는 외부의 소음은 이곳까지 닿지 않았다.

말없이 다가선 리더의 손이 레이첼의 젖은 머리카락
위에 얹어졌다. 레이첼의 어깨가 그 손길을 따라 미세하게 위로
당겨졌다. 긴장으로 잔뜩 몸을 굳힌 탓에 바닥을 딛고 있던 왼쪽 발목에서
약간의 통증이 느껴졌고, 축축한 공기 사이로 두 사람의
거리는 이제 한없이 줄어들었다. 리더의 손가락 끝이 두피를 지긋이
누르며 젖은 머리타래를 타고 내려오는 손길이 그녀에게 그대로 전해졌다.


choices:
  - id: ch1
    label: "그대로 있는다"
    resolution:
      - condition: { stat: { actor: "Rachel", 침식도: { lt: 30 } } }
        narration: |
          레이첼은 거울에서 시선을 거두며 질끈 눈을
          감았다. 리더의 손길이 자신의 머리카락을 쓸어내릴때,
          그 온도와 촉감을 거부하지 않고 순순히
          받아들였다. 마른 수건이 목선과 어깨를 가볍게
          마사지하며 축축한 물기를 흡수하는 행위가 피부로
          전해지는 순간까지도, 그녀의 척추는 단단하게
          긴장을 풀지 않았다. 그 일련의 행위를 겪으면서도, 여전히 그녀는 흥분하지 않고
          차분하게 손길을 견뎌내고 있었다.
          리더의 손길이 수건을 통해 머리를 말려주는
          마지막까지도, 그 미묘한 거리감은 계속됐다.
        stat_delta:
          "Rachel.스트레스": -1
          "Rachel.친밀도": +1
        flags_emit:
          - Flag_Memory_Rachel_ShowerHair
          - Flag_Trace_Rachel_LeaderTouchAllowed
          - Rel_Rachel_Leader_Intimacy_Up

      - condition: { stat: { actor: "Rachel", 침식도: { gte: 30 } } }
        narration: |
          리더의 손가락 마디마디가 그녀의 머리를 감싸안을때, 레이첼은 차마 거울 속의 자신이 무슨 표정을 짓고있는지 마주할 자신이 없었다. 이내 얼마 견디지 못하고, 그녀의 양 어깨에서부터 급격하게 힘이 빠져나갔다. 그녀는 간간히 긴 호흡을 내뱉으며, 리더가 만져주는 촉감에 온 신경을 기울였다. 리더의 끈질긴 애무에, 그녀의 신체는 어느새 리더의 손길을 따라 열기를 띄기 시작했다. 마른 수건이 마치 목을 조르기라도 하는 것처럼 목선을 감싸 쥐며 강하게 물기를 닦아낼때, 레이첼의 호흡은 자비를 구하는 것처럼 비강을 울리는 높은 숨소리로 새어 나왔다. 어느새 손길이 그녀의 무방비한 밑가슴을 유린하고, 다른 손은 허리와 골반을 강하게 짓누르고 주무르기 시작했다. 레이첼은 반쯤 정신이 혼미해진 채로, 마음없는 거부와 함께 울먹이는 듯한 달뜬 신음소리를 내뱉었다. 그녀의 신체 중심부로 축축하고 뜨거운 열기가 들이닥치고 있었고, 그녀의 젖가슴과 비부를 유린하는 손길은 그녀의 사정을 봐줄 생각이 없었다. 레이첼은 완전히 리더에게 몸을 기댄채로, 가해지는 손길의 궤적을 따라 자신의 골반과 몸을 비틀고 예민한 부위를 스스로 손가락에 밀착시키며 쾌감을 찾았다. 완전히 달아오른 신음소리와 애절한 간구가 한계에 달했을때, 그녀의 다리가 꺾이며 마지막 몸부림에 가까운 발작적인 떨림, 단전에서부터 터져나오는 깊은 절정이 하복부를 관통했고, 깨진 거울 조각들은 그녀가 쏟아낸 체액, 침과 눈물, 리더에게 완전히 안겨서 포로가 된 그 두 사람의 희열가득한 눈동자를 온전히 담아냈다.
        stat_delta:
          "Rachel.스트레스": -1
          "Rachel.침식도": +3
          "Rachel.친밀도": +1
        flags_emit:
          - Flag_Memory_Rachel_ShowerHair
          - Flag_Trace_Rachel_CrackingEdge
          - Rel_Rachel_Leader_Intimacy_Up

  - id: ch2
    label: "손을 치우려 한다"
    resolution:
      - condition: { stat: { actor: "Rachel", 침식도: { lt: 30 } } }
        narration: |
          레이첼은 반사적으로 오른손을 뻗어 자신의
          머리카락을 쓰다듬으며, 쥐고 있는 리더의 손목을 움켜쥐었다.
          단호한 의사를 드러내는 강하지도, 약하지도 않은 악력이 리더의 피부
          위에 그대로 전해졌다. 그녀는 리더의 손을
          옆으로 밀어내며 거리를 조금 벌렸다.
          "여기까지."
          짧은 경고조의 한마디만을 남긴 채, 레이첼은
          리더의 손에서 수건을 직접 낚아채 자신의
          머리카락을 서늘하고 단호한 동작으로 닦아내기
          시작했다. 그러나 차가운 행동과는 다르게, 그녀의 눈동자는 안타까운 듯이 미묘한 빛을 내며 빛나고 있었다.
        stat_delta:
          "Rachel.스트레스": +0
          "Rachel.친밀도": +0
        flags_emit:
          - Flag_Memory_Rachel_ShowerHair
          - Flag_Trace_Rachel_DistanceReset

      - condition: { stat: { actor: "Rachel", 침식도: { gte: 30 } } }
        narration: |
          레이첼은 크게 동요했다. 그리고 그 감정을 억누르기 위해 리더의 손목을 움켜쥐려고
          오른손을 뻗었다. 그러나 그녀의 어설픈 저항에도, 아랑곳하지 않은 리더는 레이첼의 손을 가볍게 때렸다.
          마치 매질을 당한 사냥개마냥, 그녀의 손은 허공에서 힘을 잃고 꺾여서 내려갔다.
          "가만히 있어. 힘을 빼."
          리더의 속삭이는 듯한 목소리를 들은 레이첼은 더 이상 아무런 저항도 하지 못했다. 
          그 손길은 머리에서 내려와 목덜미, 나신으로 무방비하게 드러난 젖가슴, 그리고 흥분과 기대감으로 잔뜩 부풀어오른
          유륜과 유두를 부드럽게 문질렀다.
          손길이 닿을때마다, 그녀는 달뜬 신음을 뱉으며 몸을 비틀었지만, 용서없는 유린이 이어졌다. 
          그녀가 잘못을 빌며 애걸할때에서야, 겨우 리더의 손은 아래로 내려가 그녀의 하복부를 천천히 문질러댔다.
          레이첼은 금간 거울에 비친 자신의 음란하게 흐트러진 모습을 차마 더 바라보지 못하고, 고개를 완전히 꺾어 거울속의 시선을 외면했다.
          가쁜 호흡과 신음은 그녀의 통제를 벗어나있었고, 찰박거리는 음란한 물소리와 그녀의 절규와 쾌락이 뒤섞인 신음이 샤워실을 가득 채웠다. 
          "이 음란한 년."
          리더의 빨라진 손길이 그녀의 가장 예민한 비부 끝의 맨 살, 음핵을 엄지손가락으로 드러내고, 짓눌렀을때, 그녀는 허리를 떨며 하반신을 관통하는 절정을 맛보았다. 
          "하아, 하아... 이제 용서해주세요. 으극!"
          그러나, 애달픈 눈물젖은 눈과 침을 흘리며 그녀의 애원에도 다시금 욕망을 쫓는 애무는 시작되었다. 
          영원과도 같은 시간속에서, 레이첼 로페즈는 자신의 처절하고 비참한 모습을 영혼깊숙히 느껴야만 했다. 
        stat_delta:
          "Rachel.스트레스": +2
          "Rachel.침식도": +2
          "Rachel.친밀도": -1
        flags_emit:
          - Flag_Memory_Rachel_ShowerHair
          - Flag_Trace_Rachel_CollapseShame

shirley_jackson_axes:
  primary: 신경증적_투사
  secondary: 무력한_목소리