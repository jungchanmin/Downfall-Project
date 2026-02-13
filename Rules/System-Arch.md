# Downfall: System Architecture

## 1. Core Pattern: Data-Driven
- 모든 게임 데이터(아이템, 캐릭터 스탯, 이벤트)는 `ScriptableObject`로 관리한다.
- 하드코딩된 수치는 '죄악'이다.

## 2. Event System
- 클래스 간의 직접적인 참조를 피하기 위해 `UnityEvent` 또는 `C# Action` 기반의 옵저버 패턴을 권장한다.
- 예: 시간이 흐르면 `OnTimeChanged` 이벤트를 발생시키고, UI는 이를 구독한다.

## 3. Singleton Policy
- `GameManager`, `TimeManager` 등 전역 관리가 필수적인 시스템에 한해서만 싱글톤을 허용한다.