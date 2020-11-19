import click

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
    click.echo(f"User with {email} was created succesfully.")


@cli.command(name='create-trans')
@click.argument('author')
@click.argument('receiver')
@click.argument('amount')
def create_transaction(author,receiver,amount):
    """
    Create transaction with arguments: author, receiver,amount.\n
    Example: 
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