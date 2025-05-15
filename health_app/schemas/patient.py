from typing import Optional

from pydantic import BaseModel, field_validator, Field

from health_app.schemas.base_schemas import BaseReadSchema, BasePersonSchema
from health_app.utils.constants import Gender


class BasePatientSchema(BasePersonSchema):
    emergency_contact: str = Field(..., min_length=7)
    address: str = Field(..., min_length=2)
    gender: str
    age: int = Field(..., ge=0)

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


CreatePatientSchema = BasePatientSchema

UpdatePatientSchema = BasePatientSchema


class ReadPatientSchema(BaseReadSchema, BasePatientSchema):
    patient_number: str = Field(..., min_length=2)
