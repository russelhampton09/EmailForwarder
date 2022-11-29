import datetime
import uuid
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class EmailTransaction(db.Model):
    __tablename__ = "EmailTransactions"
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255))
    date = db.Column(db.DateTime)

    def __init__(self, address):
        self.date=datetime.datetime.now()
        self.address = address

    def __repr__(self):
        return  f"User(id={self.id!r}, address={self.address!r}, date={self.date!r}"