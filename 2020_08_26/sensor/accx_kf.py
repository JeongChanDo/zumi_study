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

def kalman_filter(z_meas, x_esti, P):
    """Kalman Filter Algorithm for One Variable."""
    # (1) Prediction.
    x_pred = A * x_esti
    P_pred = A * P * A + Q

    # (2) Kalman Gain.
    K = P_pred * H / (H * P_pred * H + R)

    # (3) Estimation.
    x_esti = x_pred + K * (z_meas - H * x_pred)

    # (4) Error Covariance.
    P = P_pred - K * H * P_pred

    return x_esti, P


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
A = 1
H = 1
Q = 0
R = 4


# Initialization for estimation.
xEst = 0
pEst = 1



def main():

    #plot
    fig, ax = plt.subplots(1)
    ln0, = ax[0].plot(t, accxs, 'r')

    #animation
    ani = FuncAnimation(fig, update, frames=t, blit=True)
    plt.show()



if __name__ == "__main__":
    main()