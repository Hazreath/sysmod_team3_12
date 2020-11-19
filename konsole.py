import click
from src.model import *
import dataclasses

@dataclasses
class CreateAccount:
    """
    Dataclass for creating account with account email, password and isAdmin attributes
    """
    email: str
    password: str
    isAdmin: bool = False


@click.group()
def cli():
    """
    Usage: python konsole.py [OPTIONS] command-name [ARGUMENTS]
    """
    pass

@cli.command(name='create-account')
@click.argument('email', type=str)
@click.argument('password', type=str)
def create_account(email, password):
    """
    Create account with arguments: email, password.\n
    Example: python konsole.py create-account example@company.com example password123
    """
    if click.confirm('is it an admin account?'):
        _account = CreateAccount(email,password,True)
    else:
        _account = CreateAccount(email,password) 
    
    # TODO:  Integrate with model
    
    click.echo(f"User with {email} was created succesfully.")


@cli.command(name='create-trans')
@click.argument('author',)
@click.argument('receiver')
@click.argument('amount')
def create_transaction(author,receiver,amount):
    """
    Create transaction with arguments: author, receiver,amount.\n
    Example: python konsole.py create-trans author-mail receiver-mail 1234
    """
    click.echo(f"User with author:{author} was created succesfully.")


@cli.command(name='undo-trans')
@click.argument('id')
def undo_trans(id):
    """
    Undo transaction with arguments: id.
    Example: 
    """

if __name__ == '__main__':
    cli()