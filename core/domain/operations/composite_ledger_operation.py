from typing import Set

from core.domain.operations.base_ledger_operation import BaseLedgerOperation


class CompositeLedgerOperation:
    """
    Paylaşılan ve özel operasyonları dinamik olarak birleştirir.
    """

    def __init__(self, custom_operations: Set[str] = None):
        """
        custom_operations: Uygulamaya özel operasyonlar.
        """
        if custom_operations is None:
            custom_operations = set()
        self.operations = {op.value for op in BaseLedgerOperation}.union(
            custom_operations
        )

    def validate_operation(self, operation: str) -> bool:
        """
        Operasyonun geçerli olup olmadığını kontrol eder.
        """
        return operation in self.operations

    def get_operations(self) -> Set[str]:
        """
        Tüm geçerli operasyonları döner (paylaşılan + özel).
        """
        return self.operations
