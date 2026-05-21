# 🗂️ Downfall Wiki Master Index

*Auto-generated on 2026-05-21T14:55:08*  
*Total entries: 15*  
*⚠️ DO NOT EDIT BY HAND — modify each file's frontmatter, then re-run build_index.py.*

---

## 📁 `./`

### ✅ `ConText_Manifest.md`
- **Title:** Downfall Project Context Manifest
- **ID:** `SYS_Manifest` | **Type:** `system`
- **Summary:** 프로젝트의 핵심 아키텍처·디자인 필러·라이팅 지침·태그 스키마를 정의한 헌법 문서.
- **Keywords:** 필러, 셜리잭슨, 태그, 리더권한


## 📁 `00_Templates/`

### ✅ `Bot_Universal_Template.md`
- **Title:** 보편적 생존자 가이드 봇 템플릿
- **ID:** `TMPL_Universal_Survivor_Guide_Bot` | **Type:** `template`
- **Summary:** 캐릭터 로어 바이블 작성을 위한 11개 섹션 표준 양식. Declared/Believed/Actual/Lack 의 4층 내면 구조와 상황별 말투 10종을 포함.
- **Keywords:** 캐릭터 양식, 로어 바이블, 내면 구조, 상황별 말투, Identity, Personality, Voice, Relationships

### ✅ `EVT_Conveyor_Belt_Master_Prompt.md`
- **Title:** Downfall 이벤트 컨베이어 벨트 마스터 프롬프트 v2.2
- **ID:** `EVT_Conveyor_Belt` | **Type:** `template`
- **Summary:** 이벤트 생성 5단계 프로세스. v2 스키마(패밀리·Trigger DSL·조사 슬롯·Resolution Mode) 반영.
- **Keywords:** 이벤트 생성, 컨베이어 벨트, 프로세스, 작가 모드
- **Depends on:** `SYS_Manifest`, `SYS_EVT_Template_v2_Spec`, `TMPL_EVT_Notification`, `TMPL_EVT_Interactive`

### ✅ `EVT_Interactive.md`
- **Title:** 개입형 이벤트 (Track B) 생성 양식 v2
- **ID:** `TMPL_EVT_Interactive` | **Type:** `template`
- **Summary:** 2~3 선택지를 가진 개입형 이벤트의 v2 표준 양식. 내러티브 모듈 분리 + Trigger DSL + 조사 슬롯 + 선택지 내부 stat_check.
- **Keywords:** 이벤트, Track B, 개입형, 선택지, 판정
- **Depends on:** `SYS_Manifest`, `SYS_EVT_Template_v2_Spec`, `EVT_Conveyor_Belt`

### ✅ `EVT_Notification.md`
- **Title:** 통보형 이벤트 (Track A) 생성 양식 v2
- **ID:** `TMPL_EVT_Notification` | **Type:** `template`
- **Summary:** 선택지 없는 단일 결과 이벤트의 v2 표준 양식. 셜리 잭슨 작법 유지 + Trigger DSL + 조사 슬롯 + Resolution Mode.
- **Keywords:** 이벤트, Track A, 통보형, 셜리잭슨
- **Depends on:** `SYS_Manifest`, `SYS_EVT_Template_v2_Spec`, `EVT_Conveyor_Belt`

### ⚪ `EVT_Template_v2_Spec.md`
- **Title:** 범용 이벤트 템플릿 v2 사양 — 4대 문제 해결안
- **ID:** `SYS_EVT_Template_v2_Spec` | **Type:** `system`
- **Summary:** EVT_Notification 의 콘텐츠 다양화·맥락 필터링·한국어 조사 처리·판정 구조를 통합한 v2 템플릿 사양.
- **Keywords:** 이벤트, 템플릿, 필터링, 조사, 판정, DC
- **Depends on:** `SYS_Manifest`, `TMPL_EVT_Notification`, `TMPL_EVT_Interactive`


## 📁 `01_Mechanics/`

### ✅ `Time_System.md`
- **Title:** 5페이즈 시간 시스템
- **ID:** `MECH_Time_System` | **Type:** `mechanic`
- **Summary:** 새벽·아침·점심·저녁·밤의 5단계 페이즈 정의와 각 페이즈의 가능 행동·금기 행동·종료 조건.
- **Keywords:** 페이즈, 새벽, 아침, 점심, 저녁, 밤, 턴


