import click

from business.models.bank import TransactionCreateInput
from sql_app.account_repository import AccountRepository
from sql_app.database import SessionLocal
from sql_app.transaction_repository import TransactionRepository
from sql_app.user_repository import UserRepository


@click.command(name='create-trans')
@click.argument('author', type=str)
@click.argument('receiver', type=str)
@click.argument('amount', type=str)  # will get from user as string but need to be an int
def create_transaction(author, receiver, amount):
    """
    Create transaction with arguments: author, receiver,amount.\n
    Example: python konsole.py create-trans author@mail.com receiver@mailcom 1234
    """

    # _transaction = Transaction("def", author, receiver, amount)
    click.echo(f"Transaction was created successfully.")

@click.command(name='create_seed_transaction')
@click.argument('receiver', type=int)
@click.argument('amount', type=float)
def create_seed_transaction(receiver, amount):
    transaction = TransactionCreateInput(dest_account_email=receiver, amount=amount)
    db = SessionLocal()

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

if __name__ == "__main__":
    create_seed_transaction()