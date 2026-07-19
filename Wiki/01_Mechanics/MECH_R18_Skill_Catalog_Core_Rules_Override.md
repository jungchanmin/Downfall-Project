---
id: MECH_R18_Skill_Catalog_Core_Rules_Override
title: "핵심 시스템 사양서 — R18 Skill Catalog 규칙 골격 오버라이드"
type: mechanic
status: wip
version: 1.0.0
summary: >
  기존 MECH_R18_Skill_Catalog의 기술 예시를 보존하면서 소유권·스키마·상성 책임·참조 방식·게이팅 키를 최신 승인 규칙으로 교체한다.
tags: [mechanic, r18, skill, catalog, override, migration]
depends_on:
  - MECH_R18_Skill_Catalog
  - MECH_R18_Skill_Ownership_Unlock_Contract
  - MECH_R18_Gate_Tag_Standard
  - MECH_R18_Submission_Core_System
  - MECH_R18_Telegraph_Bark_Content_Policy
last_updated: 2026-07-19
---

# R18 Skill Catalog 규칙 골격 오버라이드 v1.0

## 0. 적용 우선순위

이 문서는 기존 `MECH_R18_Skill_Catalog.md`의 기술 ID·기술 예시·연출 텍스트를 보존하면서 다음 SECTION의 규칙 해석을 최신 기준으로 덮어쓴다.

```text
SECTION 0 — 소유·연동 규칙
SECTION 1 — 기술 정의 스키마
SECTION 5 — 상성 책임
SECTION 7 — 참조 방식
SECTION 8 — 자세·부위·행동 게이팅
```

충돌 시 본 문서와 다음 정본 문서를 우선한다.

1. `MECH_R18_Submission_Core_System`
2. `MECH_R18_Skill_Ownership_Unlock_Contract`
3. `MECH_R18_Gate_Tag_Standard`
4. `MECH_R18_Skill_Data_Contract`
5. 기존 `MECH_R18_Skill_Catalog`

---

## SECTION 0 OVERRIDE — 소유·연동 규칙

### 0-1. 기술 정의와 기술 소유 분리

본 카탈로그는 기술 정의를 소유한다. 개별 캐릭터가 실제로 어떤 기술을 보유하는지는 캐릭터 기술 상태가 소유한다.

```text
카탈로그
→ 기술 정의·ID·기본 위력·게이트·효과

생존자 데이터
→ initial_skills / known_skills / learned_skills / signature_skills

괴물 데이터
→ signature_skills / core_skills / conditional_skills / variant_pools
```

생존자 굴복 기술은 더 이상 전원 공용 풀이 아니다.

### 0-2. 공용 요소

모든 생존자가 공유하는 것은 5대 커맨드 역할과 시스템 안전 행동뿐이다.

```text
커맨드 역할:
Service / Tease / Domination / Absorption / Defiance

공용 안전 행동:
버티기 / 거리 벌리기 / 도움 요청 / 교대 요청 / 행동 포기
```

`SB_Service_Kiss`, `SB_Tease_Caress`, `SB_Dom_Ride`, `SB_Absorb_Drink`, `SB_Defiance_Focus`는 분류 기준 템플릿이다. 실제 보유 여부는 생존자 데이터가 결정한다.

### 0-3. 연동 책임

- 합 처리·주도권·행동 취소: `MECH_R18_Submission_Core_System`
- 기술 소유·해금·숙련: `MECH_R18_Skill_Ownership_Unlock_Contract`
- 기벽 변종·Return: `MECH_R18_Quirk_Skill_Return_Map`
- 메모리 로그·부위 경험: `MECH_R18_Memory_Log`
- 게이트·카운터 태그: `MECH_R18_Gate_Tag_Standard`
- 전조 표현: `MECH_R18_Telegraph_Bark_Content_Policy`

---

## SECTION 1 OVERRIDE — R18SkillDef 최신 스키마

