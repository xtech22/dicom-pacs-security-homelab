# Scope and Rules of Engagement

## In Scope

- Orthanc PACS and REST/API management surface
- DICOM workflow endpoints and authorization behavior
- DCMTK modality-simulation host
- Mirth Connect / HL7 integration paths
- Active Directory controls relevant to the lab
- Proxmox management, storage, and backup controls
- OPNsense segmentation and egress policy
- Logging, time synchronization, certificates, and evidence integrity

## Objectives

- Validate PACS management/API authentication and authorization.
- Validate calling/called AE controls and query/retrieve/store behavior.
- Evaluate management and DICOM transport encryption.
- Assess host exposure, SSH, permissions, privilege boundaries, patch status, logging, secrets, and encryption at rest.
- Review backup/recovery security and recoverability indicators.
- Validate least-privilege network segmentation and egress.
- Confirm post-test restoration and evidence integrity.

## Safety Constraints

- Authorized testing only inside the isolated homelab.
- Synthetic DICOM data only for controlled write-path testing.
- No real patient data.
- No destructive modification of legitimate studies.
- No brute-force or intentional account-lockout campaigns.
- Temporary firewall exceptions were narrowly scoped and removed after testing.
