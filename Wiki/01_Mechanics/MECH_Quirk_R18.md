---
id: MECH_Quirk_R18_DB
title: "핵심 시스템 사양서 — R18 전용 변이 및 정신 개변 기벽 데이터베이스"
type: mechanic
status: wip
version: 1.3.0
summary: >
  R18 트랙 직결 특수 기벽 24종의 Risk & Return, 처리 모델, 고착 상태,
  완화 방식, 메모리 로그 연결, 획득 조건과 고착 조건을 정규화한다.
tags: [mechanic, quirk, database, r18]
keywords:
  - 기벽, R18, 신체 변이, 감도 개발, 성벽, 상식 개변, 침식도, 욕구불만,
    해금 조건, 완화, 메모리 로그, 굴복 기술
depends_on:
  - SYS_Manifest
  - MECH_R18_Memory_Log
  - MECH_Combat_System
  - MECH_Quirk_Treatment_System
runtime_dependencies:
  stats:
    - "#Stat_HP"
    - "#Stat_Sanity"
    - "#Stat_Stress"
    - "#Stat_Condition"
    - "#Stat_Fatigue"
    - "#Stat_Libido"
    - "#Stat_Frustration"
  traits: []
  locations: []
  flags:
    - "#Flag_R18_Erosion_Track"
last_updated: 2026-07-14
---

# 🔞 DOWNFALL R18 전용 변이 및 정신 개변 데이터베이스 (v1.3)

> 실제 수치는 후속 밸런스 패스에서 확정한다. 본 버전은 데이터 흐름과 문서 책임을 정본화한다.

## 0. 공통 처리 원칙

- R18 기벽은 일반 간호·의무실로 제거하지 않는다.
- 모든 기벽은 `Risk`와 `Return`을 함께 가진다.
- 완화·지속 종료 후에도 획득 기록, 최고 고착 단계, 로그와 해금 플래그는 유지한다.
- 축 단계는 공통 `Record / Proficiency / Milestone` 구조를 사용한다.
- 실제 기벽 획득은 축 단계 + 부위 레벨 + 사건·플래그 조건을 사용한다.
- 재획득 횟수만으로 자동 영구화하지 않는다.
- 일반 `색광증`은 공통 충동 패널티를 담당하고, 본 모듈은 R18 장기 변화·로그·고착을 담당한다.

## 1. 공통 데이터 규격

```yaml
r18_quirk_meta:
  treatment_model: self_expiring | suppressible | irreversible
  lock_state: temporary | persistent | permanent
  mitigation_model: duration_reduction | stage_down | temporary_suppression | none
  risk_effects: []
  return_effects: []
  memory_log_links:
    axes: []
    parts: []
    acts: []
  unlock_condition:
    minimum_axis_stage: record | proficiency | milestone
    minimum_part_level: 0
    required_events: []
    required_flags: []
  lock_condition:
    acquisition_count: TBD
    required_axis_stage: null
    required_events: []
  submit_skill_boost: []
```

책임 분리:

- Quirk DB: Risk·Return 종류, 획득·고착 조건 구조
- Memory Log: 카운터, 단계, 이력과 해금 판정
- Skill Catalog: 실제 굴복 기술과 수치
- Combat System: 전투 판정과 효과 적용
- Event: 특수 사건·선택지·서사 결과

---

## SECTION 1 — 신체 변이 계열

### 1-1. 살점 융기 — `#Trait_Flesh_Anomalous_Swelling`
- **Risk**: 피로 누적 증가 / 외출 회피 판정 난이도 상승
- **Return**: 외형·관계 반응 선택지 해금
- **처리/고착/완화**: `irreversible / permanent / none`
- **로그 연결**: `Mutation`, `Chest`, `Developed`
- **획득 조건**: `Mutation milestone + Chest Lv2 + 영구 변이 사건`
- **고착 조건**: `획득 즉시 permanent`

### 1-2. 이종 이식 — `#Trait_Androgynous_Sprout`
- **Risk**: 욕구불만 누적 / 일부 거절 선택지 제한
- **Return**: 신체 개조·관계 이벤트 해금
- **처리/고착/완화**: `irreversible / permanent / none`
- **로그 연결**: `Mutation`, `LowerBody`, `Developed`
- **획득 조건**: `Mutation milestone + LowerBody Lv2 + 특수 이식 사건`
- **고착 조건**: `획득 즉시 permanent`

