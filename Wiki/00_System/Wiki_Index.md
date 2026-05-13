# 🗂️ Downfall Wiki Master Index

*Auto-generated on 2026-05-13T14:21:53*  
*Total entries: 10*  
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

