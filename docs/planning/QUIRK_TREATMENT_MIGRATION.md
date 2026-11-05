# 기벽 치료 데이터 마이그레이션 메모

## 1. 목적

기존 일반·R18 기벽 DB를 `MECH_Quirk_Treatment_System`의 필드로 옮길 때 사용할 기본 분류와 충돌 항목을 기록한다.

이 문서는 정본 DB가 아니라 마이그레이션 검토용이다.

## 2. 일반 기벽 기본값

| 계열 | 기본 treatment_model | 기본 treatment_grade | 시설 방향 |
|---|---|---|---|
| 신체 외부 | removable | easy~hard | 의무실·위생실 |
| 신체 내부 | removable | hard~professional | 의무실·전문 의료장비·회복실 |
| 정신이상 | removable | normal~professional | 상담실·회복실 |
| 욕구폭발·충동 | removable | easy~hard | 상담실·기호품·관계 행동 |
| 트라우마 | removable | normal~hard | 상담실·특수 관계·사건 |

예외 기벽은 `special` 또는 `irreversible`로 개별 지정한다.

## 3. R18 기벽 기본값

| 계열 | 기본 treatment_model | 기본 lock_state | 완화 방향 |
|---|---|---|---|
| 신체 개조 | irreversible | permanent | 원칙적으로 없음, 특수 사건 예외 |
| 감도 개발 | suppressible 또는 irreversible | persistent~permanent | 단계 하향·일시 억제 |
| 내구성 | suppressible 또는 irreversible | persistent~permanent | Risk 효과 일부 억제 |
| 성벽 | irreversible | permanent | Return/Risk 조정만 가능 |
| 상식 개변 | suppressible 또는 irreversible | persistent~permanent | 일시 억제·고착 지연 |
| 욕구 | self_expiring 또는 suppressible | temporary~persistent | 지속시간 감소·일시 안정 |

## 4. 메모리 로그 연결 원칙

- 완화 또는 지속시간 종료 후에도 경험 카운터와 해금 특성은 유지한다.
- 같은 기벽을 반복 획득하면 고착 단계가 상승할 수 있다.
- 고착된 기벽은 `irreversible`로 승격될 수 있다.
- R18 기벽 제거를 보상으로 제공하지 않는다.
- 특수 제거 사건이 존재해도 기록과 해금은 초기화하지 않는다.

## 5. 기존 문서 충돌

### 5.1 일반 기벽

- `간호 요구치`가 난이도와 자원 요구를 한 필드에 혼합하고 있다.
- 일반 의약품과 전문 의료품 구분이 부족하다.
- 일부 정신 기벽은 `사치품`을 치료 자원과 임시 억제 자원으로 혼용한다.
- 삭제되었거나 재검토 중인 스탯 참조가 남아 있다.
- 부분 성공과 실패 비용이 정의되지 않았다.

### 5.2 R18 기벽

- `지속시간`과 `영구 변이`는 존재하지만 고착 단계가 없다.
- Risk와 Return이 별도 필드로 분리되지 않았다.
- `mitigable` 불리언만으로 완화 방식과 범위를 표현하기 어렵다.
- 일부 기벽은 순수 패널티에 가까워 Risk & Return 재검토가 필요하다.
- 메모리 로그 카운터와 개별 기벽의 실제 해금 조건이 대부분 미확정이다.

## 6. 권장 마이그레이션 순서

1. 일반 기벽 DB에 공통 `quirk_treatment` 필드 추가
2. 기존 `간호 요구치`를 새 필드로 이동
3. 삭제·변경 스탯 참조 정리
4. R18 기벽에 `risk_effects`, `return_effects`, `mitigation_model`, `lock_state` 추가
5. 메모리 로그 해금 조건과 고착 임계값 연결
6. 실제 치료·완화 수치 밸런스 테스트

## 7. 이번 단계에서 확정하지 않는 내용

- 개별 일반 기벽의 실제 의료품 이름과 수량
- 치료 DC
- 부분 성공 수치
- R18 기벽별 최종 Risk & Return
- 고착 임계값
- 특수 제거·역행 이벤트 목록
