from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from business.models.user import User, UserCreate
from middleware.get_current_user import get_current_active_user
from sql_app.get_db import get_db
from sql_app.user_repository import UserRepository

from fastapi import APIRouter
router = APIRouter()


@router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)

    db_user = user_repository.get_by_email(user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return user_repository.create_user(user=user)


@router.get("/users/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)

    users = user_repository.get_list(skip=skip, limit=limit)

    return users


@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)

    db_user = user_repository.get_by_id(user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user


@router.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
