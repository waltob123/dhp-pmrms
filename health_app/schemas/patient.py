import re

from pydantic import field_validator, Field

from health_app.schemas.base_schemas import BaseReadSchema, BasePersonSchema
from health_app.utils.constants import Gender, DATE_FORMAT_PATTERN


class BasePatientSchema(BasePersonSchema):
    emergency_contact: str = Field(..., min_length=7)
    address: str = Field(..., min_length=2)
    gender: str
    date_of_birth: str

    @field_validator("gender")
    @classmethod
    def gender_id_valid(cls, value: str) -> str:
        """
        Validate that the given gender

        :param value: The value to validate
        :return: The validated value
        """
        if not Gender.__contains__(value.lower().strip()):
            raise ValueError(f"Gender must be either: {", ".join([gender.value for gender in Gender])}")
        return value.lower().strip()

    @field_validator("date_of_birth")
    @classmethod
    def date_is_valid_format(cls, value: str) -> str:
        """
        Validate that the given date is in the correct format.

        :param value: The date to validate
        :return: The validated date
        """
        if not re.match(DATE_FORMAT_PATTERN, value):
            raise ValueError("Invalid date format. Expected format: YYYY-MM-DD")
        return value


CreatePatientSchema = BasePatientSchema

UpdatePatientSchema = BasePatientSchema


class ReadPatientSchema(BaseReadSchema, BasePatientSchema):
    patient_number: str = Field(..., min_length=2)
    age: int = Field(..., ge=0)
