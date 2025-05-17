from fastapi import FastAPI
from fastapi.exceptions import HTTPException, RequestValidationError

from health_app.handlers.exception_handlers import http_exception_handler, validation_exception_handler
from health_app.routers.api.v1.patients import patients_router

# Initialize the FastAPI application
app = FastAPI(debug=True, version="1.0.0")

# Register the exception handlers
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)

# Register the routers
app.include_router(patients_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        log_level="info",
        use_colors=True,
        reload=True
    )
