# 🗂️ Downfall Wiki Master Index

*Auto-generated on 2026-06-24T12:50:42*  
*Total entries: 39*  
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
- **Summary:** EVT_Notification 의 콘텐츠 다양화·맥락 필터링·한국어 조사 처리·판정 구조를 통합한 v2 템플릿 사양. v2.1: 아이템·유물 획득 블록 확장.
- **Keywords:** 이벤트, 템플릿, 필터링, 조사, 판정, DC, 유물, 아이템, relic_acquire, item_acquire
- **Depends on:** `SYS_Manifest`, `TMPL_EVT_Notification`, `TMPL_EVT_Interactive`, `MECH_Resource_System`, `ITEM_Relic_DB`

### ✅ `QA_Refactoring_Anchor_Protocol.md` ⚠️
- **Title:** 품질 보증 및 검증 사양서 — 프론트매터 앵커 기반 사후 리팩토링 지원 프로토콜
- **ID:** `QA_R02_Post_Refactoring_Anchor_Protocol` | **Type:** `qa_protocol`
- **Summary:** 컨텍스트 한계 및 저장소 크롤링 불가를 극복하기 위해, 모든 생성 파일에  정형화된 프론트매터 앵커(Anchor) 데이터를 심고, 이를 차후 정적 분석 및  일괄 리팩토링 스크립트가 파싱할 수 있도록 지원하는 사후 검수 규칙서.


## 📁 `01_Mechanics/`

### 🟡 `MECH_Combat_System.md`
- **Title:** 핵심 시스템 사양서 — 전투 시스템 (턴제 레이드형)
- **ID:** `MECH_Combat_System` | **Type:** `mechanic`
- **Summary:** 다운폴 턴제 전투 시스템. d6 성공 풀 위에 8개 능력 스탯별 전투 커맨드(NPC 스탯 임계 해금), swarm 다수전(규모×개체체력), 거리·무기 약점·정밀타, 전투기벽, 격파/도주 이중 승리, 그리고 R18 전투 레이어(분노/흥분 게이지·성감/굴복도/의복·굴복 페이즈·전용 기술)를 규정. 코드 구현 가능한 데이터 구조·의사코드 포함.
- **Keywords:** 전투, 턴제, 전투 커맨드, 스탯별 역할, swarm, 다수전, 개방 게이지, 거리, 무기 약점, 전투기벽, 격파, 도주 락, 분노 게이지, 흥분 게이지, 성감, 굴복도, 굴복 페이즈, R18, 대사 템플릿
- **Depends on:** `SYS_Manifest`, `MECH_NPC_Stats_System`, `MECH_Resource_System`, `MONSTER_DB`, `MECH_Status_Effect_DB`, `MECH_Event_Reward_Appraisal`, `MECH_Quirk_Physical_DB`, `MECH_Quirk_Mental_DB`, `MECH_Quirk_R18_DB`

### ✅ `MECH_Event_Reward_Appraisal.md`
- **Title:** 핵심 시스템 사양서 — 이벤트 보상 책정기 (역방향 검수형)
- **ID:** `MECH_Event_Reward_Appraisal` | **Type:** `mechanic`
- **Summary:** 완성된 이벤트 출력물(텍스트·선택지)을 입력으로 받아 스탯 패널티·기벽·자원· 판정 난이도를 역방향으로 산정하는 총체적 보상 책정 사양서. 강도 밴드 가산점 모델, 패널티/보상 이중 사다리, 성패 4단 구조, 복합 스탯 판정, 기벽 계열 결정 트리를 규정. Downfall AI Assistant 모드 D(태그·보상·코드 통합)의 상세 사양서 역할.
- **Keywords:** 보상 책정, 패널티, 강도 밴드, 성패 분기, 복합 판정, 기벽 부여, 자원 보상, 난이도, DC
- **Depends on:** `SYS_Manifest`, `SYS_Downfall_AI_Assistant`, `MECH_NPC_Stats_System`, `MECH_Resource_System`, `MECH_Quirk_Physical_DB`, `MECH_Quirk_Mental_DB`, `MECH_Quirk_R18_DB`

