from typing import Optional

from sqlalchemy.orm import Session

from business.models.token import TokenData
from business.models.user import User
from sql_app.repository import UserRepository
from jose import JWTError, jwt

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "dce20b68a0b29e729fd96d3806589fe1c0f7e1b2b7cfed2e471b3c1ec932bf3e"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class JwtAuth:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository


    def get_user_from_token(self, token) -> Optional[User]:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            email: str = payload.get("sub")
            if email is None:
                return None

            token_data = TokenData(email=email)
        except JWTError:
            return None

        user = self.user_repository.get_by_email(token_data.email)

        if user is None:
            raise None

        return user


def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
    user_repository = UserRepository(db)

    user = user_repository.get_by_email(email)

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user


def verify_password(plain_password, hashed_password):
    # return pwd_context.verify(plain_password, hashed_password)
    return plain_password == hashed_password
