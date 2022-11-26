from sqlalchemy import String, DateTime, Integer, Column, create_engine
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from datetime import datetime
import uuid

class EmailAddress(declarative_base()):
    __tablename__ = "emailaddress"
    id = Column(Integer, primary_key=True)
    publicId = UUID()
    address = Column(String(255))
    date = Column(DateTime)

    def __init__(self, **kwargs):
        publicId=uuid.uuid1()
        date=datetime.time()
        address = kwargs['address']

    def __repr__(self):
        return f"User(id={self.id!r}, address={self.address!r}, date={self.date!r}, publicId={self.publicId})"
