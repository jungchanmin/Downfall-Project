# ConfigureBook Import Tracker

## 1. 목적

이 문서는 `ConfigureBook/` 원고가 Wiki 정본 또는 런타임 데이터로 등록되었는지 추적한다.

## 2. 상태 코드

| 상태 | 의미 |
|---|---|
| Draft | 원고만 존재 |
| Reviewing | 등록 검토 중 |
| Partially Imported | 핵심 구조는 Wiki에 반영됐지만 세부 원고 전체 검수는 남아 있음 |
| Imported Candidates Added | 세부 공간·상호작용·이상현상 후보가 Wiki에 반영됐으나 자원/괴물/수치 검증이 남아 있음 |
| Imported | Wiki 또는 런타임 데이터에 등록됨 |
| Superseded | 더 최신 정본으로 대체됨 |
| Archived | 보존 처리됨 |

## 3. Place 원고

| ConfigureBook 원고 | 대응 Wiki 문서 | 상태 | 메모 |
|---|---|---|---|
| `ConfigureBook/Place/Azit.md` | `Wiki/02_World/Locations/Hideout.md` | Imported Candidates Added | 세부 공간·상호작용·이상현상 후보 반영 |
| `ConfigureBook/Place/Cathedral.md` | `Wiki/02_World/Locations/Cathedral.md` | Imported Candidates Added | 지상·지하 금기 구역 후보 반영 |
| `ConfigureBook/Place/Park.md` | `Wiki/02_World/Locations/Foggy_Park.md` | Imported Candidates Added | 방랑자 캠프·안개·호수·온실 시드 반영 |
| `ConfigureBook/Place/Abandoned_Houses.md` | `Wiki/02_World/Locations/Abandoned_Cabins.md` | Imported Candidates Added | 납치·함정·폐가 내부 시드 반영 |
| `ConfigureBook/Place/Town_Hall.md` | `Wiki/02_World/Locations/Town_Hall.md` | Imported Candidates Added | 자경단 통제·지휘·처벌 구역 후보 반영 |
| `ConfigureBook/Place/Market_District.md` | `Wiki/02_World/Locations/Shopping_District.md` | Imported Candidates Added | 대로·보급 거점·특수 구역 후보 반영 |
| `ConfigureBook/Place/SteelFort.md` | `Wiki/02_World/Locations/Hardware_Store.md` | Imported Candidates Added | 검문소·하역장·공구·화학·창고 후보 반영 |
| `ConfigureBook/Place/PoliceOffice.md` | `Wiki/02_World/Locations/Police_Station.md` | Imported Candidates Added | 로비·보관실·격리·교육 구역 후보 반영 |
| `ConfigureBook/Place/DownTown.md` | `Wiki/02_World/Locations/Residential_Area.md` | Imported Candidates Added | A·B·C동 구조와 광신도 감시·괴물 둥지 후보 반영 |
| `ConfigureBook/Place/NightLife_District.md` | `Wiki/02_World/Locations/Nightlife_District.md` | Imported Candidates Added | 공통 위협 반영. R18 세부는 모듈 분리 |
| `ConfigureBook/Place/Wharf.md` | `Wiki/02_World/Locations/Dockyard.md` | Imported Candidates Added | 컨테이너·해안선·폐선박·크레인 후보 반영 |
| `ConfigureBook/Place/Hospital.md` | `Wiki/02_World/Locations/Hospital.md` | Imported Candidates Added | 층별 병원 구조와 실험·영안실 후보 반영 |
| `ConfigureBook/Place/Factory.md` | `Wiki/02_World/Locations/Factory.md` | Imported Candidates Added | 방어선·생산·배양·금고·지휘부 후보 반영 |
| `ConfigureBook/Place/Department_Store.md` | `Wiki/02_World/Locations/Department_Store.md` | Imported Candidates Added | 층별 미궁과 광신도 시험 후보 반영. 중심부 표현 폐기 |
| `ConfigureBook/Place/LAB.md` | `Wiki/02_World/Locations/Research_Lab.md` | Imported Candidates Added | 연구 구역 후보 반영. 플레이어 괴물화·미확정 진엔딩은 보류 |

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

1. Place 원고 15개 Archive 이동 승인 여부 판단
2. Resource System 또는 Item DB 기준 자원 후보 정리
3. Monster DB 및 Entity 문서 기준 등장 후보 정리
4. 연구소 충돌 설정의 별도 승인 여부 판단
5. Survivor 원고와 Wiki 생존자 문서 대응
6. Event 원고의 ID·파일명 정규화
