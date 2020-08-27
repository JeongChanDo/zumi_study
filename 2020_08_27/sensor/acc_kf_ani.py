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

def get_acc(zumi):
    acc = get_mpu_val(zumi)[0][0:3]
    acc = np.array([acc])
    return acc.T



def update(i):
    global zumi, accs, xEst, pEst
    z = get_acc(zumi)
    xEst, pEst = kalman_filter(z, xEst, pEst)
    accs = new_data_insert(accs, xEst.T)
    ln0.set_data(t, accs[:, 0])
    ln1.set_data(t, accs[:, 1])
    ln2.set_data(t, accs[:, 2])
    return ln0, ln1, ln2



#initialize
zumi = Zumi()
t, mpu = init()
accs = mpu[:, 0:3]



# Initialization for system model.
A = np.diag([1, 1, 1])
H = np.diag([1, 1, 1])
Q = np.zeros((3,3))
R = np.diag([1, 1, 1])


# Initialization for estimation.
xEst = np.zeros((3,1))
pEst = np.diag([1, 1, 1])


#plot
fig, ax = plt.subplots(3,1)
print(accs.shape)
ln0, = ax[0].plot(t, accs[:, 0], 'r')
ln1, = ax[1].plot(t, accs[:, 1], 'g')
ln2, = ax[2].plot(t, accs[:, 2], 'b')

accx_min = accs[:, 0].min()
accx_max = accs[:, 0].max()
accy_min = accs[:, 1].min()
accy_max = accs[:, 1].max()
accz_min = accs[:, 2].min()
accz_max = accs[:, 2].max()
plot_scale = 2

ax[0].set_ylim((-accx_min*plot_scale, accx_max*plot_scale))
ax[1].set_ylim((-accy_min*plot_scale, accy_max*plot_scale))
ax[2].set_ylim((-accz_min*plot_scale, accz_max*plot_scale))

ani = FuncAnimation(fig, update, frames=t, blit=True)
plt.show()