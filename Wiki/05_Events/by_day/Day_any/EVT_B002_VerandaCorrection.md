---
id: EVT_B002_VerandaCorrection
title: 피스트 위의 사냥개
type: event
status: complete
summary: >
  아침 섀도우 펜싱 훈련 중 리더가 베란다에 진입해
  레이첼의 동작을 뒤에서 교정하면서 신체 접촉이
  발생하는 아지트 베란다 개입형 이벤트.
  친밀도에 따라 차가운 수용, 경계 붕괴, 거리 재설정,
  명령 갈구 폭발로 분기됨.
tags:
  - event
  - track_b
  - F3_Internal
  - day_any
  - Loc_아지트_베란다_C2
  - R18
keywords:
  - 베란다
  - 레이첼
  - 섀도우펜싱
  - 동작교정
  - 안개
  - 흔들의자
  - 친밀도_분기
depends_on:
  - LORE_CHAR_Rachel_Lopez
  - SYS_EVT_Template_v2_Spec
emits:
  - Flag_Memory_Rachel_VerandaCorrection
  - Flag_Trace_Rachel_CommandAccepted
  - Flag_Trace_Rachel_BoundaryCollapse
  - Flag_Trace_Rachel_DistanceReclaimed
  - Flag_Trace_Rachel_HungerExposed
  - Rel_Rachel_Leader_Intimacy_Up
last_updated: 2026-05-21
---

event_meta:
  id: EVT_B002_VerandaCorrection
  track: B
  family: F3_Internal
  phase: 아침
  location: Loc_아지트_베란다_C2
  weight: 1.0

trigger:
  all:
    - phase: 아침
    - location: Loc_아지트_베란다_C2
    - day: { gte: 3 }
    - any:
        - stat: { actor: "Rachel", 친밀도: { gte: 1 } }
        - day: { gte: 6 }
    - not: { flag: Flag_Memory_Rachel_VerandaCorrection }
    - not: { event_history: { id: EVT_B002_VerandaCorrection,
        within_days: 7 } }

intro_narration: |
  베란다 난간 너머로 끝없이 밀려든 짙은 안개가
  아지트 외부의 세계를 완벽하게 지워버리고 있었다.
  마치 공중에 떠 있는 고립된 섬이 된 듯한 2층
  베란다에서, 레이첼은 펜싱 검을 쥔 채 안개
  속을 향해 날카로운 스텝을 딛고 있었다. 바람이
  전혀 불지 않는 고요 속에서, 구석에 놓인 낡은
  흔들의자만이 미세하게 삐걱거리며 스스로 흔들리고
  있었다.

  간간히 레이첼의 후우, 훅 하는 숨이 내뱉어지는 사이로, 리더가 베란다 안으로 조용히
  진입했다. 레이첼은 검을 내찌르는 동작을
  멈추지 않았으나, 문을 여는 미세한 마찰음과  안개를 헤집고 들어오는 리더의
  짙은 실루엣을 통해 이미 그 인기척을 포착했다.
  안개는 두 사람의 사방을 두껍게 감싸 안으며,
  이 피스트를 오직 두 사람만을 위해 격리된 밀실로
  빚어내고 있었다.

  말없이 레이첼의 뒤로 바짝 다가선 리더의 손이
  검을 겨누고 있던 그녀의 팔꿈치와 어깨를 부드럽게
  감싸 쥐었다. 흐트러진 각도를 뒤에서 강제로 교정하는
  묵직한 악력이 전해졌다. 레이첼은 순식간에 온몸의
  세포가 바짝 긴장으로 굳어 들어감을 느꼈다. 이대로 검을
  찔러야 하는지, 아니면 동작을 멈추고 뒤를 돌아야
  하는지, 엘리트 선수로서 평생을 다듬어온 육체의
  연산 능력이 리더의 손길 한 번에 통째로 정지해
  버렸다. 뒤에서 밀착해오는 체온이 안개의 한기를
  사정없이 짓밟고 있었다.

