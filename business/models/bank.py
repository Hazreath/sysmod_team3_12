from pydantic import BaseModel

from business.models.user import User


class Account(BaseModel):
    id: int
    name: str
    status: bool
    balance: float

    user: User


class Transaction(BaseModel):
    id: int
    amount: float

    source_account: Account
    dest_account: Account
