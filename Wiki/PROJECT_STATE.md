# 🌑 Downfall Project State

## 🎯 Current Phase
**Phase 1: 인프라 구축 및 위키(Wiki) 데이터베이스 세팅 (완료율 85%)**
게임의 철학, 시간 규칙, 데이터 양식 설정을 완료하고, 구체적인 수치 밸런싱과 지리 정보를 구축하는 최종 단계입니다.

## ✅ Completed Tasks (최근 완료된 작업)
- **인프라**: GitHub 저장소 초기화, `.cursorrules` AI 가이드라인 적용 완료.
- **구조**: `Downfall Wiki` 전체 디렉토리 트리 구축 완료.
- **데이터 양식**: `00_Templates/Survivor_Template.md` (6모자 기법 및 턴제 스탯 포함) 작성 완료.
- **핵심 규칙**: `01_Mechanics/Time_System.md` (5단계 하루 사이클 및 식량 페널티) 정의 완료.
- **세계관**: `02_World/World_Concept.md` (3대 지주, 의식의 감옥, 29일의 시련) 확립 완료.

## 🚀 Current Objective (현재 진행 중인 목표)
- **지리 정보 구체화**: 오뱅마을의 주요 병목지점 및 장소 정보(`02_World/Oebeng_Village/`) 문서화.
- **수치 밸런싱**: 자원 소모량, 상태이상 전이 확률 등 `01_Mechanics/Resource_Logic.md` 설계.
- **초기 데이터 생성**: 확정된 템플릿을 바탕으로 '가빈 잭슨' 등 주요 생존자 위키 등록.

## 📝 Next Steps (다음 할 일)
1. **Phase 2 진입**: 위키의 시간 규칙을 바탕으로 Unity 엔진 내 `TimeManager.cs` 코어 로직 구현.
2. **이벤트 엔진 설계**: 페즈별 돌발 이벤트 트리거 시스템(`05_Events`) 구조 설계.
3. **UI 프로토타이핑**: 텍스트 로그 및 5단계 페이즈 표시를 위한 HUD 기본 기획.

## ⚠️ Important Notes (AI 필수 인지 사항)
- **턴제 시스템 고수**: 모든 로직은 5단계 페이즈(새벽-아침-점심-저녁-밤)를 기준으로 작동함.
- **Single Source of Truth**: 모든 수치와 설정의 근거는 반드시 `/Wiki` 폴더 내 마크다운 문서를 최우선으로 참조함.
- **분위기 유지**: 모든 텍스트와 이벤트 생성 시 '이해 불가능한 공포'와 '내부의 갈등' 테마를 유지할 것.