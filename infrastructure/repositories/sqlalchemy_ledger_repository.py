import datetime

from sqlalchemy.orm import Session

from core.domain.entities.ledger_entity import LedgerEntity
from core.domain.exceptions.ledger_exceptions import UserNotFoundException
from core.domain.models.ledger_entry import LedgerEntry
from core.domain.models.user import User
from core.repositories.ledger_repository import LedgerRepository


class SQLAlchemyLedgerRepository(LedgerRepository):
    def __init__(self, session: Session):
        self.session = session

    def add_user(self, owner_id: str) -> User:
        user = User(owner_id=owner_id)
        self.session.add(user)
        self.session.commit()
        return user

    def get_user(self, owner_id: str) -> User:
        return self.session.query(User).filter_by(owner_id=owner_id).first()

    def get_balance(self, owner_id: str) -> float:
        user = self.get_user(owner_id)
        if user:
            return user.balance

        raise UserNotFoundException(owner_id)

    def save_entry(self, entry: LedgerEntity, price: float) -> None:
        if entry.created_on is None:
            entry.created_on = datetime.datetime.now(datetime.timezone.utc)
        model = LedgerEntry(**entry.__dict__)
        user = self.get_user(entry.owner_id)
        self.session.add(model)
        if not user:
            user = self.add_user(entry.owner_id)
        user.balance += price
        self.session.commit()

    def nonce_exists(self, nonce: str) -> bool:
        return (
            self.session.query(LedgerEntry).filter_by(nonce=nonce).first() is not None
        )
