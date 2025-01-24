from unittest.mock import Mock

import pytest
from sqlalchemy.orm import Session

from core.domain.entities.ledger_entity import LedgerEntity
from core.domain.exceptions.ledger_exceptions import UserNotFoundException
from core.domain.models.ledger_entry import LedgerEntry
from core.domain.models.user import User
from infrastructure.repositories.sqlalchemy_ledger_repository import \
    SQLAlchemyLedgerRepository


def test_add_user_returns_user_object_when_owner_id_is_valid(mocker):
    session_mock = mocker.Mock()
    owner_id = "valid_owner_id"

    session_mock.add.return_value = None
    session_mock.commit.return_value = None

    repository = SQLAlchemyLedgerRepository(session=session_mock)

    result = repository.add_user(owner_id=owner_id)

    assert isinstance(result, User)
    assert result.owner_id == owner_id


def test_get_balance_returns_0_when_user_has_no_transactions(session):
    repository = SQLAlchemyLedgerRepository(session)
    owner_id = "test_owner_id"
    repository.add_user(owner_id)
    balance = repository.get_balance(owner_id)

    assert balance == 0.0


def test_get_balance_raises_user_not_found_exception(session):
    repository = SQLAlchemyLedgerRepository(session)
    owner_id = "non_existent_user"

    with pytest.raises(UserNotFoundException):
        repository.get_balance(owner_id)


def test_save_entry_updates_user_balance(session):
    repository = SQLAlchemyLedgerRepository(session)
    owner_id = "test_owner_id"
    repository.add_user(owner_id)
    repository.save_entry(
        LedgerEntity(
            id=None,
            operation="DAILY_REWARD",
            amount=50,
            nonce="trial",
            owner_id="test_owner_id",
        ),
        50.0,
    )
    balance = repository.get_balance(owner_id)

    assert balance == 50.0


def test_nonce_exists_returns_true_when_nonce_exists():
    session = Mock(spec=Session)
    ledger_repo = SQLAlchemyLedgerRepository(session)
    nonce = "some_nonce"
    existing_entry = LedgerEntry(nonce=nonce)
    session.query(LedgerEntry).filter_by.return_value.first.return_value = (
        existing_entry
    )

    result = ledger_repo.nonce_exists(nonce)

    assert result is True
