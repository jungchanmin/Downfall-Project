# 🌑 Downfall Project State (v1.2)

## 🎯 Current Phase
**Phase 1: 인프라 구축 및 위키(Wiki) 데이터베이스 세팅 (완료율 95%)**
세계관, 시간 시스템, 자원 경제 로직, 생존자 데이터 규격 및 이벤트 태그 아키텍처 수립 완료. 현재 '개입형 이벤트(Track B)' 설계만을 남겨둔 최종 인프라 마감 단계입니다.

## ✅ Completed Tasks (최근 완료된 작업)
- **세계관/지리**: `Oebeng_Village_Lore.md` 작성 완료 (15개 구역 배경 및 위험도 확정).
- **자원 경제**: `Resource_Logic.md` 확정 (식량/부품/금화/명성 및 유물 장비 로직).
- **데이터 표준**: `Survivor_Template.md` 고도화 및 `Gavin_Jackson.md` 위키 등록 완료.
- **이벤트 아키텍처**: `EVT_Notification.md` (통보형) 설계 완료.
  - **태그 규칙**: `#Stat_`, `#Trait_`, `#Env_`, `#Flag_` 표준 명명 규칙 수립.
  - **작문 가이드**: `Downfall Voice` (하드보일드, 감각적 묘사) 지침 확립.

## 🚀 Current Objective (현재 진행 중인 목표)
- **개입형 이벤트 설계**: TRPG식 선택지와 주사위 판정이 포함된 `EVT_TRPG_Interactive.md` (Track B) 템플릿 완성.
- **상태 관리**: `#Trait_` 태그에 들어갈 부상, 기벽, 광기 등의 상세 리스트(`Mental_Ailments.md`) 기획.
- **초기 이벤트 풀(Pool) 양산**: 가빈 잭슨 및 공통 환경에서 발생할 초기 통보형 이벤트 5~10종 생성.

## 📝 Next Steps (다음 할 일)
1. **Phase 2 (구현) 진입**: Unity `TimeManager.cs` 및 `StatSystem.cs` 코어 로직 코딩 착수.
2. **이벤트 파서 설계**: 위키의 태그를 읽어 C# 딕셔너리로 변환하는 `EventParser.cs` 설계.
3. **UI/UX**: 5단계 페이즈 연출 및 텍스트 로그 출력 프로토타이핑.

## ⚠️ Important Notes (AI 필수 인지 사항)
- **Tag-Driven Logic**: 모든 이벤트 발동 조건은 위키의 태그 표준 규칙을 엄격히 준수할 것.
- **Downfall Voice**: 모든 내러티브 출력은 하드보일드 문체와 '보여주기(Show)' 원칙을 유지할 것.
- **캐릭터 일관성**: NPC 이벤트 생성 시 반드시 해당 인물의 '6모자 기법' 데이터를 동적으로 주입할 것.