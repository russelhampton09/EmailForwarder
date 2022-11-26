from sqlalchemy import String, DateTime, Integer, Column, create_engine
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase
import datetime
import uuid

class EmailAddress(DeclarativeBase):
    __tablename__ = "emailaddress"
    id = Column(Integer, primary_key=True)
    publicId = UUID()
    address = Column(String(255))
    date = Column(DateTime)

    def __init__(self, **kwargs):
        publicId=uuid.uuid1()
        date=datetime.datetime.now()
        address = kwargs['address']

    def __repr__(self):
        return f"User(id={self.id!r}, address={self.address!r}, date={self.date!r}, publicId={self.publicId})"
