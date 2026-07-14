---
id: MECH_Quirk_R18_DB
title: "핵심 시스템 사양서 — R18 전용 변이 및 정신 개변 기벽 데이터베이스"
type: mechanic
status: wip
version: 1.2.0
summary: >
  R18 트랙 직결 특수 신체 변이·감도 개발·성벽·상식 개변·욕구 기벽 24종.
  일반 간호 제거를 배제하고 Risk & Return, 완화 방식, 고착 상태와 메모리 로그 보존 규칙을 정의한다.
tags:
  - mechanic
  - quirk
  - database
  - r18
keywords:
  - 기벽, R18, 신체 변이, 감도 개발, 성벽, 상식 개변, 침식도, 욕구불만,
    해금 조건, 완화, 메모리 로그, 굴복 전용 기술
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

# 🔞 DOWNFALL R18 전용 변이 및 정신 개변 데이터베이스 (v1.2)

> ⚠️ 저수치 스케일 롤백 반영 주의: `상한치 -5/-10` 류 패널티는 0~10 체력/정신력 스케일에 맞춰 **−1~−2 급으로 재튜닝 대상**이다. 본 버전은 연동 구조를 우선 정식화하며, 개별 수치는 밸런스 패스에서 조정한다.

## 0. 공통 처리 원칙

- R18 기벽은 일반 간호·의무실로 제거하지 않는다.
- 각 기벽은 `Risk`와 `Return`을 함께 가진다.
- 완화·지속 종료 후에도 메모리 로그, 획득 기록과 해금 플래그는 유지한다.
- 반복 경험은 `temporary → persistent → permanent` 고착 후보가 된다.
- 일반 `색광증`과 R18 기벽은 중첩 가능하며, 공통 충동 패널티는 일반 DB, 고착·로그·R18 선택지는 본 모듈이 소유한다.

---

## SECTION 1 — 신체 변이 계열 (Anatomical Mutation)

### 1-1. 살점 융기 (유방 비대화) — `#Trait_Flesh_Anomalous_Swelling`
- 상시: `#Stat_Fatigue 누적 +1`, `#Stat_Libido +1`
- 선택지 변동: 외출·탐험 회피 `stat_check` DC +2
- **처리 모델**: `irreversible`
- **고착 상태**: `permanent`
- **완화 방식**: `none`
- **Risk**: 피로 누적 증가 / 회피 판정 난이도 상승
- **Return**: 특정 R18 관계·외형 반응 선택지 해금
- **메모리 로그**: `관련 부위·행위 로그 누적, 효과 변화 후에도 기록 유지`
- 지속: 영구 변이

### 1-2. 이종 이식 (후타나리화) — `#Trait_Androgynous_Sprout`
- 상시: 매 새벽 `#Stat_Frustration +2`
- 선택지 변동: Track B 스킨십 거절 선택지 강제 잠금
- **처리 모델**: `irreversible`
- **고착 상태**: `permanent`
- **완화 방식**: `none`
- **Risk**: 욕구불만 누적 / 일부 거절 선택지 잠금
- **Return**: 특정 신체 개조·관계 이벤트 해금
- **메모리 로그**: `관련 부위·행위 로그 누적, 효과 변화 후에도 기록 유지`
- 지속: 영구 변이

### 1-3. 피부 유즙화 — `#Trait_Cutaneous_Secretion`
- 상시: `#Stat_Condition -1`
- 선택지 변동: 치료/간호 진입 시 `[식량]` 1개 추가 요구
- **처리 모델**: `self_expiring`
- **고착 상태**: `temporary`
- **완화 방식**: `duration_reduction`
- **Risk**: 컨디션 저하 / 치료 자원 추가 소모
- **Return**: 특정 영양·간호·R18 이벤트 선택지 해금
- **메모리 로그**: `관련 부위·행위 로그 누적, 효과 변화 후에도 기록 유지`
- 지속: 15페이즈 (관련 이벤트 시 10페이즈 갱신)

