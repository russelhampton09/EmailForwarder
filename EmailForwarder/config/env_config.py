from config.config import Config
import os

class EnvConfig(Config): 
    def __init__(self):
        configs = {}
        configs["SENDER_EMAIL"] = os.environ.get("SENDER_EMAIL")
        configs["SENDER_KEY_HASH"] = os.environ.get("SENDER_KEY_HASH")
        
        configs["ENVIRONMENT"] = os.environ.get("ENVIRONMENT")
        if configs["ENVIRONMENT"] is None:
            configs["ENVIRONMENT"] = "development"
        
        configs["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
        if configs["SQLALCHEMY_DATABASE_URI"] is None:
            basedir = os.path.abspath(os.path.dirname(__file__))
            configs["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'database.db')
            
        configs["SENDER_MESSAGE"] = os.environ.get("SENDER_MESSAGE")
        if configs["SENDER_MESSAGE"] is None:
            configs["SENDER_MESSAGE"] = "Automated message from Russel's toy python app!"
        
        Config.__init__(self, configs) 