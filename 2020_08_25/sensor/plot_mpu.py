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
functions for animation
"""
def mpu_init_plot(ax, mpu):
    ln0, = ax[0].plot(t,mpu[:,0], 'r')
    ax[0].grid(True)
    ax[0].set_title("acc x")
    ln1, = ax[1].plot(t,mpu[:,1], 'g')
    ax[1].grid(True)
    ax[1].set_title("acc y")
    ln2, = ax[2].plot(t,mpu[:,2], 'b')
    ax[2].grid(True)
    ax[2].set_title("acc z")
    ln3, = ax[3].plot(t,mpu[:,3], 'r')
    ax[3].grid(True)
    ax[3].set_title("gyro x")
    ln4, = ax[4].plot(t,mpu[:,4], 'g')
    ax[4].grid(True)
    ax[4].set_title("gyro y")
    ln5, = ax[5].plot(t,mpu[:,5], 'b')
    ax[5].grid(True)
    ax[5].set_title("gyro z")
    return ln0, ln1, ln2, ln3, ln4, ln5



#initialize
zumi = Zumi()
t, mpu = init()

#plot
fig, ax = plt.subplots(6,1)
ln0, ln1, ln2, ln3, ln4, ln5 = mpu_init_plot(ax, mpu)
plt.show()
