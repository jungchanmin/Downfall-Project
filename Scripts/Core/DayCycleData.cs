using UnityEngine;

namespace Downfall.Core
{
    /// <summary>
    /// 29일 의식의 시간·멸망 확률 데이터. 데이터와 로직 분리를 위한 ScriptableObject.
    /// </summary>
    [CreateAssetMenu(fileName = "DayCycleData", menuName = "Downfall/Core/Day Cycle Data", order = 0)]
    public class DayCycleData : ScriptableObject
    {
        [Header("의식 기간")]
        [SerializeField] [Min(1)] private int _totalDays = 29;
        [SerializeField] [Min(0.1f)] private float _phaseDurationSeconds = 60f;

        [Header("멸망의 날 (Pillar 2)")]
        [SerializeField] [Range(0f, 1f)] private float _doomsdayProbabilityMin = 0.05f;
        [SerializeField] [Range(0f, 1f)] private float _doomsdayProbabilityMax = 0.95f;

        public int TotalDays => _totalDays;
        public float PhaseDurationSeconds => _phaseDurationSeconds;
        public float DoomsdayProbabilityMin => _doomsdayProbabilityMin;
        public float DoomsdayProbabilityMax => _doomsdayProbabilityMax;
    }
}
