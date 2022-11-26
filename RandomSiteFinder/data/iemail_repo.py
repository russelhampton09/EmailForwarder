import abc

class IEmailRepo(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def insert(obj):
        pass
    @abc.abstractclassmethod
    def get(public_id):
        pass
    @abc.abstractclassmethod
    def delete(public_id):
        pass