from datetime import datetime, timedelta
from data import db

class EmailTransaction(db.Model):
    __tablename__ = "EmailTransactions"
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255))
    date = db.Column(db.DateTime)

    def __init__(self, **kwargs):
        self.date = datetime.now()
        if 'address' in kwargs:
            self.address = kwargs['address']
        if 'date' in kwargs:
            self.date = kwargs['date']

    def __repr__(self):
        return  f"User(id={self.id!r}, address={self.address!r}, date={self.date!r}"

    def is_recent(self):
        return self.date > datetime.now() - timedelta(minutes=5)