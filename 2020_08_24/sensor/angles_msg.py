from zumi.zumi import Zumi
import time

zumi = Zumi()


for i in range(0, 50):
    vals = zumi.update_angles()
    gyroX = " gyroX : " +str(round(vals[0],2))
    gyroY = ", gyroY : " +str(round(vals[1],2))
    gyroZ = ", gyroZ : " +str(round(vals[2],2))
    accX = ", accX : " + str(round(vals[3],2))
    accY = ", accY : " + str(round(vals[4],2))
    msg = gyroX + gyroY + gyroZ + accX + accY
    print(msg)
    time.sleep(0.1)

print("Done")