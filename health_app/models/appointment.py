from datetime import datetime
from typing import Optional

from health_app.models.base_model import BaseModel


class Appointment(BaseModel):
    """
    Appointment class representing an appointment in the health application.

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
        doctor_id: str,
        appointment_date: str,
        status: str,
    ) -> None:
        """
        Appointment constructor.

        :param id: The unique identifier for the appointment.
        :param date_created: The date and time when the appointment was created.
        :param date_updated: The date and time when the appointment was last updated.
        :param date_deleted: The date and time when the appointment was deleted.
        :param patient_id: The unique identifier for the patient associated with the appointment.
        :param doctor_id: The unique identifier for the doctor associated with the appointment.
        :param appointment_date: The date and time of the appointment.
        :param status: The status of the appointment (e.g., "scheduled", "completed", "canceled").
        """
        super().__init__(
            id=id,
            date_created=date_created,
            date_updated=date_updated,
            date_deleted=date_deleted,
        )
        self.__patient_id = patient_id
        self.__doctor_id = doctor_id
        self.__appointment_date = self._set_date(date=appointment_date)
        self.__status = status

    @property
    def patient_id(self) -> str:
        """Get the unique identifier for the patient associated with the appointment."""
        return self.__patient_id

    @property
    def doctor_id(self) -> str:
        """Get the unique identifier for the doctor associated with the appointment."""
        return self.__doctor_id

    @property
    def appointment_date(self) -> datetime:
        """Get the date and time of the appointment."""
        return self.__appointment_date

    @property
    def status(self) -> str:
        """Get the status of the appointment."""
        return self.__status

    @patient_id.setter
    def patient_id(self, value: str) -> None:
        """Set the unique identifier for the patient associated with the appointment."""
        raise AttributeError("Cannot set attribute")

    @doctor_id.setter
    def doctor_id(self, value: str) -> None:
        """Set the unique identifier for the doctor associated with the appointment."""
        self.__doctor_id = value

    @appointment_date.setter
    def appointment_date(self, value: str) -> None:
        """Set the date and time of the appointment."""
        self.__appointment_date = self.__set_date(date=value)

    @status.setter
    def status(self, value: str) -> None:
        """Set the status of the appointment."""
        self.__status = value

    def to_dict(self) -> dict:
        """
        Convert the appointment object to a dictionary.

        :return: The dictionary representation of the appointment object.
        """
        return {
            "id": self.id,
            "patient_id": self.patient_id,
            "doctor_id": self.doctor_id,
            "appointment_date": self._convert_to_string(date=self.appointment_date),
            "status": self.status,
            "date_created": self._convert_to_string(date=self.date_created),
            "date_updated": self._convert_to_string(date=self.date_updated),
            "date_deleted": self._convert_to_string(date=self.date_deleted)
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Appointment":
        """
        Create an Appointment instance from a dictionary.

        :param data: The dictionary containing appointment data.
        :return: An Appointment instance.
        """
        return cls(
            id=data.get("id"),
            date_created=data.get("date_created"),
            date_updated=data.get("date_updated"),
            date_deleted=data.get("date_deleted"),
            patient_id=data.get("patient_id"),
            doctor_id=data.get("doctor_id"),
            appointment_date=data.get("appointment_date"),
            status=data.get("status")
        )
