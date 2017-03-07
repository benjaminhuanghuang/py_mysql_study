# coding: utf-8
import pymysql
import sys

try:
    # 打开数据库连接
    conn = pymysql.connect(host='127.0.0.1', port=3308, user='root', passwd='ben123', db='ben_test_db', charset='utf8')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    print ("Database version : %s " % data)


except Exception as e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)
finally:
    if conn:
        # 关闭数据库连接
        conn.close()