### 1-3. 피부 유즙화 — `#Trait_Cutaneous_Secretion`
- **Risk**: 컨디션 저하 / 치료 자원 추가 소모
- **Return**: 영양·간호·R18 사건 선택지 해금
- **처리/고착/완화**: `self_expiring / temporary / duration_reduction`
- **로그 연결**: `Mutation + Fluid`, `Chest or WholeBody`, `Developed`
- **획득 조건**: `Mutation proficiency + 관련 분비 사건`
- **고착 조건**: `반복 획득 + Fluid proficiency + 고착 사건`

### 1-4. 음핵 비대증 — `#Trait_Hypertrophied_Clitoris`
- **Risk**: 이동 후 스트레스 / 탐색 실패 부작용
- **Return**: 감도·굴복 기술 강화
- **처리/고착/완화**: `irreversible / permanent / none`
- **로그 연결**: `Mutation + Penetration`, `LowerBody`, `Developed`
- **획득 조건**: `Mutation milestone + LowerBody Lv2 + 영구 변이 사건`
- **고착 조건**: `획득 즉시 permanent`

---

## SECTION 2 — 감도 개발 계열

### 2-1. 유두 민감화 — `#Trait_Hypersensitive_Nipples`
- **Risk**: 스트레스 누적 / 제작 판정 불이익
- **Return**: 접촉·감도 기술 강화
- **처리/고착/완화**: `self_expiring / temporary / duration_reduction`
- **로그 연결**: `Contact`, `Chest`, `Received or Developed`
- **획득 조건**: `Contact proficiency + Chest Lv1`
- **고착 조건**: `반복 획득 + Chest Lv2 + 감도 고착 사건`

### 2-2. 자궁 개발 — `#Trait_Uterine_Sensitization`
- **Risk**: 욕구 증가 / 침식도 상승 증폭
- **Return**: 하복부·굴복 기술 강화
- **처리/고착/완화**: `irreversible / permanent / none`
- **로그 연결**: `Penetration + Subjugation`, `LowerBody`, `Developed`
- **획득 조건**: `Penetration milestone + LowerBody Lv3 + 영구 개발 사건`
- **고착 조건**: `획득 즉시 permanent`

### 2-3. 후장 개발 — `#Trait_Anal_Sensitization`
- **Risk**: 컨디션 저하 / 불침번 판정 불이익
- **Return**: 후방 감도·굴복 선택지 강화
- **처리/고착/완화**: `suppressible / persistent / stage_down`
- **로그 연결**: `Penetration`, `Rear`, `Received or Developed`
- **획득 조건**: `Penetration proficiency + Rear Lv2`
- **고착 조건**: `재획득 + Penetration milestone + Rear Lv3`

### 2-4. 전신 성감대화 — `#Trait_Pansexual_Skin_Erosion`
- **Risk**: 정신력 상한 감소 / 교류 난이도 상승
- **Return**: 전신 접촉 반응·굴복 기술 강화
- **처리/고착/완화**: `irreversible / permanent / none`
- **로그 연결**: `Contact + Mutation`, `WholeBody`, `Developed`
- **획득 조건**: `Contact milestone + Mutation milestone + WholeBody Lv3`
- **고착 조건**: `획득 즉시 permanent`

---

## SECTION 3 — 내구성·양날 계열

### 3-1. 피학증 — `#Trait_Masochistic_Surrender`
- **Risk**: 부상 상태 공격 판정 불이익
- **Return**: 체력 감소 시 스트레스 회복 / 피학·굴복 기술 강화
- **처리/고착/완화**: `irreversible / permanent / temporary_suppression`
- **로그 연결**: `Subjugation`, `WholeBody`, `Received`
- **획득 조건**: `Subjugation milestone + 반복 부상·굴복 사건`
- **고착 조건**: `획득 즉시 permanent`

### 3-2. 노출증 — `#Trait_Exhibitionistic_Urge`
- **Risk**: 거점 대기 욕구 증가 / 공공구역 판정 불이익
- **Return**: 노출·수치 사건 보상 강화
- **처리/고착/완화**: `self_expiring / temporary / duration_reduction`
- **로그 연결**: `Contact + Cognition`, `WholeBody`, `Performed`
- **획득 조건**: `Contact proficiency + 노출 사건`
- **고착 조건**: `반복 획득 + Cognition proficiency + 공개 고착 사건`

### 3-3. 정액 중독 — `#Trait_Semen_Dependency`
- **Risk**: 미충족 시 컨디션 저하
- **Return**: 충족 시 단기 능력 강화 / 중독 선택지 해금
- **처리/고착/완화**: `irreversible / permanent / temporary_suppression`
- **로그 연결**: `Fluid`, `Mouth or LowerBody`, `Received`
- **획득 조건**: `Fluid milestone + 관련 부위 Lv2 + 의존 사건`
- **고착 조건**: `획득 즉시 permanent`

