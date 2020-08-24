from zumi.zumi import Zumi
import numpy as np
import time

zumi = Zumi()
idx = 0
print("curr idx : " + str(idx))

while idx < 30:
    accX = round(zumi.update_angles()[3],3)
    print("acc X : " + str(accX))
    time.sleep(0.1)
    idx = idx + 1

