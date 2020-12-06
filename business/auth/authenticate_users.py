from abc import ABCMeta, abstractmethod
from typing import Optional

from attr import dataclass
from sqlalchemy.orm import Session

from business.models.user import User
from sql_app.user_repository import UserRepository


@dataclass(frozen=True)
class JwtConfig:
    # to get a string like this run:
    # openssl rand -hex 32
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int


class Auth(metaclass=ABCMeta):
    @abstractmethod
    def get_user_from_token(self, token) -> Optional[User]:
        pass


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
