from pydantic import BaseModel


class Account(BaseModel):
    id: int
    # name: str
    # status: bool
    balance: float

    def seedMoney(self, amount: int):
        self.balance += amount

    def withdraw(self, amount: float):
        if self.balance < amount:
            return False
        self.balance -= amount
        return True

    def deposit(self, amount: float):
        if self.balance < amount:
            return False
        self.balance += amount
        return True


class Transaction(BaseModel):
    id: int
    amount: float
    operation: str

    def custom_validate(self):
        pass

    def abort(self):
        pass


class Logger():

    id: int
    def log(self, transaction: Transaction):
        return True
