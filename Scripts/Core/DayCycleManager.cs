using System;
using UnityEngine;

namespace Downfall.Core
{
    /// <summary>
    /// 하루 5단계(새벽→오전→오후→저녁→밤)와 29일 흐름을 관리한다.
    /// 밤이 끝나면 다음 날로 넘어가며, Pillar 2에 따라 멸망의 날 확률이 선형 증가한다.
    /// </summary>
    public class DayCycleManager : MonoBehaviour
    {
        public enum DayPhase
        {
            Dawn,    // 새벽
            Morning, // 오전
            Afternoon,
            Evening,
            Night
        }

        private static DayCycleManager _instance;

        [SerializeField] private DayCycleData _data;

        private int _currentDay = 1;
        private DayPhase _currentPhase = DayPhase.Dawn;

        /// <summary>전역 접근용 싱글톤. 씬에 한 개의 DayCycleManager가 있어야 한다.</summary>
        public static DayCycleManager Instance => _instance;

        /// <summary>현재 일차 (1 ~ TotalDays)</summary>
        public int CurrentDay => _currentDay;

        /// <summary>현재 하루 단계</summary>
        public DayPhase CurrentPhase => _currentPhase;

        /// <summary>시간이 바뀔 때마다 발행. (이전 단계 → 새 단계)</summary>
        public event Action<DayPhase> OnPhaseChanged;

        /// <summary>단계 전환 후, 해당 단계에서 발생할 수 있는 잠재적 이벤트를 체크할 때 사용.</summary>
        public event Action<DayPhase> OnPhaseUpdate;

        /// <summary>밤이 지나 다음 날로 넘어갈 때 발행. (새 일차)</summary>
        public event Action<int> OnDayChanged;

        /// <summary>현재 일차 기준 멸망의 날 발생 확률 (0~1). Pillar 2 선형 증가.</summary>
        public float DoomsdayProbability => GetDoomsdayProbability(_currentDay);

        private void Awake()
        {
            if (_instance != null && _instance != this)
            {
                Destroy(gameObject);
                return;
            }

            _instance = this;
        }

        private void OnDestroy()
        {
            if (_instance == this)
                _instance = null;
        }

        private void Start()
        {
            if (_data == null)
            {
                Debug.LogError("[DayCycleManager] DayCycleData가 할당되지 않았습니다. 의식이 진행되지 않습니다.");
                return;
            }

            OnPhaseChanged?.Invoke(_currentPhase);
            OnPhaseUpdate?.Invoke(_currentPhase);
        }

        /// <summary>
        /// 외부에서 호출 시 DayPhase를 한 단계 진행한다.
        /// Night에서 호출하면 AdvanceDay() 후 Dawn으로 돌아간다.
        /// </summary>
        public void AdvancePhase()
        {
            if (_data == null) return;

            if (_currentPhase == DayPhase.Night)
            {
                AdvanceDay();
                _currentPhase = DayPhase.Dawn;
            }
            else
            {
                _currentPhase = (DayPhase)((int)_currentPhase + 1);
            }

            OnPhaseChanged?.Invoke(_currentPhase);
            OnPhaseUpdate?.Invoke(_currentPhase);
        }

        private void AdvanceDay()
        {
            if (_currentDay >= _data.TotalDays)
            {
                // 29일 종료 시 동작은 게임 종료 등 상위 시스템에 맡김
                return;
            }

            _currentDay++;
            OnDayChanged?.Invoke(_currentDay);
        }

        /// <summary>
        /// 지정 일차에서의 멸망의 날 확률. 1일은 최소값, 29일은 최대값으로 선형 보간.
        /// </summary>
        public float GetDoomsdayProbability(int day)
        {
            if (_data == null) return 0f;

            int total = _data.TotalDays;
            if (total <= 1) return _data.DoomsdayProbabilityMin;

            float t = Mathf.Clamp01((float)(day - 1) / (total - 1));
            return Mathf.Lerp(_data.DoomsdayProbabilityMin, _data.DoomsdayProbabilityMax, t);
        }

#if UNITY_EDITOR
        /// <summary>에디터/테스트용: 현재 단계와 일차를 강제 설정. 이벤트를 발행한다.</summary>
        public void SetStateForTest(int day, DayPhase phase)
        {
            _currentDay = Mathf.Clamp(day, 1, _data != null ? _data.TotalDays : 29);
            _currentPhase = phase;
            OnPhaseChanged?.Invoke(_currentPhase);
            OnDayChanged?.Invoke(_currentDay);
        }
#endif
    }
}
