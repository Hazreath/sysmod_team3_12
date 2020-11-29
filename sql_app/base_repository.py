from sqlalchemy.orm import Session


class BaseRepository:
    def __init__(self, db: Session, model):
        self.db = db
        self.model = model

    def get_by_id(self, id_search: int):
        return self.db.query(self.model).filter(self.model.id == id_search).first()

    def get_by_email(self, email: str):
        return self.db.query(self.model).filter(self.model.email == email).first()

    def get_list(self, skip: int = 0, limit: int = 100):
        return self.db.query(self.model).offset(skip).limit(limit).all()

