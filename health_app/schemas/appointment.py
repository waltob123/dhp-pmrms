import re

from pydantic import field_validator, BaseModel

from health_app.schemas.base_schemas import BaseReadSchema
from health_app.utils.constants import DATE_FORMAT_PATTERN, Appointment
from health_app.utils.validators import is_valid_uuid


class BaseAppointmentSchema(BaseModel):
    doctor_id: str
    appointment_date: str
    status: str

    @field_validator("doctor_id")
    @classmethod
    def is_valid_uuid(cls, value: str) -> str:
        """
        Validate that the given id is a valid UUID.

        :param value: The id to validate
        :return: The validated id
        """
        if is_valid_uuid(uuid_to_test=value):
            return value
        raise ValueError("Invalid id format.")

    @field_validator("appointment_date")
    @classmethod
    def date_is_valid_format(cls, value: str) -> str:
        """
        Validate that the given date is in the correct format.

        :param value: The date to validate
        :return: The validated date
        """
        if not re.match(DATE_FORMAT_PATTERN, value):
            raise ValueError("Invalid date format. Expected format: YYYY-MM-DD HH:MM:SS")
        return value

    @field_validator("status")
    @classmethod
    def status_is_valid(cls, value: str) -> str:
        """
        Validate that the given status is valid.

        :param value: The status to validate
        :return: The validated status
        """
        if not Appointment.__contains__(value.lower().strip()):
            raise ValueError(f"Invalid status. Expected one of: {", ".join([status.value for status in Appointment])}")
        return value


class CreateAppointmentSchema(BaseAppointmentSchema):
    """
    Schema for creating an appointment.
    """
    patient_id: str

    @field_validator("patient_id")
    @classmethod
    def is_valid_uuid(cls, value: str) -> str:
        """
        Validate that the given id is a valid UUID.

        :param value: The id to validate
        :return: The validated id
        """
        if is_valid_uuid(uuid_to_test=value):
            return value
        raise ValueError("Invalid id format.")


UpdateAppointmentSchema = BaseAppointmentSchema


class ReadAppointmentSchema(BaseReadSchema, BaseAppointmentSchema):
    pass
