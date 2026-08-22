# GitHub Upload Steps

## Recommended repository name

`dicom-pacs-security-homelab`

## Option A — GitHub CLI

From the folder containing this repository:

```bash
cd dicom-pacs-security-homelab

git init
git branch -M main
git add .
git status
git commit -m "Initial DICOM/PACS security homelab portfolio"

gh auth login

gh repo create dicom-pacs-security-homelab \
  --public \
  --source=. \
  --remote=origin \
  --push
```

## Option B — GitHub Website + Git

1. Sign in to GitHub.
2. Create a new public repository named `dicom-pacs-security-homelab`.
3. Do not initialize it with a README because this folder already contains one.
4. Copy the repository URL.
5. Run:

```bash
cd dicom-pacs-security-homelab

git init
git branch -M main
git add .
git status
git commit -m "Initial DICOM/PACS security homelab portfolio"

git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin main
```

## Before the First Push

Run:

```bash
git status
git diff --cached
```

Confirm that you do **not** see:

- `.dcm` files
- `.pcap` / `.pcapng` files
- credentials
- tokens
- private configuration exports
- raw evidence

## Suggested GitHub About Text

**Segmented DICOM/PACS & HL7 healthcare cybersecurity homelab for authorized penetration testing, protocol analysis, detection engineering, and remediation practice.**

## Suggested Topics

```text
dicom
pacs
healthcare-security
cybersecurity
penetration-testing
orthanc
dcmtk
hl7
mirth-connect
opnsense
wireshark
network-security
homelab
```
