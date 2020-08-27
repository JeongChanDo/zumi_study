from zumi.zumi import Zumi
import time
import datetime as pydatetime

def get_now():
    return pydatetime.datetime.now().timestamp()

#initialize
zumi = Zumi()
vel = 0
alpha = 0.7
bf_time = 0
curr_time = 0
prev_acc = 0
def get_offset(zumi, sampling):
    offset = 0
    for i in range(1, sampling):
        acc = zumi.get_acc()
        accx = round(acc[0], 3)
        offset = offset + accx
    
    offset = offset/sampling
    print("offset : " + str(offset))
    return offset


def LPF(alpha, prev, curr):
    val = alpha * prev + (1-alpha) * curr
    return val

def print_acc(zumi, offset):
    global curr_time, bf_time, vel, prev_acc
    acc = zumi.get_acc()
    acc_x = LPF(alpha, prev_acc,acc[0])
    acc_x = round(acc[0] - offset, 2)

    curr_time = get_now()
    dt = round(curr_time - bf_time, 2)
    vel = vel + acc_x * dt
    vel = round(vel, 2)
    msg = "acc x : "+str(acc_x)  + ", vel : " +str(vel)+", dt : " + str(dt)
    bf_time = curr_time
    prev_acc = acc_x
    print(msg)

def do_something(zumi, offset):
    print_acc(zumi, offset)
    time.sleep(0.1)



try:
    offset = get_offset(zumi, 100)
    bf_time = get_now()
    while True:
        do_something(zumi, offset)
except KeyboardInterrupt:
    pass