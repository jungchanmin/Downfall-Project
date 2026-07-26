# MECH_R18_Body_Sensitivity_System

> Status: Canonical Draft
> Phase: 5N-3
> Scope: 특수 굴복페이즈 신체 부위·약점·감응·반복 공략 규칙

---

## 1. 문서 목적

이 문서는 특수 굴복페이즈에서 사용하는 신체 부위 계층, 개체 고유 약점, 전투 중 부위 감응도, 반복 공략과 보호 행동, 비인간형 괴물의 특수 기관, 약점 공개 단계를 정본화한다.

이 문서는 `MECH_R18_Submission_Resource_System`의 굴복도·탈진력·절정도 규칙을 확장한다. 이 문서가 자원 수치를 직접 소유하지 않으며, 부위 상태가 해당 자원에 어떤 보정을 제공하는지만 정의한다.

---

## 2. 정본 우선순위

부위·약점·감응 규칙이 다른 문서와 충돌할 경우 다음 순서를 따른다.

1. `MECH_R18_Body_Sensitivity_System`
2. `MECH_R18_Submission_Resource_System`
3. `MECH_R18_Submission_Core_System`
4. `MECH_R18_Skill_Data_Contract`
5. 개별 기술·괴물·이벤트 문서

개별 괴물과 기술은 이 문서의 기본값을 명시적으로 오버라이드할 수 있으나, 오버라이드 필드와 출처를 기록해야 한다.

---

## 3. 핵심 개념 분리

### 3.1 신체 부위

신체 부위는 기술의 표적, 사용 가능 여부, 자세·점유·의복 Gate를 결정하는 데이터다.

신체 부위 자체는 자동으로 약점이나 감응 보너스를 갖지 않는다.

### 3.2 약점

약점은 전투 시작 전부터 존재하는 개체 고유 특성이다.

- 반복 공격으로 생성되지 않는다.
- 괴물·생존자·기벽·변이·장비에 의해 정의될 수 있다.
- 약점 정보는 단계적으로 공개될 수 있다.

### 3.3 감응도

감응도는 현재 굴복페이즈에서 특정 부위가 자극에 얼마나 누적 노출되었는지를 나타내는 일시적 상태다.

```text
Normal
→ Sensitive
→ Overstimulated
```

약점과 감응도는 별도 필드로 관리한다.

---

## 4. 부위 계층

부위는 `대분류 group`과 `세부 부위 specific_part`를 함께 사용한다.

| 대분류 | 세부 부위 예시 |
|---|---|
| Mouth | 입술, 입, 혀 |
| Chest | 가슴, 유두 |
| LowerBody | 성기, 허벅지 안쪽 |
| Rear | 엉덩이, 항문 |
| WholeBody | 피부, 전신 밀착 |
| SpecialOrgan | 촉수, 점액기관, 감각핵, 흡반, 뿌리 기관 |

기술은 기본적으로 대분류를 목표로 삼고, 특정 기술·약점·피니셔만 세부 부위를 요구한다.

```yaml
body_part:
  group: Mouth
  specific_part: Tongue
```

### 4.1 표시명 원칙

- 내부 키는 영문 정규화 키를 사용한다.
- UI·Narration·Bark는 플레이어가 이해하기 쉬운 직접적인 한국어 명칭을 사용한다.
- 인간형이 아닌 괴물은 존재하지 않는 인간 부위를 강제로 부여하지 않는다.

---

## 5. 공통 부위 데이터 계약

```yaml
body_part_state:
  part_id: Genitals
  display_name: 성기
  group: LowerBody

  availability:
    usable: true
    targetable: true

  weakness:
    level: Major
    effect_type: Exhaustion
    hidden: true
    disclosure_state: Unknown

  sensitivity:
    stage: Normal
    progress_mark: 0

  protection:
    guarded: false
    clothing_state: Intact

  occupancy:
    occupied_by: null
    restricted_actions: []

  effect_profile: SurvivorDefault
```

런타임에서는 실제로 목표가 되었거나 상태가 변한 부위만 동적 상태 객체를 생성한다.

---

## 6. 감응 단계

### 6.1 생존자 기본 효과

| 단계 | 효과 |
|---|---|
| Normal | 추가 효과 없음 |
| Sensitive | 해당 부위가 받는 절정도 증가 `+1` |
| Overstimulated | 해당 부위가 받는 절정도 증가 `+1`, 굴복도 피해 `+1` |

