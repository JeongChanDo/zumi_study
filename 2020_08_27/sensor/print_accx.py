from zumi.zumi import Zumi
import time
import datetime as pydatetime

def get_now():
    return pydatetime.datetime.now().timestamp()

#initialize
zumi = Zumi()


bf_time = 0
curr_time = 0

def get_offset(zumi, sampling):
    offset = 0
    for i in range(1, sampling):
        acc = zumi.get_acc()
        accx = round(acc[0], 3)
        offset = offset + accx
    
    offset = offset/sampling
    print("offset : " + str(offset))
    return offset

def print_acc(zumi, offset):
    global curr_time, bf_time
    acc = zumi.get_acc()
    acc_x = round(acc[0] - offset, 2)
    curr_time = get_now()
    dt = round(curr_time - bf_time, 3)
    msg = "acc x : "+str(acc_x)  + ", dt : " + str(dt)
    bf_time = curr_time
    print(msg)

def do_something(zumi, offset):
    print_acc(zumi, offset)
    time.sleep(0.1)



try:
    offset = get_offset(zumi, 100)
    while True:
        do_something(zumi, offset)
except KeyboardInterrupt:
    pass