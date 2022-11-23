from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from data.email_repo import EmailRepository

sqlengine = create_engine("sqlite://", echo=True, future=True)
email_repo = EmailRepository(engine=sqlengine)
base = declarative_base()
base.metadata.create_all(sqlengine)