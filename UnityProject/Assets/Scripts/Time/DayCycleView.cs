using UnityEngine;

namespace Downfall.Time
{
    public sealed class DayCycleView : MonoBehaviour
    {
        private DayCycle cycle;

        private void Awake()
        {
            cycle = new DayCycle();
        }

        private void OnGUI()
        {
            GUILayout.BeginArea(new Rect(20, 20, 260, 120), GUI.skin.box);
            GUILayout.Label($"Day {cycle.CurrentDay} / {cycle.CurrentPhase}");
            if (cycle.IsCampaignTimeEnded)
                GUILayout.Label("Campaign time ended");
            else if (GUILayout.Button("Complete phase"))
                cycle.CompletePhase();
            GUILayout.EndArea();
        }
    }
}
