from zumi.zumi import Zumi
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



"""
common functions
"""
def get_mpu_val(zumi):
    mpus = zumi.get_all_mpu_data()
    acc_x = mpus[0]
    acc_y = mpus[1]
    acc_z = mpus[2]
    gyro_x = mpus[3]
    gyro_y = mpus[4]
    gyro_z = mpus[5]
    mpu_val = np.array([[acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z]])
    return mpu_val


def new_data_insert(mpu, mpu_val):
    mpu = np.append(mpu, mpu_val, axis=0)
    mpu = np.delete(mpu, 0, 0)
    return mpu



"""
initialize mpu data
"""
def init():
    idx = 0
    mpu = np.zeros((100, 6))
    t = np.linspace(0, 1, 100)

    while idx < 100:
        mpu_val = get_mpu_val(zumi)
        mpu = new_data_insert(mpu, mpu_val)
        idx = idx + 1
    return t, mpu



"""
kf
"""
def kalman_filter(z, xEst, P):
    print("z : \n"+str(z))
    xPred = A @ xEst
    print("xPred : \n"+str(xPred))
    pPred = A @ P @ A + Q
    print("pPred :\n " + str(pPred))
    K = pPred @ H @ np.linalg.inv(H @ pPred @ H + R)
    print("K : \n" + str(K))
    xEst = xPred + K @ (z - H @ xPred)
    print("xEst : \n" + str(xEst))
    P = pPred - K @ H @ pPred
    return xEst, P

def get_acc(zumi):
    acc = get_mpu_val(zumi)[0][0:3]
    acc = np.array([acc])
    return acc.T





#initialize
zumi = Zumi()
t, mpu = init()
accxs = mpu[:, 0:2]



# Initialization for system model.
A = np.diag([1, 1, 1])
H = np.diag([1, 1, 1])
Q = np.zeros((3,3))
R = np.diag([1, 1, 1])


# Initialization for estimation.
xEst = np.zeros((3,1))
pEst = np.diag([1, 1, 1])

z =get_acc(zumi)
xEst, pEst = kalman_filter(z, xEst, pEst)