`Overstimulated`의 굴복도 피해는 기술 직접 굴복 피해와 합산된다.

### 6.2 괴물 기본 효과

| 단계 | 효과 |
|---|---|
| Normal | 추가 효과 없음 |
| Sensitive | 해당 부위가 받는 탈진력 피해 `+1` |
| Overstimulated | 해당 부위가 받는 탈진력 피해 `+1`, 안정성 `-1` |

괴물 `Overstimulated`가 탈진력 피해 `+2`를 주는 기본 규칙은 사용하지 않는다. 약점과 중첩될 때 피해가 폭증하는 것을 방지하기 위해 추가 이득 일부를 안정성 약화로 분산한다.

### 6.3 효과 프로필 분리

공통 데이터 구조를 사용하되 생존자와 괴물의 효과는 별도 프로필로 관리한다.

```yaml
sensitivity_effect_profile: SurvivorDefault
```

```yaml
sensitivity_effect_profile: MonsterDefault
```

개별 괴물은 전용 프로필을 사용할 수 있다.

---

## 7. 감응 진행

감응도는 별도 대형 게이지를 사용하지 않고 `진행 표식 progress_mark`로 단계 상승을 처리한다.

### 7.1 기본 진행값

| 기술 등급 | 감응 진행 |
|---|---:|
| Minor | `+1` 표식 |
| Standard | `+2` 표식 |
| Major | 기술별 정의, 기본적으로 다음 단계 즉시 상승 가능 |
| Finisher | 기술별 정의 |

### 7.2 단계 상승

```text
진행 표식 2 이상
→ 감응 단계 1단계 상승
→ 진행 표식 0으로 재설정
```

예:

- Minor 성공 2회 → 다음 단계
- Standard 성공 1회 → 다음 단계
- Major 성공 → 기술 정의에 따라 즉시 상승

### 7.3 상한

감응 단계는 기본적으로 `Overstimulated`를 초과하지 않는다.

추가 단계가 필요한 괴물은 개별 전용 상태를 사용한다.

### 7.4 진행 적용 조건

감응 진행은 다음 조건을 모두 만족할 때만 적용한다.

- 기술이 실제 대상 부위에 유효하게 접촉함
- 기술 결과가 감응 진행을 허용함
- 대상 부위가 `targetable: true`
- 보호·점유·상태가 진행을 완전히 차단하지 않음

부분 성공은 기술 계약에 따라 진행값을 감소시킬 수 있다.

---

## 8. 약점 시스템

### 8.1 약점 등급

```text
None
Minor
Major
Critical
```

| 등급 | 역할 |
|---|---|
| None | 약점 효과 없음 |
| Minor | 단일 소규모 보너스 |
| Major | 주요 보너스와 조건부 부가 효과 |
| Critical | 엄격한 조건을 만족했을 때 강력한 효과 또는 피니셔 연결 |

### 8.2 약점 효과 유형

약점은 다음 세 유형 중 하나 이상을 가진다.

#### Exhaustion

괴물 탈진력 피해를 증가시키거나 탈진 결착을 가속한다.

#### Control

자세·점유·주도권·기술 사용·안정성에 영향을 준다.

#### ClimaxSensitivity

절정도 증가, 감응 진행, 자기 절정 위험 또는 부위 반응에 영향을 준다.

약점은 반드시 탈진력 피해를 올릴 필요가 없다.

```yaml
weakness:
  level: Major
  effect_type: Control
  effects:
    on_success_status: ST_BreathDisrupted
    disable_skill_tag: CognitionFocus
```

### 8.3 중첩 원칙

약점과 감응도는 중첩 가능하지만 서로 다른 역할을 유지한다.

- 약점: 개체 고유 취약성
- 감응도: 현재 전투에서 누적된 상태

동일 공격에서 약점·감응도·판정 보너스가 모두 적용되더라도 기술 등급별 피해·절정 상한을 초과할 수 없다. 피니셔와 명시적 오버라이드만 예외다.

---

## 9. 약점 공개 단계

```text
Unknown
→ Suspected
→ Confirmed
→ Mastered
```

| 단계 | 공개 정보 |
|---|---|
| Unknown | 정보 없음 |
| Suspected | 반응이 크다는 Narration·불확실 Bark |
| Confirmed | 약점 부위와 핵심 효과 공개 |
| Mastered | 최적 자세·기술·대응·보호 행동까지 공개 |

### 9.1 공개 조건 후보

