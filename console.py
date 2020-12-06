import click

import business
from business.models.bank import TransactionCreateInput
from sql_app import models
from sql_app.account_repository import AccountRepository
from sql_app.base_repository import BaseRepository
from sql_app.database import SessionLocal
from sql_app.models import Transaction, User, Account
from sql_app.transaction_repository import TransactionRepository
from sql_app.user_repository import UserRepository
import re

db = SessionLocal()
# Error codes
ERROR_EMAIL_ALREADY_IN_USE = -1
ERROR_EMAIL_FORMAT_INCORRECT = -2
ERROR_USER_DOES_NOT_EXIST = -3
ERROR_ACCOUNT_DOES_NOT_EXIST = -4
ERROR_NOT_ENOUGH_MONEY = -5
ERROR_ACCOUNT_DISABLED = -5


@click.group()
def commands():
    pass


@click.command(name="create_user")
@click.argument('email', type=str)
@click.argument('password', type=str)
def create_user(email, password):
    """
    Create account with specified credentials, arguments: email password.\n
    Example: python console.py create_user receiver@mailcom 1234
    """
    user_repo = UserRepository(db)

    # check if user does not exists
    db_user = user_repo.get_by_email(email)

    if db_user:
        click.echo("User with same email already exists.")
        return ERROR_EMAIL_ALREADY_IN_USE

    # check email format
    format = "\w+@\w+.\w+"
    s = re.search(format, email)

    if not s:
        click.echo("The specified email does not match the standard email format")
        return ERROR_EMAIL_FORMAT_INCORRECT
    ucreate = business.models.user.UserCreate(email=email, password=password)
    new_user: User = user_repo.create_user(ucreate)

    click.echo("Created account " + email + " with pass " + password)

@click.command(name="delete_user")
@click.argument('id', type=int)
def delete_user(id):
    """
       Delete the user with the specified id
       ex : python console.py delete_user 7
    """
    user_repo = UserRepository(db)
    base_repo = BaseRepository(db, User)
    u = base_repo.get_by_id(id)
    if not u:
        click.echo("User with specified id does not exists.")
        return ERROR_USER_DOES_NOT_EXIST
    user_repo.delete_user(u)
    click.echo("User with id " + str(id) + " has been deleted.")


@click.command(name='create_transaction')
@click.argument('author', type=int)
@click.argument('receiver', type=int)
@click.argument('amount', type=float)  # will get from user as string but need to be an int
def create_transaction(author, receiver, amount):
    """
    Create transaction with arguments: author, receiver,amount.\n
    Example: python konsole.py create-trans author@mail.com receiver@mailcom 1234
    """

    account_repo = AccountRepository(db)
    a = account_repo.get_by_id(author)
    r = account_repo.get_by_id(receiver)
    if a is None or r is None:
        click.echo("One or both of the user don't exist.")
        return ERROR_USER_DOES_NOT_EXIST
    if a.balance < amount:
        click.echo("Author does not have enough money (<" + str(amount) + ").")
        return ERROR_NOT_ENOUGH_MONEY
    if not (a.enabled and r.enabled):
        click.echo("One or both of the accounts are disabled.")
        return ERROR_ACCOUNT_DISABLED

    trans_repo = TransactionRepository(db)
    _transaction = Transaction(source_account=author, dest_account=receiver, amount=amount)
    trans_repo.create_transaction(_transaction,a,r)
    click.echo(f"Transaction was created successfully.")


@click.command(name='undo_transaction')
@click.argument('id', type=int)
def undo_transaction(id):
    """
    Undo the specified transaction, arguments: transaction_id.\n
    Example: python console.py undo_transaction 4
    """
    transaction_repository = TransactionRepository(db)
    transaction: Transaction = transaction_repository.undo_transaction_by_id(id)

    if transaction is None:
        click.echo('transaction not found')
        return

    click.echo('transaction undo')


@click.command(name='enable_account')
@click.argument('id', type=int)
@click.argument('value', type=bool)
def enable_account(id, value):
    """
        Enable/disable the account designed by argument id, depending
        of value.
        ex : python console.py enable_account 3 False
    """
    account_repo = AccountRepository(db)
    acc: Account = account_repo.get_by_id(id)
    if acc is None:
        click.echo("Account with specified ID does not exists.")
        return ERROR_ACCOUNT_DOES_NOT_EXIST

    acc.enabled = value
    account_repo.enable_account(acc, value)
    msg = "Account n°" + str(id) + " enabled is now " + str(value) + "."
    click.echo(msg)

@click.command(name='create_seed_transaction')
@click.argument('receiver', type=int)
@click.argument('amount', type=float)
def create_seed_transaction(receiver, amount):
    """
    Add money to the specified account, arguments: receiver,amount.\n
    Example: python console.py create_seed_transaction receiver@mailcom 1234
    """
    transaction = TransactionCreateInput(dest_account_email=receiver, amount=amount)

    transaction_repository = TransactionRepository(db)
    account_repository = AccountRepository(db)

    account = account_repository.get_by_user_id(receiver)
    if account is None:
        click.echo('account not found')
        return

    print(f'account {account}')

    transaction_repository.create_seed_transaction(transaction, account)

    print(transaction)
    click.echo(f'Transaction created {account} {account.balance}')

@click.command(name='test')
@click.argument('t_id', type=int)
def test_command(name):
    pass

# Adding commands
commands.add_command(create_user)
commands.add_command(create_transaction)
commands.add_command(create_seed_transaction)
commands.add_command(undo_transaction)
#commands.add_command(delete_user) TEST FEATURE
commands.add_command(enable_account)

if __name__ == "__main__":
    # undo_transaction()
    # create_seed_transaction()
    commands()

