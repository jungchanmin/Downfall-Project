# ConfigureBook Import Tracker

## 1. 목적

이 문서는 `ConfigureBook/` 원고가 Wiki 정본 또는 런타임 데이터로 등록되었는지 추적한다.

## 2. 상태 코드

| 상태 | 의미 |
|---|---|
| Draft | 원고만 존재 |
| Reviewing | 등록 검토 중 |
| Imported | Wiki 또는 런타임 데이터에 등록됨 |
| Superseded | 더 최신 정본으로 대체됨 |
| Archived | 보존 처리됨 |

## 3. Place 원고

| ConfigureBook 원고 | 대응 Wiki 문서 | 상태 | 메모 |
|---|---|---|---|
| `ConfigureBook/Place/Azit.md` | `Wiki/02_World/Obeng_Village_Lore.md` | Reviewing | 아지트는 고정 장소. 세부 공간과 이상현상 시드 반영 필요 |
| `ConfigureBook/Place/Cathedral.md` | `Wiki/02_World/Obeng_Village_Lore.md` | Reviewing | 성당은 중심부 근처 안전 구역 |
| `ConfigureBook/Place/Park.md` | `Wiki/02_World/Obeng_Village_Lore.md` | Reviewing | 공원은 중심부 근처, 방랑자 접촉 가능 |
| `ConfigureBook/Place/Abandoned_Houses.md` | `Wiki/02_World/Obeng_Village_Lore.md` | Reviewing | 폐가는 중심부 근처이나 납치 위험 존재 |
| `ConfigureBook/Place/Town_Hall.md` | `Wiki/02_World/Obeng_Village_Lore.md` | Reviewing | 자경단 본부 |
| `ConfigureBook/Place/Market_District.md` | `Wiki/02_World/Obeng_Village_Lore.md` | Reviewing | 상점가 대응 후보 |
| `ConfigureBook/Place/SteelFort.md` | `Wiki/02_World/Obeng_Village_Lore.md` | Reviewing | 철물점 또는 방어 거점 대응 확인 필요 |
| `ConfigureBook/Place/PoliceOffice.md` | `Wiki/02_World/Obeng_Village_Lore.md` | Reviewing | 경찰서 대응 |
| `ConfigureBook/Place/DownTown.md` | `Wiki/02_World/Obeng_Village_Lore.md` | Reviewing | 주거단지 또는 중심가 대응 확인 필요 |
| `ConfigureBook/Place/NightLife_District.md` | `Wiki/02_World/Obeng_Village_Lore.md` | Reviewing | 유흥가 대응 |
| `ConfigureBook/Place/Wharf.md` | `Wiki/02_World/Obeng_Village_Lore.md` | Reviewing | 선착장 대응 |
| `ConfigureBook/Place/Hospital.md` | `Wiki/02_World/Obeng_Village_Lore.md` | Reviewing | 병원 대응 |
| `ConfigureBook/Place/Factory.md` | `Wiki/02_World/Obeng_Village_Lore.md` | Reviewing | 공장 대응 |
| `ConfigureBook/Place/Department_Store.md` | `Wiki/02_World/Obeng_Village_Lore.md` | Reviewing | 백화점 대응 |
| `ConfigureBook/Place/LAB.md` | `Wiki/02_World/Obeng_Village_Lore.md` | Reviewing | 연구소 대응 |

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

1. Place 원고와 `Obeng_Village_Lore.md` 세부 공간 대응
2. Survivor 원고와 Wiki 생존자 문서 대응
3. Event 원고의 ID·파일명 정규화
4. Imported 원고 Archive 이동 승인
