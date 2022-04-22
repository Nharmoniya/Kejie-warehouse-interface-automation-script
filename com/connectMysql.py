import pymysql
from KeJie.com.readYaml import getDatabase


class DbConnect():
    def __init__(self, database="congku"):
        db = getDatabase()
        ip = db['dbip']
        port = db['port']
        usr = db['usr']
        pwd = db['pwd']
        self.db = pymysql.connect(host=ip, port=port, user=usr, password=pwd,database=database)
        self.cursor = self.db.cursor()

    # 关闭数据库
    def close(self):
        self.db.close()

    # 封装select
    def select(self, sql):
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        # print(res)
        return res

    # 修改，删除，插入
    def execute(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            self.db.close()

if __name__=='__main__':
    dc = DbConnect()
    #查询dtmoban_mall科捷的库存
    sql1 = "select create_time from dtmoban_warehouse_in_warehouse_chuku WHERE czc_number='PO2022442768' ORDER BY ordersn DESC"
    unix = dc.select(sql1)[0][0]
    print(unix)
