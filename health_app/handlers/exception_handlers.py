from fastapi import HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from health_app.schemas.response import ResponseSchema
from health_app.utils.constants import HTTPResponseStatus


def http_exception_handler(request: Request, exception: HTTPException) -> JSONResponse:
    """
    Custom exception handler for HTTP exceptions.

    :param request: The request object.
    :param exception: the HTTPException object.
    :return: The JSON response with the error message.
    """
    return ResponseSchema(
        status=HTTPResponseStatus.ERROR.value,
        status_code=exception.status_code,
        message=exception.detail,
    ).to_json_response()


def validation_exception_handler(request: Request, exception: RequestValidationError) -> JSONResponse:
    """
    Custom exception handler for validation exceptions.

    :param request: The request object.
    :param exception: The validation exception object.
    :return: The JSON response with the error message.
    """
    missing_attrs = []
    invalid_data = []
    errors = ""
    _types = [error["type"] for error in exception.errors()]

    for type_ in range(len(_types)):
        if _types[type_] == "missing":
            missing_attrs.append(exception.errors()[type_]["loc"][1])
        if _types[type_] == "value_error":
            invalid_data.append(exception.errors()[type_]["msg"])

    if missing_attrs:
        errors = errors + f"Fields required: {missing_attrs}"

    if invalid_data:
        errors = errors +  f"\nInvalid data: {invalid_data}"

    return ResponseSchema(
        status=HTTPResponseStatus.ERROR.value,
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        message=errors,
    ).to_json_response()
