from sqlalchemy.orm import Session

from business.models.bank import Account, TransactionCreateInput
from sql_app import models
from sql_app.base_repository import BaseRepository

class TransactionRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db, models.Transaction)

    def create_transaction(self, transaction: TransactionCreateInput, source_account: Account, dest_account: Account):
        db_transaction = models.Transaction(source_account_id=source_account.id, dest_account_id=dest_account.id, amount=transaction.amount)

        source_account.balance = source_account.balance - transaction.amount
        dest_account.balance = dest_account.balance + transaction.amount

        self.db.add(db_transaction)
        self.db.commit()
        self.db.refresh(db_transaction)
        self.db.refresh(source_account)
        self.db.refresh(dest_account)

        return db_transaction

    def create_seed_transaction(self, transaction: TransactionCreateInput, dest_account: Account):
        dest_account.balance = dest_account.balance + transaction.amount
        self.db.commit()
        self.db.refresh(dest_account)

        return dest_account
