"""


@author: Yauheni
"""
from __future__ import annotations

import tools


class Transaction:

    def __init__(self, id: int, amount: float, operation: str) -> None:
        self.__id = id
        self.__amount = amount
        self.__operation = operation

    def validate(self):
        pass

    def abort(self):
        pass


'''
Class user is a parent class for both customer (normal user of bank services) and admin (user with extended privileges)
'''


class Account:

    def __init__(self, user: User, status: bool, balance: float) -> None:
        self.__id = tools.generate_random_int()
        self.__user = user
        self.__status = status
        self.__balance = balance

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__user

    @property
    def status(self):
        return self.__status

    @property
    def balance(self):
        return self.__balance

    def send_money(self):
        pass

    def withdraw_money(self, money: float):
        self.__balance -= money

    def deposit_money(self, money: float):
        self.__balance += money


class User:

    def __init__(self, name: str) -> None:
        self.__id = tools.generate_random_int()
        self.__name = name

    @property
    def name(self):
        return self.__name

    def create_transaction(self):
        pass

    def modify_transaction(self):
        pass


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
