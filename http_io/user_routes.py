from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from business.models import user
from business.models.user import User
from main import app, get_db, get_current_active_user
from sql_app.user_repository import UserRepository


@app.post("/users/", response_model=user.User)
def create_user(user: user.UserCreate, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)

    db_user = user_repository.get_by_email(user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return user_repository.create_user(user=user)


@app.get("/users/", response_model=List[user.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)

    users = user_repository.get_users(skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=user.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)

    db_user = user_repository.get_by_id(user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user


@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
