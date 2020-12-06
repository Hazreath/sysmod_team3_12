from typing import List

from fastapi import Depends, HTTPException
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from business.models.bank import Transaction, TransactionCreateInput, Account, TransactionModifyInput
from business.models.user import User
from middleware.get_current_user import get_current_active_user
from sql_app.account_repository import AccountRepository
from sql_app.get_db import get_db
from sql_app.transaction_repository import TransactionRepository

router = APIRouter()
# HTTP EXCEPTIONS
EXC_SAME_ACCOUNT = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Error : sender and destination is same account.",
    # headers={"WWW-Authenticate": "Bearer"},
)
EXC_NOT_ENOUGH_MONEY = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Error : your balance is too low.",
    # headers={"WWW-Authenticate": "Bearer"},
)
EXC_ACC_DISABLED = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Error : one or both of the accounts involved are disabled.",
    # headers={"WWW-Authenticate": "Bearer"},
)
EXC_ACC_DONT_EXIST = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Error : destination account does not exists.",
    # headers={"WWW-Authenticate": "Bearer"},
)


def validate_transaction(source_account: Account, transaction: TransactionCreateInput):
    # 3) Then creates the transaction

    if transaction.amount <= 0:
        raise Exception('amount is negative or equal to 0')
    elif source_account.balance - transaction.amount < 0:
        raise Exception('Not enough money')


@router.get('/transaction', response_model=List[Transaction])
def get_user_transactions(current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    transaction_repository = TransactionRepository(db)
    transactions = transaction_repository.get_user_transactions(current_user)

    print(f'transactions = {transactions}')

    return transactions


@router.post('/transaction', response_model=Transaction)
def create_transaction(transaction: TransactionCreateInput, current_user: User = Depends(get_current_active_user),
                       db: Session = Depends(get_db)):
    transaction_exception = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Transaction impossible",
        # headers={"WWW-Authenticate": "Bearer"},
    )

    if transaction.dest_account_email == current_user.email:
        raise EXC_SAME_ACCOUNT

    account_repository = AccountRepository(db)
    transaction_repository = TransactionRepository(db)

    source_account = account_repository.get_by_user_id(current_user.id)

    # 1) check if the User account balance has enough money
    try:
        validate_transaction(source_account, transaction)
    except Exception:
        raise EXC_NOT_ENOUGH_MONEY

    # 2) check if "transaction.dest_account_email" exists -> get the account linked to it.
    dest_account = account_repository.get_by_user_email(transaction.dest_account_email)
    if dest_account is None:
        raise EXC_ACC_DONT_EXIST

    # 3) check if both accounts are enabled
    if not (source_account.enabled and dest_account.enabled):
        raise EXC_ACC_DISABLED

    transaction = transaction_repository.create_transaction(transaction, source_account, dest_account)

    return transaction


@router.post('/transaction/modify', response_model=Transaction)
def modify_transaction(transaction: TransactionModifyInput, current_user: User = Depends(get_current_active_user),
                       db: Session = Depends(get_db)):

    transaction_repository = TransactionRepository(db)
    account_repository = AccountRepository(db)
    t = transaction_repository.get_by_id(transaction.id)
    source_account = account_repository.get_by_user_id(current_user.id)


    # 1) check if the User account balance has enough money
    try:
        validate_transaction(source_account, t)
    except Exception:
        raise EXC_NOT_ENOUGH_MONEY

    # 2) check if "transaction.dest_account_email" exists -> get the account linked to it.
    dest_account = account_repository.get_by_user_email(transaction.dest_account_email)
    if dest_account is None:
        raise EXC_ACC_DONT_EXIST

    # 3) check if both accounts are enabled
    if not (source_account.enabled and dest_account.enabled):
        raise EXC_ACC_DISABLED

    # Undo previous transaction
    undo = transaction_repository.undo_transaction_by_id(transaction.id)

    # the transaction has been modified
    m = transaction_repository.has_been_modified(t.id)
    # Change amount
    # t.amount = transaction.amount
    transaction = transaction_repository.create_transaction(transaction, source_account, dest_account)

    return transaction

@router.post('/transaction/delete', response_model=Transaction)
def delete_transaction(transaction: TransactionModifyInput, current_user: User = Depends(get_current_active_user),
                       db: Session = Depends(get_db)):
    transaction_repository = TransactionRepository(db)
    account_repository = AccountRepository(db)
    t = transaction_repository.get_by_id(transaction.id)
    source_account = account_repository.get_by_user_id(current_user.id)

    # 1) check if the User account balance has enough money
    try:
        validate_transaction(source_account, t)
    except Exception:
        raise EXC_NOT_ENOUGH_MONEY

    # 2) check if "transaction.dest_account_email" exists -> get the account linked to it.
    dest_account = account_repository.get_by_user_email(transaction.dest_account_email)
    if dest_account is None:
        raise EXC_ACC_DONT_EXIST

    # 3) check if both accounts are enabled
    if not (source_account.enabled and dest_account.enabled):
        raise EXC_ACC_DISABLED

    # Delete/Undo previous transaction
    undo = transaction_repository.undo_transaction_by_id(transaction.id)

    # the transaction has been modified
    m = transaction_repository.has_been_modified(t.id)
    return undo
