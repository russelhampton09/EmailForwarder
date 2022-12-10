import abc


class IEmailSender(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def send(self, to):
        pass