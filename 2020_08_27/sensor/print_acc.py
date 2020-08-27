from zumi.zumi import Zumi
import time

#initialize
zumi = Zumi()



def get_offset(zumi, sampling):
    offset = [0, 0, 0]
    for i in range(1, sampling):
        acc = zumi.get_acc()
        accx = round(acc[0], 3)
        accy = round(acc[1], 3)
        accz = round(acc[2], 3)
        offset[0] = offset[0] + accx
        offset[1] = offset[1] + accy
        offset[2] = offset[2] + accz
    
    offset[0] = offset[0]/sampling
    offset[1] = offset[1]/sampling
    offset[2] = offset[2]/sampling
    print("offset : " + str(offset))
    return offset

def print_acc(zumi, offset):
    acc = zumi.get_acc()
    acc_x = round(acc[0] - offset[0], 2)
    acc_y = round(acc[1] - offset[1], 2)
    acc_z = round(acc[2] - offset[2], 2)

    msg = "acc x : "+str(acc_x) +", acc y : " + str(acc_y) + ", acc z : " + str(acc_z)
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