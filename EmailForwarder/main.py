from flask import Flask
from flask_marshmallow import Marshmallow
from data import db
from data.email_transaction_repo import EmailTransactionRepo
from api.emailController import EmailController
from flask_restful import Api
from config.env_config import EnvConfig
from services.email_sender import EmailSender

config = EnvConfig()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.sql_db_uri
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

api = Api(app)
ma = Marshmallow(app)
email_trans_repo = EmailTransactionRepo(db)
email_sender = EmailSender(config)

### Default splash page in case someone navigates here
@app.route('/')
def hello_world():
   return "Hello! Russel Hampton's flask api"

def init():
    api.add_resource(EmailController, '/email',resource_class_kwargs={'email_repo': email_trans_repo, 'email_sender':email_sender, 'config':config})
    app.run(host='0.0.0.0', port="5001")

if __name__ == '__main__':
    init()