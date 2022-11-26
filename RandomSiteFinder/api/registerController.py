from flask_restful import Resource,reqparse
from data.iemail_repo import IEmailRepo
from data.emailaddress import EmailAddress



class RegisterController(Resource):
    def __init__(self, email_repo: IEmailRepo):
        self.repo = email_repo
    def put(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('address', type=str, help='email address')
            args = parser.parse_args()
            email = EmailAddress(address=args['address'])
            self.repo.insert(email)
        except Exception as err:
            print(f"Something went wrong {err=}, {type(err)=}")
        return email.publicId
    def get(self):
        return "Test"
    def delete(self, public_id):
        pass

class TestController(Resource):
    def get(self):
        return "Test" 