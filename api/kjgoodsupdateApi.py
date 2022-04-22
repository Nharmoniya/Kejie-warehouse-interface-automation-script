import requests
from KeJie.api.loginApi import KEJIE
from KeJie.com.readYaml import getIndex
from KeJie.com.connectMysql import DbConnect
from KeJie.com.transformTime import transUnixchuo


class KEJIEUPDATE():
    def __init__(self, s=requests.session()):
        self.s = s
        self.url = getIndex()
        # 连接数据库
        dc = DbConnect()
        select_czcnumber = "select czc_number from dtmoban_warehouse_in_warehouse_chuku WHERE czc_number='PO2022954894' ORDER BY ordersn DESC"
        select_datetime = "select create_time from dtmoban_warehouse_in_warehouse_chuku WHERE czc_number='PO2022954894' ORDER BY ordersn DESC"
        self.czcnumber = dc.select(select_czcnumber)[0][0]
        czccreatetime = dc.select(select_datetime)
        # 将czcreatetime的时间戳转换成datetime格式
        self.date = transUnixchuo(dt=int((czccreatetime)[0][0]))

    def updategoods(self, hcClass="czc", gwall_rk_status="出库/出库修改", goodsOwner="004", warehouser="KEJIECZC",
                    outdety="update", number="2", code="130204000037",
                    price="200", ftax="13", unit="1"):
        sg = KEJIE()
        sig = sg.singPost(outdety=outdety, date=self.date, gwall_number=self.czcnumber, number=number, code=code, price=price,
                          ftax=ftax)
        signid = sig.text
        url = self.url
        datas = {
            "hcClass": hcClass,
            "data": {
                "date": self.date,
                "gwall_rk_status": gwall_rk_status,
                "goodsOwner": goodsOwner,
                "warehouse": warehouser,
                "gwall_number": self.czcnumber,
                "outdety": outdety,
                "sign": signid,
                "goodsData": [
                    {
                        "code": code,
                        "price": price,
                        "ftax": ftax,
                        "unit1": unit,
                        "number": number,
                    }
                ]
            }
        }
        head = {"Content-Type": "application/json; charset=UTF-8"}
        res = self.s.post(url=url, json=datas, headers=head)
        print(res.json())
        return res

if __name__ =='__main__':
    kj = KEJIEUPDATE()
    kj.updategoods(hcClass="czc", gwall_rk_status="出库/出库修改", goodsOwner="004", warehouser="KEJIECZC",
                    outdety="cancel", number="1", code="130201000069",
                    price="212", ftax="10", unit="3")
