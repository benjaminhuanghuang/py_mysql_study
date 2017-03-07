from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'school'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
