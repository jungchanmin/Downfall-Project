---
id: MECH_R18_Memory_Log
title: "핵심 시스템 사양서 — R18 기록·변질 시스템 (메모리 로그)"
type: mechanic
status: wip
version: 2.1.0
summary: >
  R18 경험을 변질 6축과 신체부위 민감도로 누적하고, 기록·숙련·업적 단계에서
  R18 기벽의 획득·재획득·완화·고착·기술 해금을 연결하는 장기 변화 시스템.
tags:
  - mechanic
  - system
  - r18
  - memory
  - corruption
keywords:
  - R18 기록, 메모리 로그, 변질 6축, 신체부위 민감도, 기벽 고착,
    재획득, 완화, Risk & Return, 굴복 기술, 기록 보존
depends_on:
  - SYS_Manifest
  - MECH_Combat_System
  - MECH_Quirk_R18_DB
  - MECH_NPC_Stats_System
last_updated: 2026-07-14
---

# 📓 DOWNFALL R18 기록·변질 시스템 (v2.1)

> R18은 제거 가능한 확장 모듈이다. SFW 빌드에서는 본 시스템 전체를 비활성화한다.
> 성인 캐릭터에만 적용하며, 모든 로그와 해금은 NPC 개별 데이터로 저장한다.

---

## SECTION 0 — 설계 원칙

1. **2층 누적 구조**: 대분류 6축은 변질 방향, 소분류 부위 로그는 구체적인 약점과 숙련을 담당한다.
2. **기록은 삭제하지 않는다**: 기벽이 완화되거나 지속시간이 끝나도 경험 기록·해금·과거 고착 단계는 유지한다.
3. **현재 효과와 변화 이력을 분리한다**: 기벽의 활성 상태와 캐릭터가 겪은 경험은 별도 데이터다.
4. **Risk & Return 연결**: 로그 진척은 패널티뿐 아니라 R18 선택지·굴복 기술·특수 대응을 해금한다.
5. **수동 기본 + 제한적 능동**: 기본 진척은 괴물·사건 주도이며, 능동 가속은 굴복 페이즈와 양날 행동으로 제한한다.
6. **고착은 자동이 아니다**: 재획득과 임계값은 고착 후보를 만들지만, 실제 단계 상승은 기벽별 조건과 사건을 요구한다.

---

## SECTION 1 — 변질 6축

| 축 | 방향 | 대표 연결 |
|---|---|---|
| 접촉 침윤 `Contact` | 거부감 소실 | 접촉·노출·관계 반응 |
| 침범 수용 `Penetration` | 경계에서 수용으로 변화 | 감도·침범 대응 |
| 체액 동화 `Fluid` | 거부에서 의존으로 변화 | 중독·흡수·체액 기벽 |
| 변이 각인 `Mutation` | 인간 신체에서 비인간 신체로 변화 | 영구 신체 변이 |
| 인지 개변 `Cognition` | 상식과 자기인식 왜곡 | 성벽·상식 개변 |
| 결착 함락 `Subjugation` | 저항에서 굴복으로 변화 | 굴복 기술·리더 의존 |

```text
축 카운터 키: Log_R18_{Axis}
예: Log_R18_Fluid, Log_R18_Mutation
```

- 같은 침식도라도 가장 높은 축에 따라 NPC의 변화 방향이 달라진다.
- 체액·변이·인지는 우선 구현 축이다.
- 접촉·침범·함락은 동일 데이터 구조를 사용하며 콘텐츠 확충 시 세부 단계표를 추가한다.

---

## SECTION 2 — 신체부위·행위 로그

### 2-1. 기본 구조

```text
부위 카운터 키: Log_R18_{Part}_{Act}

Part:
- Mouth
- Chest
- LowerBody
- Rear
- WholeBody

Act:
- Received
- Climaxed
- Developed
- Performed
```

부위 경험치는 민감도 레벨을 산출한다.

```text
부위 경험치 누적
→ 민감도 레벨 상승
→ 같은 부위 공격의 축 진척 보정 증가
→ 감도 계열 기벽·기술 해금 후보
```

### 2-2. 전략적 양면성

- **약점화**: 개발된 부위는 같은 계열 공격과 사건에 더 취약해진다.
- **무기화**: 굴복 페이즈에서는 개발된 부위를 이용하는 기술의 효과가 강화된다.
- 플레이어는 개발을 억제할지, Risk를 감수하고 Return으로 전환할지 선택한다.

