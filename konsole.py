import click
from dataclasses import dataclass

@dataclass
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
        click.echo(f"Admin user with {email} was created succesfully.")
    else:
        _account = CreateAccount(email,password) 
        click.echo(f"User with {email} was created succesfully.")
    # TODO:  Integrate with model
    
    


@cli.command(name='create-trans')
@click.argument('author',type=str)
@click.argument('receiver',type=str)
@click.argument('amount',type=str)#will get from user as string but need to be an int
def create_transaction(author,receiver,amount):
    """
    Create transaction with arguments: author, receiver,amount.\n
    Example: python konsole.py create-trans author@mail.com receiver@mailcom 1234
    """
    #TODO: Validate amount
    click.echo(f"User with author:{author} was created succesfully.")


@cli.command(name='undo-trans')
@click.argument('id')
def undo_trans(id):
    """
    Undo transaction with arguments: id.
    Example:  python konsole.py undo-trans 123
    """
    #TODO: undo transaction in model

if __name__ == '__main__':
    cli()