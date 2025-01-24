import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from infrastructure.db.base import Base


# Test için geçici bir veritabanı oluştur
@pytest.fixture(scope="function")
def session():
    engine = create_engine("sqlite:///:memory:")  # In-memory SQLite
    Base.metadata.create_all(engine)  # Tüm tabloları oluştur
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
