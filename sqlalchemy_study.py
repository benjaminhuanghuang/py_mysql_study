# coding: utf-8
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

# connect to database
# 'database type+db driver://username:password@server_address:port/db_name'
#  sqllite: create_engine('sqlite:///:memory:')
#  default driver to mysql is mysqldb
# echo 是为了方便 控制台 logging 输出一些sql信息，默认是False
engine = create_engine("mysql+pymysql://root:ben123@127.0.0.1:3308/ben_test_db?charset=utf8", encoding="utf-8",
                       echo=True)

# 获取元数据
metadata = MetaData()
# 定义表
user_table = Table('user', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String(20)),
                   Column('fullname', String(40)),
                   )

address_table = Table('address', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('user_id', None, ForeignKey('user.id')),
                      Column('email', String(60), nullable=False)
                      )
# 创建数据表，如果数据表存在，则忽视
metadata.create_all(engine)
# 获取数据库连接
conn = engine.connect()
