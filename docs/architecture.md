# Architecture

## Segmentation Model

The homelab separates administrative infrastructure, clinical imaging, healthcare applications, and security testing into dedicated VLANs.

| VLAN | Function | Network |
|---|---|---|
| 20 | Infrastructure / Administration | `10.10.20.0/24` |
| 30 | Imaging / Clinical | `10.10.30.0/24` |
| 40 | Applications / HL7 | `10.10.40.0/24` |
| 50 | Security / Pentest | `10.10.50.0/24` |

OPNsense provides routing and firewall enforcement between segments.

## Clinical Segment

The clinical VLAN contains:

- A Windows radiology workstation
- Orthanc PACS
- A DICOM viewer
- A separate DCMTK modality-simulator station

Primary DICOM services:

- Orthanc DICOM: TCP 4242
- Orthanc Web/API: TCP 8042
- DCMTK Store SCP receiver: TCP 11112

## Applications Segment

Mirth Connect simulates healthcare interface-engine workflows and provides HL7 message processing.

Publicly documented ports used by this project:

- TCP 8443 — Mirth administration
- TCP 6662 — HL7 test listener
- TCP 6663 — HL7-to-Orthanc workflow

## Security Segment

Kali Linux is isolated in the security VLAN and is used as the authorized penetration-testing workstation.

## Public Documentation Decision

This repository intentionally publishes network ranges but not individual endpoint IP addresses. That keeps the architecture understandable while avoiding unnecessary disclosure of system-specific addressing.
