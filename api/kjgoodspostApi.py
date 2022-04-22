import requests
from KeJie.com.readYaml import getIndex
from KeJie.api.loginApi import KEJIE
from KeJie.com.gwallNumber import getGwallnumber
from KeJie.com.getDate import getNow


class KEJIEPOST():
    def __init__(self, s=requests.session()):
        self.s = s
        self.url = getIndex()
        self.id = getGwallnumber()
        self.date = getNow()
        print(self.id)

    def goodPost(self,hcClass="czc",gwall_rk_status="出库/出库修改",goodsOwner="004",warehouser="KEJIECZC",outdety="save", number="1", code="130204000037",
                 price="200", ftax="13",unit="1"):
        sg = KEJIE()
        sig = sg.singPost(outdety=outdety, date=self.date, gwall_number=self.id, number=number, code=code, price=price,
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
                "gwall_number": self.id,
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



if __name__ == '__main__':
    kj = KEJIEPOST()
    kj.goodPost(hcClass="czc",gwall_rk_status="出库/出库修改",goodsOwner="004",warehouser="KEJIECZC",outdety="save", number="100", code="130204000037",
                 price="100", ftax="13",unit="1")
