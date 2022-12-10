class Config(object):
    def __init__(self, config):
        self._config = config # set it to conf

    def get_property(self, property_name):
        if property_name not in self._config.keys(): # we don't want KeyError
            return None  # just return None if not found
        return self._config[property_name]
    
    @property
    def sender_key(self):
        return self.get_property("SENDER_KEY_HASH")
        
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
    

    
