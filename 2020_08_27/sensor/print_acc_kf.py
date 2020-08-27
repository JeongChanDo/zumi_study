from zumi.zumi import Zumi
import time
import numpy as np

#initialize
zumi = Zumi()

# Initialization for system model.
A = np.diag([1, 1, 1])
H = np.diag([1, 1, 1])
Q = np.zeros((3,3))
R = np.diag([1, 1, 1])


# Initialization for estimation.
xEst = np.zeros((3,1))
pEst = np.diag([1, 1, 1])


def get_offset(zumi, sampling):
    global xEst, pEst
    offset = [0, 0, 0]
    for i in range(1, sampling):
        z = np.array([zumi.get_acc()]).T
        xEst, pEst = kalman_filter(z, xEst, pEst)
        accx = round(xEst[0, 0], 3)
        accy = round(xEst[1, 0], 3)
        accz = round(xEst[2, 0], 3)
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


"""
kf
"""
def kalman_filter(z, xEst, P):
    #print("z : \n"+str(z))
    xPred = A @ xEst
    #print("xPred : \n"+str(xPred))
    pPred = A @ P @ A + Q
    #print("pPred :\n " + str(pPred))
    K = pPred @ H @ np.linalg.inv(H @ pPred @ H + R)
    #print("K : \n" + str(K))
    xEst = xPred + K @ (z - H @ xPred)
    #print("xEst : \n" + str(xEst))
    P = pPred - K @ H @ pPred
    return xEst, P

def do_something(zumi, offset):
    global xEst, pEst
    z = np.array([zumi.get_acc()]).T
    xEst, pEst = kalman_filter(z, xEst, pEst)
    x = xEst.T - np.array([offset])
    print(x)
    time.sleep(0.1)




try:
    offset = get_offset(zumi, 100)
    while True:
        do_something(zumi, offset)
except KeyboardInterrupt:
    pass