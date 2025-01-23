from pydantic import BaseModel, Field


class LedgerEntrySchema(BaseModel):
    """
    Ledger entry schema
    """

    operation: str = Field(..., description="Ledger operation type")
    amount: int = Field(..., description="Amount of credits")
    nonce: str = Field(..., description="Unique identifier for the operation")
    owner_id: str = Field(..., description="Owner of the operation")

    class Config:
        from_attributes = True


class OwnerBalanceResponse(BaseModel):
    """
    Owner balance response schema
    """

    owner_id: str
    balance: float


class AddLedgerResponse(BaseModel):
    """
    Add ledger entry response schema
    """

    status: str
    message: str
