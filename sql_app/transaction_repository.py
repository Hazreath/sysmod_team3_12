from sqlalchemy.orm import Session

from business.models.bank import Account, TransactionCreateInput
from sql_app import models
from sql_app.base_repository import BaseRepository
from sql_app.models import Transaction
from business.models.user import User
from sqlalchemy import or_


class TransactionRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db, models.Transaction)

    def get_user_transactions(self, user: User):
        return self.db.query(models.Transaction).filter(
            or_(
                models.Transaction.source_account_id == user.id,
                models.Transaction.dest_account_id == user.id,
            )
        ).all()


    def create_transaction(self, transaction: TransactionCreateInput, source_account: Account, dest_account: Account):
        db_transaction = models.Transaction(source_account_id=source_account.id, dest_account_id=dest_account.id,
                                            amount=transaction.amount,modified=False)

        source_account.balance = source_account.balance - transaction.amount
        dest_account.balance = dest_account.balance + transaction.amount

        self.db.add(db_transaction)
        self.db.commit()
        self.db.refresh(db_transaction)
        self.db.refresh(source_account)
        self.db.refresh(dest_account)

        return db_transaction


    def undo_transaction_by_id(self, transaction_id: int):
        transaction: Transaction = self.db.query(self.model).filter(self.model.id == transaction_id).first()

        if transaction is None:
            return None

        source_account: models.Account = self.db.query(models.Account).filter(models.Account.id == transaction.source_account_id).first()
        dest_account: models.Account = self.db.query(models.Account).filter(models.Account.id == transaction.dest_account_id).first()

        new_transaction = TransactionCreateInput(amount=transaction.amount, dest_account_email='')

        return self.create_transaction(new_transaction, source_account=dest_account, dest_account=source_account)


    def create_seed_transaction(self, transaction: TransactionCreateInput, dest_account: Account):
        dest_account.balance = dest_account.balance + transaction.amount
        self.db.commit()
        self.db.refresh(dest_account)

        return dest_account

    def has_been_modified(self,t_id):
        t = self.db.query(self.model).filter(self.model.id == t_id).first()
        #t = self.db.query(Transaction).get(id)
        # setattr(t,'modified', True)
        t.modified = True
        print("my id ",t_id)
        #print("Result : ",t)
        return self.db.commit()
