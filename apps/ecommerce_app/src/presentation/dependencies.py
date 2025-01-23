from fastapi import Depends
from sqlalchemy.orm import Session
from src.services.ecommerce_service import ECommerceService

from infrastructure.db.base import get_db
from infrastructure.repositories.sqlalchemy_ledger_repository import \
    SQLAlchemyLedgerRepository


def get_ecommerce_service(db: Session = Depends(get_db)) -> ECommerceService:
    repository = SQLAlchemyLedgerRepository(db)
    return ECommerceService(repository)
