# Documentation Migration Plan

## 1. 목적

Phase 1에서 확정된 프로젝트 정본을 기준으로 Wiki에는 게임 콘텐츠 정본만 남기고, 개발·기획·AI 운영 문서는 `docs/`로 분리한다.

## 2. Phase 2 승인 결정

- `World_Concept.md`는 신규 정본에 흡수된 레거시 안내 문서로 전환한다.
- `Obeng_Village_Lore.md`는 오벵마을 상세 설정 정본으로 유지한다.
- 기존 `PROJECT_STATE.md`는 Archive로 이동하고 새 상태 문서를 작성한다.
- `Entities.md`는 엔티티 카테고리 인덱스로 개편한다.
- `ConfigureBook/`은 Wiki 등록 전 콘텐츠 원고 저장소다. 원본은 Wiki 반영과 검수 전 삭제하지 않는다.
- AI가 참고하는 개발 절차와 도구 문서는 반드시 Wiki에 있을 필요가 없다.

## 3. Phase 3 승인 결정

- 공식 한국어 표기는 `오벵마을`로 통일한다.
- 공식 영문 표기는 `Obeng Village`로 통일한다.
- 오벵마을은 중소형 관광도시다.
- 15개 주요 지역은 모두 고정한다.
- 지역의 기본 위치는 매 회차 동일하다.
- 세력 접촉 지점, 지역 이벤트, 시나리오 풀, 괴물 출현과 자원 결과는 회차 또는 날짜에 따라 변동될 수 있다.
- 아지트는 항상 고정된 장소다.
- 위험도가 낮을수록 의식의 중심부에 가깝다.
- 아지트, 성당, 버려진 폐가, 공원은 중심부 또는 중심부 근처로 본다.
- Wiki 등록 후에는 Wiki가 정본이며 ConfigureBook 원고는 수정 중단한다.
- 등록 완료 원고는 Archive 이동을 기본 방침으로 한다.
- R18 문서는 장기적으로 `Wiki/90_Modules/R18/` 아래에 모아 관리한다.
- 파일명은 영문 파일명, 본문은 한글을 기본으로 한다.

## 4. Phase 2 이동표

| 기존 경로 | 처리 | 목적지 |
|---|---|---|
| `Wiki/00_System/Planning/01_AI_Event_Pipeline_Roadmap.md` | 구형 29일 구조로 Archive | `docs/archive/ai/AI_EVENT_PIPELINE_ROADMAP_legacy.md` |
| `Wiki/00_System/Planning/02_Event_QA_Protocol.md` | 현행 CI와 재검토 전 Archive | `docs/archive/development/EVENT_QA_PROTOCOL_legacy.md` |
| `Wiki/00_System/Planning/03_Downfall_PRD.md` | 29일·구형 비전으로 Archive | `docs/archive/planning/DOWNFALL_PRD_legacy.md` |
| `Wiki/00_System/Planning/04_Solo_Dev_AI_Tools_Tutorial.md` | 운영 문서로 이동 | `docs/ai/SOLO_DEV_AI_TOOLS_TUTORIAL.md` |
| `Wiki/PROJECT_STATE.md` | 과거 기록 보존 | `docs/archive/planning/PROJECT_STATE_legacy.md` |
| `Wiki/02_World/World_Concept.md` | deprecated 안내 문서로 전환 | 기존 경로 유지 |
| `Wiki/03_Entities/Entities.md` | 정본 인덱스로 재작성 | 기존 경로 유지 |

## 5. 원고 저장소 정책

`ConfigureBook/`은 런타임에 직접 읽는 확정 데이터가 아니라, Wiki 양식으로 정제하기 전의 콘텐츠 원고다.

1. 원고 작성
2. 정본·DB·템플릿 검수
3. Wiki 또는 런타임 데이터로 등록
4. 참조 및 내용 일치 확인
5. 디렉터 승인 후에만 원본 삭제 또는 Archive

## 6. 이번 구조 개편에서 제외

- Combat 세부 문서 분리
- R18 모듈 실제 이동
- Monster DB 재구성
- Event 폴더 재편
- Survivor 전체 문서 이동
- ConfigureBook 원본 삭제 또는 이동

## 7. 완료 조건

- Wiki에서 관리·개발 문서가 제거된다.
- 레거시는 Archive에서 추적 가능하다.
- World Concept의 대체 정본 경로가 명확하다.
- Entity 분류의 진입점이 존재한다.
- 오벵마을 공식 표기와 고정 지리 원칙이 정본화된다.
- ConfigureBook 원고의 등록·Archive 정책이 문서화된다.
- 현재 프로젝트 상태를 `docs/planning/PROJECT_STATE.md`에서 확인할 수 있다.