- 최초 유효 공략
- 동일 반응 반복 확인
- 지능·탐색 판정
- 동료 조언
- Memory Log
- 괴물 연구·도감
- 기벽·직업 고유 능력

### 9.2 연출 규칙

`Suspected` 단계에서는 확정 표현을 사용하지 않는다.

예:

> “거길 건드릴 때 반응이 큰 것 같은데….”

`Confirmed` 이후에는 명확한 Bark를 허용한다.

> “확실해. 혀가 약점이야.”

---

## 10. 반복 공략

감응도 상승만 존재하면 동일 부위 반복이 최적해가 되므로, 반복 공략은 방어자의 보호 행동을 해금한다.

### 10.1 기본 규칙

| 동일 부위 연속 공략 | 방어자 효과 |
|---:|---|
| 첫 번째 | 추가 효과 없음 |
| 두 번째 | 해당 부위 보호 행동 해금 |
| 세 번째 이상 | 해당 부위 반응 판정 `+1` 후보 |

`+1`은 자동 상시 보너스가 아니라 실제 보호 행동 또는 대응 기술을 선택했을 때만 적용한다.

### 10.2 연속 판정 기준

다음 중 하나가 발생하면 연속 공략 카운트를 초기화한다.

- 다른 부위를 목표로 유효 기술 사용
- 자세 변화로 해당 부위 접근이 끊김
- 보호 행동으로 공략 흐름이 완전히 차단됨
- 개별 기술이 반복 카운트 초기화를 명시함

실패한 공격이 연속 공략으로 계산되는지는 기술별 계약을 따른다. 기본값은 `유효 접촉 성공`만 계산한다.

---

## 11. 보호 행동

보호 행동은 부위를 영구 무효화하지 않고 공략 방향을 바꾸게 해야 한다.

### 11.1 기본 효과 후보

- 해당 부위 Gate 강도 `+1`
- 해당 부위 감응 진행 `-1`
- 해당 부위 반응 판정 `+1`
- 주도권을 포기하고 완전 보호
- 다른 부위 노출

### 11.2 권장 계약

```yaml
guard_part:
  protected_part: Chest
  gate_strength_bonus: 1
  sensitivity_progress_reduction: 1
  reactive_modifier: 1
  exposes_part: LowerBody
```

### 11.3 설계 원칙

- 한 부위를 보호하면 다른 부위·자세·행동 기회가 열려야 한다.
- 모든 부위를 동시에 보호하는 공용 행동은 기본 제공하지 않는다.
- 보호 행동은 공격을 완전히 봉쇄하기보다 다음 선택을 바꾸는 역할을 우선한다.

---

## 12. 감응 감소

### 12.1 자연 감소

감응도는 전투 중 자연 감소하지 않는다.

감소는 다음을 통해서만 발생한다.

- Defiance
- 부위 보호 행동
- 감각 차단 기술
- 괴물 재생·변형
- 생존자 고유 능력
- 기벽 Return

### 12.2 감소 방식

기본 감소 단위는 다음 중 하나다.

- 진행 표식 감소
- 감응 단계 1단계 하향
- 특정 부위 감응 효과 1회 무효

감응 단계 전체 초기화는 희귀 효과로 제한한다.

---

## 13. 전투 종료 후 처리

기본 처리:

| 종료 시 단계 | 처리 |
|---|---|
| Normal | 제거 |
| Sensitive | 제거 |
| Overstimulated | 전투 후 후유 상태 전환 후보 |

`Overstimulated`의 실제 지속 여부와 회복 시간은 전투 후 상태·완화 시스템이 소유한다.

```yaml
battle_end_conversion:
  from: Overstimulated
  to: ResidualSensitivity
  policy: system_defined
```

---

## 14. 비인간형 괴물

모든 괴물은 굴복페이즈용 신체 구조를 직접 선언한다.

```yaml
submission_anatomy:
  body_groups:
    - Mouth
    - SpecialOrgan
    - WholeBody

  specific_parts:
    - id: Tongue
      group: Mouth
      targetable: true

    - id: TentacleRoot
      group: SpecialOrgan
      targetable: true

    - id: SensoryCore
      group: SpecialOrgan
      targetable: false
      unlock_condition: ST_ArmorOpened
```

### 14.1 부위 부재

존재하지 않는 부위를 요구하는 기술은 사용할 수 없다.

예:

