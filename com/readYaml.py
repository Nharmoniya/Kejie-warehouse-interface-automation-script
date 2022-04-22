from KeJie.com.readConfig import getYaml


def getSign():
    host = getYaml(file="\conf\db.yaml")
    res = host['sign']
    print(res)
    return res


def getIndex():
    host = getYaml(file="\conf\db.yaml")
    res = host['index']
    print(res)
    return res

def getDatabase():
    host = getYaml(file="\conf\database.yaml")
    return host



if __name__ == '__main__':
    getSign()
    getIndex()
