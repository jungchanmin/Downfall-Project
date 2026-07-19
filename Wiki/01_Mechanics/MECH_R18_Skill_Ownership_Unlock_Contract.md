---
id: MECH_R18_Skill_Ownership_Unlock_Contract
title: "핵심 시스템 사양서 — R18 기술 소유·해금·괴물 키트 계약"
type: mechanic
status: wip
version: 1.0.0
summary: >
  생존자별 개별 굴복 기술 소유, 초기 기술, 학습·숙련·기벽 변종 해금과
  괴물별 고정 기술 키트·쿨타임·전조·게이팅·카운터 태그를 정의한다.
tags: [mechanic, r18, skill, ownership, unlock, monster_kit]
depends_on:
  - MECH_R18_Submission_Core_System
  - MECH_R18_Skill_Access_And_Recall_System
  - MECH_R18_Telegraph_Bark_Content_Policy
  - MECH_R18_Memory_Log
  - MECH_Quirk_R18_DB
  - MONSTER_DB
last_updated: 2026-07-15
---

# R18 기술 소유·해금·괴물 키트 계약 v1.0

## 1. 핵심 분리 원칙

```text
커맨드 분류
≠ 실제 기술
≠ 캐릭터 보유 기술
```

- `Service / Tease / Domination / Absorption / Defiance`는 전술 역할 분류다.
- 실제 행동은 개별 `skill_id`로 정의한다.
- 생존자와 괴물은 각자 보유한 기술만 사용한다.
- 학습한 기술은 장착 제한 없이 계속 보유한다.
- 현재 상황에 적합한 기술을 UI가 우선 노출한다.

---

## 2. 생존자 기술 소유 데이터

```yaml
SurvivorSubmissionSkillState:
  survivor_id: str

  known_skills: [SkillId]
  initial_skills: [SkillId]
  learned_skills: [SkillId]
  signature_skills: [SkillId]

  category_proficiency:
    Service: int
    Tease: int
    Domination: int
    Absorption: int
    Defiance: int

  skill_proficiency:
    SkillId: int

  preparation_focus:
    category: null | Service | Tease | Domination | Absorption | Defiance
    skill_id: null | SkillId
```

`known_skills`는 현재 사용할 수 있는 전체 기술 목록이다. `preparation_focus`는 사용 권한을 제한하지 않고 첫 사용 안정성·우선 노출·전조 연계 후보만 제공한다.

---

## 3. 초기 기술 결정

초기 기술은 다음 출처를 조합한다.

- 직업·경력
- 능력 스탯
- 신체 훈련
- 성격·행동 성향
- 배경 플래그
- 시작 시점의 Memory Log
- 시작 기벽 또는 고유 상태

```yaml
InitialSkillGrantRule:
  rule_id: str
  required_background_flags: []
  required_stats: {}
  preferred_categories: []
  grant_skills: []
  fallback_skills: []
```

현재 권장 초기 범위는 생존자당 2~4개 기술이다. 최종 수치는 캐릭터별 대응 공백 검증 후 확정한다.

모든 생존자는 기술과 별도로 다음 공용 안전 행동을 가진다.

- 버티기
- 거리 벌리기
- 도움 요청
- 교대 요청
- 행동 포기

---

## 4. 기술 정의 계약

```yaml
SubmissionSkillDef:
  skill_id: str
  display_name: str
  side: survivor | monster

  command_category: null | Service | Tease | Domination | Absorption | Defiance
  attack_axis: null | Contact | Penetration | Fluid | Mutation | Cognition | Subjugation

  base_power: int
  accuracy_profile: stable | normal | risky
  self_cost: {}
  cooldown_turns: int

  valid_postures: []
  required_target_parts: []
  required_action_parts: []
  forbidden_statuses: []
  required_conditions: []

  gate_attack:
    posture_force: null | PostureKey
    occupy_target_parts: []
    occupy_action_parts: []
    gate_tags: []

  counter_profile:
    counter_tags: []
    counter_axes: []
    counter_result: none | mitigate | cancel | reverse

  initiative_effects: []
  status_effects: []
  progress_axis: null | R18Axis
  progress_part: null | R18PartKey

  telegraph_profile_id: null | TelegraphProfileId
  effect_ids: []
```

