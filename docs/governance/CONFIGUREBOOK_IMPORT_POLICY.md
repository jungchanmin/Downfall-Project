# ConfigureBook Import Policy

## 1. 목적

`ConfigureBook/`은 Wiki 양식에 맞춰 등록되기 전의 콘텐츠 원고 저장소다. 이 문서는 원고가 언제 정본으로 승격되고, 승격 후 원본을 어떻게 처리하는지 정의한다.

## 2. 기본 원칙

- Wiki가 정본이다.
- `ConfigureBook/`은 원고다.
- Wiki 등록 후에는 해당 원고를 수정하지 않는다.
- 원고와 Wiki 등록본을 동시에 수정하지 않는다.
- 원고 삭제와 Archive 이동은 디렉터 승인 후에만 수행한다.

## 3. 원고 상태

| 상태 | 의미 |
|---|---|
| Draft | 아직 Wiki에 등록되지 않은 원고 |
| Reviewing | Wiki 등록 후보로 검토 중인 원고 |
| Imported | Wiki 또는 런타임 데이터에 등록된 원고 |
| Superseded | 더 최신 정본에 의해 대체된 원고 |
| Archived | 보존 목적으로 Archive된 원고 |

## 4. 등록 절차

1. 원고 작성
2. 기존 정본·DB·템플릿과 충돌 검사
3. Wiki 양식으로 변환
4. Wiki 문서 또는 런타임 데이터로 등록
5. 원고와 등록본 대응표 갱신
6. 디렉터 검수
7. `ConfigureBook/Archive/Imported/`로 이동 또는 보존 결정

## 5. 충돌 규칙

Wiki 등록본과 ConfigureBook 원고가 충돌하면 Wiki를 우선한다.

단, ConfigureBook 원고에 Wiki에 반영되지 않은 유용한 묘사나 세부 공간이 남아 있다면 삭제하지 않고 누락 후보로 기록한다.

## 6. 경로 정책

- 장소 원고: `ConfigureBook/Place/`
- 생존자 원고: `ConfigureBook/Survivors/`
- 이벤트 원고: `ConfigureBook/Events/`
- 등록 완료 원고 권장 Archive: `ConfigureBook/Archive/Imported/`

## 7. 후속 작업

- 원고와 Wiki 등록본의 1:1 대응표 작성
- 장소 원고부터 Import 상태 판정
- 생존자 원고의 Wiki 등록률 조사
- 이벤트 원고의 ID·파일명 정규화
