import os
from pathlib import Path
from enum import Enum

BASE_DIR = Path(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
APP_DIR = Path(os.path.join(BASE_DIR, "health_app"))
DATA_DIR = Path(os.path.join(APP_DIR, "data"))

BASE_FILTERS = ["first_name", "last_name", "contact"]

ALLOWED_PATIENT_FILTERS = ["patient_number"].extend(BASE_FILTERS)
ALLOWED_DOCTOR_FILTERS = ["specialty"].extend(BASE_FILTERS)
ALLOWED_APPOINTMENT_FILTERS = ["doctor_id", "patient_id", "appointment_date", "status"]
ALLOWED_MEDICAL_RECORD_FILTERS = ["patient_id"]

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT_PATTERN = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$"

PAGE = 1
PAGE_SIZE = 10


class Gender(Enum):
    """
    Enum for gender.
    """
    MALE = "male"
    FEMALE = "female"


class Appointment(Enum):
    """
    Enum for appointment status.
    """
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class HTTPResponseStatus(Enum):
    """
    Enum for HTTP response status.
    """
    SUCCESS = "success"
    ERROR = "error"
