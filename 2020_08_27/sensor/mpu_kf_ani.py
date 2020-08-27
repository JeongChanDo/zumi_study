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

def change_ylim(ax, mpu, ylim_scale):
    ax[0, 0].set_ylim(-abs(max(mpu[:,0])) *ylim_scale ,abs(max(mpu[:,0])) *ylim_scale)
    ax[1, 0].set_ylim(-abs(max(mpu[:,1])) *ylim_scale ,abs(max(mpu[:,1])) *ylim_scale)
    ax[2, 0].set_ylim(-abs(max(mpu[:,2])) *ylim_scale ,abs(max(mpu[:,2])) *ylim_scale)
    ax[0, 1].set_ylim(-abs(max(mpu[:,3])) *ylim_scale ,abs(max(mpu[:,3])) *ylim_scale)
    ax[1, 1].set_ylim(-abs(max(mpu[:,4])) *ylim_scale ,abs(max(mpu[:,4])) *ylim_scale)
    ax[2, 1].set_ylim(-abs(max(mpu[:,5])) *ylim_scale ,abs(max(mpu[:,5])) *ylim_scale)



def mpu_init_plot(ax, mpu):
    ln0, = ax[0, 0].plot(t,mpu[:,0], 'r')
    ax[0, 0].grid(True)
    ax[0, 0].set_title("acc x")
    ln1, = ax[1, 0].plot(t,mpu[:,1], 'g')
    ax[1, 0].grid(True)
    ax[1, 0].set_title("acc y")
    ln2, = ax[2, 0].plot(t,mpu[:,2], 'b')
    ax[2, 0].grid(True)
    ax[2, 0].set_title("acc z")
    ln3, = ax[0, 1].plot(t,mpu[:,3], 'r')
    ax[0, 1].grid(True)
    ax[0, 1].set_title("gyro x")
    ln4, = ax[1, 1].plot(t,mpu[:,4], 'g')
    ax[1, 1].grid(True)
    ax[1, 1].set_title("gyro y")
    ln5, = ax[2, 1].plot(t,mpu[:,5], 'b')
    ax[2, 1].grid(True)
    ax[2, 1].set_title("gyro z")
    return ln0, ln1, ln2, ln3, ln4, ln5




def update(i):
    global zumi, mpu, xEst, pEst
    z = get_mpu_val(zumi)
    xEst, pEst = kalman_filter(z.T, xEst, pEst)
    mpu = new_data_insert(mpu, xEst.T)
    ln0.set_data(t, mpu[:, 0])
    ln1.set_data(t, mpu[:, 1])
    ln2.set_data(t, mpu[:, 2])
    ln3.set_data(t, mpu[:, 3])
    ln4.set_data(t, mpu[:, 4])
    ln5.set_data(t, mpu[:, 5])

    return ln0, ln1, ln2, ln3, ln4, ln5

def zumi_calib(zumi):
    #Zumi will take 500 samples/readings
    zumi.mpu.calibrate_MPU(count=500)

    #this is the order the offsets will be printed
    print("angular speed rad/sec Gx,Gy,Gz")
    print("linear acceleration   Ax,Ay,Az")

    #print the offsets of each Axis
    zumi.mpu.print_offsets()



#initialize
zumi = Zumi()

zumi_calib(zumi)


t, mpu = init()


# Initialization for system model.
A = np.diag([1, 1, 1, 1, 1, 1])
H = np.diag([1, 1, 1, 1, 1, 1])
Q = np.zeros((6,6))
R = np.diag([1, 1, 1, 1, 1, 1])


# Initialization for estimation.
xEst = np.zeros((6,1))
pEst = np.diag([1, 1, 1, 1, 1, 1])


#plot
fig, ax = plt.subplots(3,2)
ln0, ln1, ln2, ln3, ln4, ln5 = mpu_init_plot(ax, mpu)

ylim_scale = 10
change_ylim(ax, mpu, ylim_scale)

ani = FuncAnimation(fig, update, frames=t, blit=True)
plt.show()