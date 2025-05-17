from typing import Optional, Union, List, Any

from fastapi.responses import JSONResponse
from pydantic import BaseModel, field_validator, Field

from health_app.schemas.base_schemas import BaseReadSchema


class ResponseSchema(BaseModel):
    """Schema for error responses."""
    status: str
    status_code: int = Field(..., ge=100, le=599)
    message: str = Field(..., min_length=1)
    data: Optional[Union[List[Any], Any]]= None
    extras: Optional[dict] = None

    @field_validator("status")
    @classmethod
    def validate_status(cls, value: str) -> str:
        """
        Validate that the status is either 'success' or 'error'.
        """
        if value not in ['success', 'error']:
            raise ValueError("Status must be either 'success' or 'error'.")
        return value


    def to_json_response(self) -> JSONResponse:
        """
        Convert the schema to a JSON response.
        """
        return JSONResponse(
            status_code=self.status_code,
            content={
                "status": self.status,
                "status_code": self.status_code,
                "message": self.message,
                "data": self.data,
                "extras": self.extras
            }
        )
