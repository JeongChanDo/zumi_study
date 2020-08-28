from zumi.zumi import Zumi
import numpy as np
import time


zumi =  Zumi()

zumi.reset_drive()

while True:

    angle_list = zumi.update_angles()
    x = round(angle_list[0],3)
    y = round(angle_list[1],3)
    z = round(angle_list[2],3)
    print("x : " + str(x) + ", y : "+str(y)+", z : "+str(z))

    time.sleep(0.1)
