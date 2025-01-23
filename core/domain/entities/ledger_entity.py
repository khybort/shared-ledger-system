from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class LedgerEntity:
    id: int
    operation: str
    amount: int
    nonce: str
    owner_id: str
    created_on: Optional[datetime] = field(default=None)
