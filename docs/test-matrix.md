# Test Matrix

Legend:

- ✅ Complete
- 🟡 In progress
- 👁 Observed control behavior
- ⏳ Planned
- 🚫 Not applicable / intentionally excluded

| ID | Test | Component | Status | Evidence |
|---|---|---|---|---|
| BASE-01 | DICOM C-ECHO | Orthanc/DCMTK | ✅ | Add sanitized screenshot |
| BASE-02 | DICOM C-STORE | Orthanc/DCMTK | ✅ | Add sanitized screenshot |
| BASE-03 | DICOM C-FIND | Orthanc/DCMTK | ✅ | Add sanitized screenshot |
| BASE-04 | DICOM C-MOVE / C-GET | Orthanc/DCMTK | ✅ | Add sanitized screenshot |
| BASE-05 | HL7 ADT workflow | Mirth | ✅ | Add sanitized screenshot |
| BASE-06 | HL7 ORM workflow | Mirth | ✅ | Add sanitized screenshot |
| BASE-07 | HL7 ORU workflow | Mirth | ✅ | Add sanitized screenshot |
| NET-01 | Security VLAN discovery | Network | 🟡 | Add Nmap excerpt |
| NET-02 | Clinical VLAN service enumeration | Network | 🟡 | Add Nmap excerpt |
| NET-03 | Cross-VLAN denied-service validation | OPNsense | 🟡 | Add firewall/Nmap evidence |
| DCM-01 | Known AE Title association | Orthanc | 👁 | Add association evidence |
| DCM-02 | Unknown AE Title association | Orthanc | 👁 | Add rejection evidence |
| DCM-03 | AE Title spoofing/bypass test | Orthanc | ⏳ | — |
| DCM-04 | Unauthorized C-FIND | Orthanc | ⏳ | — |
| DCM-05 | Unauthorized C-STORE | Orthanc | ⏳ | — |
| DCM-06 | Unauthorized C-MOVE/C-GET | Orthanc | ⏳ | — |
| API-01 | Orthanc HTTP service enumeration | Orthanc | 🟡 | Add curl/Nmap evidence |
| API-02 | Orthanc REST authentication review | Orthanc | 🟡 | Add sanitized HTTP evidence |
| INT-01 | Synthetic DICOM metadata modification | DICOM object | 🟡 | Script available |
| INT-02 | Tampered object acceptance test | Orthanc | ⏳ | — |
| NET-04 | DICOM transport confidentiality capture | DICOM | ⏳ | Sanitized packet excerpt |
| MON-01 | Orthanc abnormal-event log review | Orthanc | 🟡 | Script available |
| HL7-SEC-01 | HL7 listener exposure test | Mirth | ⏳ | — |
| HL7-SEC-02 | HL7 message validation/security test | Mirth | ⏳ | — |
| POST-01 | Lateral movement/privilege escalation | Lab hosts | ⏳ | Future phase |
