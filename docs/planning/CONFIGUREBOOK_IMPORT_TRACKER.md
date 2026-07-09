# ConfigureBook Import Tracker

## 1. 목적

이 문서는 `ConfigureBook/` 원고가 Wiki 정본 또는 런타임 데이터로 등록되었는지 추적한다.

## 2. 상태 코드

| 상태 | 의미 |
|---|---|
| Draft | 원고만 존재 |
| Reviewing | 등록 검토 중 |
| Partially Imported | 핵심 구조는 Wiki에 반영됐지만 세부 원고 전체 검수는 남아 있음 |
| Imported | Wiki 또는 런타임 데이터에 등록됨 |
| Superseded | 더 최신 정본으로 대체됨 |
| Archived | 보존 처리됨 |

## 3. Place 원고

| ConfigureBook 원고 | 대응 Wiki 문서 | 상태 | 메모 |
|---|---|---|---|
| `ConfigureBook/Place/Azit.md` | `Wiki/02_World/Locations/Hideout.md` | Partially Imported | 고정 장소·세부 구역 반영. 세부 이상현상 시드 검수 필요 |
| `ConfigureBook/Place/Cathedral.md` | `Wiki/02_World/Locations/Cathedral.md` | Partially Imported | 중심부 근처 안전 구역 반영. 지하/공동묘지 시드 검수 필요 |
| `ConfigureBook/Place/Park.md` | `Wiki/02_World/Locations/Foggy_Park.md` | Partially Imported | 방랑자·암상인 역할 반영. 호수/안개 시드 검수 필요 |
| `ConfigureBook/Place/Abandoned_Houses.md` | `Wiki/02_World/Locations/Abandoned_Cabins.md` | Partially Imported | 폐가·납치 위험 반영. 세부 구조 검수 필요 |
| `ConfigureBook/Place/Town_Hall.md` | `Wiki/02_World/Locations/Town_Hall.md` | Partially Imported | 자경단 본부 반영. 행정 공간 세부 검수 필요 |
| `ConfigureBook/Place/Market_District.md` | `Wiki/02_World/Locations/Shopping_District.md` | Partially Imported | 디렉터 결정에 따라 상점가로 확정 |
| `ConfigureBook/Place/SteelFort.md` | `Wiki/02_World/Locations/Hardware_Store.md` | Partially Imported | 디렉터 결정에 따라 철물점으로 확정 |
| `ConfigureBook/Place/PoliceOffice.md` | `Wiki/02_World/Locations/Police_Station.md` | Partially Imported | 경찰서 대응 |
| `ConfigureBook/Place/DownTown.md` | `Wiki/02_World/Locations/Residential_Area.md` | Partially Imported | 디렉터 결정에 따라 주거단지로 확정 |
| `ConfigureBook/Place/NightLife_District.md` | `Wiki/02_World/Locations/Nightlife_District.md` | Partially Imported | 유흥가 대응. R18 확장과 분리 필요 |
| `ConfigureBook/Place/Wharf.md` | `Wiki/02_World/Locations/Dockyard.md` | Partially Imported | 선착장 대응 |
| `ConfigureBook/Place/Hospital.md` | `Wiki/02_World/Locations/Hospital.md` | Partially Imported | 병원 대응 |
| `ConfigureBook/Place/Factory.md` | `Wiki/02_World/Locations/Factory.md` | Partially Imported | 공장 대응 |
| `ConfigureBook/Place/Department_Store.md` | `Wiki/02_World/Locations/Department_Store.md` | Partially Imported | 백화점 대응 |
| `ConfigureBook/Place/LAB.md` | `Wiki/02_World/Locations/Research_Lab.md` | Partially Imported | 연구소 대응 |

## 4. Survivor 원고

| ConfigureBook 원고 | 대응 Wiki 문서 | 상태 | 메모 |
|---|---|---|---|
| `ConfigureBook/Survivors/Gavin_Jackson` | `Wiki/03_Entities/Survivors/Guide_Gavin_Jackson.md` | Reviewing | 세부 비교 필요 |
| `ConfigureBook/Survivors/Rachel_Lopez` | `Wiki/03_Entities/Survivors/Guide_Rachel_Lopez.md` | Reviewing | 세부 비교 필요 |
| 기타 Survivor 원고 | 없음 | Draft | 향후 Wiki 등록 순서 결정 필요 |

## 5. Event 원고

| 원고 범위 | 대응 Wiki 문서 | 상태 | 메모 |
|---|---|---|---|
| `ConfigureBook/Events/N18/**` | 일부 `Wiki/05_Events/**` | Draft | ID·파일명 정규화 필요 |
| `ConfigureBook/Events/R18/**` | 일부 R18 모듈 후보 | Draft | R18 모듈 이동 계획 후 처리 |

## 6. 다음 검토 순서

1. Place 원고의 세부 공간·이상현상 시드 전체 Import 여부 판단
2. Imported 판정된 원고의 Archive 이동 승인
3. Survivor 원고와 Wiki 생존자 문서 대응
4. Event 원고의 ID·파일명 정규화
