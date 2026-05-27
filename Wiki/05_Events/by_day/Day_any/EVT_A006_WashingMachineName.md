---
id: EVT_A006_WashingMachineName
title: 레이첼
type: event
status: complete
summary: >
  아침 세탁 루틴 중 레이첼이 구형 세탁기 회전음
  사이에서 자신의 이름을 웅얼대는 정체불명의 소리를
  감지하는 아지트 세탁실 단독 돌발 이벤트.
  정신 판정에 따라 세탁기를 멈추고 확인하거나
  끝까지 멈추지 못하고 기다림.
tags:
  - event
  - track_a
  - F5_Cosmic
  - day_any
  - Loc_아지트_세탁실_B5
keywords:
  - 세탁실
  - 레이첼
  - 세탁기
  - 이름
  - 웅얼거림
  - 전투복
depends_on:
  - LORE_CHAR_Rachel_Lopez
  - SYS_EVT_Template_v2_Spec
emits:
  - Flag_Memory_Rachel_WashingMachineName
  - Flag_Trace_Rachel_NameHeard
  - Flag_Trace_Rachel_MachineOpened
  - Flag_Trace_Rachel_MachineNotOpened
last_updated: 2026-05-26
---

event_meta:
  id: EVT_A006_WashingMachineName
  track: A
  family: F5_Cosmic
  phase: 아침
  location: Loc_아지트_세탁실_B5
  weight: 1.0

trigger:
  all:
    - phase: 아침
    - location: Loc_아지트_세탁실_B5
    - day: { gte: 3 }
    - any:
        - stat: { actor: "Rachel", 스트레스: { gte: 2 } }
        - day: { gte: 6 }
    - not: { flag: Flag_Memory_Rachel_WashingMachineName }
    - not: { event_history: { id: EVT_A006_WashingMachineName,
        within_days: 99 } }

narration: |
  아침 세탁실 내부에는 눅눅한 습기와 세탁조에서
  배어 나오는 특유의 열기가 빽빽하게 차올라 있었다.
  레이첼은 핏자국이 벌겋게 굳어 얼룩진 전투복을
  구형 세탁기의 원형 입구 안으로 깊숙이 밀어 넣었다.
  철제 문을 닫자 텅 하는 탁한 타격음이 축축한 콘크리트
  벽을 치고 사방으로 흩어졌다. 손가락 끝으로 돌출된
  작동 버튼을 정밀하게 내리누르자, 기계가 가동하기
  시작하며 낮고 육중한 회전음이 시멘트 바닥을 타고
  발끝으로 낮게 울렸다. 레이첼은 세탁기 문 앞에서
  걸음을 옮기지 않은 채 돌아가는 통 내부를 물끄러미
  응시했다. 매일 반복되는 이 기계적인 루틴 속에서,
  물줄기가 차오르고 회전 속도가 가파르게 상승할수록
  유리문 표면에 비친 그녀의 흐릿한 실루엣도 거칠게
  뒤섞여 돌았다.

  그녀의 호흡이 세탁기의 정밀한 회전 주기에 맞춰
  무의식적으로 동기화될 무렵, 고막을 때리던 일정한
  기계음 사이로 이질적인 음파의 결이 끼어들었다.
  웅웅거리는 모터의 울림과 물이 출렁이는 날카로운
  마찰음 한가운데에서, 마치 물밑에 잠긴 누군가가
  조용히 웅얼거리는 듯한 둔탁한 목소리가 서서히
  늘어지며 섞여 들었다. 단어의 명확한 형태를 포착하기는
  불가능했으나, 수류가 회전하는 엇박자의 끝자락이
  규칙적으로 끊어지며 레이첼이라는 이름을 부르는
  음성의 고저를 기이하게 닮아 있었다. 세탁기 내부의
  드럼통 중심부인지, 건조대가 놓인 세탁실 구석의
  뒤편 벽면인지, 그 기척의 출처와 거리를 무의식적으로
  가늠하려 고개를 비틀었으나 출처를 특정할 수 없었다.
  오직 드럼통이 최고 속도로 가속하며 돌아가는 그
  물리적 가동의 순간에만, 소리는 기계음과 완벽히
  얽힌 채 세탁실의 공기를 무겁게 채워 나갔다.

  소리가 귀에 닿는 순간 레이첼의 상체가 딱딱하게
  정지했다. 세탁기 정지 버튼을 향해 뻗어 나가던
  오른손이 손잡이와 버튼의 중간 지점에서 멈춰 섰다.
  손가락 끝이 경직된 채 허공에 고정되었고, 가죽
  구두 굽은 단 한 치의 미동도 없이 바닥의 진동을
  받아냈다. 세탁실 내부에는 회전하는 모터의 마찰음과
  그 안에 섞인 웅얼거림 외에는 그 어떤 기척도
  흐르지 않았다.

