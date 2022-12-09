from flask_restful import Api,Resource,reqparse
from flask import Flask
from flask_marshmallow import Marshmallow

app = Flask(__name__)
api = Api(app)
ma = Marshmallow(app)

