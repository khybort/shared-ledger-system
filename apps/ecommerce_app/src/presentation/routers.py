from fastapi import APIRouter, Depends, Query, Request
from src.presentation.dependencies import get_ecommerce_service

from core.schemas.ledger import (AddLedgerResponse, LedgerEntrySchema,
                                 OwnerBalanceResponse)
from infrastructure.rate_limiter import limiter

router = APIRouter()


@router.get(
    "/ledger",
    response_model=OwnerBalanceResponse,
    summary="Get Owner Balance",
    description="Returns the balance of the specified owner.",
)
@limiter.limit("5/minute")
def get_balance(
    request: Request,
    owner_id: str = Query(
        ..., description="The ID of the owner to fetch the balance for."
    ),
    service=Depends(get_ecommerce_service),
):
    """
    Fetch the balance of a specified owner using their ID.
    """
    balance = service.get_balance(owner_id)
    return OwnerBalanceResponse(owner_id=owner_id, balance=balance)


@router.post("/ledger", response_model=AddLedgerResponse)
@limiter.limit("5/minute")
def add_ecommerce_entry(
    entry: LedgerEntrySchema, request: Request, service=Depends(get_ecommerce_service)
):
    """
    Add a new ledger entry for the specified owner and operation.
    """
    service.add_ecommerce_entry(entry)
    return AddLedgerResponse(
        status="success", message="Ecommerce ledger entry added successfully"
    )
