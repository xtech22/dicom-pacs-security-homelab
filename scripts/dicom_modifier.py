# dicom_modifier.py
# Modify DICOM metadata using pydicom

from pydicom import dcmread
from pydicom.filewriter import write_file
import sys

def modify_dicom(input_file, output_file, patient_name="HACKED^PHI", institution="Compromised Hospital"):
    try:
        ds = dcmread(input_file)
        ds.PatientName = patient_name
        ds.InstitutionName = institution
        write_file(output_file, ds)
        print(f"Modified DICOM saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python dicom_modifier.py input.dcm output.dcm")
    else:
        modify_dicom(sys.argv[1], sys.argv[2])
