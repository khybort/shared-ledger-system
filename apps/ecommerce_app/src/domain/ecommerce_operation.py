from core.domain.operations.composite_ledger_operation import \
    CompositeLedgerOperation
from core.domain.value_objects.operation_config import OperationConfig


class ECommerceOperation:
    def __init__(self):
        custom_operations = {"PURCHASE_ITEM", "REFUND_ITEM"}
        custom_config = {"PURCHASE_ITEM": -10, "REFUND_ITEM": 10}

        self.operations = CompositeLedgerOperation(custom_operations)
        self.config = OperationConfig(custom_config)

    def validate_operation(self, operation: str) -> bool:
        return self.operations.validate_operation(operation)

    def get_value(self, operation: str) -> int:
        return self.config.get_value(operation)
