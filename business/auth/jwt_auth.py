from typing import Optional

from jose import jwt, JWTError

from business.auth.authenticate_users import Auth, JwtConfig
from business.models.token import TokenData
from business.models.user import User
from sql_app.repository import UserRepository


class JwtAuth(Auth):

    def __init__(self, jwt_config: JwtConfig, user_repository: UserRepository):
        self.user_repository = user_repository
        self.jwt_config = jwt_config


    def get_user_from_token(self, token) -> Optional[User]:
        try:
            payload = jwt.decode(token, self.jwt_config.SECRET_KEY, algorithms=[self.jwt_config.ALGORITHM])
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
