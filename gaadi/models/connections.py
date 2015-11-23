__author__ = 'yusuf'
import pymysql

class mysql_con():
    def __init__(self, db):
        try:
            self.con = pymysql.connect(host='localhost',
                             user='root',
                             passwd='root',
                             db=str(db),
                             autocommit=True,
                             cursorclass=pymysql.cursors.DictCursor)
            self.cur = self.con.cursor()

        except Exception as e:
            print e

    def execute_query(self, sql_statement):
        self.cur.execute(sql_statement)
        return self.cur.fetchall()

    def insert_query(self, sql_statement):
        return self.cur.execute(sql_statement)

    def close_con(self):
        if self.con:
            self.con.close()