### 🟡 `MECH_Monster_AI.md`
- **Title:** 핵심 시스템 사양서 — 괴물 행동 결정 (AI) 시스템
- **ID:** `MECH_Monster_AI` | **Type:** `mechanic`
- **Summary:** 괴물의 턴 행동 선택 로직. 괴물 전용 게이지 3종(분노·흥분·위압)이 전투 진행에 따라 누적되어 행동 분포(기본기/고유기/R18 전조/방어 빈도)를 동적으로 변화시킨다. R18 ON=흥분, OFF=위압으로 배타 적용. 분노 우선 에스컬레이션. 괴물 스타일 프로파일(신중형/호전형 등) 선호율로 개체 차별화. 정의/참조 분리 — 개체는 ai_profile 참조만.
- **Keywords:** 괴물 AI, 행동 결정, 분노 게이지, 흥분 게이지, 위압 게이지, 행동 분포, 스타일 프로파일, 신중형, 호전형, 기본 세트, 선호율, 에스컬레이션
- **Depends on:** `SYS_Manifest`, `MECH_Combat_System`, `MECH_Skill_Catalog`, `MECH_R18_Skill_Catalog`, `MECH_Status_Effect_DB`, `MONSTER_DB`

### ✅ `MECH_NPC_Stats_System.md`
- **Title:** NPC 생존자 스탯 시스템
- **ID:** `MECH_NPC_Stats_System` | **Type:** `mechanic`
- **Summary:** 다운폴 NPC 생존자의 전체 스탯 체계 정의. 기본 스탯 6종 / 능력 스탯 8종 / 감정·사회 스탯 5종 / 성격 스탯 6종. 수치 범위·상호작용·이벤트 판정 기준 포함.
- **Keywords:** 스탯, 체력, 정신력, 스트레스, 허기, 컨디션, 피로도, 전투, 탐색, 대화, 간호, 제작, 기술, 매력, 지능, 친밀도, 침식도, 판정, DC
- **Depends on:** `SYS_Manifest`, `MECH_Resource_System`

### ✅ `MECH_Quirk_Mental_DB.md`
- **Title:** 핵심 시스템 사양서 — 기벽 데이터베이스: 정신적 문제 (정신이상/욕구폭발/트라우마)
- **ID:** `MECH_Quirk_Mental_DB` | **Type:** `mechanic`
- **Summary:** 정신이상형 8종, 욕구폭발형 8종, 트라우마형 8종의 인게임 발동문 및 명확한 스탯 패널티, 간호 요구치를 정리한 정신적 기벽 마스터 데이터베이스.
- **Keywords:** 기벽, 정신적 문제, 정신이상, 욕구폭발, 트라우마, 패널티, 간호, 사치품
- **Depends on:** `SYS_Manifest`

### ✅ `MECH_Quirk_Physical_DB.md`
- **Title:** 핵심 시스템 사양서 — 기벽 데이터베이스: 육체적 문제 (신체 외/내부)
- **ID:** `MECH_Quirk_Physical_DB` | **Type:** `mechanic`
- **Summary:** 인게임 효과 발동문 규격과 정형화된 시스템 스탯 패널티, 의약품 통합 소모 규칙을 반영하여 전면 리팩토링된 육체적 기벽(외/내부 총 16종) 마스터 데이터베이스.
- **Keywords:** 기벽, 육체적 문제, 신체 외부, 신체 내부, 패널티, 간호, 의약품
- **Depends on:** `SYS_Manifest`

### ✅ `MECH_Quirk_R18.md`
- **Title:** 핵심 시스템 사양서 — R18 전용 변이 및 정신 개변 기벽 데이터베이스
- **ID:** `MECH_Quirk_R18_DB` | **Type:** `mechanic`
- **Summary:** R18 트랙과 직결되는 특수 신체 변이, 감도 개발, 성벽 및 상식 개변 기벽 24종 정의. 간호 제거를 배제하고 지속시간 및 특수 이벤트 연동형 선택지 변동 효과 탑재.
- **Keywords:** 기벽, R18, 신체 변이, 감도 개발, 성벽, 상식 개변, 침식도, 욕구불만
- **Depends on:** `SYS_Manifest`

