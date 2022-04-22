import datetime


def getNow():
    now = datetime.datetime.today().now().strftime("%Y-%m-%d %H:%M:%S")
    return now


if __name__ =='__main__':
    getNow()
