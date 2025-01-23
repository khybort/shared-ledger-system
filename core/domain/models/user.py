from sqlalchemy import Column, Float, Integer, String

from infrastructure.db.base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    owner_id = Column(String, unique=True, nullable=False)
    balance = Column(Float, default=0.0, nullable=False)
