using System;
using System.Collections.Generic;
using NUnit.Framework;

namespace Downfall.Time.Tests
{
    public class DayCycleTests
    {
        [Test]
        public void StartsAtDayOneDawnAndAdvancesInOrder()
        {
            var cycle = new DayCycle();
            Assert.AreEqual(1, cycle.CurrentDay);
            Assert.AreEqual(DayPhase.Dawn, cycle.CurrentPhase);

            foreach (var phase in new[] { DayPhase.Morning, DayPhase.Noon, DayPhase.Evening, DayPhase.Night })
            {
                Assert.IsTrue(cycle.CompletePhase());
                Assert.AreEqual(1, cycle.CurrentDay);
                Assert.AreEqual(phase, cycle.CurrentPhase);
            }
        }

        [Test]
        public void TransitionNotificationsObserveTheDocumentedStateAndOrder()
        {
            var cycle = new DayCycle();
            var events = new List<string>();
            cycle.PhaseEnded += phase => events.Add($"end {phase} {cycle.CurrentDay}/{cycle.CurrentPhase}");
            cycle.DayEnded += day => events.Add($"day end {day} {cycle.CurrentDay}/{cycle.CurrentPhase}");
            cycle.DayStarted += day => events.Add($"day start {day} {cycle.CurrentDay}/{cycle.CurrentPhase}");
            cycle.PhaseStarted += phase => events.Add($"start {phase} {cycle.CurrentDay}/{cycle.CurrentPhase}");

            cycle.CompletePhase();
            CollectionAssert.AreEqual(new[] { "end Dawn 1/Dawn", "start Morning 1/Morning" }, events);
            for (var i = 0; i < 3; i++) cycle.CompletePhase();
            events.Clear();
            cycle.CompletePhase();
            CollectionAssert.AreEqual(new[] { "end Night 1/Night", "day end 1 1/Night", "day start 2 2/Dawn", "start Dawn 2/Dawn" }, events);
        }

        [Test]
        public void FinalNightEndsCampaignOnceWithoutStartingDay26()
        {
            var cycle = new DayCycle();
            for (var i = 0; i < 124; i++) Assert.IsTrue(cycle.CompletePhase());
            Assert.AreEqual(25, cycle.CurrentDay);
            Assert.AreEqual(DayPhase.Night, cycle.CurrentPhase);
            var events = new List<string>();
            cycle.PhaseEnded += phase => events.Add("phase ended " + phase);
            cycle.DayEnded += day => events.Add("day ended " + day);
            cycle.CampaignTimeEnded += () => events.Add("campaign ended");
            cycle.DayStarted += day => events.Add("day started " + day);
            cycle.PhaseStarted += phase => events.Add("phase started " + phase);

            Assert.IsTrue(cycle.CompletePhase());
            Assert.IsFalse(cycle.CompletePhase());
            Assert.IsTrue(cycle.IsCampaignTimeEnded);
            Assert.AreEqual(25, cycle.CurrentDay);
            Assert.AreEqual(DayPhase.Night, cycle.CurrentPhase);
            CollectionAssert.AreEqual(new[] { "phase ended Night", "day ended 25", "campaign ended" }, events);
        }

        [Test]
        public void NestedCompletionDoesNotAdvanceOrDuplicateEvents()
        {
            var cycle = new DayCycle();
            var calls = 0;
            cycle.PhaseEnded += phase => { calls++; Assert.IsFalse(cycle.CompletePhase()); };
            Assert.IsTrue(cycle.CompletePhase());
            Assert.AreEqual(1, calls);
            Assert.AreEqual(DayPhase.Morning, cycle.CurrentPhase);
        }

        [Test]
        public void PhaseEndedFailureDoesNotStopOtherSubscribersOrAdvanceTwice()
        {
            var cycle = new DayCycle();
            var error = new InvalidOperationException("expected phase end failure");
            var observed = new List<DayPhase>();
            cycle.PhaseEnded += _ => throw error;
            cycle.PhaseEnded += observed.Add;
            Assert.IsTrue(cycle.CompletePhase());
            Assert.AreEqual(DayPhase.Morning, cycle.CurrentPhase);
            CollectionAssert.AreEqual(new[] { DayPhase.Dawn }, observed);
            Assert.AreEqual(1, cycle.LastNotificationFailures.Count);
            Assert.AreEqual("PhaseEnded", cycle.LastNotificationFailures[0].EventName);
            Assert.AreSame(error, cycle.LastNotificationFailures[0].Exception);
            Assert.IsTrue(cycle.CompletePhase());
            CollectionAssert.AreEqual(new[] { DayPhase.Dawn, DayPhase.Morning }, observed);
        }

        [Test]
        public void DayEndedFailureStillCompletesTransitionOnce()
        {
            var cycle = new DayCycle();
            for (var i = 0; i < 4; i++) cycle.CompletePhase();
            var ends = new List<int>();
            cycle.DayEnded += _ => throw new InvalidOperationException("expected day end failure");
            cycle.DayEnded += ends.Add;
            Assert.IsTrue(cycle.CompletePhase());
            Assert.AreEqual(2, cycle.CurrentDay);
            Assert.AreEqual(DayPhase.Dawn, cycle.CurrentPhase);
            CollectionAssert.AreEqual(new[] { 1 }, ends);
            Assert.AreEqual("DayEnded", cycle.LastNotificationFailures[0].EventName);
            Assert.IsTrue(cycle.CompletePhase());
            CollectionAssert.AreEqual(new[] { 1 }, ends);
            Assert.AreEqual(0, cycle.LastNotificationFailures.Count);
        }

        [Test]
        public void PhaseStartedFailureIsReportedAndOtherSubscribersRun()
        {
            var cycle = new DayCycle();
            var observed = new List<DayPhase>();
            cycle.PhaseStarted += _ => throw new InvalidOperationException("expected phase start failure");
            cycle.PhaseStarted += observed.Add;
            Assert.IsTrue(cycle.CompletePhase());
            CollectionAssert.AreEqual(new[] { DayPhase.Morning }, observed);
            Assert.AreEqual("PhaseStarted", cycle.LastNotificationFailures[0].EventName);
        }

        [Test]
        public void FinalBoundarySurvivesSubscriberFailuresAndRejectsRepeatedCompletion()
        {
            var cycle = new DayCycle();
            for (var i = 0; i < 124; i++) cycle.CompletePhase();
            var ends = 0;
            cycle.DayEnded += _ => throw new InvalidOperationException("expected end failure");
            cycle.CampaignTimeEnded += () => throw new InvalidOperationException("expected campaign failure");
            cycle.CampaignTimeEnded += () => ends++;
            Assert.IsTrue(cycle.CompletePhase());
            Assert.IsFalse(cycle.CompletePhase());
            Assert.AreEqual(1, ends);
            Assert.IsTrue(cycle.IsCampaignTimeEnded);
            Assert.AreEqual(25, cycle.CurrentDay);
            Assert.AreEqual(2, cycle.LastNotificationFailures.Count);
        }
    }
}
