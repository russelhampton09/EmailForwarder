import abc

class IEmailTransactionRepo(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def insert(self, model):
        pass
    @abc.abstractclassmethod
    def get(self, address):
        pass