resolution:
  mode: stat_check
  check:
    stat: 정신
    dc: 12
    modifiers:
      - condition: { trait: { actor: "Rachel",
          trait: "Trait_비정상적_침착함" } }
        bonus: +2
      - condition: { trait: { actor: "Rachel",
          trait: "Trait_변형된_펜싱_룰" } }
        bonus: +1
      - condition: { flag: "Flag_Memory_Rachel_EchoStep" }
        bonus: -1
      - condition: { stat: { actor: "Rachel",
          스트레스: { gte: 4 } } }
        bonus: -2

  on_success:
    narration: |
      레이첼은 공중에 멈춰 있던 오른손 검지를 정지
      버튼 위로 단호하게 내리눌렀다. 틱 하는 마찰음과
      함께 요란하게 돌던 드럼통이 속도를 줄이며
      완만하게 감속하기 시작했다. 기계의 진동이 바닥에서
      소거되는 순간, 웅얼거림도 뚝 끊겼다. 레이첼은
      완전히 정지한 세탁기의 원형 유리문 손잡이를
      잡아당겨 열었다. 안에는 축축하게 젖은 채 뒤엉킨
      전투복 외에는 아무것도 없었다. 그녀는 유리문을
      세차게 닫은 뒤 기계 재작동 버튼을 눌렀다.
      세탁실 문이 닫히는 순간에도 기계는 다시 회전음을
      토해내며 돌아가고 있었고, 레이첼은 복도로
      나가면서 끝내 뒤를 돌아보지 않았다.
    stat_delta:
      "Rachel.스트레스": +1
      "Rachel.정신": -1
    flags_emit:
      - Flag_Memory_Rachel_WashingMachineName
      - Flag_Trace_Rachel_NameHeard
      - Flag_Trace_Rachel_MachineOpened

  on_fail:
    narration: |
      세탁기 버튼을 향해 뻗어 나가던 레이첼의 손끝이
      공중에서 멈췄다. 기계를 강제로 멈추면 물살 속에
      묻혀 있던 소리가 더 또렷한 형태로 올라올 것 같은
      감각에 손이 거두어졌다. 레이첼은 타일 벽면을
      향해 등을 붙이고 낮게 기대어 섰다. 세탁기가
      헹굼과 탈수 코스를 끝마칠 때까지 미동도 없이
      서서 돌아가는 통만을 응시했다. 마지막 탈수
      회전이 끝나고 기계가 완전히 멈추는 순간,
      웅얼거림도 흔적 없이 사그라졌다. 레이첼은 벽에서
      등을 떼고 느리게 다가가 세탁기 문 손잡이에
      손을 얹은 뒤, 젖은 전투복만을 묵묵히 꺼냈다.
      세탁기 원형 유리문 안쪽에는 텅 빈 드럼만이
      정적 속에 정지해 있었고, 그녀의 손가락이
      손잡이에서 천천히 떨어졌다.
    stat_delta:
      "Rachel.스트레스": +2
      "Rachel.정신": -1
    flags_emit:
      - Flag_Memory_Rachel_WashingMachineName
      - Flag_Trace_Rachel_NameHeard
      - Flag_Trace_Rachel_MachineNotOpened

shirley_jackson_axes:
  primary: 공간의_악의
  secondary: 신경증적_투사