### 1-4. 음핵 비대증 — `#Trait_Hypertrophied_Clitoris`
- 상시: 이동 완료 시 `#Stat_Stress +1`
- 선택지 변동: 탐색 실패 시 `#Stat_Condition -2`
- **처리 모델**: `irreversible`
- **고착 상태**: `permanent`
- **완화 방식**: `none`
- **Risk**: 이동 후 스트레스 / 탐색 실패 부작용
- **Return**: 감도·굴복 계열 선택지 강화
- **메모리 로그**: `관련 부위·행위 로그 누적, 효과 변화 후에도 기록 유지`
- 지속: 영구 변이

---

## SECTION 2 — 감도 개발 계열 (Anatomical Sensitivity)

### 2-1. 유두 민감화 — `#Trait_Hypersensitive_Nipples`
- 상시: `#Stat_Stress 누적 +1`
- 선택지 변동: 제작 명령 판정 −2
- **처리 모델**: `self_expiring`
- **고착 상태**: `temporary`
- **완화 방식**: `duration_reduction`
- **Risk**: 스트레스 누적 / 제작 판정 불이익
- **Return**: 접촉·감도 계열 선택지 강화
- **메모리 로그**: `관련 부위·행위 로그 누적, 효과 변화 후에도 기록 유지`
- 지속: 20페이즈

### 2-2. 자궁 개발 — `#Trait_Uterine_Sensitization`
- 상시: 매 밤 `#Stat_Libido +2`
- 선택지 변동: 리더 단독 개입 시 침식도 상승 2배
- **처리 모델**: `irreversible`
- **고착 상태**: `permanent`
- **완화 방식**: `none`
- **Risk**: 욕구 증가 / 침식도 상승 증폭
- **Return**: 하복부·굴복 기술 강화
- **메모리 로그**: `관련 부위·행위 로그 누적, 효과 변화 후에도 기록 유지`
- 지속: 영구 변이

### 2-3. 후장 개발 — `#Trait_Anal_Sensitization`
- 상시: `#Stat_Condition -1`
- 선택지 변동: 불침번(탐색) −1
- **처리 모델**: `suppressible`
- **고착 상태**: `persistent`
- **완화 방식**: `stage_down`
- **Risk**: 컨디션 저하 / 불침번 판정 불이익
- **Return**: 후방 감도·굴복 선택지 강화
- **메모리 로그**: `관련 부위·행위 로그 누적, 효과 변화 후에도 기록 유지`
- 지속: 25페이즈

### 2-4. 전신 성감대화 — `#Trait_Pansexual_Skin_Erosion`
- 상시: `#Stat_Sanity 상한치 -2`
- 선택지 변동: 대화·교류 판정 시 `#Stat_Frustration` 만큼 DC 증가
- **처리 모델**: `irreversible`
- **고착 상태**: `permanent`
- **완화 방식**: `none`
- **Risk**: 정신력 상한 감소 / 교류 난이도 상승
- **Return**: 전신 감도·접촉 반응 선택지 강화
- **메모리 로그**: `관련 부위·행위 로그 누적, 효과 변화 후에도 기록 유지`
- 지속: 영구 변이

---

## SECTION 3 — 내구성(음란 내성) 계열 (Erotic Endurance)

### 3-1. 피학증 — `#Trait_Masochistic_Surrender`
- 상시: 체력 감소 이벤트 시 `#Stat_Stress -2`
- 선택지 변동: 부상 상태 진입 시 공격 판정 −2
- **처리 모델**: `irreversible`
- **고착 상태**: `permanent`
- **완화 방식**: `temporary_suppression`
- **Risk**: 부상 시 공격 판정 불이익
- **Return**: 체력 감소 시 스트레스 회복 / 피학·굴복 기술 강화
- **메모리 로그**: `관련 부위·행위 로그 누적, 효과 변화 후에도 기록 유지`
- 지속: 영구 변이

