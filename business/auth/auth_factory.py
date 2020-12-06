from business.auth.authenticate_users import JwtConfig, Auth
from business.auth.jwt_auth import JwtAuth
from sql_app.user_repository import UserRepository


jwt_config = JwtConfig(
    'dce20b68a0b29e729fd96d3806589fe1c0f7e1b2b7cfed2e471b3c1ec932bf3e',
    'HS256',
    30)


def auth_factory(user_repository: UserRepository) -> Auth:
    return JwtAuth(jwt_config, user_repository)
