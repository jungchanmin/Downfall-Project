---
id: EVT_A003_MusicBox
title: 아무도 이 곡을 알 수 없다
type: event
status: complete
summary: >
  아침 장비 점검 중 레이첼이 작은방에서 스스로 연주하는
  오르골이 국가대표 시절 훈련 루틴 곡과 정확히 일치함을
  인지하는 아지트 단독 돌발 이벤트.
  정신 판정에 따라 투지 발현 또는 과거 기억 침습으로 분기.
tags:
  - event
  - track_a
  - F5_Cosmic
  - day_any
  - Loc_아지트_작은방_B7
keywords:
  - 작은방
  - 레이첼
  - 오르골
  - 훈련루틴
  - 과거침습
  - 커리어붕괴
depends_on:
  - LORE_CHAR_Rachel_Lopez
  - SYS_EVT_Template_v2_Spec
emits:
  - Flag_Memory_Rachel_MusicBox
  - Flag_Trace_Rachel_PastInvasion
  - Flag_Trace_Rachel_MelodyLoop
  - Flag_Trace_Rachel_CareerFlashback
last_updated: 2026-05-21
---

event_meta:
  id: EVT_A003_MusicBox
  track: A
  family: F5_Cosmic
  phase: 아침
  location: Loc_아지트_작은방_B7
  weight: 1.0

trigger:
  all:
    - phase: 아침
    - location: Loc_아지트_작은방_B7
    - day: { gte: 2 }
    - any:
        - stat: { actor: "Rachel", 스트레스: { gte: 1 } }
        - day: { gte: 4 }
    - not: { flag: Flag_Memory_Rachel_MusicBox }
    - not: { event_history: { id: EVT_A003_MusicBox, within_days: 99 } }

narration: |
  아침의 서늘한 한기가 칠이 벗겨진 아이용 이층 침대와
  바닥에 뒹구는 부서진 장난감들 사이로 묵직하게
  스며들고 있었다. 레이첼은 아침 장비 점검을 위해
  무거운 걸음으로 1층 작은방의 문을 열고 진입했다.
  사방을 채운 비정한 정적 속에서 그녀가 가죽 구두를
  내딛는 순간, 방 구석의 먼지 쌓인 가구 위에서
  소리가 흘러나왔다.

  태엽을 감아줄 이가 아무도 없었던 장난감 오르골이
  스스로 돌아가며 맑은 멜로디를 연주하기 시작한
  것이다. 레이첼은 그 자리에 박힌 듯 동작을 완전히
  멈췄다. 단순한 기계 고장이나 무작위적인 소음따위가
  아니었다. 투명하게 울려 퍼지는 멜로디의 첫 마디가
  고막을 뚫고 뇌리에 박히는 순간, 레이첼은 온몸의
  피가 순식간에 얼어붙는 패닉을 느꼈다. 이 곡이다.
  틀림없이 이 곡이었다. 국가대표 시절, 피스트에
  오르기 직전 대기실에서 홀로 이어폰을 꽂고 온전히 혼자만의 세계에 잠겨들었던. 
  오직 그녀만이 알고 있는 비밀스러운 훈련 루틴 곡. 아무도 이 곡을 알지 못한다. 그녀의 서투른 자작곡이었으니까. 
  이 아지트에  버려진 고물 장난감이 이 멜로디를 담고 있어서, 이 곡을 연주할
  논리적 이유 따위는 세상에 존재하지 않았다.

  레이첼은 더 이상 장비 점검을 지속할 수 없었다.
  그녀는 오르골 쪽으로 한 걸음 다가서려 했으나
  걸음이 너무나도 무거웠다. 한 걸음 내딛는 순간,
  갑작스럽게 왼쪽 발목에서 그날 커리어가 무참히 부서지던 순간의 끔찍한 통증이
  다시금 생생하게 느껴졌다. 멜로디의 두 번째 마디가
  이어질수록, 무의식적으로 그녀의 오른손은 검자루를
  쥐는 각도를 바꾸며 과거 피스트 위에 섰던 완벽한
  훈련 자세를 재현하고 있었다. 이 공간이, 이 방
  전체가 그녀의 심장 가장 깊숙한 영광과 상실의
  기억까지 통째로 훔쳐보고 조롱하고 있다는 확실한
  인지였다. 레이첼은 입술을 피가 나도록 꽉 깨물면서,
  폭발할 것 같은 심장 소리를 강제로 낮추기 위해
  연신 가쁜 숨을 들이켜고 내쉬며 침착하려고 애썼다.
  펜싱 검 날의 단면은 작은방의 흐릿한 햇빛을 받아
  차갑게 번뜩였다.

