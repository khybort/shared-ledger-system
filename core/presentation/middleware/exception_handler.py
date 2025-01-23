from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

from core.domain.exceptions.base_ledger_exception import BaseLedgerException
from infrastructure.logger.logger import logger


async def exception_handler(request: Request, exc: Exception):
    """
    Tüm exception'ları ele alan global handler.
    """
    if isinstance(exc, BaseLedgerException):
        logger.error(f"Domain Exception: {exc.message}")
        return JSONResponse(
            status_code=400,
            content={"detail": exc.message},
        )
    elif isinstance(exc, HTTPException):
        logger.warning(f"HTTP Exception: {exc.detail}")
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail},
        )
    else:
        logger.critical(f"Unexpected Exception: {str(exc)}")
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal Server Error"},
        )
