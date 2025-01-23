from fastapi import Depends
from sqlalchemy.orm import Session
from src.services.content_service import ContentService

from infrastructure.db.base import get_db
from infrastructure.repositories.sqlalchemy_ledger_repository import \
    SQLAlchemyLedgerRepository


def get_content_service(db: Session = Depends(get_db)):
    repository = SQLAlchemyLedgerRepository(db)
    return ContentService(repository)
