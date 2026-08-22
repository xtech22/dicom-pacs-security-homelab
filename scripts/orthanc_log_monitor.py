# orthanc_log_monitor.py
# Basic log parser to detect abnormal activity in Orthanc PACS logs

import re

def parse_log(log_file):
    with open(log_file, 'r') as f:
        lines = f.readlines()

    alerts = []

    for line in lines:
        if "StoreInstance" in line and "Unauthorized" in line:
            alerts.append(f"Unauthorized DICOM store attempt: {line.strip()}")
        elif "RetrieveInstance" in line and "Failed" in line:
            alerts.append(f"Failed image retrieval: {line.strip()}")
        elif "Query" in line and "AE Title" in line:
            alerts.append(f"Suspicious AE title used in query: {line.strip()}")

    if alerts:
        print("Suspicious activity detected:")
        for alert in alerts:
            print(alert)
    else:
        print("No suspicious activity found.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python orthanc_log_monitor.py orthanc.log")
    else:
        parse_log(sys.argv[1])
