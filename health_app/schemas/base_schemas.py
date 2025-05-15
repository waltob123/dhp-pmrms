from typing import Optional

from pydantic import BaseModel, field_validator, Field

from health_app.utils.validators import is_valid_uuid


class BaseReadSchema(BaseModel):
    """
    Base schema for read operations.
    This schema is used to define the structure of the data returned by the API.
    """
    id: str
    created_at: str
    updated_at: Optional[str] = None

    @field_validator("id")
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

    class Config:
        """
        Pydantic configuration.
        """
        from_attributes = True


class BasePersonSchema(BaseModel):
    """
    Base schema for person-related operations.
    This schema is used to define the structure of the data related to a person.
    """
    first_name: str = Field(..., min_length=2)
    last_name: str = Field(..., min_length=2)
    other_names: Optional[str] = None
    contact: str = Field(..., min_length=7)
