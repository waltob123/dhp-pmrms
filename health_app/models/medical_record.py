from datetime import datetime
from typing import Optional

from health_app.models.base_model import BaseModel


class MedicalRecord(BaseModel):
    """
    MedicalRecord class represents a medical record in the health application.

    (BaseModel) This class inherits from the BaseModel class and adds additional
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        date_created: Optional[str] = None,
        date_updated: Optional[str] = None,
        date_deleted: Optional[str] = None,
        patient_id: str,
        recorded_by: str,
        diagnosis: list[str],
        prescriptions: list[str],
        treatment_date: str,
        doctor_notes: str
    ) -> None:
        """
        MedicalRecord constructor.

        :param id: The unique identifier for the medical record.
        :param date_created: The date and time when the medical record was created.
        :param date_updated: The date and time when the medical record was last updated.
        :param date_deleted: The date and time when the medical record was deleted.
        :param patient_id: The unique identifier for the patient associated with the medical record.
        :param recorded_by: The unique identifier for the doctor who recorded the medical record.
        :param diagnosis: A list of diagnoses associated with the medical record.
        :param prescriptions: A list of prescriptions associated with the medical record.
        :param treatment_date: The date and time of the treatment.
        :param doctor_notes: Additional notes from the doctor regarding the medical record.
        """
        super().__init__(
            id=id,
            date_created=date_created,
            date_updated=date_updated,
            date_deleted=date_deleted,
        )
        self.__patient_id = patient_id
        self.__recorded_by = recorded_by
        self.__diagnosis = diagnosis
        self.__prescriptions = prescriptions
        self.__treatment_date = self._set_date(date=treatment_date)
        self.__doctor_notes = doctor_notes

    @property
    def patient_id(self) -> str:
        """Get the unique identifier for the patient associated with the medical record."""
        return self.__patient_id

    @property
    def recorded_by(self) -> str:
        """Get the unique identifier for the doctor who recorded the medical record."""
        return self.__recorded_by

    @property
    def diagnosis(self) -> list[str]:
        """Get the list of diagnoses associated with the medical record."""
        return self.__diagnosis

    @property
    def prescriptions(self) -> list[str]:
        """Get the list of prescriptions associated with the medical record."""
        return self.__prescriptions

    @property
    def treatment_date(self) -> datetime:
        """Get the date and time of the treatment."""
        return self.__treatment_date

    @property
    def doctor_notes(self) -> str:
        """Get additional notes from the doctor regarding the medical record."""
        return self.__doctor_notes

    @patient_id.setter
    def patient_id(self, value: str) -> None:
        """Set the unique identifier for the patient associated with the medical record."""
        raise AttributeError("patient_id is read-only and cannot be modified.")

    @recorded_by.setter
    def recorded_by(self, value: str) -> None:
        """Set the unique identifier for the doctor who recorded the medical record."""
        raise AttributeError("recorded_by is read-only and cannot be modified.")

    @diagnosis.setter
    def diagnosis(self, value: list[str]) -> None:
        """Set the list of diagnoses associated with the medical record."""
        self.__diagnosis = value

    @prescriptions.setter
    def prescriptions(self, value: list[str]) -> None:
        """Set the list of prescriptions associated with the medical record."""
        self.__prescriptions = value

    @treatment_date.setter
    def treatment_date(self, value: str) -> None:
        """Set the date and time of the treatment."""
        self.__treatment_date = self._set_date(date=value)

    @doctor_notes.setter
    def doctor_notes(self, value: str) -> None:
        """Set additional notes from the doctor regarding the medical record."""
        self.__doctor_notes = value

    def to_dict(self) -> dict:
        """
        Convert the medical record object to a dictionary.

        :return: The dictionary representation of the medical record object.
        """
        return {
            "id": self.id,
            "patient_id": self.patient_id,
            "recorded_by": self.recorded_by,
            "diagnosis": self.diagnosis,
            "prescriptions": self.prescriptions,
            "treatment_date": self._convert_to_string(date=self.treatment_date),
            "doctor_notes": self.doctor_notes,
            "date_created": self._convert_to_string(date=self.date_created),
            "date_updated": self._convert_to_string(date=self.date_updated),
            "date_deleted": self._convert_to_string(date=self.date_deleted)
        }

    @classmethod
    def from_dict(cls, data: dict) -> "MedicalRecord":
        """
        Create a MedicalRecord object from a dictionary.

        :param data: The dictionary containing the medical record data.
        :return: A MedicalRecord object.
        """
        return cls(
            id=data.get("id"),
            date_created=data.get("date_created"),
            date_updated=data.get("date_updated"),
            date_deleted=data.get("date_deleted"),
            patient_id=data.get("patient_id"),
            recorded_by=data.get("recorded_by"),
            diagnosis=data.get("diagnosis"),
            prescriptions=data.get("prescriptions"),
            treatment_date=data.get("treatment_date"),
            doctor_notes=data.get("doctor_notes")
        )
