# Consolidated Findings

Repeated tests that demonstrated the same root cause were consolidated to avoid inflating the finding count.

| ID | Finding | Severity | Status | Primary Test(s) |
|---|---|---|---|---|
| F-01 | Unauthenticated Orthanc REST API read/download access | High | Open | 001, 007, 026 |
| F-02 | Unauthenticated DICOM object creation/deletion via REST API | High | Open | 002 |
| F-03 | Unauthenticated Orthanc modality configuration modification | High | Open | 010 |
| F-04 | Orthanc management/API traffic uses plaintext HTTP | High | Open | 011, 025 |
| F-05 | DICOM transport is unencrypted | High | Open | 005, 006, 029 |
| F-06 | Unregistered DICOM AE can inject objects with C-STORE | High | Open | 009, 032 |
| F-07 | Registered AE Title can be spoofed from another host | High | Open | 033 |
| F-08 | DCMTK SSH broadly exposed without host-based source restriction | Medium | Open | 012 |
| F-09 | Sensitive lab storage lacks verified encryption at rest | Medium | Open | 018 |
| F-10 | Backup and recovery controls are insufficient | Medium | Open | 019 |
| F-11 | Weak Active Directory password policy | Medium | Open | 027 |
| F-12 | Weak local Linux password/lockout controls | Medium | Open | 027 |
| F-13 | Insufficient end-to-end security audit visibility | Medium | Open | 016, 028 |
| F-14 | Time synchronization and audit timestamp integrity | Medium | Remediated | 024 |
| F-15 | DCMTK security updates unavailable without ESM Apps | Low | Open | 015 |
| F-16 | DCMTK host firewall not enforcing inbound source restrictions | Low | Open | 021 |
| F-17 | Mirth management certificate requires hardening | Low | Open | 025 |
| F-18 | Proxmox privileged administration lacks TFA/delegation | Low | Open | 026 |

## Public-Safe Note

Exact endpoint addresses are intentionally omitted. The sanitized PDF contains the detailed descriptions, impact statements, and remediation recommendations without publishing the private addressing plan.
