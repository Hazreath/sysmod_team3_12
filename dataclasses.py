from dataclasses import dataclass

@dataclass
class Account:
    id: int
    name: str
    status: bool
    balance: float

    def seedMoney(self, amount:int):
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

@dataclass
class Transaction:
    id: int
    amount: float
    operation: str

    def validate(self):
        pass

    def abort(self):
        pass

@dataclass
class Logger:
    id: int
    def log(self, transaction: Transaction):
        return True

