from flask import jsonify
from flask_restful import Resource,reqparse
from data.email_transaction_repo import IEmailTransactionRepo
from data.email_transaction import EmailTransaction
from api import ma
from services.email_sender import IEmailSender

class EmailTransactionSchema(ma.Schema):
    class Meta:
        fields = ('id','addres','date')

schema = EmailTransactionSchema()
schemas = EmailTransactionSchema(many=True)

class EmailController(Resource):
    def __init__(self, email_repo: IEmailTransactionRepo, email_sender: IEmailSender, **kwargs):
        self.repo = email_repo
        self.email_sender = email_sender
        if 'config' in kwargs:
            self.message = kwargs['config'].sender_message
        else:
            self.message = "Hello! This message is from Russel's learning python app! I'm learning python and cloud hosting with AWS! Someone hit my api and provided this email."    

    def put(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('address', type=str, help='email address destination')
            args = parser.parse_args()
            email_transaction = EmailTransaction(**args)

            latest_transactions = self.repo.get(**args)
            latest_transaction = None
            
            if latest_transactions is not None and latest_transactions:
                latest_transaction = latest_transactions[0]

            
            if latest_transaction is not None and latest_transaction.is_recent():
                return "Email sent recently to that address, rate limiting"
            
            self.email_sender.send(email_transaction.address)
            self.repo.insert(email_transaction)
                
        except Exception as err:
            print(f"Something went wrong {err=}, {type(err)=}")
            return "Message not sent! Something went wrong..."
        return "message sent"