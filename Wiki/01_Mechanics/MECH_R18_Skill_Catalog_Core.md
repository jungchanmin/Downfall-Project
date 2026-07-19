---
id: MECH_R18_Skill_Catalog_Core
title: "핵심 시스템 사양서 — R18 기술 카탈로그 코어"
type: mechanic
status: wip
version: 1.0.0
summary: >
  R18 기술 카탈로그의 소유권, 데이터 스키마, 상성 책임, 캐릭터 참조 방식,
  자세·부위·행동 게이팅 규칙을 소유한다. 기술별 예시·연출·레거시 effect 목록은
  MECH_R18_Skill_Catalog를 콘텐츠 데이터 원본으로 참조한다.
tags: [mechanic, combat, r18, skill, catalog, canonical]
depends_on:
  - MECH_R18_Submission_Core_System
  - MECH_R18_Skill_Ownership_Unlock_Contract
  - MECH_R18_Gate_Tag_Standard
  - MECH_R18_Skill_Access_And_Recall_System
  - MECH_R18_Skill_Data_Contract
  - MECH_R18_Skill_Catalog
last_updated: 2026-07-19
---

# R18 기술 카탈로그 코어 v1.0

> 이 문서는 기존 `MECH_R18_Skill_Catalog.md`의 SECTION 0·1·5·7·8을 대체하는 정본이다.
> 기존 카탈로그의 기술 ID, 표시명, effect 의도, Narration과 세력별 연출은 콘텐츠 데이터로 보존한다.

---

## SECTION 0 — 소유·연동 규칙

### 0-1. 문서 책임

| 문서 | 책임 |
|---|---|
| `MECH_R18_Skill_Catalog_Core` | 소유권·스키마·상성·게이팅·참조 규칙 |
| `MECH_R18_Skill_Catalog` | 기술 ID·기존 예시·effect 의도·연출 원문 |
| `MECH_R18_Skill_Ownership_Unlock_Contract` | 초기 기술·학습·숙련·괴물 키트 |
| `MECH_R18_Gate_Tag_Standard` | Gate Tag와 Tease Counter Tag |
| `MECH_R18_Submission_Core_System` | 합 처리·주도권·전조·상태 콤보 |

### 0-2. 기술 정의와 소유 분리

```text
커맨드 5분류
≠ 실제 기술 정의
≠ 캐릭터 보유 기술
```

- Service·Tease·Domination·Absorption·Defiance는 공통 전술 역할이다.
- 실제 기술은 Skill Catalog에 ID로 정의한다.
- 생존자의 실제 사용 가능 기술은 `known_skills`가 결정한다.
- 괴물의 실제 기술은 `monster_submission_kit`이 결정한다.
- 기술을 학습하면 고정 장착 제한 없이 계속 보유한다.

### 0-3. 공용 안전 행동

모든 생존자가 자동으로 공유하는 것은 굴복 기술이 아니라 다음 시스템 행동이다.

- HoldOut — 버티기
- CreateDistance — 거리 벌리기
- RequestHelp — 도움 요청
- RequestTag — 교대 요청
- ForfeitAction — 행동 포기

공용 안전 행동은 5대 커맨드 숙련이나 기벽 변종의 base skill로 사용하지 않는다.

### 0-4. 대표 기술 5종

다음 ID는 전원 자동 지급 기술이 아니라 분류 기준 템플릿이다.

- `SB_Service_Kiss`
- `SB_Tease_Caress`
- `SB_Dom_Ride`
- `SB_Absorb_Drink`
- `SB_Defiance_Focus`

실제 생존자 보유 여부는 캐릭터 데이터가 결정한다.

---

## SECTION 1 — R18 기술 정의 스키마

```yaml
R18SkillDef:
  id: string
  name: string
  side: monster | survivor
  phase: normal_r18 | submission

  command_category: null | Service | Tease | Domination | Absorption | Defiance
  attack_axis: null | Contact | Penetration | Fluid | Mutation | Cognition | Subjugation

  base_power: number
  stability: number | grade
  self_cost: {}
  cooldown: number | null

  gauge_delta:
    arousal_self: number | null
    arousal_target: number | null
    clothing: number | null
    submission: number | null

  progress_axis: null | Contact | Penetration | Fluid | Mutation | Cognition | Subjugation
  progress_part: null | Mouth | Chest | LowerBody | Rear | WholeBody
  display_part: string | null

  valid_postures: [Confrontation | Front | RearEntry | Mount | Bound]
  posture_force: null | Confrontation | Front | RearEntry | Mount | Bound

  required_target_parts: [Mouth | Chest | LowerBody | Rear | WholeBody]
  action_parts: [Mouth | Hand | LowerBody]

  gate_attack: null | GateAttackProfile
  counter_profile: null | TeaseCounterProfile
  telegraph_profile_id: string | null

  status_inflict: []
  effect_ids: []
  lock_conditions: []
  scaling: []

  ownership_paths: []
  unlock_rules: []

  log:
    on_use: []
    on_hit: []
    on_fail: []
```

