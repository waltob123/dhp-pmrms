from builtins import Exception


class InvalidDateFormatException(Exception):
    """Exception raised for invalid date format."""
    pass


class EntityDoesNotExistException(Exception):
    """Exception raised when an entity does not exist."""
    pass


class FailedToSaveObjectException(Exception):
    """Exception raised when an object fails to save."""
    pass