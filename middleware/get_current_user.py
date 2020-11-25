from business.auth.auth_factory import auth_factory
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from business.models.user import User

#
# """
# Auth
# """
from fastapi.security import OAuth2PasswordBearer

from sql_app.get_db import get_db
from sql_app.user_repository import UserRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_repository = UserRepository(db)

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    user = auth_factory(user_repository).get_user_from_token(token)

    if user is None:
        raise credentials_exception

    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    # if current_user.disabled:
    #     raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
