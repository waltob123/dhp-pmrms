import uuid


def is_valid_uuid(*, uuid_to_test: str, version=4) -> bool:
    """
    Validate that the given id is a valid UUID.

    :param uuid_to_test: The id to validate
    :param version: The uuid version. Defaults to 4.
    :return: True if the id is valid, False otherwise
    """
    try:
        uuid_obj = uuid.UUID(uuid_to_test, version=version)
    except (ValueError, AttributeError):
        return False

    return str(uuid_obj) == uuid_to_test
