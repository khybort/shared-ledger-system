from core.domain.operations.composite_ledger_operation import \
    CompositeLedgerOperation
from core.domain.value_objects.operation_config import OperationConfig


class ContentOperation:
    """
    Content uygulamasına özel operasyonlar ve değerler.
    """

    def __init__(self):
        custom_operations = {"CONTENT_CREATION", "CONTENT_ACCESS"}
        custom_config = {"CONTENT_CREATION": -5, "CONTENT_ACCESS": 0}

        self.operations = CompositeLedgerOperation(custom_operations)
        self.config = OperationConfig(custom_config)

    def validate_operation(self, operation: str) -> bool:
        return self.operations.validate_operation(operation)

    def get_value(self, operation: str) -> int:
        return self.config.get_value(operation)
