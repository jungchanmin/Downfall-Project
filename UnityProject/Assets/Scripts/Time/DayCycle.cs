using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;

namespace Downfall.Time
{
    public sealed class DayCycle
    {
        public const int CampaignDays = 25;

        public int CurrentDay { get; private set; } = 1;
        public DayPhase CurrentPhase { get; private set; } = DayPhase.Dawn;
        public bool IsCampaignTimeEnded { get; private set; }
        public IReadOnlyList<NotificationFailure> LastNotificationFailures => notificationFailuresView;

        public event Action<DayPhase> PhaseEnded;
        public event Action<DayPhase> PhaseStarted;
        public event Action<int> DayEnded;
        public event Action<int> DayStarted;
        public event Action CampaignTimeEnded;

        private bool transitioning;
        private readonly List<NotificationFailure> notificationFailures = new List<NotificationFailure>();
        private readonly ReadOnlyCollection<NotificationFailure> notificationFailuresView;

        public DayCycle()
        {
            notificationFailuresView = notificationFailures.AsReadOnly();
        }

        public sealed class NotificationFailure
        {
            public string EventName { get; }
            public Exception Exception { get; }

            internal NotificationFailure(string eventName, Exception exception)
            {
                EventName = eventName;
                Exception = exception;
            }
        }

        public bool CompletePhase()
        {
            if (transitioning || IsCampaignTimeEnded)
                return false;

            transitioning = true;
            notificationFailures.Clear();
            try
            {
                Dispatch(PhaseEnded, CurrentPhase, nameof(PhaseEnded));

                if (CurrentPhase != DayPhase.Night)
                {
                    CurrentPhase++;
                    Dispatch(PhaseStarted, CurrentPhase, nameof(PhaseStarted));
                    return true;
                }

                Dispatch(DayEnded, CurrentDay, nameof(DayEnded));
                if (CurrentDay == CampaignDays)
                {
                    IsCampaignTimeEnded = true;
                    Dispatch(CampaignTimeEnded, nameof(CampaignTimeEnded));
                    return true;
                }

                CurrentDay++;
                CurrentPhase = DayPhase.Dawn;
                Dispatch(DayStarted, CurrentDay, nameof(DayStarted));
                Dispatch(PhaseStarted, CurrentPhase, nameof(PhaseStarted));
                return true;
            }
            finally
            {
                transitioning = false;
            }
        }

        private void Dispatch<T>(Action<T> handlers, T value, string eventName)
        {
            if (handlers == null) return;
            foreach (Action<T> handler in handlers.GetInvocationList())
            {
                try { handler(value); }
                catch (Exception exception) { notificationFailures.Add(new NotificationFailure(eventName, exception)); }
            }
        }

        private void Dispatch(Action handlers, string eventName)
        {
            if (handlers == null) return;
            foreach (Action handler in handlers.GetInvocationList())
            {
                try { handler(); }
                catch (Exception exception) { notificationFailures.Add(new NotificationFailure(eventName, exception)); }
            }
        }
    }
}
