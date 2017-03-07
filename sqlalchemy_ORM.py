# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.user import User
from models.book import Book

# connect to database
# 'database type+db driver://username:password@server_address:port/db_name'
#  default db driver is mysqldb
# echo 是为了方便 控制台 logging 输出一些sql信息，默认是False
engine = create_engine("mysql+pymysql://root:ben123@127.0.0.1:3308/ben_test_db?charset=utf8", encoding="utf-8",
                       echo=True)

DBSession = sessionmaker(bind=engine)
ses = DBSession()
#
# Create
#
new_user = User(id='5', name='Bob')
ses.add(new_user)
ses.commit()
ses.close()

#
# Query
#
user = ses.query(User).filter(User.id == '5').one()
print 'type:', type(user)
print 'name:', user.name
# 关闭Session:
ses.close()
