from abc import abstractmethod
from typing import Union

from fastapi import HTTPException, Request, status
from pydantic import BaseModel as PydanticBaseModel

from health_app.models.base_model import BaseModel
from health_app.repositories.private_repository import PrivateRepository
from health_app.repositories.public_repository import PublicRepository
from health_app.utils.exceptions import EntityDoesNotExistException, FailedToSaveObjectException
from health_app.utils.misc import filter_sort_processor, set_filter_defaults


class BaseService:
    """A mixin class that provides common service methods for handling data."""

    def __init__(self, *, repository: Union[PrivateRepository, PublicRepository]) -> None:
        """
        Initializes the ServiceMixin with a repository.

        :param repository: The repository to be used for data operations.
        """
        self._repository = repository

    def get_by_id(self, *, record_id: str) -> BaseModel:
        """
        Retrieves a record by their ID.

        :param record_id: The ID of the record to retrieve.
        :return: The record with the specified ID.
        """
        try:
            return self._repository.get_by_id(record_id=record_id)
        except EntityDoesNotExistException as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

    def get_all(self, *, request: Request) -> list[BaseModel]:
        """
        Retrieves all records with optional filters and sorting.

        :param request: The request object containing filters and sorting options.
        :return: A list of all records.
        """
        filters = filter_sort_processor(filters_or_sort_param=request.query_params.getlist("filters"))
        sort = filter_sort_processor(filters_or_sort_param=request.query_params.getlist("sort"))
        filters = set_filter_defaults(filters=filters)
        return self._repository.get_all(filters=filters, sort=sort)

    @abstractmethod
    def create(self, *args, **kwargs) -> BaseModel:
        pass

    def update(self, record_id: str, record_update_data: PydanticBaseModel) -> BaseModel:
        """
        Updates an existing record.

        :param record_id: The ID of the record to update.
        :param record_update_data: The data to update the record with.
        :return: The updated record.
        """
        try:
            record_to_update = self._repository.get_by_id(record_id=record_id)
        except EntityDoesNotExistException as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

        try:
            updated_record = self._repository.update(
                data_to_update=record_to_update,
                update_data=record_update_data
            )
        except FailedToSaveObjectException as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

        return updated_record
    
    def delete(self, *, record_id: str) -> BaseModel:
        """
        Deletes a record.

        :param record_id: The ID of the record to delete.
        :return: The deleted record.
        """
        try:
            record_to_delete = self._repository.get_by_id(record_id=record_id)
            return self._repository.delete(object_to_delete=record_to_delete)
        except EntityDoesNotExistException as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except FailedToSaveObjectException as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    def restore(self, *, record_id: str) -> BaseModel:
        """
        Restores a deleted record.

        :param record_id: The ID of the record to restore.
        :return: The restored record.
        """
        try:
            record_to_restore = self._repository.get_by_id(record_id=record_id)
            return self._repository.restore(object_to_restore=record_to_restore)
        except EntityDoesNotExistException as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        except FailedToSaveObjectException as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
