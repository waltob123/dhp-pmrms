from health_app.models.appointment import Appointment
from health_app.models.doctor import Doctor
from health_app.models.medical_record import MedicalRecord
from health_app.models.patient import Patient
from health_app.schemas.appointment import CreateAppointmentSchema
from health_app.utils.constants import DATA_DIR
from health_app.utils.json_file_manager import JSONFileManager


patient = Patient(
    first_name="John",
    last_name="Doe",
    gender="male",
    contact="1234567890",
    address="123 Main St",
    emergency_contact="0987654321",
)
#
doctor = Doctor(
    first_name="Abraham",
    last_name="Lincoln",
    years_of_experience=23,
    contact="1234568903"
)


print(patient.to_dict())
print(doctor.to_dict())
print()

b = Patient.from_dict(data=patient.to_dict())
print(b.first_name)
print(b.to_dict())

appointment = Appointment(
    patient_id=patient.id,
    doctor_id=doctor.id,
    appointment_date="2023-10-01 10:00:00",
    status="scheduled",
)

medical_record = MedicalRecord(
    patient_id=patient.id,
    recorded_by=doctor.id,
    diagnosis=["Flu"],
    prescriptions=["Paracetamol"],
    treatment_date="2023-10-01 10:00:00",
    doctor_notes="Patient is recovering well.",
)

file_manager = JSONFileManager(file_path=DATA_DIR / "appointments.json")
file_manager.write_file(content=[appointment.to_dict()])
a = file_manager.read_file()
print(a)

print(appointment.to_dict())
print(appointment.appointment_date)
print()
print(medical_record.to_dict())
print(medical_record.treatment_date)

a = CreateAppointmentSchema(
    doctor_id=doctor.id,
    appointment_date="2023-10-01 10:00:00",
    status="scheduled",
    patient_id=patient.id
)

print(a)
