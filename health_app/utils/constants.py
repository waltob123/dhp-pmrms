import os
from pathlib import Path
from enum import Enum

BASE_DIR = Path(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
APP_DIR = Path(os.path.join(BASE_DIR, "health_app"))
DATA_DIR = Path(os.path.join(APP_DIR, "data"))


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
