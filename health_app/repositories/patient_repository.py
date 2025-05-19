from health_app.utils.file_manager import FileManager
import uuid
from datetime import datetime

class PatientRepository:
    def __init__(self):
        self.file_manager = FileManager("health_app/data/patients.json")

    def list(self):
        return self.file_manager.read_data()

    def get(self, patient_id):
        return next((p for p in self.list() if p["id"] == patient_id and not p.get("date_deleted")), None)

    def create(self, data):
        data["id"] = str(uuid.uuid4())
        now = datetime.utcnow().isoformat()
        data["date_created"] = data["date_updated"] = now
        data["date_deleted"] = None
        patients = self.list()
        patients.append(data)
        self.file_manager.write_data(patients)
        return data

    def update(self, patient_id, updates):
        patients = self.list()
        for patient in patients:
            if patient["id"] == patient_id and not patient.get("date_deleted"):
                patient.update(updates)
                patient["date_updated"] = datetime.utcnow().isoformat()
                self.file_manager.write_data(patients)
                return patient
        return None

    def soft_delete(self, patient_id):
        patients = self.list()
        for patient in patients:
            if patient["id"] == patient_id:
                patient["date_deleted"] = datetime.utcnow().isoformat()
                self.file_manager.write_data(patients)
                return True
        return False

