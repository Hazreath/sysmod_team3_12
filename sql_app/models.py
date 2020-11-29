from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Float, Integer, String, Boolean

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
    enabled = Column(Boolean)
    balance = Column(Float)

    # One To One relationship.
    # @see https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html#one-to-one
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="account")


class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, index=True)

    source_account_id = Column(Integer, ForeignKey('account.id'))
    dest_account_id = Column(Integer, ForeignKey('account.id'))

    # https://docs.sqlalchemy.org/en/14/orm/join_conditions.html
    source_account = relationship("Account", foreign_keys=[source_account_id])
    dest_account = relationship("Account", foreign_keys=[dest_account_id])

    amount = Column(Float)
