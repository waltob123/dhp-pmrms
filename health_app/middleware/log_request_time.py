from fastapi import Request
import time

async def log_request_time(request: Request, call_next):
    """
    Middleware to log the time taken to process a request.
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Request: {request.method} {request.url} completed in {process_time:.4f}s")
    return response
