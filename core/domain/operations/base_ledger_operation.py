from enum import Enum


class BaseLedgerOperation(Enum):
    """
    Paylaşılan operasyonların sabit tanımı.
    """

    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT"
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"