```yaml
R18SkillDef:
  id: str
  name: str
  side: monster | survivor
  phase: normal_r18 | submission

  command_category: null | Service | Tease | Domination | Absorption | Defiance
  attack_axis: null | Contact | Penetration | Fluid | Mutation | Cognition | Subjugation

  base_power: number
  stability: number | tier
  self_cost: {}
  cooldown: number | null

  gauge_delta: {}
  status_inflict: []
  effect_ids: []

  progress_axis: null | Contact | Penetration | Fluid | Mutation | Cognition | Subjugation
  progress_part: null | Mouth | Chest | LowerBody | Rear | WholeBody
  display_part: null | 입 | 가슴 | 하복부 | 후부 | 전신

  valid_postures: [Confrontation | Front | RearEntry | Mount | Bound]
  posture_force: null | Confrontation | Front | RearEntry | Mount | Bound

  required_target_parts: [Mouth | Chest | LowerBody | Rear | WholeBody]
  action_parts: [Mouth | Hand | LowerBody]

  gate_attack: null | GateAttackProfile
  counter_profile: null | TeaseCounterProfile
  bypass_gating: false

  telegraph_profile_id: str | null
  unlock_profile_id: str | null
  variant_profile_id: str | null

  lock_conditions: []
  scaling: []
  log: { on_use: [str], on_hit: [str] }
```

### 1-1. 필드 분리 원칙

- `required_parts`는 폐기 대상이다.
- 공격 대상 부위는 `required_target_parts` 또는 `gate_attack.target_parts`가 소유한다.
- 시전에 사용하는 신체는 `action_parts`가 소유한다.
- 공격축과 커맨드 분류는 별개다.
- 기벽은 기본 위력을 대신하지 않는다. 모든 실제 기술은 `base_power`를 가진다.

### 1-2. 영문 정본 키

```text
Posture:
Confrontation / Front / RearEntry / Mount / Bound

Target Part:
Mouth / Chest / LowerBody / Rear / WholeBody

Action Part:
Mouth / Hand / LowerBody
```

한글 명칭은 UI·연출용 표시명으로만 사용한다.

---

## SECTION 5 OVERRIDE — 상성 책임 재정의

기존 6축 × 5분류 표는 카운터 성립을 직접 결정하지 않는다.

### 5-1. 처리 우선순위

```text
1. 기술 사용 가능 여부
   자세·부위·행동·상태 게이트

2. Tease 카운터 적합성
   gate_attack.required tags × counter_profile.required matches

3. 공격축 친화도
   로그·기벽·효과·판정 보정

4. 기술 기본 위력·숙련·상태
   최종 합 결과
```

### 5-2. Tease 카운터

Tease는 `Contact` 축 전체의 자동 카운터가 아니다.

```text
필수 Gate Tag 완전 일치
+ 사용 부위 가능
+ 카운터 판정 성공
→ 공격 취소
→ 카운터 측 주도권 확정 획득
```

부분 일치는 역상성 카운터가 아니다. 부분 경감·자세 강제 방지·점유 방지·중립 전환 중 하나로 처리하며 실제 수치는 후속 밸런스 문서가 소유한다.

### 5-3. 축 친화도 표의 지위

기존 표는 다음 용도로만 보존 가능하다.

- 공격축별 로그·기벽 친화도
- 특정 커맨드의 조건부 보정
- AI 추천과 설명용 경향

축 표만으로 행동 취소·주도권 탈취·카운터 성공을 확정할 수 없다.

---

## SECTION 7 OVERRIDE — 참조 방식

### 7-1. 생존자

```yaml
survivor_submission_skills:
  survivor_id: Rachel
  initial_skills: []
  known_skills: []
  learned_skills: []
  signature_skills: []
  category_proficiency: {}
  skill_proficiency: {}
```

기술을 배우면 계속 보유한다. 고정 장착 슬롯은 사용하지 않는다. 현재 상황에 적합한 기술을 UI에서 우선 노출한다.

### 7-2. 괴물

