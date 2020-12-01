from datetime import timedelta

from fastapi import Depends, HTTPException, FastAPI
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status
#
from business.auth.auth_factory import jwt_config
from business.models.token import Token
from business.token import create_access_token
from business.auth.authenticate_users import authenticate_user
from sql_app.get_db import get_db


from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware

router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # <!> form_data.username but it will be an email. Confusing but we use the generic OAuth2PasswordRequestForm
    user = authenticate_user(db, form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=jwt_config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}
