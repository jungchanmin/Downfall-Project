---
id: LORE_LOC_Index
title: 오벵마을 장소 상세 인덱스
type: lore_world
status: wip
summary: 오벵마을 15개 고정 지역의 상세 문서 진입점을 제공한다.
tags: [lore, world, location, obeng, index]
keywords: [오벵마을, 장소, 지역, 인덱스, 고정 지리]
depends_on: [LORE_LOC_Obeng]
emits: []
last_updated: 2026-07-09
---

# 오벵마을 장소 상세 인덱스

## 1. 목적

이 문서는 오벵마을 15개 고정 지역의 세부 문서 목록을 관리한다.

`Obeng_Village_Lore.md`는 도시 전체의 상위 구조와 위험도 분류를 소유하고, 이 폴더의 개별 문서는 장소별 세부 공간, 이상현상 시드, 주요 활동, 이벤트 제작 참고 정보를 소유한다.

## 2. 중심부 및 중심부 근처

| 지역 | 상세 문서 | ConfigureBook 원고 |
|---|---|---|
| 아지트 | `Hideout.md` | `ConfigureBook/Place/Azit.md` |
| 성당 | `Cathedral.md` | `ConfigureBook/Place/Cathedral.md` |
| 공원 | `Foggy_Park.md` | `ConfigureBook/Place/Park.md` |
| 버려진 폐가 | `Abandoned_Cabins.md` | `ConfigureBook/Place/Abandoned_Houses.md` |

## 3. 중간 지대

| 지역 | 상세 문서 | ConfigureBook 원고 |
|---|---|---|
| 마을회관 | `Town_Hall.md` | `ConfigureBook/Place/Town_Hall.md` |
| 상점가 | `Shopping_District.md` | `ConfigureBook/Place/Market_District.md` |
| 철물점 | `Hardware_Store.md` | `ConfigureBook/Place/SteelFort.md` |
| 경찰서 | `Police_Station.md` | `ConfigureBook/Place/PoliceOffice.md` |

## 4. 외곽 및 외곽 심부

| 지역 | 상세 문서 | ConfigureBook 원고 |
|---|---|---|
| 주거단지 | `Residential_Area.md` | `ConfigureBook/Place/DownTown.md` |
| 유흥가 | `Nightlife_District.md` | `ConfigureBook/Place/NightLife_District.md` |
| 선착장 | `Dockyard.md` | `ConfigureBook/Place/Wharf.md` |
| 병원 | `Hospital.md` | `ConfigureBook/Place/Hospital.md` |
| 공장 | `Factory.md` | `ConfigureBook/Place/Factory.md` |
| 백화점 | `Department_Store.md` | `ConfigureBook/Place/Department_Store.md` |
| 연구소 | `Research_Lab.md` | `ConfigureBook/Place/LAB.md` |

## 5. Import 상태

현재 장소별 상세 문서는 ConfigureBook 원고의 전체 문장을 완전 흡수한 상태가 아니다. 우선 상위 정본과 충돌하지 않는 구조, 위험도, 세부 구역, 이벤트 제작 방향을 분리했다.

다음 단계에서 원고별 세부 공간, 이상현상 시드, 풍경 묘사와 상호작용 후보를 검수해 `Imported` 여부를 판단한다.