### ✅ `MECH_R18_Disposition_System.md`
- **Title:** 핵심 시스템 사양서 — R18 성향 5대 축 및 신체 오염 시스템
- **ID:** `MECH_R18_Disposition_System` | **Type:** `mechanic`
- **Summary:** 생존자들의 심리적·성적 타락 단계를 추적하는 5대 성향 주축(Disposition Axes),  국소 부위별 성감 개발도(Anatomical Sensitivity), 육체 오염 및 도구 경험 기록 테이블의  데이터 아키텍처와 JRPG/미연시식 동적 트리거(Trigger DSL) 연동 규격을 정의한 마스터 문서.

### 🟡 `MECH_R18_Memory_Log.md`
- **Title:** 핵심 시스템 사양서 — R18 기록·변질 시스템 (메모리 로그)
- **ID:** `MECH_R18_Memory_Log` | **Type:** `mechanic`
- **Summary:** R18 경험을 변질 6축(대분류)으로 누적하고, 그 아래 신체부위 민감도(소분류·경험치형)를 곱연산으로 얹어 '개발된 부위가 약점이자 무기'가 되게 하는 시스템. 각 축은 기록→숙련→업적 3단 단계별로 텍스트 변질 묘사 + 인게임 변화(진행 규칙 수정 포함)를 발생. 진척은 괴물 주도(수동) 기본 + 굴복 페이즈·양날 커맨드로만 능동 가속. R18 기벽 DB와 해금/완화/강화 상호보완.
- **Keywords:** R18 기록, 메모리 로그, 변질 6축, 접촉, 침범, 체액, 변이, 인지, 함락, 신체부위 민감도, 경험치, 레벨, 업적, 양날, 능동 가속, 완화, 침식도
- **Depends on:** `SYS_Manifest`, `MECH_Combat_System`, `MECH_Quirk_R18_DB`, `MECH_NPC_Stats_System`

### 🟡 `MECH_R18_Skill_Catalog.md`
- **Title:** 핵심 시스템 사양서 — R18 전투 기술 카탈로그
- **ID:** `MECH_R18_Skill_Catalog` | **Type:** `mechanic`
- **Summary:** R18 전투 기술 정의의 단일 출처. 괴물 R18/굴복 커맨드(공유 풀)와 생존자 굴복 페이즈 기술 5대분류(봉사·유혹·농락·흡수·저항)를 ID로 정의. 개체/NPC는 참조만. 파일 단위로 SFW 빌드에서 제외(토글). 일반 기술 스키마(MECH_Skill_Catalog)를 확장해 R18 게이지·진척 필드를 추가.
- **Keywords:** R18 기술, 굴복 기술, 굴복 페이즈, 봉사형, 유혹형, 농락형, 흡수형, 저항형, 음담패설, 주무르기, 옷찢기, 주도권, 흥분, 성감, 진척 가속, 기술 ID
- **Depends on:** `SYS_Manifest`, `MECH_Combat_System`, `MECH_Skill_Catalog`, `MECH_R18_Memory_Log`, `MECH_Quirk_R18_DB`, `MONSTER_DB`

### ✅ `MECH_Resource_System.md`
- **Title:** 자원 체계 시스템
- **ID:** `MECH_Resource_System` | **Type:** `mechanic`
- **Summary:** 다운폴 자원 체계 전체 정의. 식량·부품·장비·유물·금화·명성· 단서·세력평판·동료 9종 자원의 역할·범위·관리 방식 정의. 이벤트별 획득·소비는 각 이벤트 파일에서 개별 관리.
- **Keywords:** 자원, 식량, 부품, 장비, 유물, 금화, 명성, 단서, 세력평판, 동료, 생존자, 암시장
- **Depends on:** `SYS_Manifest`, `MECH_NPC_Stats_System`

### 🟡 `MECH_Skill_Catalog.md`
- **Title:** 핵심 시스템 사양서 — 일반 전투 기술 카탈로그
- **ID:** `MECH_Skill_Catalog` | **Type:** `mechanic`
- **Summary:** 괴물 일반 전투 기술(약기술·공유 준강기술)의 정의 단일 출처. 개체는 본 카탈로그를 기술 ID로 참조만 한다(정의 복사 금지). 공유되는 약기술은 카탈로그 소유, 네임드 시그니처 강기술은 개체 잔류. 단순 수치는 데이터로, 복잡한 조건부 로직은 effect_id로 코드 핸들러를 가리킨다. R18 기술은 별도 MECH_R18_Skill_Catalog 가 소유.
- **Keywords:** 기술 카탈로그, 약기술, 강기술, 공유 풀, 기술 ID, 참조, effect_id, 정의, 휘두르기, 외치기, 물기, 꼬리치기, 붙잡기, 텍스트 로그, 밸런스 패치
- **Depends on:** `SYS_Manifest`, `MECH_Combat_System`, `MONSTER_DB`

