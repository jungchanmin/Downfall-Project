---
id: SYS_Document_Rules
title: Downfall 문서 소유권 및 폴더 규칙
type: system
status: draft
summary: Wiki와 docs의 역할, 정본·DB·세부 규칙·R18 모듈의 의존 방향과 단계적 이전 원칙을 정의한다.
tags: [system, documentation, ownership, folder, module]
keywords: [Wiki, docs, 정본, DB, 폴더, R18, Archive, depends_on]
depends_on: [SYS_Project_Canon, SYS_Wiki_Operations]
emits: []
last_updated: 2026-07-06
---

# Downfall 문서 소유권 및 폴더 규칙

## 1. 기본 원칙
- Wiki에는 게임이 직접 참조하는 세계관, 시스템, DB, 이벤트와 시나리오 정본을 둔다.
- `docs/`에는 개발 절차, 로드맵, 프로젝트 상태, 도구 사용법과 저장소 운영 문서를 둔다.
- 같은 규칙을 여러 문서에 복제하지 않는다.
- 상위 문서는 개요와 불변 규칙, 하위 문서 탐색 경로를 소유한다.
- 상세 계산, 예외, 알고리즘과 개별 데이터는 세부 문서 또는 DB 한 곳에서만 소유한다.

## 2. 목표 구조
```text
Wiki/
├─ 00_System/
├─ 01_Mechanics/
├─ 02_World/
├─ 03_Entities/
├─ 04_Items/
├─ 05_Events/
├─ 06_Narrative/
├─ 90_Modules/R18/
└─ 99_Archive/

docs/
├─ governance/
├─ planning/
├─ development/
└─ ai/
```
기존 파일은 검토 없이 일괄 이동하지 않는다.

## 3. 문서 소유권
- 프로젝트 정본: 프로젝트 정의, 디자인 필러, 절대 세계 규칙과 문서 우선순위
- 상위 시스템 문서: 목적, 핵심 흐름, 불변 규칙, 통합 계약과 세부 문서 참조표
- 세부 시스템 문서: 복잡한 내부 규칙, 계산, 상태 전이, 예외, 알고리즘과 테스트 사례
- DB: 개별 기술, 상태이상, 괴물, 아이템, 기벽과 밸런스 값
- 이벤트: 장면, 조건, 선택, 판정, 결과, 기억과 후속 연결

`MECH_Combat_System.md`는 원형을 유지하되 상세 계산과 DB를 참조하는 전투 허브로 발전시킨다.

## 4. Core와 R18
```text
Core 시스템 ← R18 모듈
Core 시스템 ✕ R18 전용 문서 직접 의존
```
Core에는 친밀도, 관계, 기억, 침식도, 욕구불만, 동의·거부 판단과 선택지 조건을 남긴다. R18 모듈은 성인 이벤트, 기술, 상태이상, 괴물 행동, 패배 결과와 묘사 규칙을 소유한다.

## 5. 이전 절차
1. 신규 정본 문서 작성
2. 기존 문서와 충돌 목록 작성
3. 목적지와 소유권 승인
4. 파일 이동 및 참조 갱신
5. Wiki Index와 Manifest 재생성
6. CI 검사
7. 기존 문서 deprecated 또는 Archive 처리

삭제, 대규모 이동, ID 변경과 기존 문서 덮어쓰기는 별도 승인 후 수행한다.
