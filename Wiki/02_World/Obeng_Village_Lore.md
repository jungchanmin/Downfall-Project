---
id: LORE_LOC_Obeng
title: 오벵마을 15구역 로어
type: lore_world
status: wip
summary: 오벵마을 15개 고정 구역의 위험도, 세력 영향, 환경과 상세 문서 진입점을 정의한다.
tags: [lore, world, location, obeng]
keywords: [오벵마을, Obeng Village, 성당, 상점가, 폐가, 아지트, 위험도, Locations]
depends_on: [LORE_WORLD_Overview, LORE_WORLD_Ritual_25_Days, LORE_LOC_Index]
emits: []
last_updated: 2026-07-09
---

# 오벵마을 15구역 로어

## 1. 정본 기준

오벵마을은 가상의 근현대 중소형 관광도시다. 공식 한국어 표기는 `오벵마을`, 공식 영문 표기는 `Obeng Village`로 통일한다.

오벵마을의 15개 주요 구역과 기본 위치는 매 회차 동일하다. 매 회차 변동되는 것은 세력 접촉 지점, 지역 이벤트, 괴물 출현, 자원 결과와 시나리오 풀이다.

아지트는 항상 고정된 장소이며 생존자 무리의 기본 거점이다.

## 2. 문서 소유권

이 문서는 오벵마을 전체의 상위 인덱스다.

- 도시 규모, 고정 지리, 위험도 단계, 중심성 분류는 이 문서가 소유한다.
- 장소별 세부 공간, 이상현상 시드, 이벤트 제작 참고 정보는 `Wiki/02_World/Locations/` 하위 문서가 소유한다.
- ConfigureBook 원고의 전체 문장 Import 여부는 `docs/planning/CONFIGUREBOOK_IMPORT_TRACKER.md`에서 추적한다.

상세 문서 인덱스: `Wiki/02_World/Locations/LOCATION_INDEX.md`

## 3. 위험도와 의식 구조

위험도가 낮을수록 의식의 중심부에 가깝다. 중심부의 안전은 자비가 아니라 어머니의 그릇 후보와 제물을 보존하기 위한 의식적 제어다.

외곽으로 갈수록 괴물, 이상현상, 적대 세력과 멸망의 괴물 위험이 증가한다. 대신 희귀 자원, 신화, 명성, 광신도의 시험과 핵심 단서를 획득할 가능성도 커진다.

## 4. 1단계: 안전 및 비교적 안전 구역

초기 생존의 거점이자 비교적 낮은 위험으로 탐색과 교류가 가능한 구역이다.

| 번호 | 지역 | 위험도 | 중심성 | 세력 영향 | 상세 문서 |
|---:|---|---|---|---|---|
| 1 | 아지트 | 안전 | 중심부 | 생존자 무리 | `Locations/Hideout.md` |
| 2 | 성당 | 안전 | 중심부 근처 | 중립 지대 | `Locations/Cathedral.md` |
| 3 | 공원 | 비교적 안전 | 중심부 근처 | 방랑자 | `Locations/Foggy_Park.md` |
| 4 | 버려진 폐가 | 비교적 안전 | 중심부 근처 | 방랑자, 비정규 적대 집단 | `Locations/Abandoned_Cabins.md` |

## 5. 2단계: 위험 구역

세력의 이권이 충돌하는 분쟁 지대이며 생존 필수 자원을 구하기 위해 반드시 거쳐야 하는 구역이다.

| 번호 | 지역 | 위험도 | 중심성 | 세력 영향 | 상세 문서 |
|---:|---|---|---|---|---|
| 5 | 마을회관 | 위험 | 중간 지대 | 자경단 | `Locations/Town_Hall.md` |
| 6 | 상점가 | 위험 | 중간 지대 | 자경단, 악마 조직 | `Locations/Shopping_District.md` |
| 7 | 철물점 | 위험 | 중간 지대 | 자경단 | `Locations/Hardware_Store.md` |
| 8 | 경찰서 | 위험 | 중간 지대에서 외곽 사이 | 악마 조직 | `Locations/Police_Station.md` |

## 6. 3단계: 매우 위험 및 접근금지 구역

외곽에 가까운 고위험 지역이다. 막대한 이득이 있으나 파멸 가능성이 높다.

| 번호 | 지역 | 위험도 | 중심성 | 세력 영향 | 상세 문서 |
|---:|---|---|---|---|---|
| 9 | 주거단지 | 매우 위험 | 외곽 | 광신도 | `Locations/Residential_Area.md` |
| 10 | 유흥가 | 매우 위험 | 외곽 | 악마 조직 | `Locations/Nightlife_District.md` |
| 11 | 선착장 | 매우 위험 | 외곽 봉쇄선 | 없음, 무법 지대 | `Locations/Dockyard.md` |
| 12 | 병원 | 매우 위험 | 외곽 | 자경단 | `Locations/Hospital.md` |
| 13 | 공장 | 접근금지 | 외곽 심부 | 악마 조직 | `Locations/Factory.md` |
| 14 | 백화점 | 접근금지 | 외곽 심부 | 광신도 | `Locations/Department_Store.md` |
| 15 | 연구소 | 접근금지 | 외곽 심부 | 광신도 | `Locations/Research_Lab.md` |

## 7. 원고 및 세부 문서 관계

`ConfigureBook/Place/` 문서는 Wiki 등록 전 장소 콘텐츠 원고다. Wiki에 반영된 뒤에는 Wiki가 정본이 되며, 원고는 `ConfigureBook/Archive/Imported/`로 이동하는 것을 기본 방침으로 한다.

세부 묘사, 소분류 공간, 이상현상 시드는 ConfigureBook 원고에서 가져오되, 위험도와 세계 규칙은 본 문서와 `WORLD_OVERVIEW.md`, `RITUAL_OF_25_DAYS.md`를 우선한다.
