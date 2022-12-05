import abc
from data import EmailTransaction
from typing import List

class IEmailTransactionRepo(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def insert(self, model: EmailTransaction):
        pass
    @abc.abstractclassmethod
    def get(self, address) -> List[EmailTransaction]:
        pass