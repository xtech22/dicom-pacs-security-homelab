# Findings

This file intentionally separates **confirmed findings** from **observations** and **test candidates**.

Do not promote a test idea to a vulnerability until reproducible evidence exists.

---

## Security Control Observation — AE Title Filtering

**Status:** Observed; bypass testing pending  
**Risk:** Informational  
**Affected component:** Orthanc DICOM service

### Description

During baseline testing, legitimate DICOM communication was observed to depend on configured/known modality information. Unknown or non-approved modality behavior should be documented with sanitized association evidence before this is treated as a security-control conclusion.

### Why it matters

AE Title restrictions can reduce accidental or unauthorized DICOM associations, but an AE Title is an identifier rather than a strong authentication secret. The next test phase should determine whether a client on an allowed network path can impersonate a trusted AE Title.

### Evidence Needed

- Known-AE successful association
- Unknown-AE failed association
- Orthanc log entries for both cases
- Network source context
- Spoofed-AE retest result

### Recommendation

Treat AE Title allowlisting as one layer of defense, not as the sole authentication mechanism. Pair it with network segmentation, host-level controls, secure transport where supported, logging, and strong web/API authentication.

---

## Test Candidate — DICOM Transport Confidentiality

**Status:** Not yet published as a finding  
**Risk:** To be determined

### Test Objective

Capture an authorized lab DICOM transfer and verify whether patient/study metadata is readable in transit.

### Evidence Required Before Reporting

- Packet capture from the isolated lab
- Sanitized screenshot showing the protocol/metadata exposure
- Confirmation that no TLS or equivalent encrypted transport protected the tested path
- Clear identification of the affected workflow

---

## Test Candidate — Orthanc Web/API Access Control

**Status:** Assessment in progress  
**Risk:** To be determined

### Test Objective

Determine which Orthanc HTTP/API resources are reachable from the security VLAN and whether authentication and authorization are correctly enforced.

### Evidence Required Before Reporting

- Nmap/service evidence
- `curl` request/response excerpts
- Authentication behavior
- Authorization boundary test
- Sanitized screenshots or HTTP excerpts

---

## Finding Template

Copy this section for each confirmed issue.

### F-XXX — Finding Title

**Severity:** Critical / High / Medium / Low / Informational  
**Affected component:**  
**Status:** Open / Remediated / Accepted / Retest required

#### Description

Describe what was observed and the security condition that caused it.

#### Reproduction Summary

1. Starting position
2. Test action
3. Observed result
4. Reproduction condition

#### Evidence

- Screenshot:
- Command output:
- Log excerpt:
- Packet excerpt:

#### Impact

Explain what an attacker could accomplish in the context of a healthcare imaging workflow.

#### Recommendation

Provide specific defensive actions.

#### Retest

Document the remediation and the result of the verification test.