## 📁 `02_World/`

### 🟡 `Obeng_Village_Lore.md`
- **Title:** 오뱅마을 15구역 로어
- **ID:** `LORE_LOC_Oebeng` | **Type:** `lore_world`
- **Summary:** 오뱅마을 15개 구역(성당·상점가·폐가 등)의 분위기·위험도·고유 이벤트 시드.
- **Keywords:** 오뱅마을, 성당, 상점가, 폐가
- **Depends on:** `SYS_Manifest`


## 📁 `03_Entities/Survivors/`

### ✅ `Guide_Gavin_Jackson.md`
- **Title:** 보편적 생존자 가이드 — 레이첼 로페즈
- **ID:** `LORE_CHAR_Rachel_Lopez` | **Type:** `lore_char`
- **Summary:** 과거 '은빛 칼날' 펜싱 국가대표였으나 동료의 사보타주로 발목이 부서져 몰락. 현재는 아지트의 '사냥개'로서 리더의 명령에 맹목적으로 종속된 전투원.
- **Keywords:** 레이첼, Rachel, Lopez, 사냥개, 은빛 칼날, 펜싱, 피스트, 동적_자기파멸욕, 리더, 가빈
- **Depends on:** `TMPL_Universal_Survivor_Guide_Bot`, `MECH_Mental_Ailments`
- **Emits:** `Trait_비정상적_침착함`, `Trait_펜싱_룰`, `Trait_동적_자기파멸욕`, `Trait_부상_왼쪽발목`, `Flag_Past_Rachel_Career_Broken`, `Flag_Past_Rachel_Betrayed_By_Peer`, `Rel_Rachel_Leader_Blind_Devotion`

### ✅ `Guide_Rachel_Lopez.md`
- **Title:** 보편적 생존자 가이드 — 레이첼 로페즈
- **ID:** `LORE_CHAR_Rachel_Lopez` | **Type:** `lore_char`
- **Summary:** 과거 '은빛 칼날' 펜싱 국가대표였으나 동료의 사보타주로 발목이 부서져 몰락. 현재는 아지트의 '사냥개'로서 리더의 명령에 맹목적으로 종속된 전투원.
- **Keywords:** 레이첼, Rachel, Lopez, 사냥개, 은빛 칼날, 펜싱, 피스트, 동적_자기파멸욕, 리더, 가빈
- **Depends on:** `TMPL_Universal_Survivor_Guide_Bot`, `MECH_Mental_Ailments`
- **Emits:** `Trait_비정상적_침착함`, `Trait_펜싱_룰`, `Trait_동적_자기파멸욕`, `Trait_부상_왼쪽발목`, `Flag_Past_Rachel_Career_Broken`, `Flag_Past_Rachel_Betrayed_By_Peer`, `Rel_Rachel_Leader_Blind_Devotion`


## 📁 `05_Events/by_day/Day_any/`

### ✅ `EVT_A001_RibbonAnomaly.md`
- **Title:** 아침의 리본
- **ID:** `EVT_A001_RibbonAnomaly` | **Type:** `event`
- **Summary:** 레이첼이 아침 검 점검 루틴 중 보관함의 금메달 리본 색조가 어제와 미세하게 어긋난 것을 포착하고, 꺼진 TV 브라운관의 반사상과의 불일치를 목격하는 아지트 거실 단독 돌발 이벤트.
- **Keywords:** 거실, 레이첼, 금메달_리본, 브라운관_반사, 색조_불일치
- **Depends on:** `LORE_CHAR_Rachel_Lopez`, `SYS_EVT_Template_v2_Spec`
- **Emits:** `Flag_Memory_Rachel_RibbonAnomaly`, `Flag_Trace_Rachel_RibbonDoubt`, `Flag_Trace_Rachel_HandTremor_Morning`

