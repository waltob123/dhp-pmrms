from health_app.repositories.patient_repository import PatientRepository
from health_app.services.patient_service import PatientService
from health_app.utils.file_manager import FileManager


class PatientServiceFactory:
    @staticmethod
    def create_patient_service(
        db_connection: FileManager,
        allowed_filters: list[str],
        allowed_sort: list[str]
    ) -> PatientService:
        """
        Creates an instance of the PatientService with the given database connection.

        :param db_connection: The database connection object.
        :param allowed_filters: The list of allowed filters for the service.
        :param allowed_sort: The list of allowed sorting options for the service.
        :return: An instance of the PatientService.
        """
        patient_repository = PatientRepository(
            db_connection=db_connection, allowed_filters=allowed_filters, allowed_sort=allowed_sort
        )
        return PatientService(patient_repository=patient_repository)
