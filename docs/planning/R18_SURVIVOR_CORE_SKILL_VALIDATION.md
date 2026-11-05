# R18 Survivor Core Skill Validation

## 데이터 계약

- [ ] 5개 기본 Skill ID가 기존 카탈로그와 동일하다.
- [ ] `progress_part`는 영문 정본 키 또는 null이다.
- [ ] `display_part`는 UI 출력 외 판정에 사용하지 않는다.
- [ ] 기본 기술의 `variant_source_quirks`는 빈 배열이다.
- [ ] 기본 기술은 완화 상태에서도 선택 가능하다.

## 전투 회귀

- [ ] 봉사형 게이지 변화가 기존과 동일하다.
- [ ] 유혹형 `fx_sub_weaken_next`가 유지된다.
- [ ] 농락형 `fx_sub_dom_scaling`과 `ST_Afterglow`가 유지된다.
- [ ] 흡수형 `fx_sub_absorb_recover`와 Fluid 진척이 유지된다.
- [ ] 저항형 `fx_sub_defiance`와 `bypass_gating`이 유지된다.

## 변종 제한

- [ ] Proficiency에서 동일 기벽의 활성 변종은 최대 1개다.
- [ ] Milestone에서만 두 번째 변종 또는 강한 특수 효과를 선택할 수 있다.
- [ ] 완화 중 기벽 전용 Return과 변종만 비활성화된다.
- [ ] 단순 수치 상위호환 변종이 존재하지 않는다.

## 마이그레이션 종료

- [ ] 런타임의 동일 ID 우선순위가 정본 샤드를 가리킨다.
- [ ] 기존 Skill Catalog SECTION 4를 제거하거나 샤드 참조로 전환한다.
- [ ] 중복 ID 기술 부채를 PROJECT_STATE에서 제거한다.
