---
id: LORE_LOC_Police_Station
title: 경찰서 상세 설정
type: lore_world
status: wip
summary: 악마 조직이 점거한 옛 치안 중심지이자 무기 확보 위험 지역인 경찰서를 정의한다.
tags: [lore, world, location, obeng, police_station]
keywords: [경찰서, Police Station, PoliceOffice, 악마 조직, 무기창고]
depends_on: [LORE_LOC_Obeng, ENTITY_Index]
emits: []
last_updated: 2026-07-09
---

# 경찰서 상세 설정

## 1. 기본 정보

- **공식 명칭**: 경찰서
- **영문명**: Police Station
- **위험도**: 위험
- **중심성**: 중간 지대에서 외곽 사이
- **세력 영향**: 악마 조직
- **ConfigureBook 원고**: `ConfigureBook/Place/PoliceOffice.md`
- **Import 상태**: Reviewing

## 2. 역할

경찰서는 과거 치안 중심지였으나 현재는 악마 조직이 점거한 무기 확보 지역이다. 화력 보상은 크지만 감금, 고문, 추격과 괴생명체 난입 위험이 공존한다.

## 3. 세부 구역

- 경찰서 본부
- 구치소
- 무기창고
- 검열소
- 주차장

## 4. 이벤트 제작 방향

- 무기창고 침투
- 악마 조직과의 협상 또는 교전
- 구치소의 포로 구출
- 검열소 통과와 위장
- 주차장의 탈출 실패와 괴물 난입

## 5. 원고 반영 메모

`PoliceOffice` 원고는 경찰서 대응 원고로 유지한다. 세부 공간별 위험도는 후속 Import 패스에서 보강한다.
