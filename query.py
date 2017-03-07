# coding: utf-8
from __future__ import print_function

import pymysql
import sys

try:
    conn = pymysql.connect(host='127.0.0.1', port=3308, user='root', passwd='ben123', db='ben_test_db', charset='utf8')

    cursor = conn.cursor()

    sql = 'SELECT * from `user`'
    rows = cursor.execute(sql)
    print("Number of rows : ", rows)

    data = cursor.fetchone()
    # data = cursor.fetchall()   # read all data

    print("Data: ", data)
except Exception as e:
    print("Error %d: %s" % e.args[0], e.args[1])
    sys.exit(1)
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
