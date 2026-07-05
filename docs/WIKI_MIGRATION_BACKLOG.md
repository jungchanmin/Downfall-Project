# Wiki Migration Backlog

이 문서는 현재 `Wiki_Index.md`의 정식 관리 대상에 아직 편입되지 않은 레거시 문서를 추적한다.

## 운영 원칙

- 아래 문서는 존재 자체를 숨기지 않는다.
- frontmatter와 내용 정합성을 검토하기 전까지 정본 문서로 취급하지 않는다.
- 자동 검사에서는 경고 대상으로 보고하되, CI 전체를 차단하지 않는다.
- 검토 완료 후 frontmatter를 추가하고 본 목록에서 제거한다.
- `Wiki/Garbage/`는 역사적 폐기 보관소이며 정식 인덱스 대상이 아니다.

## 마이그레이션 대기 문서

| 경로 | 현재 문제 | 권장 처리 |
|---|---|---|
| `Wiki/00_System/Planning/02_Event_QA_Protocol.md` | frontmatter 없음 | 최신 QA·CI 체계와 비교 후 등록 또는 대체 |
| `Wiki/00_System/Planning/03_Downfall_PRD.md` | frontmatter 없음 | 현재 프로젝트 목표와 일치 여부 검토 후 등록 |
| `Wiki/00_System/Planning/04_Solo_Dev_AI_Tools_Tutorial.md` | frontmatter 없음 | 프로젝트 Wiki보다 `docs/`가 적합한지 검토 |
| `Wiki/00_Templates/EVT_NotificationTest.md` | frontmatter 없음 | 테스트 샘플 유지 여부 및 위치 검토 |
| `Wiki/02_World/World_Concept.md` | frontmatter 없음 | 25일 구조 및 최신 세계관과 정합성 검토 |
| `Wiki/PROJECT_STATE.md` | 구형 파일명·시스템명·진행 상태 | 최신 상태 문서로 재작성하거나 Archive 이동 |
| `Wiki/03_Entities/Entities.md` | 빈 파일 | 삭제 또는 엔티티 인덱스로 작성 |

## 인덱스 제외 경로

```text
Wiki/Garbage/**
```

현재 보관 파일:

- `Downfall_AI_Writing.md`
- `Downfall_AI_Writing_8.0.md`
- `Mental_Aliments.md`
- `Resources_Logic.md`

이 파일들은 최신 시스템 문서의 정본으로 사용하지 않는다.
