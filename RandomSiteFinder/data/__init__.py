from sqlalchemy import create_engine
from data.email_repo import EmailRepository

sqlengine = create_engine("sqlite://", echo=True, future=True)
email_repo = EmailRepository(engine=sqlengine)