```yaml
monster_submission_kit:
  monster_id:
  signature_skills: []
  core_skills: []
  conditional_skills: []
  variant_pools: []
  opening_patterns: []
  combo_patterns: []
  finisher_patterns: []
```

괴물은 고정 시그니처·코어 기술을 중심으로 운용한다. 랜덤 변주 슬롯은 고정 코어 수를 초과할 수 없다.

### 7-3. 파일 경계

- SFW 빌드는 본 카탈로그와 연결된 R18 데이터를 로드하지 않는다.
- 성인 캐릭터에게만 적용한다.
- 신규 기술·로그·Gate Tag는 스키마 승인 후 추가한다.

---

## SECTION 8 OVERRIDE — 자세·부위·행동 게이팅

### 8-1. 게이트 검사 순서

```text
현재 자세
→ 행동 부위 사용 가능 여부
→ 목표 부위 접근 가능 여부
→ 상태·점유 봉쇄
→ Gate Tag 카운터 가능 여부
→ 상성·위력 판정
```

게이트 검사는 상성 판정보다 먼저다.

### 8-2. 행동 취소 후 주도권

피주도권자의 행동이 게이트에 의해 취소되면:

```text
피주도권자 행동 취소
→ 주도권자 기술 일방 적용
→ 기본적으로 합 종료 후 피주도권자에게 주도권 이전
```

`initiative_hold` 또는 `combo_continue` effect가 있으면 예외적으로 현재 주도권자가 유지한다.

### 8-3. 자세와 점유

- 자세는 `Confrontation / Front / RearEntry / Mount / Bound`를 사용한다.
- 대상 점유와 행동 부위 점유를 분리한다.
- 전신 점유는 강한 제한과 짧은 지속 또는 명확한 탈출구를 가져야 한다.
- 모든 부위를 동시에 영구 봉쇄할 수 없다.

### 8-4. Tease와 Defiance 역할 분리

```text
Tease
→ 특정 Gate Tag에 대한 고위험 패링
→ 성공 시 주도권 탈취
→ 불일치 또는 실패 시 큰 위험

Defiance
→ 상태 해제·피해 경감·탈출·내성 획득
→ 상태 해제만으로 주도권을 얻지 않음
```

Tease는 모든 공격에 범용 패링할 수 없다. 개별 기술의 `counter_profile`이 허용한 Gate Tag만 카운터한다.

---

## 9. 기존 기술 예시의 임시 해석

기존 기술 예시는 삭제하지 않는다. 최신 필드가 없는 기술은 다음 방식으로 임시 변환한다.

```text
required_parts
→ 문맥에 따라 action_parts 또는 required_target_parts로 분리 필요

한글 progress_part
→ 영문 canonical key로 읽기 변환

한글 valid_postures / posture_force
→ 영문 canonical key로 읽기 변환

기존 축 상성 주석
→ 친화도 설명으로만 해석

공용 생존자 기술 주석
→ 분류 템플릿으로 해석
```

저장 시에는 영문 정본 키만 사용한다.

---

## 10. 자동 검증 규칙

- 모든 실제 기술은 `base_power`를 가져야 한다.
- 모든 Tease 기술은 비어 있지 않은 `counter_profile`을 가져야 한다.
- 모든 게이팅 공격은 `gate_attack`과 `telegraph_profile_id`를 가져야 한다.
- `required_parts` 신규 사용을 금지한다.
- 한글 자세·부위 키 신규 저장을 금지한다.
- 생존자 기술의 전원 공용 플래그를 금지한다.
- 괴물 랜덤 변주 수는 고정 코어 기술 수를 초과할 수 없다.
- 조건부 피니셔는 복수의 발동 조건을 가져야 한다.

---

## 11. 버전 관리

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.0.0 | 2026-07-19 | 기존 Skill Catalog의 SECTION 0·1·5·7·8 규칙을 최신 소유·Gate Tag·주도권·영문 키 기준으로 오버라이드. |
