from flask_restful import Resource,reqparse
from data.iemail_repo import IEmailRepo
from data.emailaddress import EmailAddress

parser = reqparse.RequestParser()
parser.add_argument('address', type=str)

class RegisterController(Resource):
    def __init__(self, email_repo: IEmailRepo):
        self.repo = email_repo
    def put(self):
        args = parser.parse_args()
        email = EmailAddress(args['address'])
        self.repo.insert(email)
        return email.publicId
    def get(self):
        return "Test"
    def delete(self, public_id):
        pass

class TestController(Resource):
    def get(self):
        return "Test" 