### 4-1. 기본 위력

최종 위력은 다음 요소를 합성한다.

```text
기술 기본 위력
+ 분류 숙련
+ 기술 숙련
+ 관련 능력
+ Memory Log·부위 경험
+ 기벽 Return
+ 자세·전조 적합
+ 상태 보정
- 자기 부담·피로·봉쇄
```

기술 자체의 기본 위력이 먼저 존재하며 기벽과 로그는 이를 보완·변형한다.

---

## 5. Tease 게이팅 카운터 계약

Tease는 특정 공격축 전체의 자동 강상성이 아니다.

```text
Tease 분류
→ 자세·부위·행동 점유 시도를 패링할 수 있는 전술 자격

개별 Tease 기술
→ 실제로 카운터할 수 있는 gate tag 범위
```

### 5-1. 카운터 성립

```text
상대 기술 gate_tags
∩
Tease 기술 counter_tags
≠ 공집합
```

이고, 사용 부위·자세 게이트를 통과해야 패링 판정이 발생한다.

```yaml
# 괴물 붙잡기 기술
attack_axis: Contact
gate_attack:
  posture_force: Front
  occupy_target_parts: [Chest]
  occupy_action_parts: [Hand]
  gate_tags:
    - CloseDistance
    - FrontalGrab
    - ChestTarget

# 생존자 Tease 기술
command_category: Tease
counter_profile:
  counter_tags:
    - FrontalGrab
    - ChestTarget
  counter_result: reverse
```

### 5-2. 결과

- 태그 일치 + 성공: 공격 취소·확정 주도권 탈취
- 태그 일부 일치: 피해 완화 또는 불완전 패링 후보
- 태그 불일치: Tease 기술이어도 카운터 불가
- 완전 구속·행동 부위 봉쇄: 기술 자체 사용 불가

축 상성은 카운터 성립 여부가 아니라 추가 보정·로그·효과 친화도를 담당한다.

---

## 6. 기술 해금 출처

### 6-1. 일반 학습

```yaml
SkillUnlockRule:
  skill_id: SkillId
  any_of:
    - all_of:
        - category_proficiency: {}
        - skill_observation_flags: []
        - memory_axis_stage: {}
        - part_level: {}
        - background_flags: []
        - trainer_flags: []
```

### 6-2. 관찰·피격·카운터 기록

괴물의 특정 기술을 반복 관찰하거나 직접 피격·카운터하면 해당 게이트를 이해하고 대응 기술 해금 후보를 얻는다.

```text
전조 관찰
→ gate tag 일부 기록

피격
→ 자세·점유 결과 기록

카운터 성공
→ 기술 구조 완전 이해 후보
```

### 6-3. 훈련·동료 전수

동료 훈련은 일반 숙련보다 빠르게 특정 기술을 해금할 수 있다. 다만 신체 조건이나 부위 사용 조건은 무시하지 않는다.

### 6-4. 기벽 변종

기벽은 일반 기술 자체보다 변종·추가 effect를 해금하는 것을 기본으로 한다.

```text
기본 기술
+ 관련 기벽
+ Memory Log 단계
+ 부위 레벨
→ 기벽 전용 변종
```

기벽 완화 중에는 변종과 직접 연결 Return만 비활성화한다.

---

## 7. 괴물 기술 키트

```yaml
MonsterSubmissionSkillKit:
  monster_id: str

  signature_skills: []
  core_skills: []
  conditional_skills: []
  variant_pools: []

  opening_patterns: []
  combo_patterns: []
  finisher_patterns: []
```

### 7-1. 구성 원칙

- 시그니처 기술 1~2개는 항상 보유한다.
- 핵심 전투 흐름을 만드는 고정 기술을 우선한다.
- 랜덤 풀은 소수의 변주 슬롯으로만 사용한다.
- 반복 조우에서 플레이어가 기술 풀과 전조를 학습할 수 있어야 한다.

