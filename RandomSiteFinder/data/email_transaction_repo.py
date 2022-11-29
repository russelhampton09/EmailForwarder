from data import EmailTransaction
from data.iemail_transaction_repo import IEmailTransactionRepo

class EmailTransactionRepo(IEmailTransactionRepo):
    def __init__(self, db):
        self.db = db

    def insert(self, model: EmailTransaction):
        self.db.session.add(model)
        self.db.session.commit()

    def get(self, date):
        return EmailTransaction.query.all()