### 🟡 `MECH_Status_Effect_DB.md`
- **Title:** 핵심 시스템 사양서 — 상태이상·전투기벽 데이터베이스
- **ID:** `MECH_Status_Effect_DB` | **Type:** `mechanic`
- **Summary:** 모든 상태이상·전투기벽의 정의 단일 출처(single source of truth). 일반 전투·R18·굴복 페이즈 전용을 ID 체계로 통합 관리. 기술 카탈로그·MONSTER_DB는 status_inflict 에 본 DB의 ID를 참조만 한다. 신규 상태이상 도입은 본 DB 등록 + 디렉터 승인 게이트. 중복 정의(같은 이름 다른 효과)를 원천 차단.
- **Keywords:** 상태이상, 전투기벽, 속박, 고통, 공포, 출혈, 낙인, 최면, 홀림, 광분, 타락욕망, 무방비, 비틀거림, 은신, 절정 여운, 굴복 페이즈, 단일 출처, ID 참조
- **Depends on:** `SYS_Manifest`, `MECH_Combat_System`, `MECH_Quirk_R18_DB`

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


## 📁 `03_Entities/Monsters/`

### 🟡 `MONSTER_DB.md`
- **Title:** 핵심 시스템 사양서 — 괴물 데이터베이스
- **ID:** `MONSTER_DB` | **Type:** `mechanic`
- **Summary:** 다운폴 괴물 DB. 위협 축(일반·네임드)×형태 축(인간형+비인간형 7) 2축 분류. 일반형은 원형 8종 + 파라미터로 양산(swarm 규모×개체체력), 네임드는 개별 상세. 세력 회피 훅, 보상 책정기 연계, r18_module/r18_weakness 필드. 첫 네임드 2종(거대이빨악어·잔혹한 살점포식자) 등재.
- **Keywords:** 괴물, 일반형, 네임드, 멸망, 원형, 파라미터, swarm, 규모, 적대적 생존자, 인간형, 비인간형, 거대이빨악어, 살점포식자, r18 module
- **Depends on:** `SYS_Manifest`, `MECH_NPC_Stats_System`, `MECH_Resource_System`, `MECH_Combat_System`, `MECH_Monster_AI`, `MECH_Skill_Catalog`, `MECH_R18_Skill_Catalog`, `MECH_Event_Reward_Appraisal`


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
- **Summary:** 과거 '은빛 칼날' 펜싱 국가대표였으나 동료의 사보타주로 몰락. 현재는 아지트의 '사냥개'로서 자신의 오만한 자부심을 증명하기 위해 선봉에 서는 차가운 엘리트 투사.
- **Keywords:** 레이첼, Rachel, Lopez, 사냥개, 은빛 칼날, 펜싱, 피스트, 리더
- **Depends on:** `TMPL_Universal_Survivor_Guide_Bot`
- **Emits:** `Trait_비정상적_침착함`, `Trait_펜싱_룰`, `Trait_엘리트_오만함`, `Flag_Past_Rachel_Career_Broken`, `Rel_Rachel_Leader_Blind_Devotion`


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

### ✅ `EVT_A004_EchoStep.md`
- **Title:** 한 박자 늦은 발소리
- **ID:** `EVT_A004_EchoStep` | **Type:** `event`
- **Summary:** 아침 순찰 중 레이첼이 복도에서 자신의 발소리를 정확히 한 박자 늦게 따라오는 정체불명의 소리를 감지하는 아지트 단독 돌발 이벤트. 탐색 판정에 따라 소리의 규칙을 읽어내거나 끝내 잡지 못하고 불안을 안은 채 순찰을 마침.
- **Keywords:** 복도, 레이첼, 발소리, 순찰, 마룻바닥, 엇박자
- **Depends on:** `LORE_CHAR_Rachel_Lopez`, `SYS_EVT_Template_v2_Spec`
- **Emits:** `Flag_Memory_Rachel_EchoStep`, `Flag_Trace_Rachel_CorridorUnease`, `Flag_Trace_Rachel_EchoAnalysis`, `Flag_Trace_Rachel_EchoMissed`

