from fastapi import FastAPI
from health_app.routers import patients, doctors, appointments, medical_records
from health_app.middleware.log_request_time import log_request_time
from health_app.schemas.patient import patient

app = FastAPI(title="Patient Medical Record Management System")
app.middleware("http")(log_request_time)

app.include_router(patients.router, prefix="/patients", tags=["Patients"])
app.include_router(doctors.router, prefix="/doctors", tags=["Doctors"])
app.include_router(appointments.router, prefix="/appointments", tags=["Appointments"])
app.include_router(medical_records.router, prefix="/medical_records", tags=["Medical Records"])
