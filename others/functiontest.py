import time

#将时间戳转换成时间格式
dt =1650353096
time_local = time.localtime(dt)

time1 =time.strftime("%Y-%m-%d %H:%M:%S",time_local)
print(time1)

x=36/4*(3+2)*4
print(x)