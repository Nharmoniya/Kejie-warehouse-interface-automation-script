import time

def transUnixchuo(dt=1650353096):
    local_time = time.localtime(dt)
    print(type(dt))
    date_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    print(date_time)
    return date_time

def transtimetoUnix(dt='2016-05-05 20:29:44'):
    #转换成时间数组
    timeArray = time.strptime(dt,"%Y-%m-%d %H:%M:%S")
    date_unix = time.mktime(timeArray)
    print(date_unix)
    return date_unix

transUnixchuo()