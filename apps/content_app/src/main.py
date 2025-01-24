from fastapi import FastAPI, Request
from prometheus_fastapi_instrumentator import Instrumentator
from src.presentation.routers import router

from core.domain.exceptions.base_ledger_exception import BaseLedgerException
from core.presentation.middleware.exception_handler import exception_handler
from infrastructure.rate_limiter import SlowAPIMiddleware, limiter

app = FastAPI(
    title="Content App API",
    description="API for managing contents and ledger operations",
    version="1.0.0",
    docs_url="/api/v1/content/docs",
    openapi_url="/api/v1/content/openapi.json",
)
app.add_middleware(SlowAPIMiddleware)
app.state.limiter = limiter
Instrumentator().instrument(app).expose(app, endpoint="/content/metrics", include_in_schema=False)

app.include_router(router, prefix="/api/v1/content")


@app.get("/content/health")
@limiter.limit("5/minute")
def health_check(request: Request):
    return {"status": "healthy"}


app.add_exception_handler(BaseLedgerException, exception_handler)
