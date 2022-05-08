import streamlit as st
import pandas as pd
import sqlite3 as sq
from base64 import b64decode
from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName
from fhirclient import client
import fhirclient.models.patient as p

from fhirclient import client
import fhirclient.models.patient as p

settings = {
    'app_id': 'my_web_app',
    'api_base': 'http://wildfhir4.aegis.net/fhir4-0-1'
}

smart = client.FHIRClient(settings=settings)

patient = p.Patient.read('f001', smart.server)
print('Birth Date', patient.birthDate.isostring)
print('Patient Name', smart.human_name(patient.name[0]))


connection = sq.connect('FHIRedUp_DB.db')
cursor = connection.cursor()

patientDataObj1 = {"resourceType": "Patient",
    "id": "p001",
    "active": True,
    "name": "Janae Spencer",
    "birthDate": "1990-7-4",
    "gender": "female"
    }

patientDataObj2 = {"resourceType": "Patient",
    "id": "p002",
    "active": True,
    "name":  "Amy Brown",
    "birthDate": "1983-3-13",
    "gender": "female"
    }

patientDataObj3 = {"resourceType": "Patient",
    "id": "p003",
    "active": True,
    "name": "Tana Smith",
    "birthDate": "1970-2-6",
    "gender": "female"
    }
patientDataObj4 = {"resourceType": "Patient",
    "id": "p004",
    "active": True,
    "name": "Kenneth White",
    "birthDate": "1972-12-21",
    "gender": "male"
    }

patientDataObj5 = {"resourceType": "Patient",
    "id": "p005",
    "active": True,
    "name": "Russell Moore",
    "birthDate": "1990-11-17",
    "gender": "male"
    }

patientDataObj6 = {"resourceType": "Patient",
    "id": "p006",
    "active": True,
    "name": "Keenan Stokes",
    "birthDate": "1999-9-9",
    "gender": "male"
    }

patientDataObj7 = {"resourceType": "Patient",
    "id": "p007",
    "active": True,
    "name": "Stephanie Reynolds",
    "birthDate": "1962-5-5",
    "gender" : "female"
    }

patientDataObj8 = {"resourceType": "Patient",
    "id": "p008",
    "active": True,
    "name": "Kylie Mills",
    "birthDate": "2000-1-5",
    "gender": "female"
    }

patientDataObj9 = {"resourceType": "Patient",
    "id": "p009",
    "active": True,
    "name": "Jane Alver",
    "birthDate": "1985-6-21",
    "gender": "female"
    }

patientDataObj10 = {"resourceType": "Patient",
    "id": "p010",
    "active": True,
    "name": "Kevin Mayer",
    "birthDate": "1965-2-13",
    "gender": "male"
    }

patientDataObj11 = {"resourceType": "Patient",
    "id": "p011",
    "active": True,
    "name": "Anna Myers",
    "birthDate": "1996-7-15",
    "gender": "female"
    }

patientObjs = [patientDataObj1, patientDataObj2, patientDataObj3, patientDataObj4, patientDataObj5, patientDataObj6, patientDataObj7, patientDataObj4, patientDataObj8, patientDataObj9, patientDataObj10, patientDataObj11]
st.write("""
# FHIRed Up""")
desiredPatientId = "p001"
desiredPatientId = st.text_input("Enter desired Patient's Id", key = "EHRSim")
for obj in patientObjs:
    if(obj.get("id") == desiredPatientId):
        desiredPatient = obj

patientName = desiredPatient.get("name")
patientName = patientName
st.write("""
## Patient Info
Name: %s \n 
DOB: %s \n
Sex: %s \n
## Testing Resources
"""%(patientName, desiredPatient.get("birthDate"), desiredPatient.get("gender")))

test_type = st.text_input("Enter desired test type:", key = "test")

def clear_text():
    st.session_state["test"] = ""
st.button("Send Testing Request", on_click= clear_text)
# st.write(""" 
#     ## Previous Tests""")
i = 0
# # reportIds = str(cursor.execute("SELECT ReportId FROM LabResults"))
# print(reportIds)
#doctorId, patientId = reportIds[0] + reportIds[1] + reportIds[3], reportIds[4] + reportIds[5] + reportIds[6]
# print(doctorId , patientId)
patientId = desiredPatientId
print("This is the Patient ID: " + patientId)
cursor.execute("SELECT count(ReportId) FROM LabResults WHERE patientId = '%s'" %(str(patientId)))
count = int(len(cursor.fetchall()))
cursor.execute("SELECT ResultPDF FROM LabResults WHERE patientId = '%s'" %(str(patientId)))

completedTestType = ""
completedTestAcc = ""
completedTestDate = ""

while(i < count):
    # b64 = str(cursor.fetchone())
    # bytes = b64decode(b64, validate=True)
    # f = open('file.pdf', 'wb')
    # f.write(bytes)
    # f.close()
    cursor.execute("SELECT testType from LabResults Where patientId = '%s'"%(str(patientId)))
    completedTestType = str(cursor.fetchall())
    cursor.execute("SELECT AccId from LabResults Where patientId = '%s'"%(str(patientId)))
    completedTestAcc = str(cursor.fetchall())
    cursor.execute("SELECT dateOfReport from LabResults Where patientId = '%s'"%(str(patientId)))
    completedTestDate = cursor.fetchone()
        

    st.write(""" 
    ## Previous Tests   
    **Test Type:** %s \n
    **ACC ID:** %s \n
    **Date Received:** %s \n
    ### File:
    """ %(completedTestType[3:-4], completedTestAcc[3:-4], completedTestDate[0]))
    downloadPdf = st.button("Download PDF", key = "PDFDownloadBTN")
    i += 1
# cursor.close
    # Import only b64decode function from the base64 module

if downloadPdf :
    # Define the Base64 string of the PDF file
    cursor.execute("SELECT ResultPDF FROM LabResults WHERE patientId = '%s'" %(str(desiredPatientId)))

    # For Anthony to complete
    b64 =  str(cursor.fetchone())

    # Decode the Base64 string, making sure that it contains only valid characters
    bytes = b64decode(b64)

    # Perform a basic validation to make sure that the result is a valid PDF file
    # Be aware! The magic number (file signature) is not 100% reliable solution to validate PDF files
    # Moreover, if you get Base64 from an untrusted source, you must sanitize the PDF contents
    if bytes[0:4] != b'%PDF':
        raise ValueError('Missing the PDF file signature')

    # Write the PDF contents to a local file
    f = open('%s.pdf' %(str(patientId)), 'wb')
    f.write(bytes)
    f.close()
    cursor.close()
