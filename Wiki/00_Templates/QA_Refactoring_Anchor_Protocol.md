---
id: QA_R02_Post_Refactoring_Anchor_Protocol
title: 품질 보증 및 검증 사양서 — 프론트매터 앵커 기반 사후 리팩토링 지원 프로토콜
type: template
status: complete
version: 1.2.0
summary: >
  컨텍스트 한계 및 저장소 크롤링 불가를 극복하기 위해, 모든 생성 파일에 
  정형화된 프론트매터 앵커(Anchor) 데이터를 심고, 이를 차후 정적 분석 및 
  일괄 리팩토링 스크립트가 파싱할 수 있도록 지원하는 사후 검수 규칙서.
tags: [qa, workflow, frontmatter, refactoring, code_generation]
last_updated: 2026-05-29
---

# 🛡️ DOWNFALL 사후 리팩토링 앵커 프로토콜 (v1.2)

## 01. 아키텍처 프레임워크 (Framework Concept)

본 프로토콜은 AI 파트너의 저장소 직접 수정 불가능성과 컨텍스트 제약을 극복한다. 

개발 단계에서 생성되는 모든 데이터, 이벤트, 로어 파일의 최상단에 **[표준화된 프론트매터(Frontmatter)]**를 엄격하게 부착한다. 이 프론트매터는 단순한 문서 요약이 아니라, 차후 디렉터가 로컬 개발 환경에서 파이썬(Python) 등 정적 분석 스크립트를 가동하여 **프로젝트 전체의 태그 오염을 추적하고, 변수명을 일괄 치환(Refactoring)할 수 있게 만드는 '정적 데이터 앵커(Anchor)'** 역할을 수행한다.

---

## 02. 프론트매터 앵커 표준 규격 (Standard Frontmatter Spec)

AI 파트너가 산출하는 모든 마크다운 파일은 예외 없이 아래 규격을 준수해야 한다. 사후 정적 분석기가 이 블록을 유기적으로 파싱하여 정형 데이터베이스로 변환할 수 있도록 엄격한 key-value 구조를 유지한다.

```yaml
---
id: [FILE_UNIQUE_ID]
title: [문서의 국문 명칭]
type: [event_track_a | event_track_b | lore_char | lore_world | mechanic]
status: complete
version: 1.0.0
summary: >
  문서 내용 요약 (정적 분석기가 맥락을 필터링할 때 참조)
runtime_dependencies:
  stats: [ #Stat_Submission, #Stat_Rationality ]  # 본 파일이 인용하는 동적 스탯 락
  traits: [ #Trait_Fencing_Rule ]                 # 본 파일이 인용하는 기벽 식별자 락
  locations: [ #Loc_아지트_거실_B2 ]              # 본 파일이 구속되는 장소 식별자 락
  flags: [ #Flag_Memory_Rachel_RibbonAnomaly ]   # 본 파일이 방출/참조하는 플래그 락
last_updated: 2026-05-29
---

```

### 락(Lock) 매커니즘의 기능

* `runtime_dependencies` 하위의 데이터는 차후 정적 분석 스크립트가 전체 프로젝트 폴더를 순회할 때 "어떤 파일이 오염된 임의 태그를 사용하고 있는가?"를 100% 찾아낼 수 있는 파싱 지점이 된다.

---

## 03. 사후 검수 및 리팩토링 스크립트 연동 프로세스

```
[AI 개발 세션] -> 임의의 변수가 포함된 표준 프론트매터 마크다운 파일 출력
                      │
                      ▼
[디렉터 로컬 환경] -> 파편화된 마크다운 파일들을 로컬 저장소에 세이브
                      │
                      ▼
[사후 검수 가동] -> 디렉터가 정적 분석 파이썬 스크립트(Parser) 구동
                      │
                      ▼
[정형 데이터 추출] -> 스크립트가 모든 파일의 runtime_dependencies 블록을 취합
                      │ (오염되거나 새로 도입된 스탯/태그/용어 일괄 리스트업)
                      ▼
[일괄 리팩토링] -> 디렉터가 확정한 정제 맵핑 데이터에 따라, 
                      스크립트가 로컬 파일 내 변수명을 일괄 치환(Find & Replace)

```

---

## 04. AI 파트너의 '사후 리팩토링 지원 리포트' 책무

특정 세션이 끝나거나 디렉터의 요청이 있을 때, AI 파트너는 새로운 프론트매터 구조를 기반으로 '정적 스크립트에 주입할 마이그레이션 데이터 블록'을 다음과 같이 정형화하여 출력해야 한다.

```json
{
  "audit_session": "2026-05-29_Batch",
  "detected_new_atoms": {
    "stats": ["#Stat_Anus_EXP"],
    "locations": ["#Loc_Cathedral_Abyss"],
    "flags": ["#Flag_Memory_Rachel_ShowerHair"]
  },
  "refactoring_mapping_hint": {
    "search_target": "#Stat_Anus_EXP",
    "replace_recommand": "#Stat_Mouth_EXP_Or_Unified_Erosion",
    "reason": "기존 스탯 스키마 오염 방지를 위해 차후 로컬 스크립트로 일괄 치환할 것을 권장함."
  }
}

```

* 디렉터는 이 JSON 블록을 그대로 로컬 리팩토링 툴의 구성 파일(config.json)로 사용하여 정제 작업을 자동화할 수 있다.

---

## 05. 형상 관리 및 커밋 규칙

* **문서 위치**: `00_Templates/QA_Refactoring_Anchor_Protocol.md`
* **커밋 메시지**: `chore(qa): implement frontmatter anchor specification for post-refactoring static analysis`
* **Wiki_Index.md 갱신 필요 여부**: **필요 (YES)**

```

---