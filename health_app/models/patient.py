from typing import Optional

from health_app.models.base_model import BaseModel


class Patient(BaseModel):
    """
    Patient class representing a patient in the health application.

    (BaseModel) This class inherits from the BaseModel class and adds additional
    """

    def __init__(
        self,
        *,
        first_name: str,
        last_name: str,
        other_names: Optional[str]=None,
        gender: str,
        contact: str,
        address: str,
        emergency_contact: str,
        id: Optional[str]=None,
        date_created: Optional[str]=None,
        date_updated: Optional[str]=None,
        date_deleted: Optional[str]=None
    ) -> None:
        """
        Patient constructor.

        :param first_name: The first name of the patient.
        :param last_name: The last name of the patient.
        :param other_names: Other names of the patient.
        :param gender: The gender of the patient.
        :param contact: The contact information of the patient.
        :param address: The address of the patient.
        :param emergency_contact: The emergency contact information of the patient.
        :param id: The unique identifier for the patient instance.
        :param date_created: The date and time when the patient instance was created.
        :param date_updated: The date and time when the patient instance was last updated.
        :param date_deleted: The date and time when the patient instance was deleted.
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
        self.__gender = gender
        self.__contact = contact
        self.__address = address
        self.__emergency_contact = emergency_contact

    @property
    def first_name(self) -> str:
        """Get the first name of the patient."""
        return self.__first_name

    @property
    def last_name(self) -> str:
        """Get the last name of the patient."""
        return self.__last_name

    @property
    def other_names(self) -> Optional[str]:
        """Get the other names of the patient."""
        return self.__other_names

    @property
    def gender(self) -> str:
        """Get the gender of the patient."""
        return self.__gender

    @property
    def contact(self) -> str:
        """Get the contact information of the patient."""
        return self.__contact

    @property
    def address(self) -> str:
        """Get the address of the patient."""
        return self.__address

    @property
    def emergency_contact(self) -> str:
        """Get the emergency contact information of the patient."""
        return self.__emergency_contact

    @first_name.setter
    def first_name(self, value: str) -> None:
        """Set the first name of the patient."""
        self.__first_name = value

    @last_name.setter
    def last_name(self, value: str ) -> None:
        """Set the last name of the patient."""
        self.__last_name = value

    @other_names.setter
    def other_names(self, value: Optional[str]) -> None:
        """Set the other names of the patient."""
        self.__other_names = value

    @gender.setter
    def gender(self, value: str) -> None:
        """Set the gender of the patient."""
        self.__gender = value

    @contact.setter
    def contact(self, value: str) -> None:
        """Set the contact information of the patient."""
        self.__contact = value

    @address.setter
    def address(self, value: str) -> None:
        """Set the address of the patient."""
        self.__address = value

    @emergency_contact.setter
    def emergency_contact(self, value: str) -> None:
        """Set the emergency contact information of the patient."""
        self.__emergency_contact = value

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
            "gender": self.gender,
            "contact": self.contact,
            "address": self.address,
            "emergency_contact": self.emergency_contact,
            "date_created": self._convert_to_string(date=self.date_created),
            "date_updated": self._convert_to_string(date=self.date_updated),
            "date_deleted": self._convert_to_string(date=self.date_deleted)
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Patient":
        """
        Create a Patient instance from a dictionary.

        :param data: The dictionary containing patient data.
        :return: A Patient instance.
        """
        return cls(
            id=data.get("id"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            other_names=data.get("other_names"),
            gender=data.get("gender"),
            contact=data.get("contact"),
            address=data.get("address"),
            emergency_contact=data.get("emergency_contact"),
            date_created=data.get("date_created"),
            date_updated=data.get("date_updated"),
            date_deleted=data.get("date_deleted")
        )
