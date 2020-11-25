from sqlalchemy.orm import Session

from business.models.bank import Account
from sql_app import models
from sql_app.base_repository import BaseRepository
from sql_app.models import User


class AccountRepository(BaseRepository):

    def __init__(self, db: Session):
        super().__init__(db, models.Account)


    def get_by_user_id(self, user_id: int) -> Account:
        print(f'search account for user {user_id}')
        # As this is a one to one relation ship (account <-> user), we take the first one to apply a SQL LIMIT 1
        # first it's good for performance but also it will give only one result instead of an array of results, which makes sens.
        return self.db.query(self.model).filter(self.model.user_id == user_id).first()

    def get_by_user_email(self, email: str) -> Account:
        print(f'user: {self.model.user}')
        return self.db.query(self.model).join(User).filter(User.email == email).first()
