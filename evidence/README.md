# Evidence

This directory is divided into two areas.

## `raw/`

Local working evidence only.

This directory is ignored by Git and should contain items such as:

- raw Nmap output
- packet captures
- unsanitized logs
- original screenshots
- temporary test DICOM objects

## `sanitized/`

Only evidence reviewed and approved for public release belongs here.

Before committing, verify that screenshots and text do not expose credentials, tokens, patient information, or unnecessary endpoint details.