choices:
  - id: ch1
    label: "동작을 계속한다"
    resolution:
      - condition: { stat: { actor: "Rachel",
          친밀도: { lt: 2 } } }
        narration: |
          레이첼은 마음을 다잡고 흔들리는 안개 너머로 시선을 단단히
          고정한 채, 리더가 교정한 각도 그대로 동작을
          이어 나갔다. 그녀는 이 손길을 배덕감이 아닌,
          오직 주인이 내리는 비정한 훈련 지시이자
          절대적인 명령으로 해석했다. 감사도, 거부도,
          어떤 사적인 감정의 동요도 섞이지 않도록 차갑게 받아들였다. 
          리더의 손길이 멀어지자, 레이첼은
          교정받은 완벽한 궤적 그대로 부러진 검을
          우아하고 서늘하게 내지르는 동작을 리더가 떠난 후에도 묵묵히 반복했다. 
          아직 손길에 길들여지지 않은 사냥개는, 끝없는 심호흡과 평정심으로 그 손길을 견뎌냈다.
        stat_delta:
          "Rachel.스트레스": -1
          "Rachel.친밀도": +1
        flags_emit:
          - Flag_Memory_Rachel_VerandaCorrection
          - Flag_Trace_Rachel_CommandAccepted
          - Rel_Rachel_Leader_Intimacy_Up

      - condition: { stat: { actor: "Rachel",
          친밀도: { gte: 2 } } }
        narration: |
          리더의 맨 손가락이 팔꿈치를 지나 얇은 셔츠 밑살을 거칠게 움켜쥐며 어깨와 목덜미를
          교정하는 압력이 지속될수록, 레이첼이 유지하려던 펜싱의 완벽한 수평 자세는 이미 온데간데 없었다.
          시선을 고정하려던 안개 너머의 세계가 흐릿하게 번졌고, 그녀는 이미 다가올 쾌락에 대한 기대감과 통제되지 않는 자신에 대한 패닉에
          빠져 있었다. 주인의 손길을 애타게 찾는 노예의 충동과, 온몸을 그 손길에 맡기고 추락하려는 타락 충동이 그녀의 온 몸을 지배해 젖게 만들었다.
          리더의 손길이 셔츠 단추를 풀어냈고, 속옷을 벗겨낸뒤 무방비하게 안개에 드러난 젖가슴을, 또 팬티속으로 파고들어 엉덩이살을 유린하기 시작하자, 레이첼은 어쩔줄 몰라하며 소중한 검을 바닥에 툭, 떨어트렸다.
          벌어진 입술 사이로 비강을 울리는 높은 숨소리와 달뜬 신음이 베란다를 가득 채웠고, 점점 리더의 손길은 과격해져갔다. 
          신체 중심부로 축축하고, 익숙한 뜨거운 열기가 무섭게 들이닥쳤고, 레이첼은 음란한 한숨을 내뱉으며 리더의 짙은 실루엣에 온몸을 기댄 채 가해지는 손길의 궤적을 따라 골반을 뒤틀며, 예민한 부위를 손길에 맞춰 스스로 비벼댔다. 
          곧이어 빨라지는 손길과 물소리에 맞춰 그녀의 하복부가 수차례 발작적인 경련을 일으켰고,
          그녀는 꼴사납게 음액을 토해내며 처참하게 절정에 달했다. 
          바람 없이 미세하게 흔들리던 흔들의자는 두 사람이 토해낸 숨결과 체액, 침과 뜨거운 온도로 가득 얼룩졌고, 그 뜨거운 공기와 열락어린 풀린 눈빛과 시선은 짙은 안개속에서도 뚜렷하게 보였다. 
        stat_delta:
          "Rachel.스트레스": -1
          "Rachel.침식도": +2
          "Rachel.친밀도": +1
        flags_emit:
          - Flag_Memory_Rachel_VerandaCorrection
          - Flag_Trace_Rachel_BoundaryCollapse
          - Rel_Rachel_Leader_Intimacy_Up

  - id: ch2
    label: "동작을 멈춘다"
    resolution:
      - condition: { stat: { actor: "Rachel",
          친밀도: { lt: 2 } } }
        narration: |
          레이첼은 내지르려던 오른팔의 동작을 그 자리에서
          즉시 동결시켰다. 그녀는 리더의 손길이 닿아
          있던 팔꿈치와 어깨를 부드럽게 빼내며 한 걸음
          뒤로 물러섰다. 서늘하게 내려앉은 눈동자로
          리더를 응시한 레이첼은 부러진 검 끝을 바닥을
          향해 정확한 사선으로 내리며 피스트의 규격을
          재설정했다.
          "여기까지입니다."
          짧고 건조한 한마디와 함께, 그녀는 무너질
          뻔했던 선공권과 자신만의 요새를 단호하게
          회복했다. 밀어내어 거역하는 것이 아닌, 오직
          펜싱 룰이 허용하는 철저한 통제와 안전거리를
          지키기 위한 사냥개 고유의 서늘한 거절이었다.
        stat_delta:
          "Rachel.스트레스": +0
          "Rachel.친밀도": +0
        flags_emit:
          - Flag_Memory_Rachel_VerandaCorrection
          - Flag_Trace_Rachel_DistanceReclaimed

      - condition: { stat: { actor: "Rachel",
          친밀도: { gte: 2 } } }
        narration: |
          레이첼은 리더의 손길을 거부하기 위해
          동작을 멈추고 물러서려 했으나, 뒤에서 목덜미를
          가볍게 매만졌던 리더의 손길이 떨어지는 그 찰나에
          신체 내부에서 지독한 갈증이 폭발했다. 통제를
          회복하려는 이성과, 주인의 손길에 더 잔인하게
          유린당하고 싶다는 명령 갈구가 정면으로 충돌했다.
          한 걸음 물러서려던 그녀의 왼쪽 발목이 무력하게
          꺾였고, 리더의 손목이 멀어지려는 순간 레이첼의
          오른손이 무의식적으로 그 짙은 실루엣을 붙잡기
          위해 허공을 향해 뻗어졌다.
          그러나 차마 붙잡지 못하고, 그녀의 손가락 끝은
          수치심과 절망으로 가득 찬 채 공중에서 사정없이
          떨리며 그대로 굳어버렸다. 이미 정신이 반쯤
          혼미해진 채로 안개를 피해 고개를 완전히 옆으로
          꺾은 레이첼은 비강을 울리는 가쁜 숨소리를
          억누르며 단전에서부터 차오르는 수치스러운 열기를
          고스란히 받아내고 있었다. 멈춰 선 그녀의 떨리는
          실루엣 뒤로, 바람 없는 흔들의자만이 비정하게
          삐걱거리며 무너진 사냥개의 자아를 담아낼 뿐이었다.
        stat_delta:
          "Rachel.스트레스": +2
          "Rachel.친밀도": -1
        flags_emit:
          - Flag_Memory_Rachel_VerandaCorrection
          - Flag_Trace_Rachel_HungerExposed

shirley_jackson_axes:
  primary: 무력한_목소리
  secondary: 신경증적_투사