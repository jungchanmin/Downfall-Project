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
  샤워실 타일 바닥 위로 번진 고인 물기 끝에 레이첼의
  두 발끝이 서 있었다. 샤워기에서 떨어지던 물소리가
  잦아들며 둔탁한 정적이 가라앉았다. 여러 갈래로 잘게
  금이 간 거울 면 위로 물방울에 젖어 어깨에 밀착된
  그녀의 실루엣이 조각조각 분절된 채 떠올랐다.
  거울의 쪼개진 틈새들은 레이첼의 움직임을 각각 다른
  각도에서 비추고 있었다.

  샤워실 문이 소리 없이 열리며 짙은 실루엣 하나가
  등 뒤로 밀려들었다. 레이첼은 정면의 깨진 거울 조각을
  통해 그 형체를 포착했다. 거울의 균열들은 두 사람의
  형상을 수십 개의 조각으로 나누어 담았고, 거실에서
  들려오는 외부의 소음은 이곳까지 닿지 않았다.

  말없이 다가선 리더의 손이 레이첼의 젖은 머리카락
  위에 얹어졌다. 레이첼의 어깨가 미세하게 위로
  당겨지며 굳어졌다. 바닥을 딛고 있던 왼쪽 발목뼈에
  팽팽하게 힘이 실렸고, 축축한 공기 사이로 두 사람의
  거리가 소거되었다. 리더의 손가락 끝이 두피를 지긋이
  누르며 젖은 머리타래를 타고 내려오는 물리적인 압력이
  전해졌다.

choices:
  - id: ch1
    label: "그대로 있는다"
    resolution:
      - condition: { stat: { actor: "Rachel", 침식도: { lt: 30 } } }
        narration: |
          레이첼은 거울에서 시선을 거두며 천천히 눈을
          감았다. 리더의 손가락이 머리카락을 쓸어내리는
          일정한 온도와 악력을 거부하지 않고 묵묵히
          받아들였다. 마른 수건이 목선과 어깨를 무겁게
          감싸며 축축한 물기를 흡수하는 마찰열이 피부로
          전해지는 순간까지도, 그녀의 척추는 단단하게
          긴장을 풀지 않았다. 주인의 처분에 몸을 맡긴
          사냥개처럼 서늘하고 절제된 수용이었다.
          리더의 손길이 수건을 통해 머리를 말려주는
          내내 레이첼은 미동도 없이 단호한 태도로
          그 거리감을 견뎌냈다.
        stat_delta:
          "Rachel.스트레스": -1
          "Rachel.친밀도": +1
        flags_emit:
          - Flag_Memory_Rachel_ShowerHair
          - Flag_Trace_Rachel_LeaderTouchAllowed
          - Rel_Rachel_Leader_Intimacy_Up

      - condition: { stat: { actor: "Rachel", 침식도: { gte: 30 } } }
        narration: |
          리더의 손가락이 두피를 누르는 압력이 강해지자,
          레이첼은 거울 속 잘게 조각난 자신의 반사상을
          응시했다. 이내 단단하게 고정되어 있던 그녀의
          양 어깨에서 선명하게 힘이 빠지기 시작했다.
          언제나 일정한 거리를 유지하려던 육체의 통제가
          무너져 내리는 신호였다. 왼쪽 발목에서 지탱하던
          힘이 풀리며 신체의 무게중심이 비스듬히 뒤로
          이동했다. 마른 수건이 목선을 감싸 쥐는 순간,
          레이첼의 호흡은 마디마디 조각나며 비강을 울리는
          높은 숨소리로 새어 나왔다. 수건 너머로 손길이
          셔츠 밑 맨살을 파고들어 허리와 골반을 주무르며
          깊어질수록, 신체 중심부로 뜨거운 열기가
          집중되었다. 척추를 지탱하던 긴장이 단계적으로
          완전히 이완되었고, 레이첼은 거부의 힘을 잃고
          가해지는 모든 압력에 순응해 갔다. 목구멍을
          긁는 가쁜 호흡만이 조용한 공간을 채웠다.
          깨진 거울 조각들은 그 일그러진 열기 속에서
          완전히 붕괴한 두 사람의 실루엣을 오직 침묵으로
          가득 담아냈다.
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
          머리칼을 쥐고 있는 리더의 손목을 움켜쥐었다.
          쇠붙이를 제압하던 단단한 악력이 리더의 피부
          위에 그대로 전해졌다. 그녀는 리더의 손을
          옆으로 밀어내며 거리를 재설정했다.
          "여기까지."
          짧은 경고조의 한마디만을 남긴 채, 레이첼은
          리더의 손에서 수건을 직접 낚아채 자신의
          머리카락을 서늘하고 단호한 동작으로 닦아내기
          시작했다. 밀어내어 배신하는 것이 아닌,
          철저히 통제된 사냥개로서의 안전거리를
          스스로 회복하는 신체적 언어였다.
        stat_delta:
          "Rachel.스트레스": +0
          "Rachel.친밀도": +0
        flags_emit:
          - Flag_Memory_Rachel_ShowerHair
          - Flag_Trace_Rachel_DistanceReset

      - condition: { stat: { actor: "Rachel", 침식도: { gte: 30 } } }
        narration: |
          레이첼은 반사적으로 리더의 손목을 움켜쥐기
          위해 오른손을 뻗었으나, 두피를 짓누르는
          손길의 악력에 전신의 관절이 무력하게
          굳어버렸다. 리더의 손목을 잡으려던 그녀의
          손은 허공에서 힘을 잃고 꺾여 내려갔다.
          디디고 서 있던 왼쪽 발목의 힘이 완전히
          풀려 무너지며 신체 중심부로 급격하게 열기가
          집중되었고, 얇은 셔츠 밑살을 파고들어 가슴과
          골반을 압착하는 강한 자극에 피부 표면이
          온통 붉게 달아올랐다. 레이첼은 거울 속
          조각난 자신의 반사상을 차마 바라보지 못한 채
          고개를 옆으로 완전히 꺾어 시선을 외면했다.
          통제를 벗어난 호흡은 점진적으로 조각나며
          비강을 울리는 높은 숨소리와 목구멍을 긁는
          가쁜 호흡으로 변해 좁은 샤워실을 채웠다.
          허리가 뒤로 크게 휘어지며 하복부가 수차례
          경련을 일으켰고, 육체는 거부의 힘을 잃고
          가해지는 압력을 고스란히 받아내며 가라앉았다.
          깨진 거울 조각들은 그 닫히지 않은 채 완전히
          무너져 내리는 레이첼의 실루엣을 비정하게
          담아낼 뿐이었다.
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