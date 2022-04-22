import pytest
from KeJie.api.kjgoodsupdateApi import KEJIEUPDATE
from KeJie.com.readCsv import READCSV

# 将修改测试csv数据导入
paraupdate = READCSV(file='update_goods_data.csv').readAll(start=1, end=6)


@pytest.mark.parametrize(
    "hcClass,gwall_rk_status,goodsOwner,warehouse,outdety,number,code,price,ftax,unit,msg_code,msg,desc", paraupdate)
def test_update_01(hcClass, gwall_rk_status, goodsOwner, warehouse, outdety, number, code, price, ftax, unit, msg_code,
                   msg, desc):
    kj = KEJIEUPDATE()
    res = kj.updategoods(hcClass, gwall_rk_status, goodsOwner, warehouse, outdety, number, code, price, ftax, unit)
    re_code = res.json()['code']
    # 打印测试数据msg
    print(msg)
    # 打印测试数据desc
    print(desc)
    # 断言，当报错吗等于0时正确
    assert int(msg_code) == re_code
