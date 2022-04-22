import os
import configparser
import yaml

cf = configparser.ConfigParser()


def getYaml(file):
    path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + file
    f = open(path,"rb")
    cf = f.read()
    res = yaml.safe_load(cf)
    return res

if __name__ == '__main__':
    getYaml()

