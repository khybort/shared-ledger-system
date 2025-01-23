from core.domain.exceptions.base_ledger_exception import BaseLedgerException


class LedgerException(Exception):
    """
    Raises when an exception is raised belongs to a ledger
    """

    def __init__(self, message: str, code: int = 400):
        self.message = message
        self.code = code


class InvalidOperationException(BaseLedgerException):
    """
    Raises when an invalid operation
    """

    def __init__(self, operation: str):
        super().__init__(f"Invalid operation: {operation}")


class UserNotFoundException(BaseLedgerException):
    """
    Raises when a user is not found
    """

    def __init__(self, owner_id: str):
        super().__init__(f"User not found with id {owner_id}")


class InsufficientBalanceException(BaseLedgerException):
    """
    Raises when insufficient balance
    """

    def __init__(self):
        super().__init__("Insufficient balance for this operation")


class DuplicateTransactionException(BaseLedgerException):
    """
    Raises when same nonce is already used for a transaction
    """

    def __init__(self):
        super().__init__("Duplicate transaction detected")
