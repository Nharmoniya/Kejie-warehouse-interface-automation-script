import datetime
import random


def getGwallnumber():
    # 随机生成id1000-9999之间的数
    id = random.randrange(100000, 999999, 1)
    date = datetime.date.today().year
    number = "PO" + str(date) + str(id)
    return number

if __name__ == '__main__':
    getGwallnumber()
