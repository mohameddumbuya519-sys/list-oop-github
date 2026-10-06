# Patient Class 
class Patient:
    def __init__(self, name, Patient_ID, age, gender, diagnosis):
        self.name = name
        self.Patient_ID = Patient_ID
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Patient ID: {self.Patient_ID}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Diagnosis: {self.diagnosis}")
