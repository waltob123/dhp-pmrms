from fastapi import HTTPException
from health_app.repositories.patient_repository import PatientRepository
from health_app.schemas.patient_schema import PatientCreate, PatientUpdate

class PatientService:
    def __init__(self):
        self.repo = PatientRepository()

    def list_patients(self, page, page_size, name=None):
        all_patients = [p for p in self.repo.list() if not p.get("date_deleted")]
        if name:
            all_patients = [p for p in all_patients if name.lower() in p["full_name"].lower()]
        start = (page - 1) * page_size
        return all_patients[start:start+page_size]

    def create_patient(self, payload: PatientCreate):
        return self.repo.create(payload.dict())

    def get_patient(self, patient_id):
        patient = self.repo.get(patient_id)
        if not patient:
            raise HTTPException(status_code=404, detail="Patient not found")
        return patient

    def update_patient(self, patient_id, payload: PatientUpdate):
        updated = self.repo.update(patient_id, payload.dict(exclude_unset=True))
        if not updated:
            raise HTTPException(status_code=404, detail="Patient not found")
        return updated

    def soft_delete_patient(self, patient_id):
        if not self.repo.soft_delete(patient_id):
            raise HTTPException(status_code=404, detail="Patient not found")
        return {"message": "Patient deleted"}

