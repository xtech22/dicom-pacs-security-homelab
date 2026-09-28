# Evidence Guide

The private assessment maintained per-test evidence directories with command output, configuration captures, synthetic DICOM objects, packet captures, and SHA-256 manifests where available.

## What is Public

- Sanitized final report
- Test matrix and consolidated findings summary
- Methodology and architecture documentation
- Non-secret helper scripts

## What is Intentionally Private

- Raw PCAP files
- Original screenshots containing exact host addresses
- Unredacted command output
- Authentication material, private keys, tokens, passwords, shell-history secrets, or other credentials
- Original evidence packages and manifests tied to private endpoint details

`evidence/raw/` is ignored by Git and should remain local only.

## Evidence Integrity

Final validation verified the reviewed SHA-256 evidence manifests without integrity failures. Public artifacts are derivatives of the original evidence and are not a replacement for the private source package.
