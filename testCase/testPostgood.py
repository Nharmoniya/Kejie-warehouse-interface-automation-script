import pytest
from KeJie.api.kjgoodspostApi import KEJIEPOST
from KeJie.com.readCsv import READCSV

# 将csv文件中的测试数据导入
para = READCSV().readAll(start=1, end=6)

# 将全字段测试csv文档数据导入
paraall = READCSV(file='alltestdata.csv').readAll(start=1, end=14)

# 将库存测试csv文档数据导入
paraamount = READCSV(file='amount_test_data.csv').readAll(start=1, end=1)

# 将修改测试csv文档数据导入
paraupdate = READCSV(file='update_goods_data.csv').readAll(start=1, end=6)


# 必填测试
@pytest.mark.parametrize("outdety, number, code,price, ftax,unit,msg_code,desc", para)
def test_good_01(outdety, number, code, price, ftax, unit, msg_code, desc):
    kj = KEJIEPOST()
    res = kj.goodPost(outdety, number, code, price, ftax, unit)
    msg = res.json()['code']
    print(msg)
    print(msg_code)
    print(desc)
    # 断言，当报错码等于10201时才正确
    assert str(msg) == msg_code


# 全字段测试
@pytest.mark.parametrize(
    "hcClass,gwall_rk_status,goodsOwner,warehouse,outdety,number,code,price,ftax,unit,msg_code,msg,desc", paraall)
def test_good_02(hcClass, gwall_rk_status, goodsOwner, warehouse, outdety, number, code, price, ftax, unit, msg_code,
                 msg, desc):
    kj = KEJIEPOST()
    res = kj.goodPost(hcClass, gwall_rk_status, goodsOwner, warehouse, outdety, number, code, price, ftax, unit)
    re_code = res.json()['code']
    # 打印测试数据msg
    print(msg)
    # 打印测试数据desc
    print(desc)
    # 断言，当报错吗等于0时正确
    assert int(msg_code) == int(re_code)


# 库存不足测试
@pytest.mark.parametrize(
    "hcClass,gwall_rk_status,goodsOwner,warehouse,outdety,number,code,price,ftax,unit,msg_code,msg,desc", paraamount)
def test_good_03(hcClass, gwall_rk_status, goodsOwner, warehouse, outdety, number, code, price, ftax, unit, msg_code,
                 msg, desc):
    kj = KEJIEPOST()
    res = kj.goodPost(hcClass, gwall_rk_status, goodsOwner, warehouse, outdety, number, code, price, ftax, unit)
    re_code = res.json()['code']
    # 打印接口回传的code
    print(type(re_code))
    # 打印测试数据msg
    print(msg)
    # 打印测试数据desc
    print(desc)
    # 断言，当报错吗等于0时正确
    assert int(msg_code) == re_code



