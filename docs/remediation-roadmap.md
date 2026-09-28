# Remediation Roadmap

The initial assessment is preserved as the baseline. Remediation work should generate new evidence and retest results rather than overwrite original test artifacts.

| Priority | Action | Related Findings | Validation Criteria |
|---|---|---|---|
| 1 - Immediate | Enable Orthanc authentication; restrict 8042; separate administrative access from clinical data paths. | F-01, F-02, F-03 | Unauthenticated reads/writes/config changes return 401/403; authorized admin workflow remains functional. |
| 2 - Immediate | Enable HTTPS for Orthanc management and DICOM TLS where supported. | F-04, F-05 | TLS validates to internal CA; plaintext management disabled; DICOM TLS succeeds with approved peers. |
| 3 - Immediate | Set DicomAlwaysAllowStore=false and combine AE registration with source-host/TLS trust. | F-06, F-07 | Registered modality stores/queries succeed; rogue and spoofed sources fail. |
| 4 - Near term | Harden DCMTK SSH/host firewall and improve credential policy. | F-08, F-12, F-16 | Host firewall default-deny; SSH restricted; strong PAM/lockout controls; keys/TFA where supported. |
| 5 - Near term | Implement encryption at rest and mature backup/recovery. | F-09, F-10 | Encrypted primary/backup storage; scheduled monitored backups; successful isolated restore test. |
| 6 - Near term | Improve end-to-end audit visibility and retention. | F-13 | Orthanc/Mirth/admin actions are attributable and forwarded/retained appropriately. |
| 7 - Planned | Close patch/certificate/MFA hygiene gaps. | F-15, F-17, F-18 | DCMTK security fixes available; Mirth trusted SAN certificate; Proxmox TFA/delegated accounts. |
| Maintain | Preserve OPNsense segmentation and internal NTP health. | F-14 / positive controls | Time remains synchronized; TEST-034-style segmentation checks continue to pass. |

## Retest Rule

Each remediated finding should be closed only after the original failing test (or an equivalent controlled retest) demonstrates the expected secure behavior and the result is preserved in a new evidence package.
