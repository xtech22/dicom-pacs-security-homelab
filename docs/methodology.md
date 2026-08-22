# Methodology

The assessment follows a practical penetration-testing workflow adapted for DICOM/PACS and healthcare-interface systems.

## Phase 1 — Baseline Validation

Before testing security controls, verify that legitimate workflows work.

- DICOM C-ECHO
- DICOM C-STORE
- DICOM C-FIND
- DICOM C-MOVE / C-GET
- DCMTK receiver operation
- Orthanc availability
- HL7 ADT / ORM / ORU processing
- Expected inter-VLAN communication

This creates a known-good baseline and prevents normal configuration problems from being mislabeled as security findings.

## Phase 2 — Reconnaissance and Service Enumeration

Goals:

- Identify reachable hosts.
- Identify open ports and service versions.
- Compare observed services with intended firewall policy.
- Record commands and raw output.

Typical tools:

- Nmap
- `nc`
- `curl`
- Wireshark
- tcpdump

## Phase 3 — DICOM Security Testing

### Association behavior
Evaluate whether the PACS accepts only intended calling modalities and how it responds to unknown AE Titles.

### Query/retrieve behavior
Test whether an authorized but untrusted network position can enumerate or retrieve studies.

### Store behavior
Test whether a non-approved modality can inject a synthetic study.

### Metadata integrity
Use synthetic DICOM files to determine whether modified patient/study metadata is accepted without additional integrity controls.

## Phase 4 — PACS Web/API Assessment

Review the Orthanc web/API surface for:

- authentication
- authorization
- exposed REST resources
- unsafe anonymous access
- administrative functions
- information disclosure

## Phase 5 — Traffic Analysis

Capture lab traffic to determine:

- whether DICOM metadata is visible in clear text
- whether credentials or tokens are exposed
- whether segmentation limits packet visibility
- whether logging captures abnormal behavior

Only sanitized excerpts should be published.

## Phase 6 — Detection and Defensive Validation

Review Orthanc and system logs to determine whether suspicious actions can be detected.

The repository includes a starter Python parser for selected Orthanc log conditions.

## Phase 7 — Reporting and Retesting

For each confirmed issue:

1. Capture evidence.
2. Explain impact.
3. Recommend remediation.
4. Apply the defensive change.
5. Retest.
6. Record the final status.
