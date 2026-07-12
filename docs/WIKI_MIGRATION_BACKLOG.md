# Wiki Migration Backlog

이 문서는 아직 정본 등록·이동·폐기 판단이 끝나지 않은 문서와 후속 구조 작업을 추적한다.

## 운영 원칙

- Wiki에는 게임이 직접 참조하는 정본만 둔다.
- 개발·기획·AI 도구 문서는 `docs/`에서 관리한다.
- 구형 설정이 포함된 문서는 활성 문서로 이동하지 않고 `docs/archive/`에 보존한다.
- `ConfigureBook/`은 Wiki 반영 전 콘텐츠 원고이며, 정본 등록과 검수 전 삭제하지 않는다.
- Wiki 등록 후에는 Wiki가 정본이며 ConfigureBook 원고는 수정 중단한다.
- 등록 완료 원고는 디렉터 승인 후 `ConfigureBook/Archive/Imported/`로 이동하는 것을 기본 방침으로 한다.
- `Wiki/Garbage/`는 역사적 폐기 보관소로 정식 인덱스에서 제외한다.

## Phase 2 처리 완료

- Planning 문서의 `docs/` 및 `docs/archive/` 이동
- `World_Concept.md` deprecated 전환
- 구형 `PROJECT_STATE.md` Archive
- `Entities.md` 인덱스 개편

## Phase 3 처리 완료

- 오벵마을 공식 표기·중소형 관광도시·고정 지리·고정 아지트 정본화
- ConfigureBook Import 정책 및 Tracker 작성

## Phase 4A 처리 완료

- `Wiki/02_World/Locations/`와 15개 장소 상세 문서 생성
- `Obeng_Village_Lore.md`를 상위 인덱스로 개편

## Phase 4B 처리 완료 — 중심부 4개

- 아지트, 성당, 공원, 버려진 폐가의 세부 공간·상호작용·이상현상 후보 반영

## Phase 4C 처리 완료 — 중간 지대 4개

- 마을회관, 상점가, 철물점, 경찰서의 세부 공간·상호작용·위협 후보 반영
- 공통 장소 정본과 R18 전용 요소 분리

## Phase 4D 처리 완료 — 외곽 및 외곽 심부 7개

| 대상 | 처리 결과 |
|---|---|
| `Residential_Area.md` | A/B/C동 구조, 광신도 감시, 주거지 변질 후보 반영 |
| `Nightlife_District.md` | 범죄·거래·투기장·납치 후보 반영, R18 전용 내용 분리 |
| `Dockyard.md` | 컨테이너·해안·폐선박·탈출 실패 후보 반영 |
| `Hospital.md` | 병동·수술실·영안실·의료 윤리 후보 반영 |
| `Factory.md` | 생산·배양·금고·지휘 구역 후보 반영, 인형화 게임오버·수치 보류 |
| `Department_Store.md` | 층별 전시장·테마파크·광신도 시험 후보 반영, 구형 중심부 표기 폐기 |
| `Research_Lab.md` | 연구·그릇·금단 아카이브 후보 반영, 확정 진엔딩·고유 간부·강제 침식 보류 |
| `CONFIGUREBOOK_IMPORT_TRACKER.md` | Place 원고 15개를 `Imported Candidates Added`로 갱신 |
| `PROJECT_STATE.md` | 현재 Phase를 외곽 장소 Import로 갱신 |

## 잔여 검토 대상

| 대상 | 현재 문제 | 후속 처리 |
|---|---|---|
| Place Import 종합 검토 | 후보는 반영됐으나 자원·괴물·수치·고유 인물은 미확정 | 15개 장소 후보 감사 문서 또는 검토표 작성 |
| 장소별 자원 후보 | 실제 게임 미등장 자원 후보가 섞일 수 있음 | Resource System 또는 Item DB 정리 후 등록 |
| 장소별 괴물/세력 후보 | 미확정 괴물명과 세력 후보가 섞일 수 있음 | Monster DB 및 Entity 문서 대조 후 등록 |
| 고유 NPC·보상·엔딩 후보 | ConfigureBook 원고와 최신 정본의 충돌 가능성 | Entity/Faction/Achievement/Ending 문서와 비교 |
| ConfigureBook Place 원고 | 후보 Import는 완료됐으나 최종 `Imported` 판정 전 | 검증 완료 후 Archive 이동 승인 요청 |
| `Wiki/00_Templates/EVT_NotificationTest.md` | frontmatter 없음, 테스트 샘플 | 테스트 데이터 전용 경로 또는 Archive 결정 |
| Combat 관련 문서 | 상위 문서에 세부 규칙·DB가 혼재 | 전투 허브와 세부 문서 분리 설계 |
| R18 관련 문서 | Core와 같은 폴더에 혼재 | `Wiki/90_Modules/R18/` 이동 계획 작성 |
| Survivor ConfigureBook 원고 | Wiki 등록본과 중복 가능성 | 원고별 Import 상태 조사 |
| Event 파일 | 파일명과 ID 불일치 경고 | 명명 규칙 확정 후 일괄 정리 |
| `depends_on` | 일부 미해결 참조 | 이동 완료 후 참조 검사 및 정규화 |

## 인덱스 제외 경로

```text
Wiki/Garbage/**
```

현재 보관 파일은 신규 설계의 정본으로 사용하지 않는다.
