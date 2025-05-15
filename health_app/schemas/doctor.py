from pydantic import BaseModel, Field

from health_app.schemas.base_schemas import BaseReadSchema


class BaseDoctorSchema(BaseModel):
    """
    Base schema for doctor-related operations.
    """
    specialty: str = Field(..., min_length=2)
    years_of_experience: int = Field(..., ge=0)


CreateDoctorSchema = BaseDoctorSchema

UpdateDoctorSchema = BaseDoctorSchema

class ReadDoctorSchema(BaseReadSchema, BaseDoctorSchema):
    pass
