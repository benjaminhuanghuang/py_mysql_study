from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from models import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 1 to many relation
    books = relationship('Book')