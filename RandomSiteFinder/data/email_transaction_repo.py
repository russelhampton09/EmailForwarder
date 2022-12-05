from ast import List
from data import EmailTransaction
from data.iemail_transaction_repo import IEmailTransactionRepo
import datetime

class EmailTransactionRepo(IEmailTransactionRepo):
    def __init__(self, db):
        self.db = db

    def insert(self, model: EmailTransaction):
        self.db.session.add(model)
        self.db.session.commit()

    def get(self, address) -> List[EmailTransaction]:
        return [EmailTransaction.query.filter(EmailTransaction.address.like(address)).order_by(EmailTransaction.id.desc()).first()]