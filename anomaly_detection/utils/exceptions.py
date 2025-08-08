from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from .logging import setup_logging

logger = setup_logging()

def setup_exception_handlers(app):
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        logger.error(f"HTTP error occurred: {exc.detail}")
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})