"""


@author: Yauheni
"""

from model import *
from view import View


class Controller:
    def __init__(self) -> None:
        self.__model: Model = Model()
        self.__view: View = View()

    def create_admin(self, name: str) -> Admin:
        admin = self.__model.create_admin(name)
        self.__view.print(f'Admin name: \'{admin.name}\' created')
        return admin

    def create_customer(self, name: str) -> User:
        customer = self.__model.create_customer(name)
        self.__view.print(f'Customer name: \'{customer.name}\' created')
        return customer

    def create_account(self, admin: Admin, user: User, status: bool, balance: float) -> Account:
        account = admin.create_account(user, status, balance)
        self.__view.print(f'Account id: \'{account.id}\' created')
        return account

    def seed_money_to_account(self, admin: Admin, account: Account, money: float):
        admin.make_a_seed_transaction(account, money)
        self.__view.print(f'Admin seeded money to account id: \'{account.id}\' amount: {money}')

    def create_transaction(self, user: User, own_account: Account, destination_account: Account, money: float) -> Transaction:
        # todo Create Transaction with source and destination accounts

        pass



