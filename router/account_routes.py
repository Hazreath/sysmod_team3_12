from typing import List

from fastapi import Depends, HTTPException
from fastapi import APIRouter
from sqlalchemy.orm import Session

from business.models.bank import Transaction, Account
from business.models.user import User
from middleware.get_current_user import get_current_active_user
from sql_app.account_repository import AccountRepository
from sql_app.get_db import get_db

router = APIRouter()


@router.get('/account', response_model=Account)
def get_account(current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    account_repository = AccountRepository(db)

    account = account_repository.get_by_user_id(current_user.id)

    print(account)

    return account


@router.get('/accounts', response_model=List[Account])
def get_accounts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    account_repository = AccountRepository(db)
    accounts = account_repository.get_list(skip=skip, limit=limit)

    return accounts
