'''
Author: Ifeoluwa Oyelowo-Paul
Date: April 8, 2025


Called Hospital but more like a Patient / Doctor Scheduler:
A Patient class and a Doctor class. 
The Doctor that can handle multiple Patients
Setup a scheduling program where a doctor can only handle 16 patients during an 8 hr work day

'''
from datetime import datetime
from datetime import timedelta

# Patient class
class Patient:

    def __init__(self, name:str,  arrival_datetime:datetime):
        self.name = name
        self.arrival_datetime = arrival_datetime # when patient arrives
        self.depature_datetime = None # when patient leaves the hospital


    def __str__(self):
        return f"My name is patient {self.name}. I arrived at {self.arrival_datetime}."

    def patient_leaving(self, depature_datetime):
        #when patient is leaving
        self.depature_datetime = datetime.now()
        

# Doctor class
class Doctor:

    def __init__(self, name:str, start_datetime:datetime):
        self.name = name
        self.start_datetime = start_datetime
        self.end_datetime = start_datetime + timedelta(hours=8)
        self.patients = []

    def __str__(self):
        return f'''Dr {self.name} started work today at {self.start_datetime}. He/She will end work at {self.end_datetime}. He/She currently has {len(self.patients)} patients.'''
        
    def add_patient(self, patient): # assume Dr only sees 1 patient at a time
        if (patient.arrival_datetime < self.end_datetime) and (len(self.patients)) < 16:
            self.patients.append(patient)
        else:
            print(f"Dr {self.name} is no longer accepting patients. Try again on another day.")

    
    def remove_patient(self, patient):
        if patient in self.patients:
            self.patients.remove(patient)
        else:
            print("The patient was not seen by the Dr and will not be removed.")
    
    




# Scheduling program
doc1 = Doctor('Jenny April',datetime(2025,5,23,9,0,0))
#print(doc1)
doc2 = Doctor('Mark Dund',datetime(2025,5,23,9,0,0))
#print(doc2)


print("\nPatient 1")
#Patient arrives i.e create patient
patient1 = Patient("Mandy Johnson",datetime(2025,5,23,13,0,0))

#Patient sees Dr if arrival is before EOD and # of patients <= 16
doc1.add_patient(patient1)
print(doc1)
print(patient1)

#Patient leaves hospital
patient1.patient_leaving(datetime(2025,5,23,15,0,0))

#Remove patient from hospital
doc1.remove_patient(patient1)
print(doc1)


#Patient arrives outside of working hours
print("\nPatient 2")
patient2 = Patient("June Johnson",datetime(2025,5,23,20,0,0))
doc1.add_patient(patient2)

#Patient arrive within working hours but after 16 patients are in the hospital
print("\nPatients 3-19")
#Recall that Patient1 has left and patient2 wasnt added
patient3 = Patient("Patient3",datetime(2025,5,23,12,0,0))
doc1.add_patient(patient3)
patient4 = Patient("Patient4",datetime(2025,5,23,12,0,0))
doc1.add_patient(patient4)
patient5 = Patient("Patient5",datetime(2025,5,23,12,0,0))
doc1.add_patient(patient5)
patient6 = Patient("Patient6",datetime(2025,5,23,12,0,0))
doc1.add_patient(patient6)
patient7 = Patient("Patient7",datetime(2025,5,23,12,0,0))
doc1.add_patient(patient7)
patient8 = Patient("Patient8",datetime(2025,5,23,12,0,0))
doc1.add_patient(patient8)
patient9 = Patient("Patient9",datetime(2025,5,23,12,0,0))
doc1.add_patient(patient9)
patient10 = Patient("Patient10",datetime(2025,5,23,12,0,0))
doc1.add_patient(patient10)
patient11 = Patient("Patient11",datetime(2025,5,23,12,0,0))
doc1.add_patient(patient11)
patient12 = Patient("Patient12",datetime(2025,5,23,12,0,0))
doc1.add_patient(patient12)
patient13 = Patient("Patient13",datetime(2025,5,23,12,0,0))
doc1.add_patient(patient13)
patient14 = Patient("Patient14",datetime(2025,5,23,12,0,0))
doc1.add_patient(patient14)
patient15 = Patient("Patient15",datetime(2025,5,23,12,0,0))
doc1.add_patient(patient15)
patient16 = Patient("Patient16",datetime(2025,5,23,12,0,0))
doc1.add_patient(patient16)
patient17 = Patient("Patient17",datetime(2025,5,23,12,0,0))
doc1.add_patient(patient17)
patient18 = Patient("Patient18",datetime(2025,5,23,12,0,0))
doc1.add_patient(patient18)
patient19 = Patient("Patient19",datetime(2025,5,23,12,0,0))
doc1.add_patient(patient19) # won't be added as hospital is full


