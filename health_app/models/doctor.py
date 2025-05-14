from typing import Optional

from health_app.models.base_model import BaseModel


class Doctor(BaseModel):
    """
    Doctor class representing a doctor in the health application.

    (BaseModel) This class inherits from the BaseModel class and adds additional
    """

    def __init__(
        self,
        *,
        first_name: str,
        last_name: str,
        other_names: Optional[str]=None,
        specialty: Optional[str]=None,
        years_of_experience: int,
        contact: str,
        id: Optional[str]=None,
        date_created: Optional[str]=None,
        date_updated: Optional[str]=None,
        date_deleted: Optional[str]=None
    ) -> None:
        """
        Doctor constructor.

        :param first_name: The first name of the doctor.
        :param last_name: The last name of the doctor.
        :param other_names: Other names of the doctor.
        :param specialty: The specialty of the doctor.
        :param years_of_experience: The years of experience of the doctor.
        :param contact: The contact information of the doctor.
        :param id: The unique identifier for the doctor instance.
        :param date_created: The date and time when the doctor instance was created.
        :param date_updated: The date and time when the doctor instance was last updated.
        :param date_deleted: The date and time when the doctor instance was deleted.
        """
        super().__init__(
            id=id,
            date_created=date_created,
            date_updated=date_updated,
            date_deleted=date_deleted
        )
        self.__first_name = first_name
        self.__last_name = last_name
        self.__other_names = other_names
        self.__specialty = specialty
        self.__years_of_experience = years_of_experience
        self.__contact = contact

    @property
    def first_name(self) -> str:
        """Get the first name of the doctor."""
        return self.__first_name

    @property
    def last_name(self) -> str:
        """Get the last name of the doctor."""
        return self.__last_name

    @property
    def other_names(self) -> Optional[str]:
        """Get the other names of the doctor."""
        return self.__other_names

    @property
    def specialty(self) -> Optional[str]:
        """Get the specialty of the doctor."""
        return self.__specialty

    @property
    def years_of_experience(self) -> int:
        """Get the years_of_experience of the doctor."""
        return self.__years_of_experience

    @property
    def contact(self) -> str:
        """Get the contact information of the doctor."""
        return self.__contact

    @first_name.setter
    def first_name(self, value: str) -> None:
        """Set the first name of the doctor."""
        self.__first_name = value

    @last_name.setter
    def last_name(self, value: str ) -> None:
        """Set the last name of the doctor."""
        self.__last_name = value

    @other_names.setter
    def other_names(self, value: Optional[str]) -> None:
        """Set the other names of the doctor."""
        self.__other_names = value

    @specialty.setter
    def specialty(self, value: Optional[str]) -> None:
        """Set the specialty of the doctor."""
        self.__specialty = value

    @years_of_experience.setter
    def years_of_experience(self, value: int) -> None:
        """Set the gender of the doctor."""
        self.__years_of_experience = value

    @contact.setter
    def contact(self, value: str) -> None:
        """Set the contact information of the doctor."""
        self.__contact = value

    def to_dict(self) -> dict:
        """
        Convert the Patient instance to a dictionary.

        :return: The dictionary representation of the Patient instance.
        """
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "other_names": self.other_names,
            "specialty": self.specialty,
            "years_of_experience": self.years_of_experience,
            "contact": self.contact,
            "date_created": self._convert_to_string(date=self.date_created),
            "date_updated": self._convert_to_string(date=self.date_updated),
            "date_deleted": self._convert_to_string(date=self.date_deleted)
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Doctor":
        """
        Create a Doctor instance from a dictionary.

        :param data: The dictionary containing the doctor data.
        :return: A Doctor instance.
        """
        return cls(
            id=data.get("id"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            other_names=data.get("other_names"),
            specialty=data.get("specialty"),
            years_of_experience=data.get("years_of_experience"),
            contact=data.get("contact"),
            date_created=data.get("date_created"),
            date_updated=data.get("date_updated"),
            date_deleted=data.get("date_deleted")
        )
