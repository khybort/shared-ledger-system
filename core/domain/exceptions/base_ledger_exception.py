class BaseLedgerException(Exception):
    """
    Tüm domain-specific exception'ların temel sınıfı.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
