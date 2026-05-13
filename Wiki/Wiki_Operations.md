# 🛠️ Wiki Operations: Frontmatter Generator

## 1. 목적 (Purpose)
이 문서는 업로드된 원시 위키 문서(Markdown)의 본문을 분석하여, Downfall 프로젝트의 표준화된 YAML 프론트매터(Frontmatter) 블록을 자동 생성하기 위한 AI 지시서(Prompt Guideline)입니다.

## 2. 작동 지시사항 (Instructions for AI)
제출된 위키 문서의 내용을 깊이 분석하고, 아래의 **필드 작성 규칙**을 엄격히 준수하여 프론트매터 9개 필드를 추론 및 작성하십시오.

### 🔧 필드별 작성 규칙
* **`id`** (식별자): 파일명이 변경되어도 유지되는 고유 앵커.
    * 규칙: `[TYPE_PREFIX]_[Name]` 형식 준수.
    * 접두사(Prefix) 허용 목록: `SYS_`, `TMPL_`, `MECH_`, `LORE_LOC_`, `LORE_CHAR_`, `LORE_FAC_`, `EVT_`, `PLAN_`, `LOG_`
* **`title`** (제목): 문서의 핵심 주제를 나타내는 직관적인 제목.
* **`type`** (분류): 문서의 성격에 맞는 단일 카테고리.
    * 허용 목록: `system`, `template`, `mechanic`, `lore_world`, `lore_char`, `lore_faction`, `event`, `planning`, `log`
* **`status`** (상태): 문서의 완성도.
    * 허용 목록: `draft` (초안) | `wip` (작업 중) | `complete` (완성) | `deprecated` (폐기)
* **`summary`** (요약) ⭐ **가장 중요**:
    * AI 컨베이어 벨트가 이 문서의 필요성을 판단하는 유일한 근거입니다.
    * 반드시 **1~2문장**으로 문서의 핵심 내용과 목적을 압축하여 작성하십시오. (예: "오뱅마을 15개 구역의 분위기·위험도·고유 이벤트 시드.")
* **`tags`** (태그): 문서를 분류하는 대분류 키워드 배열. (예: `[lore, world, location, oebeng]`)
* **`keywords`** (키워드): 검색 매칭을 위한 구체적인 등장인물, 장소, 개념어 배열.
* **`depends_on`** (종속성): 이 문서가 논리적으로 의존하는 다른 위키 문서의 `id` 배열. (파일 경로 금지, 오직 `id`만 기재)
* **`emits`** (발행): 이 문서에서 파생되거나 발행하는 상태값 배열. Gate C의 Orphan Flag 검출에 사용됩니다. (예: `#Flag_Memory_...`, `#Rel_...`)
* **`last_updated`** (갱신일): `YYYY-MM-DD` 형식의 현재 날짜.

## 3. 반환 형식 (Output Format)
분석이 완료되면, 어떠한 부가 설명이나 인사말도 덧붙이지 말고 **오직 아래의 YAML 코드 블록 형태만 정확히 반환**하십시오.

```yaml
---
id: [TYPE_PREFIX]_[Name]
title: [문서 제목]
type: [허용된 type 중 택 1]
status: [허용된 status 중 택 1]
summary: [1~2문장으로 압축된 핵심 요약]
tags: [tag1, tag2, ...]
keywords: [keyword1, keyword2, ...]
depends_on: [Ref_ID1, Ref_ID2, ...]
emits: [Flag1, Flag2, ...]
last_updated: YYYY-MM-DD
---