```text
권장 구조
고정 시그니처 1~2
+ 고정 코어 2~4
+ 조건부 피니셔 1~2
+ 변주 슬롯 0~2
```

정확한 개수는 괴물 등급별로 확정한다.

### 7-2. 조건부 기술

```yaml
ConditionalMonsterSkill:
  skill_id: SkillId
  conditions:
    target_submission_below: null | int
    target_statuses: []
    required_posture: null | PostureKey
    requires_initiative: bool
    required_occupied_parts: []
    previous_skill_tags: []
```

Subjugation 피니셔는 일반적으로 복수 조건을 요구한다.

---

## 8. 괴물 기술 쿨타임·AI

```yaml
MonsterSkillRuntime:
  skill_id: SkillId
  cooldown_remaining: int
  times_used: int
  last_used_turn: int
```

AI 선택 요소:

- 기술 쿨타임
- 현재 주도권
- 현재 자세·점유
- 대상 상태이상
- 대상 굴복도·성감·탈진
- 이전 기술과 연계 가능 여부
- 플레이어가 해당 전조를 얼마나 학습했는지
- 기술 반복 페널티

괴물 AI는 강한 기술만 반복하지 않고 시그니처 패턴과 변주를 사용한다.

---

## 9. 전조 프로필 연결

```yaml
TelegraphProfileRef:
  telegraph_profile_id: TelegraphProfileId
  archetypes: []
  signature_cues: []
  target_part_hint: null | R18PartKey
  gate_tag_hints: []
  false_telegraph_profile_id: null | TelegraphProfileId
```

전조는 Bark·Narration 문장을 직접 기술 정의에 대량 저장하지 않고 전조 아키타입과 프로필을 참조한다.

기술마다 다음은 반드시 존재한다.

- 최소 1개 물리적 Cue
- 최소 1개 전조 아키타입
- 카운터 가능 기술이면 gate tag 힌트
- 시그니처 기술이면 고유 Cue 후보

---

## 10. 기술 정보 해금

플레이어가 처음부터 괴물 기술의 모든 정보를 아는 것은 아니다.

| 관찰 단계 | 공개 후보 |
|---|---|
| unknown | 존재와 이름 비공개 |
| seen | Bark·Narration 패턴 기록 |
| identified | 공격축·목표 부위·일부 gate tag |
| understood | 쿨타임·연계·counter tag 후보 |
| mastered | 시그니처 패턴·피니셔 조건·거짓 전조 간파 후보 |

정보 해금은 전투 UI의 수치 알림보다 기록·도감·생존자 Bark 정확도에 반영한다.

---

## 11. 검증 규칙

- 모든 생존자 기술은 최소 하나의 소유·해금 경로를 가진다.
- 모든 괴물은 최소 하나의 시그니처 기술을 가진다.
- Tease 기술은 빈 `counter_tags`로 대표 카운터 기술이 될 수 없다.
- 모든 게이팅 공격은 최소 하나의 `gate_tag`를 가진다.
- 모든 조건부 피니셔는 복수의 발동 조건을 가진다.
- 기술 기본 위력이 없고 기벽 보정만으로 작동하는 기술을 금지한다.
- 랜덤 변주 슬롯이 고정 핵심 기술 수보다 많지 않게 한다.
- 전조 프로필이 없는 고위험 게이팅 기술을 금지한다.

---

## 12. 미확정 항목

- 생존자 초기 기술 최종 개수
- 분류·기술 숙련 범위와 성장식
- 기술별 실제 기본 위력 수치
- 게이트 태그 정본 목록
- 부분 일치 카운터 처리
- 괴물 등급별 키트 크기
- 쿨타임 기본 범위
- 기술 정보 해금 속도
- 준비 집중 실제 보정

---

## 13. 버전 관리

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.0.0 | 2026-07-15 | 생존자별 기술 소유·초기·학습·기벽 변종, Tease 게이팅 카운터, 괴물 고정 기술 키트·쿨타임·전조 계약 작성. |
