from health_app.repositories.private_repository import PrivateRepository
from health_app.repositories.public_repository import PublicRepository
from health_app.utils.file_manager import FileManager


class DoctorRepository(PublicRepository, PrivateRepository):
    """
    This class is responsible for managing doctor data.

    (PublicRepository) This class inherits from the PublicRepository
    (PrivateRepository) This class inherits from the PrivateRepository
    """

    def __init__(self, *, db_connection: FileManager, allowed_filters: dict, allowed_sort: dict) -> None:
        """
        Initializes the DoctorRepository with a database connection.

        :param db_connection: The database connection object.
        :param allowed_filters: The allowed filters for the repository.
        :param allowed_sort: The allowed sorting options for the repository.
        """
        PublicRepository.__init__(
            self, db_connection=db_connection, allowed_filters=allowed_filters, allowed_sort=allowed_sort
        )
        PrivateRepository.__init__(self, db_connection=db_connection)
