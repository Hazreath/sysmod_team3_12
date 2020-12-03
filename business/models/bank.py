from pydantic import BaseModel

from business.models.user import User


class Account(BaseModel):
    id: int
    # name: str
    # status: bool
    balance: float
    enabled: bool
    user: User

    class Config:
        orm_mode = True

class TransactionBase(BaseModel):
    amount: float


class TransactionCreateInput(TransactionBase):
    dest_account_email: str

class TransactionModifyInput(TransactionCreateInput):
    id: int
class Transaction(TransactionBase):
    id: int

    source_account: Account
    dest_account: Account

    modified: bool
    class Config:
        orm_mode = True
