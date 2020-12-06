"""


@author: Yauheni
"""

from src.model import *
from src.view import View


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
        account = self.__model.create_account(admin, user, status, balance)
        self.__view.print(f'Account id: \'{account.id}\' created')
        return account

    def seed_money_to_account(self, admin: Admin, account: Account, money: float):
        admin.make_a_seed_transaction(account, money)
        self.__view.print(f'Admin seeded money to account id: \'{account.id}\' amount: {money}')

    def create_transaction(self, user: User, own_account: Account, destination_account: Account,
                           money: float) -> Transaction:
        transaction = self.__model.create_transaction(user, own_account, destination_account, money)
        self.__view.print(f'transaction is created: \'{transaction}\' \n by {user.name} ')
        return transaction

    def check_transaction_validity(self, admin: Admin, transaction: Transaction):
        """
        Transaction is verified by admin and status is assigned
        :param admin:
        :param transaction:
        :return:
        """
        self.__model.check_transaction_validity(admin, transaction)
        self.__view.print(f'transaction validity is checked: \'{transaction}\' \n by {admin.name} ')

    def complete_transaction(self, admin: Admin, transaction: Transaction):
        """
        Transaction is again verified prior to completion
        :param admin:
        :param transaction:
        :return:
        """

        self.__model.complete_transaction(admin, transaction)
        self.__view.print(f'transaction completion is attempted: \'{transaction}\' \n by {admin.name} ')

    def modify_transaction(self, user: User, transaction: Transaction, source_account: Account, dest_account: Account,
                           amount: float):
        """
        Each of users are only allowed to modify his own transaction, only using his accounts as
        source account
        :param customer:
        :param transaction_2:
        :param account_1:
        :param account_2:
        :param param:
        :return:
        """

        self.__model.modify_transaction(user, transaction, source_account, dest_account, amount)
        self.__view.print(f'transaction modified: \'{transaction}\' \n by {user.name} ')