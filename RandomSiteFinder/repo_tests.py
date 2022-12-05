import datetime
import unittest
from data import db, EmailTransaction
from data.email_transaction_repo import EmailTransactionRepo
from flask import Flask

class TestEmailRepo(unittest.TestCase):
    def test_inserts_gets_transactions(self):
        """
        Check that email transactions can be inserted and queried correctly
        """

    #Arranging. Flask-SQLALchemy tightly couples flask and sqlalch
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' 
        db.init_app(app)

        #add current scope to flask context
        app.app_context().push()
        db.drop_all()
        db.create_all()

        repo = EmailTransactionRepo(db)
        repo.insert(EmailTransaction(address='test@gmail.com'))
        repo.insert(EmailTransaction(address='test@gmail.com'))
        repo.insert(EmailTransaction(address='test@gmail.com'))
        repo.insert(EmailTransaction(address='test@gmail.com'))
        repo.insert(EmailTransaction(address='test@gmail.com'))
        result = repo.get('test@gmail.com')
        self.assertTrue(result)

        #cleanup
        db.drop_all()

    def test_email_transaction_recent(self):
        """
        Check that email transactions correctly reports if it is older than 5 minutes
        """
        transaction = EmailTransaction(address='test@gmail.com')
        self.assertTrue(transaction.is_recent()) 
        transaction = EmailTransaction(address='test@gmail.com',\
            date=datetime.datetime.now() - datetime.timedelta(minutes=10))
        self.assertFalse(transaction.is_recent())

if __name__ == '__main__':
    unittest.main()