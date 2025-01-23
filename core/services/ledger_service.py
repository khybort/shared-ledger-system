from core.domain.entities.ledger_entity import LedgerEntity
from core.domain.exceptions.ledger_exceptions import (
    DuplicateTransactionException, InsufficientBalanceException,
    InvalidOperationException)
from core.domain.operations.composite_ledger_operation import \
    CompositeLedgerOperation
from core.domain.value_objects.operation_config import OperationConfig
from core.repositories.ledger_repository import LedgerRepository


class LedgerService:
    """
    Ledger service that determines business logic for ledger operation
    """

    def __init__(
        self,
        repository: LedgerRepository,
        operations: CompositeLedgerOperation,
        config: OperationConfig,
    ):
        """
        repository: LedgerRepository implementation (Ex. SQLAlchemyLedgerRepository).
        operations: Union of shared operations and app specific operations
        config: Configuration values for related operations
        """
        self.repository = repository
        self.operations = operations
        self.config = config

    def get_balance(self, owner_id: str) -> int:
        """
        Returns the current balance for the given owner
        """
        return self.repository.get_balance(owner_id)

    def add_ledger_entry(self, ledger: LedgerEntity) -> None:
        """
        Adds new ledger entry
        """
        if not self.operations.validate_operation(ledger.operation):
            raise InvalidOperationException(ledger.operation)

        if ledger.amount < 0 and self.get_balance(ledger.owner_id) < abs(ledger.amount):
            raise InsufficientBalanceException()

        if self.repository.nonce_exists(ledger.nonce):
            raise DuplicateTransactionException()

        price = self.config.get_value(ledger.operation) * ledger.amount
        self.repository.save_entry(ledger, price)