---

## SECTION 3 — 기록·숙련·업적 단계

| 단계 | 기능 | 기벽 연결 |
|---|---|---|
| 기록 `Record` | 카운터와 서사 로그만 누적 | 획득 자격·정합성 확보 |
| 숙련 `Proficiency` | 전투·사건의 제한적 양날 효과 | 일시·지속 기벽 해금 후보 |
| 업적 `Milestone` | 진행 규칙을 바꾸는 강한 변화 | 영구 기벽·고착·굴복 기술 해금 |

정확한 임계값은 밸런스 단계에서 확정한다. 문서 예시의 `3 / 5 / 8`은 초기 테스트 후보이며 정본 수치가 아니다.

---

## SECTION 4 — 기벽 획득과 정합성

### 4-1. 기벽 해금 조건

R18 기벽은 최소한 하나 이상의 관련 축 또는 부위 기록을 요구한다.

```yaml
quirk_unlock_rule:
  quirk_id:
  required_axes: []
  required_parts: []
  minimum_stage: record | proficiency | milestone
  required_flags: []
  forbidden_flags: []
  grant_mode: event | threshold | choice
```

- 관련 기록이 전혀 없는 기벽은 무작위로 부여하지 않는다.
- 영구 신체 변이는 `Mutation` 축과 관련 부위 기록을 기본 요구한다.
- 상식 개변은 `Cognition`, 굴복·복종 계열은 `Subjugation`과 연결한다.
- 하나의 기벽이 여러 축을 요구할 수 있다.

### 4-2. 획득 기록

기벽을 획득하면 다음을 저장한다.

```yaml
quirk_history_entry:
  quirk_id:
  first_acquired_at:
  last_acquired_at:
  acquisition_count:
  highest_lock_state:
  source_event_id:
  source_axis:
  source_part:
```

현재 기벽이 종료되거나 억제돼도 이 기록은 삭제하지 않는다.

---

## SECTION 5 — 재획득과 고착

### 5-1. 재획득

동일 기벽을 다시 획득하면 신규 중복 기벽을 생성하지 않고 기존 기록을 갱신한다.

```text
동일 기벽 재획득
→ acquisition_count 증가
→ 지속시간 갱신 또는 효과 단계 상승 후보
→ 관련 축·부위 로그 추가
→ 고착 판정 후보
```

### 5-2. 고착 상태

| 상태 | 의미 |
|---|---|
| `temporary` | 지속시간 종료 또는 완화가 가능한 현재 발현 |
| `persistent` | 반복 경험으로 안정화되어 단계 하향이 필요한 변화 |
| `permanent` | 일반 완화·지속 종료로 되돌릴 수 없는 장기 변화 |

### 5-3. 단계 상승 규칙

```yaml
lock_transition_rule:
  from_state: temporary | persistent
  to_state: persistent | permanent
  minimum_acquisition_count: TBD
  required_axis_stage: TBD
  required_memory_flags: []
  required_event: optional
```

- 재획득 횟수만으로 자동 영구화하지 않는다.
- 영구화에는 관련 축 숙련·업적, 특정 사건 또는 기벽별 특수 조건 중 하나 이상이 필요하다.
- `irreversible` 기벽은 최초 획득부터 `permanent`일 수 있다.
- `self_expiring` 기벽도 반복 획득과 사건 조건이 결합되면 지속형 파생 기벽으로 전환될 수 있다.

---

## SECTION 6 — 완화와 기록 보존

### 6-1. 완화 결과

| 완화 방식 | 현재 효과 | 기록 |
|---|---|---|
| `duration_reduction` | 남은 지속시간 감소 | 유지 |
| `stage_down` | 현재 고착 또는 효과 단계 하향 | 최고 도달 단계 유지 |
| `temporary_suppression` | 정해진 Risk와 Return을 함께 일시 비활성화 | 유지 |
| `none` | 완화 불가 | 유지 |

### 6-2. 영구 기벽의 일시 억제

영구 기벽의 `temporary_suppression`은 다음 원칙을 따른다.

