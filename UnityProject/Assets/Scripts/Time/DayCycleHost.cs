using UnityEngine;

namespace Downfall.Time
{
    [DefaultExecutionOrder(-100)]
    public sealed class DayCycleHost : MonoBehaviour
    {
        public DayCycle Cycle { get; private set; }
        public bool IsTransitioning { get; private set; }

        private void Awake() { Cycle = new DayCycle(); }

        public void CompletePhase()
        {
            if (IsTransitioning || Cycle == null || Cycle.IsCampaignTimeEnded) return;
            IsTransitioning = true;
            try
            {
                Cycle.CompletePhase();
                foreach (var failure in Cycle.LastNotificationFailures)
                    Debug.LogException(new System.Exception("DayCycle " + failure.EventName + " subscriber failed", failure.Exception), this);
            }
            finally { IsTransitioning = false; }
        }
    }
}
