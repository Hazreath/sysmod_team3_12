"""


@author: Yauheni
"""
from __future__ import annotations

from typing import List

import tools


class Transaction:

    def __init__(self, user: User, source_account: Account, dest_account: Account, amount: float) -> None:
        self.__id = tools.generate_random_int()
        self.__amount = amount
        self.__user = user
        self.__source_account = source_account
        self.__dest_account = dest_account
        # todo continue transaction mechanism, transaction have to be created with status

        # completed is False upon creation, means transaction is just created and nothing have been transferred
        # as soon as decision is made and transaction becomes committed, no more modifications are allowed
        # to the transaction
        self.__completed = False
        # verified if False upon creation, means transaction is not verified by admin
        self.__verified = False
        # verified if False upon creation, means transaction is not aborted, if aborted becomes True
        self.__aborted = False

        self.__admin: Admin

    @property
    def user(self):
        return self.__user

    @property
    def source_account(self):
        return self.__source_account

    @property
    def dest_account(self):
        return self.__dest_account

    @property
    def amount(self):
        return self.__amount

    def validate(self, admin: Admin):
        if not self.__completed:
            self.__verified = True
            self.__aborted = False
            self.__admin = admin
        else:
            raise tools.TransactionAccomplishedError

    def abort(self, admin: Admin):
        if not self.__completed:
            self.__verified = False
            self.__aborted = True
            self.__admin = admin
        else:
            raise tools.TransactionAccomplishedError

    # Transaction is accomplish, decision if final, nothing can be changed any more
    def accomplish(self, admin: Admin):
        self.__completed = True
        self.__admin = admin

    # Returns tru ONLY if transaction is considered valid
    def is_verified(self) -> bool:
        return self.__verified and not self.__aborted

    # returns completion status
    def is_completed(self) -> bool:
        return self.__completed

    def __repr__(self) -> str:
        transaction_verification_status = ''
        if self.__verified and not self.__aborted and not self.__completed:
            transaction_verification_status = f'transaction if verified by {self.__admin.name}'
        elif not self.__verified and self.__aborted and not self.__completed:
            transaction_verification_status = f'transaction if denied by {self.__admin.name}'

        transaction_completion_status = ''
        if self.__completed:
            transaction_completion_status = 'transaction is completed'
        else:
            transaction_completion_status = 'transaction is not completed'

        return f'Transaction id: {self.__id} owner: {self.__user.name} amount: {self.__amount} ' \
               f'from {self.__source_account} to {self.__dest_account}' \
               f' {transaction_verification_status} {transaction_completion_status}'


class TransactionDataBase:
    """
    This class can only be created as single object (may be substitute with singleton)
    and is only used by model
    """

    def __init__(self) -> None:
        self.__pool: List[Transaction] = []

    def add_transaction(self, transaction: Transaction):
        self.__pool.append(transaction)


class UserDataBase:

    def __init__(self) -> None:
        self.__user_data_base: List[User] = []

    def add_user(self, user: User):
        self.__user_data_base.append(user)


class AccountDataBase:

    def __init__(self) -> None:
        self.__account_data_base: List[Account] = []

    def add_account(self, account: Account):
        self.__account_data_base.append(account)


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

    # only admin can check if transaction is valid
    def validate_transaction(self):
        pass

    def deny_transaction(self):
        pass

    # not sure what is it
    def make_a_seed_transaction(self, account: Account, money: float):
        account.deposit_money(money)


class Logger:
    pass


class Model:
    def __init__(self) -> None:
        # model have transaction pool, object that contains transactions
        self.__transaction_data_base = TransactionDataBase()
        self.__user_data_base = UserDataBase()
        self.__account_data_base = AccountDataBase()

        # model have logger

    def create_admin(self, name: str) -> Admin:
        admin = Admin(name)
        self.__user_data_base.add_user(admin)
        return admin

    def create_customer(self, name: str) -> Customer:
        customer = Customer(name)
        self.__user_data_base.add_user(customer)
        return customer

    def create_transaction(self, user: User, own_account: Account, destination_account: Account,
                           money: float) -> Transaction:
        """
        Mode method create transaction, add it to pool of transactions, assign status to transaction as not validated
        :param user:
        :param own_account:
        :param destination_account:
        :param money:
        :return:
        """

        # todo Написать создание транзакии, добавить в пул, транзакция должна быть логически верифицирована или нет, а
        # а также должен быть статус проведена ли транзакция

        transaction = Transaction(user, own_account, destination_account, money)
        self.__transaction_data_base.add_transaction(transaction)

        return transaction

    def check_transaction_validity(self, admin: Admin, transaction: Transaction):
        # I really don't know why do you want admin to check the transaction, might be it means he can do it manually
        # we check how much money have to be transferred and how much remains, later, maybe we add other conditions
        source_account = transaction.source_account

        balance = source_account.balance
        amount = transaction.amount

        if amount < balance:
            transaction.validate(admin)
        else:
            transaction.abort(admin)

    def complete_transaction(self, admin: Admin, transaction: Transaction):

        self.check_transaction_validity(admin, transaction)
        verified = transaction.is_verified()

        if verified:
            amount = transaction.amount
            transaction.source_account.withdraw_money(amount)
            transaction.dest_account.deposit_money(amount)

        transaction.accomplish(admin)

    def modify_transaction(self, user: User, transaction: Transaction, source_account: Account, dest_account: Account,
                           amount: float):
        """
        # conditions to modify transaction: 1. transaction belongs to user 2. source account belongs to user
        :param user:
        :param transaction:
        :param source_account:
        :param dest_account:
        :param amount:
        :return:
        """

        transaction_user = transaction.user
        account_user = source_account.user

        if not (user == transaction_user and user == account_user):
            raise tools.TransactionCantBeModified(
                'Your transaction dos not belong to user or source account does not belong')

    def create_account(self, admin: Admin, user: User, status: bool, balance: float) -> Account:
        account = Account(user, status, balance)
        return account