- 기벽·외형·메모리 로그는 유지한다.
- 지정된 스탯 Risk 또는 사건 가중치를 일시 억제할 수 있다.
- 강제 선택지 잠금과 정체성 변화는 기벽별로 별도 지정한다.
- Risk가 억제되는 동안 해당 Risk에 직접 대응하는 Return도 함께 억제한다.
- 무료 버프나 영구 기벽 제거 수단으로 사용할 수 없다.

### 6-3. 역행 사건

특수 역행 사건은 현재 효과나 고착 단계를 낮출 수 있지만:

- 획득 기록과 해금 이력은 삭제하지 않는다.
- 영구 신체 변이를 일반 기벽 상태로 되돌리지 않는다.
- 새로운 대가나 다른 Risk를 부여할 수 있다.

---

## SECTION 7 — Risk & Return 해금

메모리 로그는 기벽의 Return이 언제 활성화되는지 판정한다.

```yaml
return_unlock:
  return_id:
  source_quirk:
  required_axis_stage:
  required_part_level:
  required_flags: []
  effect_owner: quirk | memory_log | skill_catalog | event
```

책임 분리:

- Quirk DB: 기벽이 가진 Risk와 Return의 종류
- Memory Log: 해금 조건과 기록
- R18 Skill Catalog: 실제 굴복 기술과 수치
- Event: 특수 선택지와 서사 결과
- Combat System: 전투 판정과 효과 적용

Return의 수치는 Skill Catalog와 Combat System 연결 후 확정한다.

---

## SECTION 8 — 괴물 성애 자제 판정

`#Trait_Xenophilic_Obsession`은 도주·기습 선택지를 완전히 차단하지 않는다.

```text
도주·기습 선택
→ 정신력 또는 자제 판정
→ 성공: 선택 수행
→ 부분 성공: 추가 스트레스·지연·침식 대가 후 수행
→ 실패: 정면 대치로 전환
```

- 괴물 조우 스트레스 면제 Return은 유지한다.
- 자제 판정의 난이도는 기벽 고착 상태와 관련 로그 단계가 높을수록 증가할 수 있다.
- 파티 전체의 선택을 한 NPC가 자동으로 봉쇄하지 않도록 한다.

---

## SECTION 9 — 구현 데이터 구조

```yaml
R18MemoryLog:
  axis_counters:
    Contact: int
    Penetration: int
    Fluid: int
    Mutation: int
    Cognition: int
    Subjugation: int
  part_exp: {}
  part_level: {}
  unlocked_milestones: []
  unlocked_returns: []
  unlocked_skills: []
  active_quirks: []
  quirk_history: []
  highest_lock_states: {}
```

```text
on_r18_experience
→ 축·부위 로그 증가
→ 부위 레벨 재계산
→ 기록·숙련·업적 단계 검사
→ 기벽 해금 조건 검사
→ 기존 기벽이면 재획득 처리
→ 고착 후보 검사
→ Return·기술 해금 검사
```

저장 데이터에서는 `active_quirks`와 `quirk_history`를 분리한다.

---

## SECTION 10 — 미확정 항목

- 축별 기록·숙련·업적 실제 임계값
- 부위 경험치와 민감도 레벨 공식
- 기벽별 실제 `memory_log_links`
- 재획득 고착 임계값
- Return과 굴복 기술의 실제 보정값
- 일시 억제의 지속시간과 비용
- 역행 사건 목록
- 접촉·침범·함락 축의 상세 단계표

---

## SECTION 11 — 콘텐츠 경계

- 성인 캐릭터에만 적용한다.
- 미성년 캐릭터에는 R18 로그·기벽·해금이 적용되지 않는다.
- SFW 빌드에서는 전체 시스템을 비활성화한다.
- 공통 게임 시스템은 이 문서에 의존하지 않는다.

---

## SECTION 12 — 버전 관리

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.0.0 | 2026-06-05 | 신체부위×행위 카운터, 양날 해금, 완화 구조 초안. |
| v2.0.0 | 2026-06-06 | 변질 6축, 부위 민감도, 기록·숙련·업적 3단 구조 도입. |
| v2.1.0 | 2026-07-14 | 기벽 획득·재획득·고착·완화 후 기록 보존, Return·기술 해금 책임 경계, 괴물 성애 자제 판정 연결. |

**갱신 기준**: 기벽별 실제 로그 키, 임계값, 굴복 기술 연결과 완화 행동이 확정되면 정본 잠금.