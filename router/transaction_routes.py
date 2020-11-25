from fastapi import Depends, HTTPException
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from business.models.bank import Transaction, TransactionCreateInput, Account
from business.models.user import User
from middleware.get_current_user import get_current_active_user
from sql_app.account_repository import AccountRepository
from sql_app.get_db import get_db
from sql_app.transaction_repository import TransactionRepository

router = APIRouter()

def validate_transaction(source_account: Account, transaction: TransactionCreateInput):
    # 3) Then creates the transaction

    if source_account.balance - transaction.amount < 0:
        raise Exception('not enough money')


@router.post('/transaction', response_model=Transaction)
def create_transaction(transaction: TransactionCreateInput, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    transaction_exception = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Transaction impossible",
        # headers={"WWW-Authenticate": "Bearer"},
    )

    if transaction.dest_account_email == current_user.email:
        raise transaction_exception


    account_repository = AccountRepository(db)
    transaction_repository = TransactionRepository(db)

    source_account = account_repository.get_by_user_id(current_user.id)



    # 1) check if the User account balance has enough money
    try:
        validate_transaction(source_account, transaction)
    except Exception:
        raise transaction_exception

    # 2) check if "transaction.dest_account_email" exists -> get the account linked to it.
    dest_account = account_repository.get_by_user_email(transaction.dest_account_email)
    if dest_account is None:
        raise transaction_exception

    transaction = transaction_repository.create_transaction(transaction, source_account, dest_account)

    return transaction
