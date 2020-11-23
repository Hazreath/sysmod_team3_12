from datetime import timedelta
from typing import List

from fastapi import FastAPI, HTTPException, Depends, status

from business.models.token import TokenData, Token
from business.models.user import User
from business.token import create_access_token
from sql_app import models, repository
from business.models import user
from sqlalchemy.orm import Session
from sql_app.database import SessionLocal, engine
from sql_app.repository import get_user_by_email

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=user.User)
def create_user(user: user.UserCreate, db: Session = Depends(get_db)):
    db_user = repository.get_user_by_email(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return repository.create_user(db=db, user=user)


@app.get("/users/", response_model=List[user.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = repository.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=user.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = repository.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

"""
Auth
"""
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "dce20b68a0b29e729fd96d3806589fe1c0f7e1b2b7cfed2e471b3c1ec932bf3e"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception

    user = get_user_by_email(db, email=token_data.email)

    if user is None:
        raise credentials_exception

    return user

def verify_password(plain_password, hashed_password):
    # return pwd_context.verify(plain_password, hashed_password)
    return plain_password == hashed_password


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    # if current_user.disabled:
    #     raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)

    if not user:
        return False

    if not verify_password(password, user.hashed_password):
        return False

    return user


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # <!> form_data.username but it will be an email. Confusing but we use the generic OAuth2PasswordRequestForm
    user = authenticate_user(db, form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

