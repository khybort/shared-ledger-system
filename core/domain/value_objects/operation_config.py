from typing import Dict

from core.domain.operations.base_ledger_operation import BaseLedgerOperation


class OperationConfig:
    """
    Holds shared and app specific configurations
    Paylaşılan ve uygulamaya özel operasyonların değerlerini tutar.
    """

    def __init__(self, custom_config: Dict[str, int] = None):
        """
        custom_config: App specific operation congifurations
        """
        self.config = {
            BaseLedgerOperation.DAILY_REWARD.value: 1,
            BaseLedgerOperation.SIGNUP_CREDIT.value: 3,
            BaseLedgerOperation.CREDIT_SPEND.value: -1,
            BaseLedgerOperation.CREDIT_ADD.value: 10,
        }

        if custom_config:
            self.config.update(custom_config)

    def get_value(self, operation: str) -> int:
        """
        Returns the value of the operation specified by operation
        """
        if operation not in self.config:
            raise ValueError(f"Invalid operation: {operation}")
        return self.config[operation]

    def get_all_values(self) -> Dict[str, int]:
        """
        Returns all values of operation
        """
        return self.config
