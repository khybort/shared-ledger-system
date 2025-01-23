from src.domain.content_operation import ContentOperation

from core.domain.entities.ledger_entity import LedgerEntity
from core.repositories.ledger_repository import LedgerRepository
from core.schemas.ledger import LedgerEntrySchema
from core.services.ledger_service import LedgerService
from infrastructure.logger import logger


class ContentService(LedgerService):
    """
    Content app specific ledger service
    """

    def __init__(self, repository: LedgerRepository):
        content_operations = ContentOperation()
        super().__init__(
            repository=repository,
            operations=content_operations.operations,
            config=content_operations.config,
        )

    def add_content_entry(self, entry: LedgerEntrySchema) -> dict:
        """
        Adds new ledger entry
        """
        domain_entry = LedgerEntity(
            id=None,
            operation=entry.operation,
            amount=entry.amount,
            nonce=entry.nonce,
            owner_id=entry.owner_id,
        )
        super().add_ledger_entry(domain_entry)
        logger.logger.info("Added ledger entry")
        return {
            "status": "success",
            "message": "Content ledger entry added successfully",
        }
