from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from data.emailaddress import EmailAddress
from data.iemail_repo import IEmailRepo

class EmailRepository(IEmailRepo):
    def __init__(self, **kwargs):
        engine = kwargs.get('engine')
        if engine is None:
            self.engine = create_engine("sqlite://", echo=True, future=True)

    def insert(self, obj):
        with Session(self.engine) as session:
            session.add(obj)
            session.commit()

    def get(self, public_id):
        with Session(self.engine) as session:
            q = session.query(EmailAddress).filter(EmailAddress.publicId == public_id)
            return q.get()

    def delete(self, public_id):
        with Session(self.engine) as session:
            session.delete(public_id)
            session.flush()