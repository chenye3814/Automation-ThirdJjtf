#-*- coding:UTF-8 -*-
import pymysql
import time

mysql_agency210_inner = {
    'host':'192.168.10.210',
    'port':3306,
    'user':'root',
    'password':'123456!@#',
    'charset':'UTF8'
    }

mysql_stocksir230_inner = {
    'host':'192.168.10.230',
    'port':3306,
    'user':'stocksir',
    'password':'stocksir1704!',
    'charset':'UTF8'
    }

class mysql_use:
    def __init__(self,host,port,user,password,database,charset):
        "使用预先配置好的字典连接数据库时，还需要单独添加‘数据库名’"
        self.host = host
        self.port = port
        self.user = user
        self.passwd = password
        self.db = database
        self.charset = charset
        self.conn = ''
        self.cur = ''
        #连接数据库：
        try:
            self.conn = pymysql.connect(host = self.host,
                                      port = self.port,
                                      user = self.user,
                                      password = self.passwd,
                                      database = self.db,
                                      charset = self.charset)
            self.cur = self.conn.cursor()
            print('connect success')
        except Exception as e:
            print (e)
            print('connect fail')

    def mysql_sql(self,sql):
        try:
            result = []
            result.append(self.cur.execute(sql))
            result.append(self.cur.fetchall())
            print('sql success')
            return result
        except Exception as e:
            print(e)
            print('sql fail')

    def mysql_close(self):
        self.conn.close()
        print('connect closed')

    def example(self):
        # test = mysql_use(host=mysql_agencyonly['host'],
        #                  port=mysql_agencyonly['port'],
        #                  user=mysql_agencyonly['user'],
        #                  password=mysql_agencyonly['password'],
        #                  database='agency',
        #                  charset=mysql_agencyonly['charset'])
        test = mysql_use(**mysql_stocksir230_inner, database='stocksir')  # 这个传入参数方式最简洁
        result = test.mysql_sql("SELECT member_name,member_id from stock_member where member_mobile='13551833814'")
        print(result)
        test.mysql_close()