### ✅ `EVT_A005_CanInPocket.md`
- **Title:** 품속의 통조림
- **ID:** `EVT_A005_CanInPocket` | **Type:** `event`
- **Summary:** 아침 배급 준비 중 레이첼이 어제 저녁 먹었다고 확신하는 통조림이 개봉 흔적 없이 훈련복 품속에 그대로 들어있음을 발견하는 아지트 주방 단독 돌발 이벤트. 정신 판정에 따라 통조림을 확인하고 서랍에 돌려놓거나, 확인하지 못하고 품속에 은닉한 채 자신의 배급을 건너뜀.
- **Keywords:** 주방, 레이첼, 통조림, 기억붕괴, 배급, 식량
- **Depends on:** `LORE_CHAR_Rachel_Lopez`, `SYS_EVT_Template_v2_Spec`, `MECH_Resource_System`
- **Emits:** `Flag_Memory_Rachel_CanInPocket`, `Flag_Trace_Rachel_MemoryDoubt`, `Flag_Trace_Rachel_CanReturned`, `Flag_Trace_Rachel_CanKept`

### ✅ `EVT_A006_WashingMachineName.md`
- **Title:** 레이첼
- **ID:** `EVT_A006_WashingMachineName` | **Type:** `event`
- **Summary:** 아침 세탁 루틴 중 레이첼이 구형 세탁기 회전음 사이에서 자신의 이름을 웅얼대는 정체불명의 소리를 감지하는 아지트 세탁실 단독 돌발 이벤트. 정신 판정에 따라 세탁기를 멈추고 확인하거나 끝까지 멈추지 못하고 기다림.
- **Keywords:** 세탁실, 레이첼, 세탁기, 이름, 웅얼거림, 전투복
- **Depends on:** `LORE_CHAR_Rachel_Lopez`, `SYS_EVT_Template_v2_Spec`
- **Emits:** `Flag_Memory_Rachel_WashingMachineName`, `Flag_Trace_Rachel_NameHeard`, `Flag_Trace_Rachel_MachineOpened`, `Flag_Trace_Rachel_MachineNotOpened`

### ✅ `EVT_A007_WaterAnomaly.md`
- **Title:** 삼켜진 질감
- **ID:** `EVT_A007_WaterAnomaly` | **Type:** `event`
- **Summary:** 레이첼이 아침 루틴 중 주방에서 물을 마시다가 끈적하고 시큼한  이상 질감을 인지하고 강박적으로 삼켜낸 뒤, 잔을 내려놓자  다시 평범한 물로 돌아와 있는 것을 목격하는 아지트 단독 돌발 이벤트.
- **Keywords:** 주방, 레이첼, 물, 이상질감, 헛구역질
- **Depends on:** `LORE_CHAR_Rachel_Lopez`, `SYS_EVT_Template_v2_Spec`
- **Emits:** `Flag_Memory_Rachel_WaterAnomaly`, `Flag_Trace_Rachel_TasteDistortion`, `Flag_Trace_Rachel_Nausea_Morning`

### ✅ `EVT_A008_WallpaperHypnosis.md`
- **Title:** 격자무늬의 방
- **ID:** `EVT_A008_WallpaperHypnosis` | **Type:** `event`
- **Summary:** 레이첼이 큰방에서 아침 붕대 정비 중 벽지의 곰팡이 얼룩이  국가대표 시절의 규격을 연상시키는 격자무늬로 왜곡되는 최면 현상을 목격,  이에 종속되어 나신으로 충성 서약 및 불수의적 자위를 저지른 뒤  현실로 귀환하는 아지트 큰방 단독 돌발 이벤트.
- **Keywords:** 큰방, 레이첼, 벽지, 격자무늬, 최면, 자위
- **Depends on:** `LORE_CHAR_Rachel_Lopez`, `SYS_EVT_Template_v2_Spec`
- **Emits:** `Flag_Memory_Rachel_WallpaperHypnosis`, `Flag_Trace_Rachel_WallSubjection`, `Flag_Trace_Rachel_EgoErosion_Morning`

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

