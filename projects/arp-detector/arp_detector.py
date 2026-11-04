"""ARP mapping-change monitor for an authorised lab network.

Reconstructed and extended from SIT379 Module 5 Task C (2026) evidence.
This is new portfolio code, not a verbatim copy of the university submission.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class Observation:
    kind: str
    ip: str
    mac: str
    previous_mac: str | None = None


class ArpMonitor:
    """Remember observed ARP mappings and flag unexpected changes."""

    def __init__(self) -> None:
        self.mappings: dict[str, str] = {}

    def observe(self, ip: str, mac: str) -> Observation:
        ip = ip.strip()
        mac = mac.strip().lower()
        if not ip or not mac:
            raise ValueError("IP and MAC must not be empty")

        previous = self.mappings.get(ip)
        if previous is None:
            self.mappings[ip] = mac
            return Observation("learned", ip, mac)
        if previous == mac:
            return Observation("unchanged", ip, mac)

        self.mappings[ip] = mac
        return Observation("alert", ip, mac, previous)


def render_observation(event: Observation) -> str | None:
    if event.kind == "learned":
        return f"[LEARNED] {event.ip} -> {event.mac}"
    if event.kind == "alert":
        return (
            "[ALERT] Possible ARP mapping change detected!\n"
            f"IP Address: {event.ip}\n"
            f"Old MAC:    {event.previous_mac}\n"
            f"New MAC:    {event.mac}"
        )
    return None


def run(interface: str, packet_count: int) -> None:
    try:
        from scapy.all import ARP, sniff
    except ImportError as exc:
        raise SystemExit("Scapy is required: python -m pip install scapy") from exc

    monitor = ArpMonitor()
    print(f"[*] Monitoring ARP replies on {interface}. Press Ctrl+C to stop.")

    def handle_packet(packet: object) -> None:
        if not packet.haslayer(ARP) or packet[ARP].op != 2:
            return
        event = monitor.observe(packet[ARP].psrc, packet[ARP].hwsrc)
        message = render_observation(event)
        if message:
            print(message, flush=True)

    sniff(
        iface=interface,
        filter="arp",
        prn=handle_packet,
        store=False,
        count=packet_count,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Detect changes in observed ARP mappings")
    parser.add_argument("--interface", default="eth0", help="Network interface to monitor")
    parser.add_argument("--packet-count", type=int, default=0, help="Stop after this many packets (0 = unlimited)")
    args = parser.parse_args()
    if args.packet_count < 0:
        parser.error("--packet-count cannot be negative")
    try:
        run(args.interface, args.packet_count)
    except PermissionError as exc:
        raise SystemExit("Packet capture requires suitable system privileges") from exc
    except KeyboardInterrupt:
        print("\n[*] Monitoring stopped.")


if __name__ == "__main__":
    main()