### 3-2. 노출증 — `#Trait_Exhibitionistic_Urge`
- 상시: 거점 대기 시 매 페이즈 `#Stat_Frustration +1`
- 선택지 변동: 공공 구역 이벤트 시 의복 착용 상태면 판정 −2
- **처리 모델**: `self_expiring`
- **고착 상태**: `temporary`
- **완화 방식**: `duration_reduction`
- **Risk**: 거점 대기 욕구 증가 / 공공구역 판정 불이익
- **Return**: 노출·수치 이벤트 보상 강화
- **메모리 로그**: `관련 부위·행위 로그 누적, 효과 변화 후에도 기록 유지`
- 지속: 15페이즈

### 3-3. 정액 중독 — `#Trait_Semen_Dependency`
- 상시: 매 새벽 미섭취 시 `#Stat_Condition -2`
- 선택지 변동: 관련 정산 성공 시 3페이즈 모든 능력 +1
- **처리 모델**: `irreversible`
- **고착 상태**: `permanent`
- **완화 방식**: `temporary_suppression`
- **Risk**: 미충족 시 컨디션 저하
- **Return**: 충족 시 단기 능력 강화 / 중독 계열 선택지 해금
- **메모리 로그**: `관련 부위·행위 로그 누적, 효과 변화 후에도 기록 유지`
- 지속: 영구 변이

### 3-4. 가학증 — `#Trait_Sadistic_Cruelty`
- 상시: 동료 불만 상승 또는 전투 시 `#Stat_Stress -1`
- 선택지 변동: 대화/간호 시 대상 불만·스트레스 +1 추가
- **처리 모델**: `suppressible`
- **고착 상태**: `persistent`
- **완화 방식**: `stage_down`
- **Risk**: 대화·간호 시 대상 관계 악화
- **Return**: 전투·불만 사건에서 스트레스 회복 / 가학 기술 강화
- **메모리 로그**: `관련 부위·행위 로그 누적, 효과 변화 후에도 기록 유지`
- 지속: 20페이즈

---

## SECTION 4 — 성벽 부여 계열 (Fetish Implantation)

### 4-1. 괴물 성애 — `#Trait_Xenophilic_Obsession`
- 상시: 괴물 조우 시 `#Stat_Stress` 증가 면제
- 선택지 변동: 전투 시 도망·기습 선택지 차단
- **처리 모델**: `irreversible`
- **고착 상태**: `permanent`
- **완화 방식**: `temporary_suppression`
- **Risk**: 도주·기습 선택지 제한
- **Return**: 괴물 조우 스트레스 면제 / 괴물 상호작용 선택지 해금
- **메모리 로그**: `관련 부위·행위 로그 누적, 효과 변화 후에도 기록 유지`
- 지속: 영구 변이

### 4-2. 강박적 자위벽 — `#Trait_Compulsive_Masturbation`
- 상시: 매 점심 종료 30% `#Stat_Fatigue +1`
- **처리 모델**: `self_expiring`
- **고착 상태**: `temporary`
- **완화 방식**: `duration_reduction`
- **Risk**: 피로 누적 확률
- **Return**: 자가 완화 행동·욕구 관리 선택지 해금
- **메모리 로그**: `관련 부위·행위 로그 누적, 효과 변화 후에도 기록 유지`
- 지속: 10페이즈

### 4-3. 도구 고착증 — `#Trait_Toy_Fixation`
- 상시: `#Stat_Combat -1`
- 선택지 변동: 제작 완료 시 20% 부품 1개 탕진
- **처리 모델**: `irreversible`
- **고착 상태**: `permanent`
- **완화 방식**: `temporary_suppression`
- **Risk**: 전투 능력 저하 / 제작 자원 손실 위험
- **Return**: 도구·장비 기반 R18 기술 강화
- **메모리 로그**: `관련 부위·행위 로그 누적, 효과 변화 후에도 기록 유지`
- 지속: 영구 변이

### 4-4. 수치성 노예벽 — `#Trait_Submissive_Slave_Urge`
- 상시: 가학 명령에 대한 불만도 증가 0
- 선택지 변동: 리더 권한 이벤트 반항·거리두기 선택지 비활성
- **처리 모델**: `irreversible`
- **고착 상태**: `permanent`
- **완화 방식**: `none`
- **Risk**: 반항·거리두기 선택지 제한 / 자기결정성 약화
- **Return**: 가학 명령 불만 증가 면제 / 굴복 기술 강화
- **메모리 로그**: `관련 부위·행위 로그 누적, 효과 변화 후에도 기록 유지`
- 지속: 영구 변이

