from fastapi import HTTPException, Request, status

from health_app.models.patient import Patient
from health_app.repositories.patient_repository import PatientRepository
from health_app.schemas.patient import CreatePatientSchema, UpdatePatientSchema
from health_app.services.base_service import BaseService
from health_app.utils.exceptions import EntityDoesNotExistException, FailedToSaveObjectException


class PatientService(BaseService):
    """
    This class handles the logic for managing patient data.
    """

    def __init__(
        self,
        patient_repository: PatientRepository
    ) -> None:
        """
        Initializes the PatientService with the given repositories.

        :param patient_repository: The repository for managing patient data.
        """
        self.__patient_repository = patient_repository
        super().__init__(repository=self.__patient_repository)

    def create(self, patient: CreatePatientSchema) -> Patient:
        """
        Creates a new patient.

        :param patient: The patient data to create.
        :return: The created patient.
        """
        try:
            return self.__patient_repository.create(data=patient, model=Patient)
        except FailedToSaveObjectException as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
