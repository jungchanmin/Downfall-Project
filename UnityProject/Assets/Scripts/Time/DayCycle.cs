using System;

namespace Downfall.Time
{
    public sealed class DayCycle
    {
        public const int CampaignDays = 25;

        public int CurrentDay { get; private set; } = 1;
        public DayPhase CurrentPhase { get; private set; } = DayPhase.Dawn;
        public bool IsCampaignTimeEnded { get; private set; }

        public event Action<DayPhase> PhaseEnded;
        public event Action<DayPhase> PhaseStarted;
        public event Action<int> DayEnded;
        public event Action<int> DayStarted;
        public event Action CampaignTimeEnded;

        private bool transitioning;

        public bool CompletePhase()
        {
            if (transitioning || IsCampaignTimeEnded)
                return false;

            transitioning = true;
            try
            {
                PhaseEnded?.Invoke(CurrentPhase);

                if (CurrentPhase != DayPhase.Night)
                {
                    CurrentPhase++;
                    PhaseStarted?.Invoke(CurrentPhase);
                    return true;
                }

                DayEnded?.Invoke(CurrentDay);
                if (CurrentDay == CampaignDays)
                {
                    IsCampaignTimeEnded = true;
                    CampaignTimeEnded?.Invoke();
                    return true;
                }

                CurrentDay++;
                CurrentPhase = DayPhase.Dawn;
                DayStarted?.Invoke(CurrentDay);
                PhaseStarted?.Invoke(CurrentPhase);
                return true;
            }
            finally
            {
                transitioning = false;
            }
        }
    }
}
