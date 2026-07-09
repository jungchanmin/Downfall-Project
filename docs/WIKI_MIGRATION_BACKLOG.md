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

| 기존 경로 | 처리 결과 |
|---|---|
| `Wiki/00_System/Planning/01_AI_Event_Pipeline_Roadmap.md` | `docs/archive/ai/AI_EVENT_PIPELINE_ROADMAP_legacy.md` |
| `Wiki/00_System/Planning/02_Event_QA_Protocol.md` | `docs/archive/development/EVENT_QA_PROTOCOL_legacy.md` |
| `Wiki/00_System/Planning/03_Downfall_PRD.md` | `docs/archive/planning/DOWNFALL_PRD_legacy.md` |
| `Wiki/00_System/Planning/04_Solo_Dev_AI_Tools_Tutorial.md` | `docs/ai/SOLO_DEV_AI_TOOLS_TUTORIAL.md` |
| `Wiki/02_World/World_Concept.md` | deprecated 대체 문서 안내로 전환 |
| `Wiki/PROJECT_STATE.md` | `docs/archive/planning/PROJECT_STATE_legacy.md`로 보존 |
| `Wiki/03_Entities/Entities.md` | 정본 엔티티 인덱스로 개편 |

## Phase 3 처리 완료

| 대상 | 처리 결과 |
|---|---|
| `Wiki/02_World/WORLD_OVERVIEW.md` | 오벵마을 공식 표기, 중소형 관광도시, 고정 지리, 고정 아지트 원칙 반영 |
| `Wiki/02_World/Obeng_Village_Lore.md` | 오벵마을 표기 통일, 15개 고정 지역, 중심성·위험도 정리 |
| `docs/governance/CONFIGUREBOOK_IMPORT_POLICY.md` | ConfigureBook 원고 등록·Archive 정책 작성 |
| `docs/planning/CONFIGUREBOOK_IMPORT_TRACKER.md` | 원고와 Wiki 등록본 대응표 초안 작성 |
| `docs/governance/DOCUMENTATION_MIGRATION_PLAN.md` | Phase 3 결정사항 반영 |
| `docs/planning/PROJECT_STATE.md` | 현재 Phase를 오벵마을 정합성 단계로 갱신 |

## Phase 4A 처리 완료

| 대상 | 처리 결과 |
|---|---|
| `Wiki/02_World/Locations/LOCATION_INDEX.md` | 15개 장소 상세 문서 인덱스 생성 |
| `Wiki/02_World/Locations/*.md` | 15개 고정 지역의 상세 문서 생성 |
| `Wiki/02_World/Obeng_Village_Lore.md` | 상위 인덱스 역할로 축소하고 상세 문서 링크 추가 |
| `docs/planning/CONFIGUREBOOK_IMPORT_TRACKER.md` | Place 원고 상태를 `Partially Imported`로 갱신 |
| `docs/planning/PROJECT_STATE.md` | 현재 Phase를 장소 상세 문서 분리 단계로 갱신 |

## Phase 4B 처리 완료

| 대상 | 처리 결과 |
|---|---|
| `Wiki/02_World/Locations/Hideout.md` | 아지트 원고의 세부 공간·상호작용·이상현상 후보 반영 |
| `Wiki/02_World/Locations/Cathedral.md` | 성당 원고의 지상·지하 금기 구역 후보 반영 |
| `Wiki/02_World/Locations/Foggy_Park.md` | 공원 원고의 방랑자 캠프·안개·호수·온실 후보 반영 |
| `Wiki/02_World/Locations/Abandoned_Cabins.md` | 폐가 원고의 납치·함정·폐가 내부 후보 반영 |
| `docs/planning/CONFIGUREBOOK_IMPORT_TRACKER.md` | 중심부 4개 원고 상태를 `Imported Candidates Added`로 갱신 |
| `docs/planning/PROJECT_STATE.md` | 현재 Phase를 중심부 장소 원고 세부 Import로 갱신 |

## 신규 관리 문서

- `docs/governance/DOCUMENTATION_MIGRATION_PLAN.md`
- `docs/governance/CONFIGUREBOOK_IMPORT_POLICY.md`
- `docs/planning/PROJECT_STATE.md`
- `docs/planning/CONFIGUREBOOK_IMPORT_TRACKER.md`

## 잔여 검토 대상

| 대상 | 현재 문제 | 후속 처리 |
|---|---|---|
| `Wiki/00_Templates/EVT_NotificationTest.md` | frontmatter 없음, 테스트 샘플 | 테스트 데이터 전용 경로 또는 Archive 결정 |
| 장소별 자원 후보 | ConfigureBook 원고에 실제 게임 미등장 자원 후보가 섞일 수 있음 | Resource System 또는 Item DB 정리 후 장소별 후보 등록 |
| 장소별 괴물/세력 후보 | ConfigureBook 원고에 미확정 괴물명과 세력 후보가 섞일 수 있음 | Monster DB 및 Entity 문서 대조 후 등록 |
| 중간 지대 Place 원고 | 세부 공간·상호작용·이상현상 후보가 아직 미반영 | Town Hall, Shopping District, Hardware Store, Police Station Import 패스 수행 |
| 외곽 Place 원고 | 세부 공간·상호작용·이상현상 후보가 아직 미반영 | Residential Area 이후 외곽 Import 패스 수행 |
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
