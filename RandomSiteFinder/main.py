from flask import Flask
from flask_marshmallow import Marshmallow
from data import db
from data.email_transaction_repo import EmailTransactionRepo
from api.emailController import EmailController
from flask_restful import Api
from config.config import EnvConfig

config = EnvConfig()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.sql_db_uri
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

api = Api(app)
ma = Marshmallow(app)
email_trans_rpeo = EmailTransactionRepo(db)

def init():
    api.add_resource(EmailController, '/email',resource_class_kwargs={'email_repo': email_trans_rpeo})
    app.run(debug=False, port="5001")
    # with app.app_context():
    #     db.create_all()

if __name__ == '__main__':
    init()