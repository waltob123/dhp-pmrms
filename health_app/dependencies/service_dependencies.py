from health_app.factories.service_factories import PatientServiceFactory
from health_app.services.patient_service import PatientService
from health_app.utils.constants import ALLOWED_PATIENT_FILTERS, DATA_DIR, ALLOWED_PATIENT_SORT
from health_app.utils.json_file_manager import JSONFileManager


def get_patient_service() -> PatientService:
    """
    Dependency function to get the PatientService instance.

    :return: An instance of the PatientService.
    """
    patients_file_manager = JSONFileManager(
        file_path=DATA_DIR / "patients.json",
    )
    return PatientServiceFactory.create_patient_service(
        db_connection=patients_file_manager,
        allowed_filters=ALLOWED_PATIENT_FILTERS,
        allowed_sort=ALLOWED_PATIENT_SORT
    )
