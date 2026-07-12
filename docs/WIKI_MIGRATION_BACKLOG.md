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

- Planning 문서의 docs/archive 이동
- World Concept deprecated 전환
- Project State 재작성
- Entity 인덱스 개편

## Phase 3 처리 완료

- 오벵마을 공식 표기, 중소형 관광도시, 고정 지리, 고정 아지트 원칙 반영
- ConfigureBook Import 정책과 Tracker 작성

## Phase 4A 처리 완료

- `Wiki/02_World/Locations/LOCATION_INDEX.md` 작성
- 15개 고정 지역의 상세 문서 생성
- `Obeng_Village_Lore.md`를 상위 인덱스로 개편

## Phase 4B 처리 완료

- 아지트, 성당, 공원, 버려진 폐가 세부 Import
- 중심부 4개 원고 상태를 `Imported Candidates Added`로 갱신

## Phase 4C 처리 완료

- 마을회관, 상점가, 철물점, 경찰서 세부 Import
- 중간 지대 4개 원고 상태를 `Imported Candidates Added`로 갱신

## Phase 4D 처리 완료

- 주거단지, 유흥가, 선착장, 병원, 공장, 백화점, 연구소 세부 Import
- 외곽 7개 원고 상태를 `Imported Candidates Added`로 갱신
- 백화점의 구형 `중심부` 표현을 현행 정본과 충돌하는 내용으로 폐기
- 연구소의 플레이어 괴물화, 미확정 진엔딩, 고유 악신 설정을 미승인 충돌 항목으로 보류
- 유흥가·공장 원고의 노골적 R18 요소를 공통 장소 정본과 분리

## 잔여 검토 대상

| 대상 | 현재 문제 | 후속 처리 |
|---|---|---|
| Place 원고 15개 | 공간·상호작용·이상현상 후보 반영 완료, DB 검증 미완료 | Archive 이동 승인 여부 판단 |
| 장소별 자원 후보 | 실제 게임 미등장 자원이 섞일 수 있음 | Resource System 또는 Item DB 정리 후 등록 |
| 장소별 괴물/세력 후보 | 미확정 괴물명과 세력 후보가 섞일 수 있음 | Monster DB 및 Entity 문서 대조 후 등록 |
| 연구소 충돌 설정 | 플레이어 괴물화·미확정 진엔딩·고유 악신 설정 | 별도 검토 및 디렉터 승인 없이는 사용 금지 |
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
