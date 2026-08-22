# Scope and Rules of Engagement

## Objective

Assess the security posture of a self-hosted DICOM/PACS and HL7 homelab while preserving normal clinical workflow behavior.

## In Scope

- OPNsense firewall policy relevant to the lab VLANs
- Orthanc PACS
- Orthanc DICOM service
- Orthanc Web/API
- DCMTK modality-simulator station
- DICOM Store SCP receiver
- Radiology workstation
- Mirth Connect interfaces used by the lab
- Network paths between the security, clinical, application, and infrastructure VLANs

## Out of Scope

- Internet hosts not owned by the lab operator
- Production healthcare systems
- Employer/customer systems
- Real patient data
- Destructive testing that could affect systems outside the homelab

## Test Origin

The primary security-testing workstation is Kali Linux on the dedicated security VLAN.

## Data Rules

Only synthetic or de-identified data may be used. Evidence intended for GitHub must be reviewed for:

- Patient names
- Patient IDs
- accession numbers
- dates of birth
- IP addresses that should remain private
- usernames
- passwords
- API tokens
- session cookies
- hostnames revealing private information
