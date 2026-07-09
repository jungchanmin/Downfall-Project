# Wiki Migration Backlog

이 문서는 아직 정본 등록·이동·폐기 판단이 끝나지 않은 문서와 후속 구조 작업을 추적한다.

## 운영 원칙

- Wiki에는 게임이 직접 참조하는 정본만 둔다.
- 개발·기획·AI 도구 문서는 `docs/`에서 관리한다.
- 구형 설정이 포함된 문서는 활성 문서로 이동하지 않고 `docs/archive/`에 보존한다.
- `ConfigureBook/`은 Wiki 반영 전 콘텐츠 원고이며, 정본 등록과 검수 전 삭제하지 않는다.
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

## 신규 관리 문서

- `docs/governance/DOCUMENTATION_MIGRATION_PLAN.md`
- `docs/planning/PROJECT_STATE.md`

## 잔여 검토 대상

| 대상 | 현재 문제 | 후속 처리 |
|---|---|---|
| `Wiki/00_Templates/EVT_NotificationTest.md` | frontmatter 없음, 테스트 샘플 | 테스트 데이터 전용 경로 또는 Archive 결정 |
| `Wiki/02_World/Obeng_Village_Lore.md` | 구형 명칭·세계관과 일부 충돌 가능 | 신규 정본과 충돌표 작성 후 상세 정본으로 보정 |
| Combat 관련 문서 | 상위 문서에 세부 규칙·DB가 혼재 | 전투 허브와 세부 문서 분리 설계 |
| R18 관련 문서 | Core와 같은 폴더에 혼재 | `Wiki/90_Modules/R18/` 이동 계획 작성 |
| ConfigureBook | 원고와 Wiki 등록본의 대응표 없음 | 원고 등록 상태 추적표 설계 |
| Event 파일 | 파일명과 ID 불일치 경고 | 명명 규칙 확정 후 일괄 정리 |
| `depends_on` | 일부 미해결 참조 | 이동 완료 후 참조 검사 및 정규화 |

## 인덱스 제외 경로

```text
Wiki/Garbage/**
```

현재 보관 파일은 신규 설계의 정본으로 사용하지 않는다.
