# Patient Class 
class Patient:
    def __init__(self, name, Patient_ID, age, gender, diagnosis):
        self.name = name
        self.Patient_ID = Patient_ID
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis

    def display_info(self):
        print("\n**** Patient Information ****")
        print(f"Name: {self.name}")
        print(f"Patient ID: {self.Patient_ID}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Diagnosis: {self.diagnosis}")

# Hospital Class
class Hospital:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
        
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print("Patient added successfully")

    def display_patients(self):
        print("\n**** All Patients ****")
        print(f"\n**** Patients in {self.hospital_name} ****")

        # check if there are any patients
        if len(self.patients) == 0:
            print("No patients found.")
        else:
            for patient in self.patients:
                patient.display_info()
        

# Patient objects
patient1 = Patient("John Doe",101, 23, "Male", "Flu")
patient2 = Patient(" Jane Smith",102, 28, "Female", "Cold")
patient3 = Patient("Michael Johnson",103, 42, "Male", "Diabetes")

# Hospital object and communication between classes
hospital = Hospital("Donal d Clinic")
for patient in [patient1, patient2, patient3]:
    hospital.add_patient(patient)

hospital.display_patients()
