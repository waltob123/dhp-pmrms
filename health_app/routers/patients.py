from fastapi import APIRouter, Depends, Query
from typing import List
from health_app.services.patient_service import PatientService
from health_app.schemas.patient_schema import PatientCreate, PatientUpdate, PatientOut

router = APIRouter()

@router.get("/", response_model=List[PatientOut])
def list_patients(page: int = 1, page_size: int = 10, name: str = None, service: PatientService = Depends()):
    return service.list_patients(page, page_size, name)

@router.post("/", response_model=PatientOut)
def create_patient(payload: PatientCreate, service: PatientService = Depends()):
    return service.create_patient(payload)

@router.get("/{patient_id}", response_model=PatientOut)
def get_patient(patient_id: str, service: PatientService = Depends()):
    return service.get_patient(patient_id)

@router.put("/{patient_id}", response_model=PatientOut)
def update_patient(patient_id: str, payload: PatientUpdate, service: PatientService = Depends()):
    return service.update_patient(patient_id, payload)

@router.delete("/{patient_id}")
def delete_patient(patient_id: str, service: PatientService = Depends()):
    return service.soft_delete_patient(patient_id)

