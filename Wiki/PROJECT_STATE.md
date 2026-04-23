# Downfall Project State

## 🎯 Current Phase
**Phase 1: 인프라 구축 및 위키(Wiki) 데이터베이스 세팅**
현재 게임의 설정과 턴제 시스템의 수치적 기준을 확립하기 위한 `/Wiki` 디렉토리 초기화 단계를 진행 중입니다.

## ✅ Completed Tasks (최근 완료된 작업)
- GitHub 저장소 및 초기 파일 시스템 구축 완료.
- 전역 AI 가이드라인(`.cursorrules`) 작성 및 적용 완료.
- `Downfall Wiki` 디렉토리 구조 확립 (`00_Templates` ~ `05_Events`).

## 🚀 Current Objective (현재 진행 중인 목표)
- AI 데이터 생성 자동화를 위한 **표준 템플릿(`00_Templates`)** 초안 작성.
- 턴제 게임의 핵심인 **시간 소모 규칙(`01_Mechanics/Time_System.md`)** 문서화.

## 📝 Next Steps (다음 할 일)
1. `Survivor_Template.md`, `Event_Template.md` 등 기획 템플릿 완성.
2. `Time_System.md`에 행동력(AP) 및 시간 변환 수치 기준 명시.
3. 위키 작성이 완료되면, 이를 바탕으로 Unity 엔진에서 `TimeManager` C# 클래스 구현 착수.

## ⚠️ Important Notes (AI 필수 인지 사항)
- **턴제 시스템 준수:** Downfall은 실시간(Real-time)이 아닌, 플레이어의 행동(Action)에 따라 시간이 흐르는 **턴제(Turn-based) TRPG**로 방향이 확정되었습니다. 모든 기획과 코드는 이 원칙을 따릅니다.