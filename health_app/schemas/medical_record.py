import re

from pydantic import BaseModel, field_validator, Field

from health_app.schemas.base_schemas import BaseReadSchema
from health_app.utils.constants import DATE_FORMAT_PATTERN
from health_app.utils.validators import is_valid_uuid


class BaseMedicalRecord(BaseModel):
    """
    This is the base schema for medical records.
    """
    diagnosis: list[str]
    prescriptions: list[str]
    treatment_date: str
    doctor_notes: str = Field(..., min_length=2)

    @field_validator("diagnosis", "prescriptions")
    @classmethod
    def validate_diagnosis(cls, value: list[str]) -> list[str]:
        """
        Validate that the diagnosis is a non-empty list of strings.
        """
        if not isinstance(value, list) or not all(isinstance(item, str) and len(item) > 2 for item in value):
            raise ValueError("Diagnosis must be a non-empty list of strings.")
        return value

    @field_validator("treatment_date")
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


class CreateMedicalRecordSchema(BaseMedicalRecord):
    patient_id: str
    recorded_by: str

    @field_validator("patient_id", "recorded_by")
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


UpdateMedicalRecordSchema = BaseMedicalRecord


class ReadMedicalRecordSchema(BaseReadSchema, BaseMedicalRecord, CreateMedicalRecordSchema):
    pass