---

## SECTION 5 — 상식 개변 계열 (Cognitive Rewriting)

### 5-1. 무조건적 성적 개방 — `#Trait_Universal_Sexual_Consent`
- 상시: `#Stat_Sanity -1`
- 선택지 변동: 외부 세력 조우 시 성적 양보 협상 선택지 강제 활성
- **처리 모델**: `suppressible`
- **고착 상태**: `persistent`
- **완화 방식**: `stage_down`
- **Risk**: 정신력 저하 / 외부 협상 선택지 왜곡
- **Return**: 특수 협상·관계 선택지 해금
- **메모리 로그**: `관련 부위·행위 로그 누적, 효과 변화 후에도 기록 유지`
- 지속: 25페이즈

### 5-2. 가학 복종의 정당성 — `#Trait_Acceptance_of_Humiliation`
- 상시: 리더 동일 구역 시 매 페이즈 `#Stat_Stress -1`
- 선택지 변동: 리더 가학/굴욕 명령 시 스트레스·불만 상승 면제
- **처리 모델**: `irreversible`
- **고착 상태**: `permanent`
- **완화 방식**: `none`
- **Risk**: 리더 의존·가학 명령 수용 고착
- **Return**: 리더 인접 시 스트레스 회복 / 굴욕 명령 비용 면제
- **메모리 로그**: `관련 부위·행위 로그 누적, 효과 변화 후에도 기록 유지`
- 지속: 영구 변이

### 5-3. 성적 보상 주의 — `#Trait_Sexual_Efficaciousness`
- 상시: 아침 배급 시 `#Stat_Frustration +1`
- 선택지 변동: 식량·기호품 배급 시 친밀도 요구 분기
- **처리 모델**: `self_expiring`
- **고착 상태**: `persistent`
- **완화 방식**: `duration_reduction`
- **Risk**: 배급 시 욕구 증가 / 보상 구조 왜곡
- **Return**: 성적 보상 협상·관계 이벤트 해금
- **메모리 로그**: `관련 부위·행위 로그 누적, 효과 변화 후에도 기록 유지`
- 지속: 20페이즈

### 5-4. 수치심 상실 — `#Trait_Shameless_Normalization`
- 상시: `#Stat_Dialogue -2`
- 선택지 변동: 거점 R18 공공 노출 이벤트 가중치 증가
- **처리 모델**: `irreversible`
- **고착 상태**: `permanent`
- **완화 방식**: `temporary_suppression`
- **Risk**: 대화 능력 저하 / 공공 노출 사건 증가
- **Return**: 수치·노출 패널티 일부 면제 / 관련 선택지 해금
- **메모리 로그**: `관련 부위·행위 로그 누적, 효과 변화 후에도 기록 유지`
- 지속: 영구 변이

---

## SECTION 6 — 성적 욕구 계열 (Hyperactive Libido)

### 6-1. 발정 상태 — `#Trait_Estrus_Hyperexcitation`
- 상시: 매 페이즈 `#Stat_Frustration +2`, `#Stat_Sanity -1`
- 선택지 변동: 전투·탐색 판정 DC +2
- **처리 모델**: `self_expiring`
- **고착 상태**: `temporary`
- **완화 방식**: `duration_reduction`
- **Risk**: 욕구·정신력 악화 / 전투·탐색 난이도 상승
- **Return**: 해소 성공 시 즉시 종료 가능 / 욕구 기술 강화
- **메모리 로그**: `관련 부위·행위 로그 누적, 효과 변화 후에도 기록 유지`
- 지속: 10페이즈