### 1-1. 필수 규칙

- 모든 실제 기술은 `base_power`를 가져야 한다.
- `command_category: Tease` 기술은 `counter_profile`을 가져야 한다.
- 자세·점유 결과를 발생시키는 공격은 `gate_attack`을 가져야 한다.
- 고위험 게이팅 공격은 `telegraph_profile_id`를 가져야 한다.
- 신규 기술은 `effect_id` 단일 필드 대신 `effect_ids` 배열을 사용한다.

### 1-2. 폐기 필드

```text
sub_category
required_parts
한글 progress_part 저장 키
한글 valid_postures 저장 키
생존자 전원 공용 플래그
```

`required_parts`는 대상 부위와 행동 부위를 혼합하므로 자동 변환하지 않는다. 기술 문맥을 검수하여 `required_target_parts`와 `action_parts`로 분리한다.

### 1-3. 레거시 읽기 변환

| 레거시 | 정본 |
|---|---|
| 입 | Mouth |
| 가슴 | Chest |
| 하복부 | LowerBody |
| 후부 | Rear |
| 전신 | WholeBody |
| 대치 | Confrontation |
| 정면 | Front |
| 후배위 | RearEntry |
| 기승 | Mount |
| 구속 | Bound |

레거시 한글 키는 읽기 호환과 UI 표시에만 허용한다. 신규 저장은 영문 정본 키를 사용한다.

---

## SECTION 5 — 상성·카운터 책임

### 5-1. 판정 책임 분리

| 요소 | 책임 |
|---|---|
| 현재 자세·점유 | 기술 사용 가능 여부 |
| Gate Tag × Counter Tag | Tease 카운터 자격 |
| 공격축 | 로그·기벽·효과 친화도 |
| 기술 기본 위력 | 합의 기본 성능 |
| 숙련·능력·기록 | 실행 품질 |
| 상태이상 | 전조·행동·주도권 교란 |

기존 `Contact → Tease 강상성 자동 적용` 규칙은 폐기한다.

### 5-2. 처리 순서

```text
1. 현재 자세 검사
2. 행동 부위 봉쇄 검사
3. 목표 부위 접근 검사
4. 상태·점유 게이트 검사
5. Gate Tag와 Counter Tag 일치 검사
6. 공격축 친화도 적용
7. base_power·숙련·능력·로그·기벽 보정
8. 최종 효과와 주도권 처리
```

### 5-3. Tease 완전 카운터

```text
필수 Gate Tag 완전 일치
+ 금지 태그 없음
+ 행동 부위 사용 가능
+ 판정 성공
→ 공격 취소
→ 카운터 측 주도권 확정 획득
```

큰 성공과 대성공은 자세 해제, 역상태이상, 공격 역이용 등의 추가 보상만 조정한다.

### 5-4. 부분 일치

부분 일치는 역상성 카운터가 아니다.

허용 결과 후보:

- 피해·게이지 일부 경감
- 자세 강제만 방지
- 부위 점유만 방지
- 중립 합으로 전환

실제 경감량과 우선순위는 밸런스 단계에서 확정한다.

### 5-5. 축 친화도

기존 축×분류 표는 자동 승패표가 아니라 다음의 초기 설계 참고표로만 유지한다.

- Memory Log 누적 방향
- 기벽 Return 친화도
- 분류별 특수 효과 후보
- AI의 대응 성향
- 일부 보조 판정

---

## SECTION 7 — 캐릭터·괴물 참조 방식

### 7-1. 생존자

```yaml
survivor_submission_skills:
  survivor_id:
  initial_skills: []
  known_skills: []
  learned_skills: []
  signature_skills: []

  category_proficiency:
    Service:
    Tease:
    Domination:
    Absorption:
    Defiance:

  skill_proficiency: {}
  preparation_focus:
    category:
    skill_id:
```

- `known_skills`만 실제 선택 후보가 된다.
- 상황에 적합한 기술은 UI 상단에 우선 노출한다.
- 후순위 기술도 전체 목록에서 선택할 수 있다.
- 기벽 변종은 기본 기술의 소유와 별도로 해금 조건을 검사한다.

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

권장 구성:

```text
시그니처 1~2
+ 고정 코어 2~4
+ 조건부 피니셔 1~2
+ 변주 슬롯 0~2
```

- 변주 슬롯 수는 고정 코어 기술 수를 넘을 수 없다.
- 피니셔는 복수 조건을 요구한다.
- 기술별 쿨타임·전조·AI 조건을 가진다.

