import unittest
from data import db, EmailTransaction
from data.email_transaction_repo import EmailTransactionRepo
from flask import Flask
from flask_restful import Api

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
        repo.insert(EmailTransaction('test@gmail.com'))
        result = repo.get('testdatenotusedyet')
        self.assertTrue(result)

        #cleanup
        db.drop_all()


if __name__ == '__main__':
    unittest.main()