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
    #push
    mpu = np.append(mpu, mpu_val, axis=0)
    #pop
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

def kalman_filter(z, xEst, PEst):
    # (1) Prediction.
    xPred = A * xEst
    pPred = A * PEst * A + Q
    # (2) Kalman Gain.
    K = pPred * H / (H * pPred * H + R)
    # (3) Estimation.
    xEst = xPred + K * (z - H * xPred)
    # (4) Error Covariance.
    PEst = pPred - K * H * pPred
    return xEst, PEst


def get_accx(zumi):
    accx = get_mpu_val(zumi)[0]
    return accx




def update(i):
    global zumi, accxs, xEst, pEst
    z = get_accx(zumi)
    xEst, pEst = kalman_filter(z, xEst, pEst)
    accxs = new_data_insert(accxs, xEst)

    ln_set_data(accxs)
    return ln0,




#initialize
zumi = Zumi()
t, mpu = init()
accxs = mpu[:, 0]



# Initialization for system model.
A = np.array([
    [1, dt],
    [0 , 1]
])
H = np.array([[0,1]])
Q = np.array([[1, 0],
            [0, 3]])
R = np.array([[3]])


# Initialization for estimation.
#x pos, x vel
xEst = np.array([0,0])
pEst = np.eye(2)



def main():

    #plot
    fig, ax = plt.subplots(1)
    ln0, = ax[0].plot(t, accxs, 'r')

    #animation
    ani = FuncAnimation(fig, update, frames=t, blit=True)
    plt.show()



if __name__ == "__main__":
    main()