### 7-3. 콘텐츠 경계

- 성인 캐릭터만 적용한다.
- SFW 빌드는 R18 카탈로그와 관련 데이터 샤드를 로드하지 않는다.
- 신규 로그 축·부위 키·Gate Tag는 디렉터 승인 후 추가한다.

---

## SECTION 8 — 자세·부위·행동 게이팅

### 8-1. 정본 자세

| 키 | 표시명 | 역할 |
|---|---|---|
| Confrontation | 대치 | 기본 중립 자세 |
| Front | 정면 | 정면 밀착·전방 부위 접근 |
| RearEntry | 후방 | 후방 제압·Rear 접근 |
| Mount | 기승 | 생존자 주도 강공 자세 |
| Bound | 구속 | 광범위 행동 제한 자세 |

자세는 기술을 자동 성공시키지 않는다. 기술 사용 가능 범위와 점유 충돌을 결정한다.

### 8-2. 대상 부위와 행동 부위

대상 부위:

```text
Mouth / Chest / LowerBody / Rear / WholeBody
```

행동 부위:

```text
Mouth / Hand / LowerBody
```

- 대상 부위 점유는 해당 부위를 요구하는 상대 기술을 제한한다.
- 행동 부위 점유는 시전자가 그 신체 수단을 사용하는 기술을 제한한다.
- `WholeBody` 점유는 광범위하지만 짧은 지속·높은 내성 상승·명확한 탈출구를 요구한다.

### 8-3. Gate Attack

```yaml
gate_attack:
  approach:
  directions: []
  target_parts: []
  action_parts: []
  controls: []
  motions: []
  results: []

  posture_force:
  occupy_target_parts: []
  occupy_action_parts: []
  telegraph_profile_id:
```

Gate Tag는 기술 이름이나 공격축을 중복 표현하지 않는다. 최소 태그를 조합한다.

### 8-4. 행동 취소와 주도권

```text
피주도권자의 대응이 게이트에 걸림
→ 대응 취소
→ 주도권자 기술 일방 적용
→ 기본적으로 합 종료 후 피주도권자에게 주도권 이전
```

다음 effect가 있으면 예외적으로 유지한다.

```text
initiative_hold
combo_continue
```

주도권 유지 effect에는 콤보 연속 상한을 적용한다.

### 8-5. Tease와 Defiance

Tease:

- 특정 Gate Tag 조합에 대한 고위험 패링
- 완전 일치 카운터 성공 시 주도권 탈취
- 모든 공격에 대한 범용 패링이 아님
- 실패 시 공격 증폭·점유 강화 가능

Defiance:

- 상태 해제
- 피해·굴복도 경감
- 자세·점유 탈출
- 동일 상태 내성 상승
- 상태 해제만으로 주도권을 자동 획득하지 않음

### 8-6. 봉쇄 안전장치

- 최소 하나 이상의 시스템 공용 안전 행동을 유지한다.
- 전 부위 동시 점유는 기본적으로 허용하지 않는다.
- `WholeBody` 점유는 내성 상승과 탈출 보정을 동반한다.
- 기술 부족 때문에 행동 선택지가 0개가 되지 않도록 한다.
- 대기 생존자의 구조·교대 지원은 후속 태그 배틀 규칙에서 연결한다.

---

## 자동 검증 규칙

```text
CAT-001 실제 기술은 base_power 필수
CAT-002 Tease 기술은 counter_profile 필수
CAT-003 게이팅 공격은 gate_attack 필수
CAT-004 고위험 게이팅 공격은 telegraph_profile_id 필수
CAT-005 신규 required_parts 사용 금지
CAT-006 신규 한글 자세·부위 저장 키 금지
CAT-007 생존자 전원 공용 기술 플래그 금지
CAT-008 괴물 variant 수가 core 수를 초과할 수 없음
CAT-009 조건부 피니셔는 복수 조건 필수
CAT-010 기술 소유 또는 해금 경로가 없는 실제 기술 금지
```

---

## 기존 카탈로그 콘텐츠 보존 정책

다음은 기존 `MECH_R18_Skill_Catalog`에서 보존한다.

- Skill ID
- 표시명
- 기존 효과 의도
- Narration·로그 문장
- 세력과 괴물별 연출 색
- 레거시 effect ID

다음은 이 문서 기준으로 재해석하거나 후속 데이터 마이그레이션에서 교체한다.

- 전원 공용 여부
- 축 상성 자동 카운터
- `required_parts`
- 한글 저장 키
- 랜덤 축 풀 중심 괴물 구성
- 범용 Tease 패링

---

## 버전 관리

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.0.0 | 2026-07-19 | 기존 Skill Catalog SECTION 0·1·5·7·8의 최신 규칙을 별도 정본 Core로 승격. |
