# Complete Test Matrix - TEST-001 through TEST-035

| Test | Title | Result | Severity | Key Outcome / Finding Link |
|---|---|---|---|---|
| TEST-001 | Unauthenticated Orthanc REST Read Access | FAIL | High | Unauthenticated PACS REST reads exposed system/study/patient information; foundation of F-01. |
| TEST-002 | Unauthenticated DICOM Object Creation/Deletion via REST API | FAIL | High | Synthetic DICOM object could be created, retrieved, and deleted without authentication; F-02. |
| TEST-003 | AE Title Access Control (C-ECHO) | PASS | - | Known DCMTK AE succeeded; rogue calling AE was aborted/denied for echo behavior. |
| TEST-004 | Called AE Title Validation | PASS | - | Correct ORTHANC called AE succeeded; incorrect called AE was rejected as not recognized. |
| TEST-005 | DICOM Transport / TLS Baseline | FAIL | High | Plain DICOM succeeded while TLS negotiation did not; supports F-05. |
| TEST-006 | Plaintext C-STORE Capture | FAIL | High | Synthetic identifiers recovered from C-STORE PCAP; confirms cleartext DICOM (F-05). |
| TEST-007 | Unauthenticated DICOM Download | FAIL | High | DICOM instance download succeeded without REST authentication; reinforces F-01. |
| TEST-008 | Rogue C-FIND Authorization | PASS | - | Known AE C-FIND succeeded; rogue AE query was aborted/denied. |
| TEST-009 | Rogue C-STORE Authorization | FAIL | High | Unregistered calling AE completed C-STORE successfully; F-06. |
| TEST-010 | Modality Configuration Write | FAIL | High | Unauthenticated temporary modality create/read/delete succeeded; F-03. |
| TEST-011 | Orthanc HTTP Transport Encryption | FAIL | High | REST/API traffic observed over plaintext HTTP; HTTPS probe failed; F-04. |
| TEST-012 | DCMTK Station Host Exposure Baseline | FAIL | Medium | SSH exposed on all interfaces with password auth and no host source restriction; F-08. |
| TEST-013 | Sensitive File Permissions | PASS w/ observation | - | No unauthorized read of sampled sensitive evidence; no world-writable files; group/umask hardening observation. |
| TEST-014 | Local Privilege Baseline | PASS w/ observation | - | No unexpected writable privilege-escalation paths; full sudo intentional; password-aging observation. |
| TEST-015 | Patch Status | FAIL | Low | Two DCMTK-related ESM security updates were pending_attach; F-15. |
| TEST-016 | Security Logging | PASS w/ observation | - | journald/rsyslog and SSH/sudo logging worked; auditd/fail2ban/retention hardening observations feed F-13. |
| TEST-017 | Local Secret Exposure | PASS | - | No strict secret pattern or overexposed private key confirmed after safe history review. |
| TEST-018 | Data-at-Rest Encryption | FAIL | Medium | No verified LUKS/ZFS/storage encryption for DCMTK VM/Proxmox path; F-09. |
| TEST-019 | Backup and Recovery Security | FAIL | Medium | Backup readability, lack of current schedule, stale recovery point, and no full restore validation; F-10. |
| TEST-020 | SSH Security | PASS w/ observation | - | Authorized Proxmox SSH path allowed; Kali/Pentest blocked; key permissions strong; config hardening opportunities only. |
| TEST-021 | Host Firewall and Exposed Services | FAIL | Low | UFW inactive, no nftables enforcement, iptables default ACCEPT; upstream segmentation compensates; F-16. |
| TEST-022 | Inter-VLAN Egress Controls | PASS | - | DCMTK Internet/Proxmox management blocked; intended Orthanc/Mirth workflow paths allowed; Kali blocked. |
| TEST-023 | DICOM Association Robustness | PASS | - | Invalid AE/malformed input handled without loss of service; post-malformed valid C-ECHO succeeded. |
| TEST-024 | Time Synchronization & Audit Timestamp Integrity | PASS after remediation | Medium (remediated) | OPNsense established as internal NTP; HOSP-AD, Orthanc, DCMTK, Mirth, Proxmox synchronized; F-14. |
| TEST-025 | Management HTTPS & Certificate Security | FAIL | High/Low | Orthanc plaintext HTTP (F-04); Mirth certificate hardening issue (F-17); Proxmox TLS passed. |
| TEST-026 | Administrative Account & Authentication Controls | FAIL | High/Low | Orthanc REST unauthenticated (F-01/F-03); Proxmox auth present but TFA/delegation hardening gap (F-18). |
| TEST-027 | Password Policy & Account Lockout Controls | FAIL | Medium | Weak AD and Linux password/aging/lockout controls; F-11 and F-12. |
| TEST-028 | Logging & Audit Coverage | FAIL | Medium | Infrastructure logs present, but PACS/admin attribution and retention gaps remain; F-13. |
| TEST-029 | DICOM Transport Encryption | FAIL | High | DicomTlsEnabled=false; synthetic identifiers recovered from C-STORE PCAP; F-05. |
| TEST-030 | DICOM Query/Retrieve Authorization | PASS | - | Registered DCMTK C-FIND/C-GET succeeded; ROGUEAE denied. |
| TEST-031 | DICOM C-MOVE Authorization | PASS | - | Authorized move succeeded to STORESCP; rogue move denied and produced zero files. |
| TEST-032 | DICOM C-STORE Authorization | FAIL | High | Unregistered ROGUEAE C-STORE succeeded and object persisted; F-06. |
| TEST-033 | AE Title Spoofing / Modality Trust | FAIL | High | Kali spoofing registered DCMTK AE Title inherited C-FIND access when network reachability was temporarily granted; F-07. |
| TEST-034 | Final Network Segmentation Validation | PASS | - | Pentest VLAN blocked from protected services while Internet remained available. |
| TEST-035 | Final Validation / Evidence Integrity | PASS | - | Final-phase SHA-256 manifests verified with no integrity failures. |
