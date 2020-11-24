from sqlalchemy.orm import Session

from . import models
from business.models import user

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, user_id: int):
        return self.db.query(models.User).filter(models.User.id == user_id).first()


    def get_by_email(self, email: str):
        return self.db.query(models.User).filter(models.User.email == email).first()


    def get_users(self, skip: int = 0, limit: int = 100):
        return self.db.query(models.User).offset(skip).limit(limit).all()


    def create_user(self, user: user.UserCreate):
        # @todo: hash maybe?
        fake_hashed_password = user.password
        db_user = models.User(email=user.email, hashed_password=fake_hashed_password)

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        return db_user

#
# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item