### ✅ `EVT_B003_DaggerFound.md`
- **Title:** 먼지 없는 단검
- **ID:** `EVT_B003_DaggerFound` | **Type:** `event`
- **Summary:** 아침 장비 점검 중 레이첼이 작은 다락방 잡동사니 속에서 먼지 없이 깨끗한 이계의 단검을 발견하고, 리더에게 보고할지 숨길지 선택하는 아지트 단독 돌발 이벤트. 숨기면 유물 귀속·패널티 활성화, 보고하면 단검과 기억이 동시에 소멸하는 분기.
- **Keywords:** 작은다락방, 레이첼, 단검, 유물, 대제사장, 기억소멸, 이계
- **Depends on:** `LORE_CHAR_Rachel_Lopez`, `SYS_EVT_Template_v2_Spec`, `ITEM_Relic_DB`
- **Emits:** `Flag_Memory_Rachel_DaggerFound`, `Flag_Item_HighPriestDagger_Owned`, `Flag_Item_HighPriestDagger_Reported`, `Flag_Trace_Rachel_DaggerObsession`, `Rel_Rachel_Leader_Trust_Up`

### ✅ `EVT_B004_SilentRequest.md`
- **Title:** 삼켜진 말
- **ID:** `EVT_B004_SilentRequest` | **Type:** `event`
- **Summary:** 아침 작전 회의 직전 레이첼이 리더에게 무언가를 말하려다 끝내 입을 열지 못하는 아지트 거실 개입형 이벤트. 친밀도에 따라 말을 꺼내거나 지나치는 선택이 분기되며, 친밀도 높음 시 리더가 레이첼의 단어를 완성해주는 구조.
- **Keywords:** 거실, 레이첼, 리더, 침묵, 명령갈구, 삼켜진말, 친밀도
- **Depends on:** `LORE_CHAR_Rachel_Lopez`, `SYS_EVT_Template_v2_Spec`
- **Emits:** `Flag_Memory_Rachel_SilentRequest`, `Flag_Trace_Rachel_WordsUnspoken`, `Flag_Trace_Rachel_LeaderNoticed`, `Flag_Trace_Rachel_PassedBy`, `Rel_Rachel_Leader_Intimacy_Up`

### ✅ `EVT_B005_LeaderAbsoluteCommand.md`
- **Title:** 복종의 각도
- **ID:** `EVT_B005_LeaderAbsoluteCommand` | **Type:** `event`
- **Summary:** 거실에 다른 생존자들이 존재하는 상황에서, 리더가 레이첼의 오만한  자존심을 꺾기 위해 나신 노출 및 가학적 굴욕 명령을 내리고,  레이첼이 강박적 통제력과 복종심 사이에서 무너지는 R18 구역 이벤트.
- **Keywords:** 레이첼, 리더, 거실, 복종, 나신, 가학
- **Depends on:** `LORE_CHAR_Rachel_Lopez`, `SYS_EVT_Template_v2_Spec`
- **Emits:** `Flag_Memory_Rachel_PublicHumiliation`, `Flag_Trace_Rachel_SubmissiveScar`

### ✅ `EVT_B006_BasementInterrogation.md` ⚠️
- **Title:** 아침의 철장 — 지하실 심문 트랙
- **ID:** `EVT_B022_BasementInterrogation` | **Type:** `event_track_b`
- **Summary:** 아침 배급 직전, 물자 도난 혐의로 지하실 의자에 결박된 레이첼을 리더가 심문하는 R18 트랙 개입형 이벤트. 레이첼은 물리적 명령에 복종하여 나신으로 결박당하면서도, 거짓 자백을 거부하고 투지로 버티는 분기와 굴복하여 거짓으로 맹세하는 분기로 대치됨.
- **Keywords:** 레이첼, 리더, 지하실, 심문, 나신, 가학, 결박
- **Depends on:** `LORE_CHAR_Rachel_Lopez`, `SYS_EVT_Template_v2_Spec`

