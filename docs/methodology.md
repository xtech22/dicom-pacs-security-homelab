# Methodology

Testing followed an incremental, evidence-preserving workflow:

1. Establish a known-good baseline.
2. Exercise the authorized/expected path.
3. Challenge the same control with a negative or adversarial case where appropriate.
4. Preserve output, packet captures, configuration excerpts, and synthetic test objects.
5. Hash evidence with SHA-256 where available.
6. Restore temporary test changes and revalidate segmentation.
7. Consolidate repeated demonstrations of the same root cause into a single finding.

## Tools

- DCMTK: `echoscu`, `storescu`, `findscu`, `getscu`, `movescu`, `storescp`, `dcmdump`, `dcmodify`
- `curl`, OpenSSL, netcat, Nmap, tcpdump/Wireshark
- Linux host-hardening and networking utilities
- Windows PowerShell and Active Directory cmdlets
- OPNsense firewall rules, logs, states, and internal NTP
- Proxmox VE CLI/storage/backup utilities
- SHA-256 hashing utilities

## Risk Rating

The assessment used High / Medium / Low qualitative ratings based on impact, ease of abuse inside the modeled trust boundary, and the presence or absence of compensating controls.
