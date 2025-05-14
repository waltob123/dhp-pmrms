import re
import uuid
from abc import abstractmethod
from datetime import datetime, timezone
from typing import Optional

from health_app.utils.exceptions import InvalidDateFormatException


class BaseModel:
    """BaseModel class for all models in the application."""

    _DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
    _DATE_STRING_PATTERN = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$"

    def __init__(
        self,
        *,
        id: Optional[str]=None,
        date_created: Optional[str]=None,
        date_updated: Optional[str]=None,
        date_deleted: Optional[str]=None,
    ) -> None:
        """
        BaseModel constructor.

        :param id: The unique identifier for the model instance.
        :param date_created: The date and time when the model instance was created.
        :param date_updated: The date and time when the model instance was last updated.
        :param date_deleted: The date and time when the model instance was deleted.
        """
        self.__id = self.__set_id(id=id)
        self.__date_created = self.__set_date_created(date_created=date_created)
        self.__date_updated = self._set_date(date=date_updated)
        self.__date_deleted = self._set_date(date=date_deleted)

    @property
    def id(self) -> str:
        """Get the unique identifier for the model instance."""
        return self.__id

    @property
    def date_created(self) -> datetime:
        """Get the date and time when the model instance was created."""
        return self.__date_created

    @property
    def date_updated(self) -> datetime:
        """Get the date and time when the model instance was last updated."""
        return self.__date_updated

    @property
    def date_deleted(self) -> datetime:
        """Get the date and time the model instance was last updated."""
        return self.__date_deleted

    @id.setter
    def id(self, value: str) -> None:
        """Set the unique identifier for the model instance."""
        raise AttributeError("Cannot set attribute")

    @date_created.setter
    def date_created(self, value) -> None:
        """Set the date and time when the model instance was created."""
        raise AttributeError("Cannot set attribute")

    @date_updated.setter
    def date_updated(self, value: datetime) -> None:
        """Set the date and time when the model instance was last updated."""
        self.__date_updated = value

    @date_deleted.setter
    def date_deleted(self, value: datetime) -> None:
        """Set the date and time when the model instance was deleted."""
        self.__date_deleted = value

    def soft_delete(self):
        """
        Soft delete the model instance by setting the date_deleted attribute to the current date and time.
        """
        self.date_deleted = self._get_current_datetime()
        return self

    def restore(self):
        """
        Restore the model instance by setting the date_deleted attribute to None.
        """
        self.date_deleted = None
        return self

    def __set_id(self, *, id: Optional[str]=None) -> str:
        """
        Set the unique identifier for the model instance.

        :param id: The unique identifier for the model instance.
        :return: The unique identifier for the model instance.
        """
        if id is None:
            return self.__generate_id()
        return id

    def __set_date_created(self, *, date_created: Optional[str]) -> datetime:
        """
        Set the date and time when the model instance was created.

        :param date_created: The date and time when the model instance was created.
        :return: The date and time when the model instance was created.
        """
        if date_created:
            return self._convert_to_datetime(date_string=date_created)
        return self._get_current_datetime()

    def _set_date(self, *, date: Optional[str]) -> Optional[datetime]:
        """
        Set the date and time.

        :param date: The date and time.
        :return: The date and time.
        """
        if date:
            return self._convert_to_datetime(date_string=date)
        return None

    @staticmethod
    def __generate_id() -> str:
        """
        Generate a unique identifier for the model instance.

        :return: A unique identifier for the model instance.
        """
        return str(uuid.uuid4())

    @staticmethod
    def _convert_to_datetime(*, date_string: str) -> datetime:
        """
        Convert a date string to a timestamp.

        :param date_string: The date string to convert.
        :return: The timestamp.
        """
        if not re.match(BaseModel._DATE_STRING_PATTERN, date_string):
            raise InvalidDateFormatException(
                f"Invalid date format: {date_string}. Expected format: {BaseModel._DATE_FORMAT}"
            )

        return datetime.strptime(date_string, BaseModel._DATE_FORMAT)

    @staticmethod
    def _convert_to_string(*, date: datetime) -> str:
        """
        Convert a timestamp to a date string.

        :param date: The timestamp to convert.
        :return: The date string.
        """
        return datetime.strftime(date, BaseModel._DATE_FORMAT) if date else None

    @staticmethod
    def _get_current_datetime() -> datetime:
        """
        Get the current date and time.

        :return: The current date and time.
        """
        return datetime.now(tz=timezone.utc)

    @abstractmethod
    def to_dict(self) -> dict:
        """
        Convert the model instance to a dictionary.

        :return: A dictionary representation of the model instance.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def __str__(self) -> str:
        """
        Return a string representation of the model instance.

        :return: A string representation of the model instance.
        """
        return f"<{self.__class__.__name__} {self.id}>"
