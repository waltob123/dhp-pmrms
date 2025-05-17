import os
from pathlib import Path
from enum import Enum

BASE_DIR = Path(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
APP_DIR = Path(os.path.join(BASE_DIR, "health_app"))
DATA_DIR = Path(os.path.join(APP_DIR, "data"))

BASE_FILTERS = ["is_deleted"]
BASE_PATIENT_DOCTOR_FILTERS_AND_SORT = BASE_FILTERS.copy() + ["first_name", "last_name", "contact"]

ALLOWED_PATIENT_FILTERS = ["patient_number"] + BASE_PATIENT_DOCTOR_FILTERS_AND_SORT
ALLOWED_DOCTOR_FILTERS = ["specialty"] + BASE_PATIENT_DOCTOR_FILTERS_AND_SORT
ALLOWED_APPOINTMENT_FILTERS = ["doctor_id", "patient_id", "appointment_date", "status"]
ALLOWED_MEDICAL_RECORD_FILTERS = ["patient_id"]

ALLOWED_PATIENT_SORT = ALLOWED_PATIENT_FILTERS.copy()

DATE_FORMAT_WITH_TIME = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT_WITHOUT_TIME = "%Y-%m-%d"
DATE_FORMAT_PATTERN = r"^\d{4}-\d{2}-\d{2}( \d{2}:\d{2}:\d{2})?$"

PAGE = 1
PAGE_SIZE = 10

API_VERSION_1 = "/api/v1"


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