resolution:
  mode: stat_check
  check:
    stat: 정신력
    dc: 13
    modifiers:
      - condition: { trait: { actor: "Rachel",
          trait: "Trait_비정상적_침착함" } }
        bonus: +2
      - condition: { flag: { actor: "Rachel",
          flag: "Flag_Past_Rachel_Career_Broken" } }
        bonus: -2
      - condition:
          all:
            - trait: { actor: "Rachel",
                trait: "Trait_동적_자기파멸욕" }
            - stat: { actor: "Rachel", 스트레스: { gte: 3 } }
        bonus: -2

  on_success:
    narration: |
      검자루를 쥔 레이첼은 오른손 가죽 장갑을 터트리기라도 할 것처럼 검을 꽉 감싸 쥐었다. 
      이 방이, 이 친숙하면서도 기이한 선율이 자신의 과거와 영혼까지 들추어 흔들려
      한다면, 주저앉는 대신 이 부조리한 흐름 자체를 베어버릴 차례였다. 
      약점이 읽혔다는 사실은 더 이상 수치심이나 공포가 아닌, 전력으로 짓밟아버려야 할 증오의 불길로 타올랐다. 
      이런것은 사냥개를 채울 목줄로써는 너무나 얇았다.
      레이첼은 오르골을 뒤로한 채 거칠게 방문을 열고 나왔다. 
      닫힌 문틀 너머로도 끔찍하도록 맑은 멜로디는 아침의 적막을 깨트리며 계속 그녀를 유혹했지만, 
      레이첼의 눈동자에는 오로지 생존의 집념과 증오의 불길만이 가득 타올랐다.
    stat_delta:
      "Rachel.스트레스": +1
      "Rachel.정신력": -1
    flags_emit:
      - Flag_Memory_Rachel_MusicBox
      - Flag_Trace_Rachel_MelodyLoop
      - Flag_Trace_Rachel_PastInvasion

  on_fail:
    narration: |
      검자루를 쥐려던 레이첼의 손가락 끝이 가늘게 떨리다 이내 그녀는 손을 힘없이 떨어트렸다.
      완벽하게 통제하고 있다고 믿었던 자신만의 요새, 아침의 루틴, 그리고 과거의 짧았던 영광과 끝이 없었던 추락.
      기억이 현재와 과거를 오가며 어지러이 뒤섞였다. 
      이 방의 정체 모를 소리에 완벽히 잠식당했다는 사실을 인지했을때, 이미 그녀는 손가락 하나 까딱할 수가 없었다. 
      그녀의 신체는 과거 발목이 짓뭉개졌던 그 대기실 바닥에 처박혔을 때처럼 도무지 말을 듣지 않았다.
      있었다. 
      도망칠 수도, 거리를 잴 틈도 없이 압도적인 침습 앞에서 퍼져나온 절대적인 무력감이 그녀의 눈에서 하염없이 눈물을 흘리게 만들었다.
      레이첼은 그녀의 아이덴티티이자 자존심인 검을 뽑아들고, 손에서 떨어뜨리지 않기 위해 안간힘을 썼으나 이내 챙그랑 소리와 함께 검은 바닥으로 추락했다. 
      손목과 어깨, 양팔과 가슴이 사정없이 덜덜 떨리기 시작했다. 
      오르골 앞에서 꼼짝없이 포로가 된 그녀의 뒤로 멈추지 않는 유령 같은 음악 소리만이 작은방의 서늘한 한기 속에 비정하게 울려 퍼졌다.
    stat_delta:
      "Rachel.스트레스": +2
      "Rachel.정신력": -2
    flags_emit:
      - Flag_Memory_Rachel_MusicBox
      - Flag_Trace_Rachel_PastInvasion
      - Flag_Trace_Rachel_CareerFlashback

shirley_jackson_axes:
  primary: 공간의_악의
  secondary: 신경증적_투사