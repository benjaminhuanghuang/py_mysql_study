from sqlalchemy import Column, String
from models import Base

class School(Base):
    __tablename__ = 'school'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
