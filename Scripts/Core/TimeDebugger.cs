using UnityEngine;

namespace Downfall.Core
{
    /// <summary>
    /// DayCycleManager 상태를 콘솔에 출력하고, 인스펙터/컨텍스트 메뉴로 수동 진행·점프를 테스트한다.
    /// </summary>
    public class TimeDebugger : MonoBehaviour
    {
        [SerializeField] [Min(1)] private int _testJumpDay = 1;

        private void OnEnable()
        {
            if (DayCycleManager.Instance == null) return;

            DayCycleManager.Instance.OnPhaseChanged += LogState;
            DayCycleManager.Instance.OnDayChanged += OnDayChangedLog;
        }

        private void OnDisable()
        {
            if (DayCycleManager.Instance == null) return;

            DayCycleManager.Instance.OnPhaseChanged -= LogState;
            DayCycleManager.Instance.OnDayChanged -= OnDayChangedLog;
        }

        private void OnDayChangedLog(int _)
        {
            LogState(DayCycleManager.Instance.CurrentPhase);
        }

        private void LogState(DayCycleManager.DayPhase phase)
        {
            var manager = DayCycleManager.Instance;
            if (manager == null) return;

            int day = manager.CurrentDay;
            float prob = manager.GetDoomsdayProbability(day);
            int percent = Mathf.RoundToInt(prob * 100f);
            Debug.Log($"[DEBUG] Day {day} - {phase} | Doomsday Prob: {percent}%");
        }

        [ContextMenu("Test: Advance Phase")]
        private void Test_AdvancePhase()
        {
            if (DayCycleManager.Instance == null)
            {
                Debug.LogWarning("[TimeDebugger] DayCycleManager.Instance가 없습니다.");
                return;
            }

            DayCycleManager.Instance.AdvancePhase();
        }

        [ContextMenu("Test: Jump To Day")]
        private void Test_JumpToDay()
        {
            Test_JumpToDay(_testJumpDay);
        }

        /// <summary>지정 일차의 새벽으로 강제 점프. 인스펙터의 _testJumpDay 또는 인자 사용.</summary>
        public void Test_JumpToDay(int day)
        {
            if (DayCycleManager.Instance == null)
            {
                Debug.LogWarning("[TimeDebugger] DayCycleManager.Instance가 없습니다.");
                return;
            }

#if UNITY_EDITOR
            DayCycleManager.Instance.SetStateForTest(day, DayCycleManager.DayPhase.Dawn);
#else
            Debug.LogWarning("[TimeDebugger] SetStateForTest는 에디터 전용입니다.");
#endif
        }
    }
}
