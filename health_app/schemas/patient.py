from pydantic import BaseModel
from typing import Optional

class PatientCreate(BaseModel):
    full_name: str
    age: int
    gender: str
    contact_info: str
    address: str
    emergency_contact: str

class PatientUpdate(BaseModel):
    full_name: Optional[str]
    age: Optional[int]
    gender: Optional[str]
    contact_info: Optional[str]
    address: Optional[str]
    emergency_contact: Optional[str]

class PatientOut(PatientCreate):
    id: str
    date_created: str
    date_updated: str
    date_deleted: Optional[str]

