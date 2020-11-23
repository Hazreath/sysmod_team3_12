from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    account = relationship("Account", uselist=False, back_populates="user")


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True, index=True)

    # name: str
    # status: bool
    balance = Column(DECIMAL)

    # One To One relationship.
    # @see https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html#one-to-one
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="account")

