from config.config import Config
import os

class EnvConfig(Config): 
    def __init__(self):
        configs = {}
        configs["SENDER_EMAIL"] = os.environ.get("SENDER_EMAIL")
        configs["ENVIRONMENT"] = os.environ.get("ENVIRONMENT")
        configs["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
        configs["SENDER_MESSAGE"] = os.environ.get("SENDER_MESSAGE")
        configs["SENDER_KEY_HASH"] = os.environ.get("SENDER_KEY_HASH")
        Config.__init__(self, configs) 