from sqlalchemy import Column, String, ForeignKey
from models import Base

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 1 user - multi book
    user_id = Column(String(20), ForeignKey('user.id'))