### 6-2. 접촉 기갈 — `#Trait_Tactile_Deprivation`
- 상시: 단독 배치 시 매 페이즈 `#Stat_Stress +2`
- 선택지 변동: 단독 배치 시 불만도 +3
- **처리 모델**: `self_expiring`
- **고착 상태**: `temporary`
- **완화 방식**: `duration_reduction`
- **Risk**: 단독 배치 스트레스 / 배치 자유도 제한
- **Return**: 동행·접촉 관계 효과 강화
- **메모리 로그**: `관련 부위·행위 로그 누적, 효과 변화 후에도 기록 유지`
- 지속: 15페이즈

### 6-3. 음어 증후군 — `#Trait_Coprolalia_Erotica`
- 상시: `#Stat_Dialogue -3`
- 선택지 변동: 교류·협상 진입 시 30% 적대화
- **처리 모델**: `self_expiring`
- **고착 상태**: `temporary`
- **완화 방식**: `duration_reduction`
- **Risk**: 대화 능력 저하 / 협상 적대화 위험
- **Return**: 도발·굴욕·음어 계열 선택지 강화
- **메모리 로그**: `관련 부위·행위 로그 누적, 효과 변화 후에도 기록 유지`
- 지속: 12페이즈

### 6-4. 쾌감 수용체 폭주 — `#Trait_Orgasmic_Amplification`
- 상시: `#Stat_Condition +1`, `#Stat_HP 상한치 -2`
- 선택지 변동: 모든 R18 트랙 개입 시 침식도 +3
- **처리 모델**: `irreversible`
- **고착 상태**: `permanent`
- **완화 방식**: `temporary_suppression`
- **Risk**: 체력 상한 감소 / R18 개입 침식도 증가
- **Return**: 컨디션 증가 / 쾌감·굴복 기술 강화
- **메모리 로그**: `관련 부위·행위 로그 누적, 효과 변화 후에도 기록 유지`
- 지속: 영구 변이

---

## SECTION 7 — Risk & Return·완화·메모리 로그 공통 규격

### 7-1. 개체별 필드
```yaml
r18_quirk_meta:
  treatment_model: suppressible | self_expiring | irreversible
  lock_state: temporary | persistent | permanent
  mitigation_model: none | duration_reduction | stage_down | temporary_suppression
  risk_effects: []
  return_effects: []
  memory_log_links: []
  unlock_condition: null
  submit_skill_boost: []
```

### 7-2. 공통 규칙

- `self_expiring`은 시간이 지나면 종료될 수 있으며 R18 전용 완화로 지속시간을 줄일 수 있다.
- `suppressible`은 기벽 기록을 유지한 채 효과 일부를 일시 억제하거나 단계를 낮출 수 있다.
- `irreversible`은 일반적인 제거·단계 하향이 불가능하다.
- 완화·종료 후에도 획득 기록, 경험 카운터와 해금 플래그는 유지한다.
- 같은 계열 경험이 반복되면 고착 단계가 상승할 수 있다.
- Return은 위험을 감수할 이유를 제공하지만 기벽 획득을 무조건 유리하게 만들지 않는다.

### 7-3. 메모리 로그 연결

```text
해금 → 기벽 부여
기벽 획득 → 관련 부위·행위 로그 기록
완화·지속 종료 → 현재 효과만 축소, 기록은 보존
반복 획득 → 고착 단계 상승 후보
영구 고착 → 최종 로그·특성·기술 해금 후보
```

---

## SECTION 8 — 저수치 재튜닝 메모 & 콘텐츠 경계

- 과거 0~100 전제 상한치 수치는 0~10 스케일 기준으로 재튜닝한다.
- 성인 캐릭터에만 적용한다.
- SFW 빌드에서는 본 DB 전체를 비활성화한다.

---

## SECTION 9 — 버전 관리

| 버전 | 날짜 | 변경 내용 |
|---|---|---|
| v1.0.0 | 2026-05-31 | 최초 24종 기벽 정의. |
| v1.1.0 | 2026-06-05 | 메모리 로그 연동과 저수치 재튜닝 메모 추가. |
| v1.2.0 | 2026-07-14 | Risk & Return, 처리 모델, 고착 상태, 완화 방식과 기록 보존 규칙 적용. |

**갱신 기준**: 개별 메모리 로그 키·해금 임계값·굴복 기술 연결 확정 후 정본 잠금.