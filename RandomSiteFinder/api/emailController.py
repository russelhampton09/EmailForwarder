from flask import jsonify
from flask_restful import Resource,reqparse
from data.email_transaction_repo import IEmailTransactionRepo
from data import EmailTransaction
from api import ma

class EmailTransactionSchema(ma.Schema):
    class Meta:
        fields = ('id','addres','date')

schema = EmailTransactionSchema()
schemas = EmailTransactionSchema(many=True)

class EmailController(Resource):
    def __init__(self, email_repo: IEmailTransactionRepo):
        self.repo = email_repo
    def put(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('address', type=str, help='email address')
            args = parser.parse_args()
            email = EmailTransaction(**args)
            self.repo.insert(email)
        except Exception as err:
            print(f"Something went wrong {err=}, {type(err)=}")
        return "message sent"
    def get(self):
        return schemas.dump(self.repo.get('blah'))
    def delete(self, public_id):
        pass

class TestController(Resource):
    def get(self):
        return "Test" 