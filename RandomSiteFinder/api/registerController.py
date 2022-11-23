from flask_restful import Resource,reqparse
from data.iemail_repo import IEmailRepo

class RegisterController(Resource):
    def __init__(self, email_repo: IEmailRepo):
        self.repo = email_repo
    def put(self):
        parser = reqparse.RequestParser()
        args = parser.parse_args()
        self.repo.insert(args)
    def get(self, public_id):
         self.repo.get(public_id)
    def delete(self, public_id):
        pass
