from health_app.utils.constants import PAGE, PAGE_SIZE
from health_app.utils.file_manager import FileManager


class PublicRepository:
    """
    Interface for the repository layer in the health app.
    """

    def __init__(self, *, db_connection: FileManager, allowed_filters: dict, allowed_sort: dict) -> None:
        """
        Initializes the repository with a database connection.

        :param db_connection: The database connection object.
        :param allowed_filters: The allowed filters for the repository.
        :param allowed_sort: The allowed sorting options for the repository.
        """
        self._db_connection = db_connection
        self.__allowed_filters = allowed_filters
        self.__allowed_sort = allowed_sort

    def get_all(self, *, filters: dict, sort: dict) -> list[dict]:
        """
        Get all records from the database.

        :param filters: The filters to apply to the query.
        :param sort: The sorting options.
        :return: A list of all records.
        """
        results = self._db_connection.read_file()
        final_result = []

        for key, value in filters.items():
            if key in self.__allowed_filters:
                for record in results:
                    if key in record.keys():
                        if record[key] == value:
                            final_result.append(record)

        if "page" in filters and "page_size" in filters:
            final_result = PublicRepository.apply_pagination(
                records=final_result, page=filters.get("page"), page_size=filters.get("page_size")
            )

        if "order_by" in sort and "order_mode" in sort:
            final_result = PublicRepository.apply_sort(
                records=final_result, order_by=sort.get("order_by"), order_mode=sort.get("order_mode")
            )

        return final_result

    def get_by_id(self, record_id: str) -> dict:
        """
        Abstract method to get a record by its ID.

        :param record_id: The ID of the record to retrieve.
        :return: The record with the specified ID.
        """
        results = self._db_connection.read_file()
        result = [
            record for record in results if record["id"] == record_id
        ][0]
        return result

    def get_by_field(self, *, field: str, value: str) -> list[dict]:
        """
        Abstract method to get records by a specific field.

        :param field: The field to filter by.
        :param value: The value to filter by.
        :return: A list of records that match the specified field and value.
        """
        results = self._db_connection.read_file()
        if not field in results[0].keys():
            raise KeyError(f"Field '{field}' not found in records.")

        result = [
            record for record in results if record[field] == value
        ]
        return result

    def check_if_exists_but_deleted(self, *, record_id: str) -> bool:
        """
        Check if a record exists but is marked as deleted.

        :param record_id: The ID of the record to check.
        :return: True if the record exists but is deleted, False otherwise.
        """
        return bool(self.get_by_id(record_id=record_id).get("deleted_at"))

    def check_if_exists(self, *, record_id: str) -> bool:
        """
        Check if a record exists.

        :param record_id: The ID of the record to check.
        :return: True if the record exists, False otherwise.
        """
        return bool(self.get_by_id(record_id=record_id))

    @staticmethod
    def __offset_calculator(*, page: int, page_size: int) -> int:
        """
        Calculate the offset for pagination.

        :param page: The page number.
        :param page_size: The number of records per page.
        :return: The offset for pagination.
        """
        page = page if page > 0 else PAGE
        page_size = page_size if page_size > 0 else PAGE_SIZE
        return (page - 1) * page_size

    @staticmethod
    def apply_pagination(*, records: list[dict], page: int, page_size: int) -> list[dict]:
        """
        Apply pagination to a list of records.

        :param records: The list of records to paginate.
        :param page: The page number.
        :param page_size: The number of records per page.
        :return: A paginated list of records.
        """
        start = PublicRepository.__offset_calculator(page=page, page_size=page_size)
        end = start + page_size
        return records[start:end]

    @staticmethod
    def apply_sort(*, records: list[dict], order_by: str, order_mode: str) -> list[dict]:
        """
        Apply sorting to a list of records.

        :param records: The list of records to sort.
        :param order_by: The field to sort by.
        :param order_mode: The order to sort by (asc or desc).
        :return: A sorted list of records.
        """
        reverse = True if order_mode == "desc" else False
        return sorted(records, key=lambda x: x[order_by], reverse=reverse)
