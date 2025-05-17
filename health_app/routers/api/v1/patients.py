from typing import Annotated

from fastapi import APIRouter, Body, Depends, Path, Query, Request, Response, status

from health_app.dependencies.service_dependencies import get_patient_service
from health_app.schemas.patient import ReadPatientSchema, CreatePatientSchema, UpdatePatientSchema
from health_app.schemas.response import ResponseSchema
from health_app.services.patient_service import PatientService
from health_app.utils.constants import API_VERSION_1

patients_router = APIRouter(
    prefix=f"{API_VERSION_1}/patients",
    tags=["Patients"]
)


@patients_router.get(
    path="/",
    response_model=ResponseSchema,
    status_code=status.HTTP_200_OK,
    summary="Get all patients",
    description="Retrieve a list of all patients."
)
async def get_all_patients(
    request: Request,
    response: Response,
    filters: Annotated[list, Query(..., description="Filters to apply to the results")] = None,
    sort: Annotated[list, Query(..., description="Sorting options for the results")] = None,
    patient_service: PatientService = Depends(get_patient_service)
) -> ResponseSchema:
    """
    Retrieves all patients with optional filters and sorting.

    :param request: The request object containing filters and sorting options.
    :param response: The response object to set headers and status codes.
    :param filters: The filters to apply to the query.
    :param sort: The sorting options.
    :param patient_service: The patient service instance.
    :return: The response containing the list of patients.
    """
    patients = patient_service.get_all(request=request)
    response_data = ResponseSchema(
        status_code=status.HTTP_200_OK,
        status="success",
        data=[ReadPatientSchema(**patient.to_dict()) for patient in patients],
        message="Patients retrieved successfully."
    )
    return response_data


@patients_router.get(
    path="/{patient_id}",
    response_model=ResponseSchema,
    status_code=status.HTTP_200_OK,
    summary="Get a patient by ID",
    description="Retrieve a patient by their ID."
)
async def get_patient_by_id(
    request: Request,
    response: Response,
    patient_id: Annotated[str, Path(..., description="The ID of the patient to retrieve")],
    patient_service: PatientService = Depends(get_patient_service)
) -> ResponseSchema:
    """
    Retrieves a patient by their ID.

    :param request: The request object.
    :param response: The response object to set headers and status codes.
    :param patient_id: The ID of the patient to retrieve.
    :param patient_service: The patient service instance.
    :return: The response containing the patient data.
    """
    patient = patient_service.get_by_id(record_id=patient_id)
    response_data = ResponseSchema(
        status_code=status.HTTP_200_OK,
        status="success",
        data=ReadPatientSchema(**patient.to_dict()),
        message="Patient retrieved successfully."
    )
    return response_data


@patients_router.post(
    path="/",
    response_model=ResponseSchema,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new patient",
    description="Create a new patient with the provided data."
)
async def create_patient(
    request: Request,
    response: Response,
    patient_data: Annotated[CreatePatientSchema, Body(..., description="The data for the new patient")],
    patient_service: PatientService = Depends(get_patient_service)
) -> ResponseSchema:
    """
    Creates a new patient with the provided data.

    :param request: The request object.
    :param response: The response object to set headers and status codes.
    :param patient_data: The data for the new patient.
    :param patient_service: The patient service instance.
    :return: The response containing the created patient data.
    """
    patient = patient_service.create(patient=patient_data)
    response_data = ResponseSchema(
        status_code=status.HTTP_201_CREATED,
        status="success",
        data=ReadPatientSchema(**patient.to_dict()),
        message="Patient created successfully."
    )
    return response_data


@patients_router.put(
    path="/{patient_id}",
    response_model=ResponseSchema,
    status_code=status.HTTP_200_OK,
    summary="Update a patient",
    description="Update a patient with the provided data."
)
async def update_patient(
    request: Request,
    response: Response,
    patient_id: Annotated[str, Path(..., description="The ID of the patient to update")],
    patient_data: Annotated[UpdatePatientSchema, Body(..., description="The data to update the patient")],
    patient_service: PatientService = Depends(get_patient_service)
) -> ResponseSchema:
    """
    Updates a patient with the provided data.

    :param request: The request object.
    :param response: The response object to set headers and status codes.
    :param patient_id: The ID of the patient to update.
    :param patient_data: The data to update the patient.
    :param patient_service: The patient service instance.
    :return: The response containing the updated patient data.
    """
    updated_patient = patient_service.update(record_id=patient_id, record_update_data=patient_data)
    response_data = ResponseSchema(
        status_code=status.HTTP_200_OK,
        status="success",
        data=ReadPatientSchema(**updated_patient.to_dict()),
        message="Patient updated successfully."
    )
    return response_data


@patients_router.delete(
    path="/{patient_id}",
    response_model=ResponseSchema,
    status_code=status.HTTP_200_OK,
    summary="Delete a patient",
    description="Delete a patient by their ID."
)
async def delete_patient(
    request: Request,
    response: Response,
    patient_id: Annotated[str, Path(..., description="The ID of the patient to delete")],
    patient_service: PatientService = Depends(get_patient_service)
) -> ResponseSchema:
    """
    Deletes a patient by their ID.

    :param request: The request object.
    :param response: The response object to set headers and status codes.
    :param patient_id: The ID of the patient to delete.
    :param patient_service: The patient service instance.
    :return: The response indicating the deletion status.
    """
    deleted_patient = patient_service.delete(record_id=patient_id)
    response_data = ResponseSchema(
        status_code=status.HTTP_200_OK,
        status="success",
        data=ReadPatientSchema(**deleted_patient.to_dict()),
        message="Patient deleted successfully."
    )
    return response_data


@patients_router.patch(
    path="/{patient_id}",
    response_model=ResponseSchema,
    status_code=status.HTTP_200_OK,
    summary="Restore a soft-deleted patient",
    description="Restore a soft-deleted patient by their ID."
)
async def restore_patient(
    request: Request,
    response: Response,
    patient_id: Annotated[str, Path(..., description="The ID of the patient to restore")],
    patient_service: PatientService = Depends(get_patient_service)
) -> ResponseSchema:
    """
    Restores a soft-deleted patient by their ID.

    :param request: The request object.
    :param response: The response object to set headers and status codes.
    :param patient_id: The ID of the patient to restore.
    :param patient_service: The patient service instance.
    :return: The response indicating the restoration status.
    """
    restored_patient = patient_service.restore(record_id=patient_id)
    response_data = ResponseSchema(
        status_code=status.HTTP_200_OK,
        status="success",
        data=ReadPatientSchema(**restored_patient.to_dict()),
        message="Patient restored successfully."
    )
    return response_data