- 성기 없는 괴물에게 핸드잡 사용 불가
- 가슴 없는 괴물에게 가슴 주무르기 사용 불가
- 촉수 괴물에게 촉수·뿌리·흡반 계열 변종 사용 가능

### 14.2 SpecialOrgan 원칙

`SpecialOrgan`은 만능 단일 부위가 아니다. 실제 개체별 기관을 세부 부위로 선언해야 한다.

---

## 15. 일반전투 부위 손상과의 경계

일반전투의 부상·파괴와 굴복페이즈 감응도는 별도 상태다.

| 일반전투 | 굴복페이즈 |
|---|---|
| 부상·파괴 | 감응·과자극 |
| 사용 불가·손상 | 절정·탈진 보정 |
| 물리적 구조 변화 | 일시적 자극 누적 |

다만 구조적 손상은 굴복페이즈에 이관된다.

예:

- 팔 골절 → Hand 행동 부위 제한
- 괴물 촉수 절단 → 해당 촉수 목표·기술 비활성
- 보호 갑각 파괴 → 내부 특수 기관 targetable 해금

일반전투 체력 손실 자체는 감응 단계로 환산하지 않는다.

---

## 16. Narration·Bark 트리거

부위 상태는 다음 연출 트리거를 제공한다.

### 16.1 Narration

- 감응 단계 상승
- 과자극 부위 재공략
- 상대 보호 행동
- 약점 의심·확정
- 특정 부위 사용 불가
- 비인간형 특수 기관 노출

### 16.2 Bark

#### 약점 의심

> “거길 건드릴 때 반응이 커….”

#### 약점 확정

> “확실해. 저기가 약점이야.”

#### 자기 부위 위험

> “또 같은 곳은 안 돼….”

#### 보호 행동 인식

> “가슴을 가렸네. 다른 곳을 노려야겠어.”

Bark 문장 자체는 전투 시나리오에서 추출하며, 이 문서는 출력 조건만 소유한다.

---

## 17. 처리 순서

한 기술이 부위에 유효하게 성공했을 때 다음 순서로 처리한다.

1. 대상 부위 유효성·접근 Gate 확인
2. 보호 행동·점유·의복 보정 적용
3. 기술 직접 효과 계산
4. 약점 효과 적용
5. 현재 감응 단계 효과 적용
6. 기술 등급별 피해·절정 상한 적용
7. 굴복도·탈진력·절정도 반영
8. 감응 진행 표식 적용
9. 감응 단계 상승 확인
10. 반복 공략 카운트 갱신
11. 약점 공개 단계 갱신
12. Narration·Bark 트리거 생성
13. 결착 확인

공격자 효과 우선은 `MECH_R18_Submission_Resource_System`을 따른다.

---

## 18. 검증 규칙

다음 상태는 데이터 검증 오류다.

- 존재하지 않는 부위를 기술이 필수 목표로 요구함
- `targetable: false` 부위를 해금 조건 없이 목표로 지정함
- 감응 단계가 `Overstimulated`를 초과하지만 전용 상태가 없음
- 약점 효과 유형이 없는데 보너스만 선언됨
- 약점 공개 상태가 `Confirmed` 이상인데 부위 정보가 비공개임
- 보호 행동이 모든 대체 부위를 동시에 차단함
- 생존자·괴물 효과 프로필이 지정되지 않음
- `SpecialOrgan`만 선언하고 세부 기관이 없음
- 일반전투 부상과 감응도를 같은 필드로 저장함

---

## 19. 현재 미확정 항목

- 기술별 실제 감응 진행값
- Major 기술의 즉시 단계 상승 범위
- 세 번째 반복 공략 반응 `+1`의 실제 적용 범위
- 약점 등급별 수치 기본값
- 탈진 피해 등급별 최종 상한
- Critical 약점의 즉시 결착 허용 여부
- 전투 후 `ResidualSensitivity`의 지속·회복
- 의복 상태와 부위 Gate의 정식 계약
- 다대일 전투에서 부위 감응 정보 공유
- Memory Log·괴물 도감의 약점 공개 승계

---

## 20. 후속 작업

1. 굴복 전용 생존자 기본 기술 풀 작성 규칙
2. 의복 상태·부위 접근 Gate 정본
3. Combat Narration 조건 블록과 우선순위
4. 광신도 6종 기술에 부위·감응·약점 필드 재배정
5. 비인간형 괴물 1종 SpecialOrgan 수직 테스트
6. Absorption·Fluid·Mutation 페이퍼 전투 테스트
