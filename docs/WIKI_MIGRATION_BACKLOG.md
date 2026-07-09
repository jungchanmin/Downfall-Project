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

## 신규 관리 문서

- `docs/governance/DOCUMENTATION_MIGRATION_PLAN.md`
- `docs/governance/CONFIGUREBOOK_IMPORT_POLICY.md`
- `docs/planning/PROJECT_STATE.md`
- `docs/planning/CONFIGUREBOOK_IMPORT_TRACKER.md`

## 잔여 검토 대상

| 대상 | 현재 문제 | 후속 처리 |
|---|---|---|
| `Wiki/00_Templates/EVT_NotificationTest.md` | frontmatter 없음, 테스트 샘플 | 테스트 데이터 전용 경로 또는 Archive 결정 |
| 장소 세부 원고 | Wiki 정본에 세부 공간과 이상현상 시드가 모두 반영되지는 않음 | Place 원고별 세부 Import 여부 결정 |
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