### 3-4. 가학증 — `#Trait_Sadistic_Cruelty`
- **Risk**: 대화·간호 시 대상 관계 악화
- **Return**: 전투·불만 사건에서 스트레스 회복 / 가학 기술 강화
- **처리/고착/완화**: `suppressible / persistent / stage_down`
- **로그 연결**: `Subjugation + Cognition`, `WholeBody`, `Performed`
- **획득 조건**: `Subjugation proficiency + 가학 행동 기록`
- **고착 조건**: `재획득 + Cognition milestone + 피해 사건`

---

## SECTION 4 — 성벽 부여 계열

### 4-1. 괴물 성애 — `#Trait_Xenophilic_Obsession`
- **Risk**: 도주·기습 선택 시 정신력 또는 자제 판정 요구
- **Return**: 괴물 조우 스트레스 면제 / 괴물 상호작용 선택지 해금
- **처리/고착/완화**: `irreversible / permanent / temporary_suppression`
- **로그 연결**: `Cognition + Contact`, `WholeBody`, `Received`
- **획득 조건**: `Cognition milestone + 반복 괴물 친화·굴복 사건`
- **고착 조건**: `획득 즉시 permanent`
- **자제 판정**: `성공=도주·기습 수행 / 부분 성공=대가 후 수행 / 실패=정면 대치`
- 한 NPC가 파티 전체의 선택을 자동 봉쇄하지 않는다.

### 4-2. 강박적 자위벽 — `#Trait_Compulsive_Masturbation`
- **Risk**: 피로 누적 확률
- **Return**: 자가 완화·욕구 관리 선택지 해금
- **처리/고착/완화**: `self_expiring / temporary / duration_reduction`
- **로그 연결**: `Contact`, `LowerBody`, `Performed`
- **획득 조건**: `Contact proficiency + 반복 자가 행위 기록`
- **고착 조건**: `반복 획득 + Cognition proficiency`

### 4-3. 도구 고착증 — `#Trait_Toy_Fixation`
- **Risk**: 전투 능력 저하 / 제작 자원 손실 위험
- **Return**: 도구·장비 기반 R18 기술 강화
- **처리/고착/완화**: `irreversible / permanent / temporary_suppression`
- **로그 연결**: `Cognition + Penetration`, `LowerBody or Rear`, `Developed`
- **획득 조건**: `Cognition milestone + 특정 도구 사건`
- **고착 조건**: `획득 즉시 permanent`

### 4-4. 수치성 노예벽 — `#Trait_Submissive_Slave_Urge`
- **Risk**: 반항·거리두기 선택지 제한 / 자기결정성 약화
- **Return**: 가학 명령 불만 증가 면제 / 굴복 기술 강화
- **처리/고착/완화**: `irreversible / permanent / none`
- **로그 연결**: `Subjugation + Cognition`, `WholeBody`, `Received`
- **획득 조건**: `Subjugation milestone + 복종 고착 사건`
- **고착 조건**: `획득 즉시 permanent`

---

## SECTION 5 — 상식 개변 계열

### 5-1. 무조건적 성적 개방 — `#Trait_Universal_Sexual_Consent`
- **Risk**: 정신력 저하 / 외부 협상 선택지 왜곡
- **Return**: 특수 협상·관계 선택지 해금
- **처리/고착/완화**: `suppressible / persistent / stage_down`
- **로그 연결**: `Cognition`, `WholeBody`, `Received`
- **획득 조건**: `Cognition proficiency + 상식 개변 사건`
- **고착 조건**: `재획득 + Cognition milestone + 외부 세력 사건`

### 5-2. 가학 복종의 정당성 — `#Trait_Acceptance_of_Humiliation`
- **Risk**: 리더 의존·가학 명령 수용 고착
- **Return**: 리더 인접 시 스트레스 회복 / 굴욕 명령 비용 면제
- **처리/고착/완화**: `irreversible / permanent / none`
- **로그 연결**: `Cognition + Subjugation`, `WholeBody`, `Received`
- **획득 조건**: `Cognition milestone + Subjugation milestone + 리더 의존 사건`
- **고착 조건**: `획득 즉시 permanent`

### 5-3. 성적 보상 주의 — `#Trait_Sexual_Efficaciousness`
- **Risk**: 배급 시 욕구 증가 / 보상 구조 왜곡
- **Return**: 성적 보상 협상·관계 사건 해금
- **처리/고착/완화**: `self_expiring / persistent / duration_reduction`
- **로그 연결**: `Cognition + Subjugation`, `WholeBody`, `Performed or Received`
- **획득 조건**: `Cognition proficiency + 반복 보상 교환 사건`
- **고착 조건**: `재획득 + Subjugation milestone`