### ✅ `EVT_A002_FleshEaterMark.md`
- **Title:** 놈은 아침을 알았다
- **ID:** `EVT_A002_FleshEaterMark` | **Type:** `event`
- **Summary:** 아침 훈련 루틴 중 레이첼이 자신의 보폭과 정확히 일치하는 간격으로 훈련 동선 위에 새겨진 U.H-028의 표식을 발견하고, 사냥감으로 지목되었음을 인지하는 아지트 수영장 인근 단독 돌발 이벤트. 정신 판정에 따라 투지 발현 또는 강박 균열로 분기.
- **Keywords:** 수영장, 레이첼, 표식, 살점포식자, UH028, 선공권, 훈련동선
- **Depends on:** `LORE_CHAR_Rachel_Lopez`, `SYS_EVT_Template_v2_Spec`, `BESTIARY_UH028`
- **Emits:** `Flag_Memory_Rachel_FleshEaterMark`, `Flag_Lore_UH028_Rachel_Targeted`, `Flag_Trace_Rachel_HuntingInstinct`, `Flag_Trace_Rachel_PatternAnxiety`

### ✅ `EVT_A003_MusicBox.md`
- **Title:** 아무도 이 곡을 알 수 없다
- **ID:** `EVT_A003_MusicBox` | **Type:** `event`
- **Summary:** 아침 장비 점검 중 레이첼이 작은방에서 스스로 연주하는 오르골이 국가대표 시절 훈련 루틴 곡과 정확히 일치함을 인지하는 아지트 단독 돌발 이벤트. 정신 판정에 따라 투지 발현 또는 과거 기억 침습으로 분기.
- **Keywords:** 작은방, 레이첼, 오르골, 훈련루틴, 과거침습, 커리어붕괴
- **Depends on:** `LORE_CHAR_Rachel_Lopez`, `SYS_EVT_Template_v2_Spec`
- **Emits:** `Flag_Memory_Rachel_MusicBox`, `Flag_Trace_Rachel_PastInvasion`, `Flag_Trace_Rachel_MelodyLoop`, `Flag_Trace_Rachel_CareerFlashback`

### ✅ `EVT_B001_Showerhair.md`
- **Title:** 물소리가 잦아드는 순간
- **ID:** `EVT_B001_ShowerHair` | **Type:** `event`
- **Summary:** 아침 샤워 루틴 중 리더가 샤워실에 진입해 레이첼의 젖은 머리카락을 씻기고 수건으로 말려주는 과정에서 스킨십이 발생하는 아지트 샤워실 개입형 이벤트. 침식도에 따라 레이첼의 반응이 절제된 수용 또는 강박 붕괴로 분기됨.
- **Keywords:** 샤워실, 레이첼, 머리카락, 수건, 깨진_거울, 침식도_분기
- **Depends on:** `LORE_CHAR_Rachel_Lopez`, `SYS_EVT_Template_v2_Spec`
- **Emits:** `Flag_Memory_Rachel_ShowerHair`, `Flag_Trace_Rachel_LeaderTouchAllowed`, `Flag_Trace_Rachel_CrackingEdge`, `Flag_Trace_Rachel_DistanceReset`, `Flag_Trace_Rachel_CollapseShame`, `Rel_Rachel_Leader_Intimacy_Up`

### ✅ `EVT_B002_VerandaCorrection.md`
- **Title:** 피스트 위의 사냥개
- **ID:** `EVT_B002_VerandaCorrection` | **Type:** `event`
- **Summary:** 아침 섀도우 펜싱 훈련 중 리더가 베란다에 진입해 레이첼의 동작을 뒤에서 교정하면서 신체 접촉이 발생하는 아지트 베란다 개입형 이벤트. 친밀도에 따라 차가운 수용, 경계 붕괴, 거리 재설정, 명령 갈구 폭발로 분기됨.
- **Keywords:** 베란다, 레이첼, 섀도우펜싱, 동작교정, 안개, 흔들의자, 친밀도_분기
- **Depends on:** `LORE_CHAR_Rachel_Lopez`, `SYS_EVT_Template_v2_Spec`
- **Emits:** `Flag_Memory_Rachel_VerandaCorrection`, `Flag_Trace_Rachel_CommandAccepted`, `Flag_Trace_Rachel_BoundaryCollapse`, `Flag_Trace_Rachel_DistanceReclaimed`, `Flag_Trace_Rachel_HungerExposed`, `Rel_Rachel_Leader_Intimacy_Up`

