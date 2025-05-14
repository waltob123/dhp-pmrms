from typing import Type

from pydantic import BaseModel as PydanticBaseModel

from health_app.models.base_model import BaseModel
from health_app.utils.file_manager import FileManager


class PrivateRepository:
    """
    Base repository class that provides a common interface for all repositories.
    """

    def __init__(self, *, db_connection: FileManager) -> None:
        """
        Initializes the BaseRepository with a database connection.

        :param db_connection: The database connection object.
        """
        self._db_connection = db_connection

    def create(self, *, data: PydanticBaseModel, model: Type[BaseModel]) -> BaseModel:
        """
        Create a new record in the database.

        :param data: The data to be created.
        :param model: The model class to be used for creating the record.

        :return: The created object.
        """
        model_instance = model(**data.model_dump())
        self._save(object_to_save=model_instance.to_dict())
        return model_instance

    def update(self, *, data_to_update: BaseModel, update_data: PydanticBaseModel) -> BaseModel:
        """
        Update an existing record in the database.

        :param data_to_update: The object to be updated.
        :param update_data: The data to update the object with.

        :return: The updated object.
        """
        try:
            for key, value in update_data.model_dump().items():
                if hasattr(data_to_update, key):
                    setattr(data_to_update, key, value)
        except AttributeError as e:
            raise AttributeError(f"Attribute error: {e}")

        self._save(object_to_save=data_to_update.to_dict())
        return data_to_update

    def delete(self, *, object_to_delete: BaseModel) -> BaseModel:
        """
        Delete an object from the database.

        :param object_to_delete: The object to be deleted.
        :return: The deleted object.
        """
        deleted_object = object_to_delete.soft_delete()
        self._save(object_to_save=deleted_object.to_dict())
        return deleted_object

    def restore(self, *, object_to_restore: BaseModel) -> BaseModel:
        """
        Restore a soft-deleted object in the database.

        :param object_to_restore: The object to be restored.
        :return: The restored object.
        """
        restored_object = object_to_restore.restore()
        self._save(object_to_save=restored_object.to_dict())
        return restored_object

    def _save(self, *, object_to_save: dict) -> None:
        """
        Save the object to the database.

        :param object_to_save: The object to be saved.
        """
        if not isinstance(object_to_save, dict):
            raise TypeError("object_to_save must be a dictionary")

        results = self._db_connection.read_file()
        results.append(object_to_save)
        self._db_connection.write_file(content=results)
