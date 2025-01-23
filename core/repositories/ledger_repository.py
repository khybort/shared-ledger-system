from abc import ABC, abstractmethod

from core.domain.entities.ledger_entity import LedgerEntity
from core.domain.models.user import User


class LedgerRepository(ABC):

    @abstractmethod
    def add_user(self, owner_id: str) -> User:
        """
        Adds new user
        """
        pass

    @abstractmethod
    def get_user(self, owner_id: str) -> User:
        """
        Returns information of specified user
        """
        pass

    @abstractmethod
    def get_balance(self, owner_id: str) -> float:
        """
        Returns balance of specified user
        """
        pass

    @abstractmethod
    def save_entry(self, entry: LedgerEntity, price: float) -> None:
        """
        Adds new ledger entry
        """
        pass

    @abstractmethod
    def nonce_exists(self, nonce: str) -> bool:
        """
        Checks whether a given nonce has been used before.
        """
        pass
