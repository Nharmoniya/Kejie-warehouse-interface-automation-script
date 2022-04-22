import requests
from KeJie.com.readYaml import getSign
from KeJie.com.getDate import getNow


class KEJIE():
    def __init__(self, s=requests.session()):
        self.s = s
        self.url = getSign()

    def singPost(self, outdety="save", date=getNow(),gwall_number="",number="1", code="130204000037",
                 price="200", ftax="13"):
        url = self.url
        datas = {
            "hcClass": "czc",
            "data": {
                "date": date,
                "gwall_rk_status": "出库/出库修改",
                "goodsOwner": "004",
                "warehouse": "KEJIECZC",
                "gwall_number": gwall_number,
                "outdety": outdety,
                "sign": "",
                "ftax": 13,
                "goodsData": [
                    {
                        "code": code,
                        "price": price,
                        "ftax": ftax,
                        "unit1": "1",
                        "number": number,
                    }
                ]
            }
        }
        head = {"Content-Type": "application/json; charset=UTF-8"}
        res = self.s.post(url=url, json=datas, headers=head)
        print(res.text)
        return res


if __name__ == '__main__':
    kj = KEJIE()
    kj.singPost()
