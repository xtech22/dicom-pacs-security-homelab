# Evidence Guide

A strong GitHub security portfolio shows enough evidence to prove the work without leaking sensitive data.

## Publish

Good public evidence includes:

- Cropped terminal screenshots
- Sanitized Nmap excerpts
- Orthanc log excerpts with identifiers removed
- DICOM association success/failure screenshots
- Redacted Wireshark screenshots
- `curl` request/response snippets without credentials/tokens
- Before/after firewall-rule validation
- Screenshots demonstrating remediation and retesting

## Do Not Publish

- Real patient data
- Unsanitized `.dcm` files
- Full PCAPs containing sensitive data
- Passwords
- API keys
- cookies/session tokens
- private keys
- exact host addresses when they add no portfolio value
- configuration exports containing secrets

## Screenshot Naming Convention

Use:

```text
<test-id>_<short-description>_<yyyy-mm-dd>.png
```

Examples:

```text
NET-01_nmap-clinical-services_2026-08-21.png
DCM-02_unknown-ae-rejected_2026-08-21.png
API-01_orthanc-http-enumeration_2026-08-21.png
```

## Evidence Workflow

1. Save the original to `evidence/raw/`.
2. Duplicate it.
3. Crop/redact the copy.
4. Place the sanitized copy in `evidence/sanitized/`.
5. Reference the sanitized file from `docs/test-matrix.md` or `docs/findings.md`.
6. Never force-add ignored raw evidence to Git.
