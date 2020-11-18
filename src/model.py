"""


@author: Yauheni
"""
from __future__ import annotations

from typing import List

import tools


class Transaction:

    def __init__(self, id: int, amount: float, user: User, source_account: Account, dest_account: Account) -> None:
        self.__id = tools.generate_random_int()
        self.__amount = amount
        self.__user = user
        self.__source_account = source_account
        # todo continue transaction mechanism
        # self.__operation = operation

    def validate(self):
        pass

    def abort(self):
        pass


'''
Class user is a parent class for both customer (normal user of bank services) and admin (user with extended privileges)
'''

"""
Class Account can have only one user by definition, but admins can do whatever with any account,
Any user can have many accounts
"""


class Account:

    def __init__(self, user: User, status: bool, balance: float) -> None:
        self.__id = tools.generate_random_int()
        self.__user = user
        self.__status = status
        self.__balance = balance
        # each user know account he have
        self.__user.add_account(self)

    @property
    def id(self) -> int:
        return self.__id

    @property
    def user(self) -> User:
        return self.__user

    @property
    def status(self) -> bool:
        return self.__status

    @property
    def balance(self) -> float:
        return self.__balance

    def send_money(self):
        pass

    def withdraw_money(self, money: float):
        self.__balance -= money

    def deposit_money(self, money: float):
        self.__balance += money

    def __repr__(self) -> str:
        return f'account id: {self.__id} owner: {self.__user.name} balance: {self.__balance}'


class User:

    def __init__(self, name: str) -> None:
        self.__id = tools.generate_random_int()
        self.__name = name
        # todo Add lists
        self.__accounts: List[Account] = []

    @property
    def name(self):
        return self.__name

    def create_transaction(self):
        pass

    def modify_transaction(self):
        pass

    def add_account(self, account: Account):
        self.__accounts.append(account)

    def __repr__(self) -> str:
        return f'user: {self.__name}, accounts: {len(self.__accounts)}'


class Customer(User):

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def check_balance(self):
        pass


class Admin(User):

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def check_logs(self):
        pass

    def validate_transaction(self):
        pass

    def deny_transaction(self):
        pass

    def create_account(self, user: User, status: bool, balance: float) -> Account:
        # def __init__(self, user: User, status: bool, balance: float) -> None:
        account = Account(user, status, balance)
        return account

    # not sure what is it
    def make_a_seed_transaction(self, account: Account, money: float):
        account.deposit_money(money)


class Logger:
    pass


class Model:
    def __init__(self) -> None:
        pass

    def create_admin(self, name: str) -> Admin:
        return Admin(name)

    def create_customer(self, name: str) -> Customer:
        return Customer(name)
