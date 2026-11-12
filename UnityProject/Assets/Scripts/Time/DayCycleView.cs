using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

namespace Downfall.Time
{
    public sealed class DayCycleView : MonoBehaviour
    {
        [SerializeField] private DayCycleHost host;
        [SerializeField] private Text dayLabel;
        [SerializeField] private Text phaseLabel;
        [SerializeField] private Text[] phaseIndicators;
        [SerializeField] private Button completeButton;
        [SerializeField] private Text transitionLog;

        private readonly Queue<string> logLines = new Queue<string>();
        private DayCycle cycle;
        private const int MaxLogLines = 8;

        private void OnEnable()
        {
            if (host == null || host.Cycle == null)
            {
                Debug.LogError("DayCycleView requires an initialized DayCycleHost.", this);
                return;
            }
            cycle = host.Cycle;
            cycle.PhaseEnded += OnPhaseEnded;
            cycle.PhaseStarted += OnPhaseStarted;
            cycle.DayEnded += OnDayEnded;
            cycle.DayStarted += OnDayStarted;
            cycle.CampaignTimeEnded += OnCampaignTimeEnded;
            completeButton.onClick.AddListener(CompletePhase);
            Refresh();
        }

        private void OnDisable()
        {
            if (cycle == null) return;
            cycle.PhaseEnded -= OnPhaseEnded;
            cycle.PhaseStarted -= OnPhaseStarted;
            cycle.DayEnded -= OnDayEnded;
            cycle.DayStarted -= OnDayStarted;
            cycle.CampaignTimeEnded -= OnCampaignTimeEnded;
            completeButton.onClick.RemoveListener(CompletePhase);
            cycle = null;
        }

        private void Update()
        {
            if (cycle != null)
                completeButton.interactable = !host.IsTransitioning && !cycle.IsCampaignTimeEnded;
        }

        private void CompletePhase()
        {
            completeButton.interactable = false;
            try { host.CompletePhase(); }
            finally { Refresh(); }
        }

        private void OnPhaseEnded(DayPhase phase) => AddLog("Phase ended: " + phase);
        private void OnPhaseStarted(DayPhase phase) { AddLog("Phase started: " + phase); Refresh(); }
        private void OnDayEnded(int day) => AddLog("Day ended: " + day);
        private void OnDayStarted(int day) => AddLog("Day started: " + day);
        private void OnCampaignTimeEnded() { AddLog("Campaign time ended"); Refresh(); }

        private void AddLog(string message)
        {
            logLines.Enqueue(message);
            while (logLines.Count > MaxLogLines) logLines.Dequeue();
            transitionLog.text = string.Join("\n", logLines);
        }

        private void Refresh()
        {
            if (cycle == null) return;
            dayLabel.text = $"DAY {cycle.CurrentDay} / {DayCycle.CampaignDays}";
            phaseLabel.text = cycle.IsCampaignTimeEnded ? "Campaign time ended" : cycle.CurrentPhase.ToString();
            for (var i = 0; i < phaseIndicators.Length; i++)
                phaseIndicators[i].color = !cycle.IsCampaignTimeEnded && i == (int)cycle.CurrentPhase ? Color.white : new Color(0.5f, 0.55f, 0.62f);
            completeButton.interactable = !host.IsTransitioning && !cycle.IsCampaignTimeEnded;
        }
    }
}
