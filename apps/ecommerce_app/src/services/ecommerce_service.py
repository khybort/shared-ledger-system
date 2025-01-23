from src.domain.ecommerce_operation import ECommerceOperation

from core.domain.entities.ledger_entity import LedgerEntity
from core.repositories.ledger_repository import LedgerRepository
from core.schemas.ledger import LedgerEntrySchema
from core.services.ledger_service import LedgerService


class ECommerceService(LedgerService):
    def __init__(self, repository: LedgerRepository):
        ecommerce_operations = ECommerceOperation()
        super().__init__(
            repository=repository,
            operations=ecommerce_operations.operations,
            config=ecommerce_operations.config,
        )

    def add_ecommerce_entry(self, entry: LedgerEntrySchema) -> dict:
        """
        Yeni bir e-ticaret işlemi ekler.

        Args:
            entry (LedgerEntrySchema): API'den gelen doğrulanmış giriş.

        Returns:
            dict: İşlem sonucu.
        """
        domain_entity = LedgerEntity(
            id=None,
            operation=entry.operation,
            amount=entry.amount,
            nonce=entry.nonce,
            owner_id=entry.owner_id,
        )
        super().add_ledger_entry(domain_entity)
        return {
            "status": "success",
            "message": "E-commerce ledger entry added successfully",
        }
