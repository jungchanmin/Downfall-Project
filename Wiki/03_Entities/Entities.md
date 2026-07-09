---
id: ENTITY_Index
title: Downfall 엔티티 인덱스
type: entity_index
status: active
summary: 생존자, 세력, 적대 집단, 광신도, 괴물과 내부 위협 문서의 분류 기준과 진입점을 제공한다.
tags: [entity, index, survivor, faction, monster]
keywords: [생존자, 세력, 적대 집단, 광신도, 괴물, 적대자]
depends_on: [SYS_Document_Rules, LORE_WORLD_Overview]
emits: []
last_updated: 2026-07-06
---

# Downfall 엔티티 인덱스

## 1. Survivors

플레이어를 제외한 네임드 생존자와 영입 가능 인물을 관리한다.

- 경로: `Wiki/03_Entities/Survivors/`
- 소유 정보: 정체성, 성격, 능력, 관계 기준, 기억, 캐릭터 고유 서사
- 현재 문서: 가빈 잭슨, 레이첼 로페즈

## 2. Factions

지속적인 관계도, 지도부, 구성원, 거점, 자원, 거래와 세력 이벤트를 가진 정식 조직이다.

- 광신도
- 자경단
- 악마 조직
- 방랑자들

목표 경로: `Wiki/03_Entities/Factions/`

## 3. Hostile Groups

지속 외교보다 약탈, 납치, 전투와 지역 사건을 중심으로 하는 비정규 적대 집단이다.

- 약탈자
- 납치꾼
- 외부 적대 생존자
- 독립 범죄 집단

목표 경로: `Wiki/03_Entities/Hostile_Groups/`

## 4. Cult

광신도의 교리, 간부, 일반 신도, 의식 역할과 어머니 통제 구조를 관리한다.

목표 경로: `Wiki/03_Entities/Cult/`

광신도는 Faction이지만 25일 의식과 어머니 설정에 직접 연결되므로 별도 하위 분류를 허용한다.

## 5. Monsters

일반형, 돌연변이형, 멸망의 괴물과 개별 몬스터 DB를 관리한다.

- 경로: `Wiki/03_Entities/Monsters/`
- 현재 핵심 DB: `MONSTER_DB.md`
- 행동 규칙은 `Wiki/01_Mechanics/MECH_Monster_AI.md`가 소유한다.

## 6. Named Antagonists

고유 이름, 반복 출현, 관계와 개인 서사를 가진 인간형 적대자를 관리한다.

목표 경로: `Wiki/03_Entities/Named_Antagonists/`

## 7. Internal Threats

아지트 내부의 배신, 범죄, 파벌 갈등과 위험 인물을 관리한다. 고정 인물 DB라기보다 이벤트 및 상태 분류로 사용될 수 있다.

목표 경로: `Wiki/03_Entities/Internal_Threats/`

## 8. ConfigureBook 원고

`ConfigureBook/`의 생존자, 지역과 이벤트 파일은 Wiki 등록 전 콘텐츠 원고다. 이 인덱스에 등재되기 전까지 정본으로 취급하지 않는다.
