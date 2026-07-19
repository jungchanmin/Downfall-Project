# R18 Skill Catalog Reconciliation Plan

## 목적

기존 `MECH_R18_Skill_Catalog.md`의 구형 규칙을 최신 굴복 페이즈 정본과 충돌하지 않도록 순차 교체한다.

기존 기술 예시와 연출 데이터는 가능한 한 보존하되, 소유·상성·게이팅·키·괴물 키트 규칙은 최신 문서를 우선한다.

## 정본 우선순위

다음 문서가 기존 Skill Catalog의 충돌 항목보다 우선한다.

1. `MECH_R18_Submission_Core_System`
2. `MECH_R18_Skill_Access_And_Recall_System`
3. `MECH_R18_Skill_Ownership_Unlock_Contract`
4. `MECH_R18_Gate_Tag_Standard`
5. `MECH_R18_Telegraph_Bark_Content_Policy`
6. `MECH_R18_Skill_Data_Contract`

## SECTION별 교체 항목

### SECTION 0 — 소유·연동 규칙

구형:

```text
생존자 굴복 기술 5대분류 = 공용 풀
전원 사용 가능
```

신규:

```text
5대분류 = 공통 전술 역할
실제 기술 = 생존자별 known_skills
공용 = 버티기·거리 벌리기·도움 요청·교대 요청·행동 포기
```

괴물도 단순 공용 풀 참조가 아니라 `MonsterSubmissionSkillKit`를 소유한다.

### SECTION 1 — 기술 스키마

다음 필드를 최신화한다.

```yaml
command_category:
base_power:
stability:
self_cost:
cooldown:
progress_part: Mouth | Chest | LowerBody | Rear | WholeBody
display_part:
required_target_parts: []
action_parts: []
valid_postures: []
posture_force:
gate_attack:
counter_profile:
telegraph_profile_id:
ownership_paths: []
unlock_rules: []
```

구형 `required_parts`는 대상 부위와 시전자 행동 부위를 혼합하므로 폐기한다.

### SECTION 3 — 괴물 굴복 기술

구형:

```text
고정 1~2 + 축 풀 랜덤 2~3
```

신규:

```text
고정 시그니처 1~2
+ 고정 코어 기술 2~4
+ 조건부 피니셔 1~2
+ 소수 변주 슬롯 0~2
```

랜덤 변주 슬롯은 고정 코어보다 많을 수 없다.

모든 고위험 게이팅 기술은 다음을 가진다.

- `cooldown`
- `gate_attack`
- `telegraph_profile_id`
- AI 사용 조건
- 필요 시 콤보·피니셔 연결

### SECTION 4 — 생존자 대표 기술

기존 5종은 전원 공용 기술이 아니라 **분류 기준 예시·템플릿**으로 지위를 변경한다.

```text
SB_Service_Kiss
SB_Tease_Caress
SB_Dom_Ride
SB_Absorb_Drink
SB_Defiance_Focus
```

실제 생존자 보유 여부는 NPC 데이터의 `known_skills`가 결정한다.

대표 기술은 다음 책임을 가진다.

- 해당 분류의 기본 전술 역할 예시
- 후속 기술 설계의 기준점
- 기벽 변종의 base_skill 후보

대표 기술이 모든 생존자에게 자동 지급되지는 않는다.

### SECTION 5 — 축 × 분류 상성표

구형 상성표는 카운터 성립 여부를 직접 결정하지 않는다.

신규 처리 순서:

```text
1. 자세·부위·행동 사용 가능 검사
2. Gate Tag × Counter Tag 일치 검사
3. Tease 역상성 카운터 성립 여부 결정
4. 공격축 친화도·기술 기본 위력·숙련·로그·기벽 보정
5. 최종 교환 결과 처리
```

특히 다음 구형 규칙은 폐기한다.

```text
Contact → Tease 강상성 자동 적용
```

신규:

```text
게이팅 시도 + 대응 Tease 기술의 필수 태그 완전 일치
→ 카운터 판정 자격
→ 성공 시 공격 취소·주도권 탈취
```

축 상성표는 다음 역할만 유지한다.

- 공격축별 친화도
- 진척 로그 방향
- 특정 분류의 추가 효과
- 일부 상태·기벽 Return 보정

### SECTION 7 — 참조 방식

구형:

```text
생존자 굴복 기술은 공용 풀, NPC 참조 불필요
```

신규:

```yaml
survivor_submission_skills:
  known_skills: []
  initial_skills: []
  learned_skills: []
  signature_skills: []
```

괴물:

```yaml
submission_skill_kit:
  signature_skills: []
  core_skills: []
  conditional_skills: []
  variant_pools: []
```

### SECTION 8 — 자세 게이팅

한글 저장 키를 영문 정본 키로 교체한다.

```text
대치 → Confrontation
정면 → Front
후배위 → RearEntry
기승 → Mount
구속 → Bound
```

대상 부위:

```text
입 → Mouth
가슴 → Chest
하복부 → LowerBody
후부 → Rear
전신 → WholeBody
```

한글은 UI 표시명으로만 유지한다.

## 기존 기술 보존 정책

다음은 가능한 한 유지한다.

- Skill ID
- 기술 표시명
- 기존 기본 효과 의도
- Narration·로그 문장
- 괴물·세력별 연출 색

다음은 최신 계약에 맞춰 재작성한다.

- 기술 소유권
- 공용 여부
- 기본 위력
- 자세·부위 키
- Gate Tag
- Counter Tag
- 전조 프로필
- 쿨타임
- 피니셔 조건
- 기벽 보정 방식

## 순차 치환 순서

1. frontmatter·제목 버전 통일
2. SECTION 0 소유 규칙 교체
3. SECTION 1 스키마 교체
4. SECTION 5 상성 책임 축소
5. SECTION 7 생존자·괴물 참조 방식 교체
6. SECTION 8 영문 키·Gate Tag 연동
7. 생존자 대표 5종을 템플릿으로 전환
8. 괴물 시그니처·코어 키트 적용
9. 기존 기술별 전조·쿨타임·Gate Tag 보강
10. 구형 중복 샤드 제거

## 검증 완료 조건

- `공용 풀`, `전원 사용 가능` 문구가 생존자 기술에 남아 있지 않음
- Tease가 Contact 전체를 자동 카운터한다는 문구가 없음
- 모든 Tease 카운터에 `counter_profile` 존재
- 모든 게이팅 공격에 `gate_attack` 존재
- 모든 고위험 게이팅 공격에 `telegraph_profile_id` 존재
- 저장 키가 영문 정본 키를 사용함
- 괴물 기술은 최소 하나의 실제 키트에 연결됨
- 생존자 기술은 최소 하나의 소유·해금 경로를 가짐

## 현재 상태

이번 문서는 기존 Skill Catalog 전체 덮어쓰기 전에 적용할 정합성 기준이다.

구형 카탈로그의 기술 예시는 아직 남아 있으나, 충돌하는 규칙 해석에서는 본 계획과 최신 정본 문서가 우선한다.
