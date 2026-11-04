"""Deterministic tests using synthetic ARP mapping observations."""

import unittest

from arp_detector import ArpMonitor, render_observation


class ArpMonitorTests(unittest.TestCase):
    def test_first_observation_builds_baseline(self):
        event = ArpMonitor().observe("192.168.1.1", "08:00:27:43:3c:1f")
        self.assertEqual(event.kind, "learned")
        self.assertIn("LEARNED", render_observation(event))

    def test_same_mapping_does_not_alert(self):
        monitor = ArpMonitor()
        monitor.observe("192.168.1.1", "08:00:27:43:3c:1f")
        event = monitor.observe("192.168.1.1", "08:00:27:43:3c:1f")
        self.assertEqual(event.kind, "unchanged")
        self.assertIsNone(render_observation(event))

    def test_changed_mac_triggers_alert(self):
        monitor = ArpMonitor()
        monitor.observe("192.168.1.1", "08:00:27:43:3c:1f")
        event = monitor.observe("192.168.1.1", "08:00:27:fa:e0:57")
        self.assertEqual(event.kind, "alert")
        self.assertEqual(event.previous_mac, "08:00:27:43:3c:1f")
        self.assertIn("08:00:27:fa:e0:57", render_observation(event))

    def test_normalises_mac_case(self):
        monitor = ArpMonitor()
        monitor.observe("192.168.1.1", "AA:BB:CC:DD:EE:FF")
        self.assertEqual(monitor.observe("192.168.1.1", "aa:bb:cc:dd:ee:ff").kind, "unchanged")

    def test_rejects_empty_fields(self):
        with self.assertRaises(ValueError):
            ArpMonitor().observe("", "aa:bb")


if __name__ == "__main__":
    unittest.main()
