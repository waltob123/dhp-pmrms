from fastapi import APIRouter, Depends, Query, BackgroundTasks
from typing import List
from health_app.services.patient_service import PatientService
from health_app.schemas.patient_schema import PatientCreate, PatientUpdate, PatientOut
from health_app.utils.email_utils import send_email_async

router = APIRouter()

@router.get("/", response_model=List[PatientOut])
def list_patients(
    page: int = 1, page_size: int = 10, name: str = None, service: PatientService = Depends()
):
    """Return a paginated list of patients."""
    return service.list_patients(page, page_size, name)

@router.post("/", response_model=PatientOut)
async def create_patient(
    payload: PatientCreate,
    background_tasks: BackgroundTasks,
    service: PatientService = Depends()
):
    """Create a patient and send notification email."""
    patient = service.create_patient(payload)
    background_tasks.add_task(
        send_email_async,
        subject="New Patient Created",
        email_to=["wilsondey1@live.com"],
        body=f"Patient {patient['full_name']} has been created."
    )
    return patient

@router.get("/{patient_id}", response_model=PatientOut)
def get_patient(patient_id: str, service: PatientService = Depends()):
    """Get details of a specific patient."""
    return service.get_patient(patient_id)

@router.put("/{patient_id}", response_model=PatientOut)
def update_patient(
    patient_id: str,
    payload: PatientUpdate,
    service: PatientService = Depends()
):
    """Update patient details."""
    return service.update_patient(patient_id, payload)

@router.delete("/{patient_id}")
def delete_patient(patient_id: str, service: PatientService = Depends()):
    """Soft delete a patient."""
    return service.soft_delete_patient(patient_id)

@router.post("/{patient_id}/restore")
def restore_patient(patient_id: str, service: PatientService = Depends()):
    """Restore a previously deleted patient."""
    return service.restore_patient(patient_id)
