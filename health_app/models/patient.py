from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Patient(BaseModel):
    id: str
    full_name: str
    age: int
    gender: str
    contact_info: str
    address: str
    emergency_contact: str
    date_created: str
    date_updated: str
    date_deleted: Optional[str] = None