### 5-4. 수치심 상실 — `#Trait_Shameless_Normalization`
- **Risk**: 대화 능력 저하 / 공공 노출 사건 증가
- **Return**: 수치·노출 패널티 일부 면제 / 관련 선택지 해금
- **처리/고착/완화**: `irreversible / permanent / temporary_suppression`
- **로그 연결**: `Cognition + Contact`, `WholeBody`, `Performed`
- **획득 조건**: `Cognition milestone + 공개 노출 사건`
- **고착 조건**: `획득 즉시 permanent`

---

## SECTION 6 — 욕구 계열

### 6-1. 발정 상태 — `#Trait_Estrus_Hyperexcitation`
- **Risk**: 욕구·정신력 악화 / 전투·탐색 난이도 상승
- **Return**: 해소 성공 시 조기 종료 / 욕구 기술 강화
- **처리/고착/완화**: `self_expiring / temporary / duration_reduction`
- **로그 연결**: `Contact + Fluid`, `WholeBody`, `Received`
- **획득 조건**: `관련 축 record + 발정 유발 사건`
- **고착 조건**: `반복 획득 + Cognition proficiency + 고착 사건`

### 6-2. 접촉 기갈 — `#Trait_Tactile_Deprivation`
- **Risk**: 단독 배치 스트레스 / 배치 자유도 제한
- **Return**: 동행·접촉 관계 효과 강화
- **처리/고착/완화**: `self_expiring / temporary / duration_reduction`
- **로그 연결**: `Contact`, `WholeBody`, `Received`
- **획득 조건**: `Contact proficiency + 접촉 단절 사건`
- **고착 조건**: `반복 획득 + Contact milestone`

### 6-3. 음어 증후군 — `#Trait_Coprolalia_Erotica`
- **Risk**: 대화 능력 저하 / 협상 적대화 위험
- **Return**: 도발·굴욕·음어 선택지 강화
- **처리/고착/완화**: `self_expiring / temporary / duration_reduction`
- **로그 연결**: `Cognition + Subjugation`, `Mouth`, `Performed`
- **획득 조건**: `Cognition proficiency + 언어 개변 사건`
- **고착 조건**: `반복 획득 + Mouth Lv2 + Cognition milestone`

### 6-4. 쾌감 수용체 폭주 — `#Trait_Orgasmic_Amplification`
- **Risk**: 체력 상한 감소 / R18 개입 침식도 증가
- **Return**: 컨디션 증가 / 쾌감·굴복 기술 강화
- **처리/고착/완화**: `irreversible / permanent / temporary_suppression`
- **로그 연결**: `Subjugation + Mutation`, `WholeBody`, `Climaxed`
- **획득 조건**: `Subjugation milestone + WholeBody Lv3 + 수용체 변이 사건`
- **고착 조건**: `획득 즉시 permanent`

---

## SECTION 7 — 완화·재획득·고착 공통 규칙

- `self_expiring`: 현재 효과는 종료되지만 로그·획득 이력은 남는다.
- `suppressible`: 기록을 유지한 채 단계 하향 또는 일부 효과 억제가 가능하다.
- `irreversible`: 일반 제거·단계 하향이 불가능하다.
- `temporary_suppression`: 지정된 Risk와 직접 연결된 Return을 함께 억제한다.
- 동일 기벽 재획득 시 중복 객체를 만들지 않고 지속시간·획득 횟수·고착 후보를 갱신한다.
- 영구화는 재획득 횟수, 관련 축 단계, 사건·플래그 조건을 함께 검사한다.

## SECTION 8 — 미확정 항목

- 공통 축 단계의 실제 임계 수치
- 부위 경험치와 레벨 공식
- 개별 사건 ID와 플래그명
- 재획득 횟수와 고착 수치
- Return·굴복 기술 보정값
- 일시 억제 비용과 지속시간

## SECTION 9 — 콘텐츠 경계

- 성인 캐릭터에만 적용한다.
- SFW 빌드에서는 본 DB 전체를 비활성화한다.
- 공통 시스템은 본 문서에 의존하지 않는다.

## SECTION 10 — 버전 관리

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.0.0 | 2026-05-31 | 최초 24종 기벽 정의. |
| v1.1.0 | 2026-06-05 | 메모리 로그 연동 초안. |
| v1.2.0 | 2026-07-14 | Risk & Return, 처리 모델, 고착과 완화 구조 적용. |
| v1.3.0 | 2026-07-14 | 24종 축·부위·행위 로그 연결, 획득·고착 조건 분리, 괴물 성애 하드락 제거. |

**갱신 기준**: 실제 임계값·사건 ID·굴복 기술 연결이 확정되면 정본 잠금.