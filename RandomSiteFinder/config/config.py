import os

class Config(object):
    def __init__(self, config):
        self._config = config # set it to conf

    def get_property(self, property_name):
        if property_name not in self._config.keys(): # we don't want KeyError
            return None  # just return None if not found
        return self._config[property_name]

class EnvConfig(Config): 
    def __init__(self):
        configs = {}
        configs["SENDER_EMAIL"] = os.environ.get("SENDER_EMAIL")
        configs["ENVIRONMENT"] = os.environ.get("ENVIRONMENT")
        configs["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
        configs["SENDER_MESSAGE"] = os.environ.get("SENDER_MESSAGE")
        Config.__init__(self, configs) 

    @property
    def sender_email(self):
        return self.get_property("SENDER_EMAIL")

    @property
    def sender_message(self):
        return self.get_property("SENDER_MESSAGE")

    @property
    def environment(self):
        return self.get_property("ENVIRONMENT")

    @property
    def sql_db_uri(self):
        return self.get_property("SQLALCHEMY_DATABASE_URI")
    
