from zumi.zumi import Zumi
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

data_len = 100
mean_len = 5

def init():
    idx = 0
    acc_x_lst = np.zeros(data_len)
    acc_xf_lst = np.zeros(data_len)

    t = np.linspace(0, 1, data_len)

    while idx < data_len:
        acc = zumi.get_acc()
        acc_x = round(acc[0], 3)
        acc_x_lst = np.append(acc_x_lst, acc_x)
        acc_x_lst = np.delete(acc_x_lst, 0)


        acc_xf_lst = np.delete(acc_xf_lst, 0)
        mean_bf = ((mean_len - 1) / mean_len) * (acc_xf_lst[len(acc_xf_lst)-mean_len:len(acc_xf_lst)-1].sum()/(mean_len-1))
        acc_xf = round(mean_bf + 1/mean_len * acc_x, 3)
        #print("acc_x : " + str(acc_x) + ",  acc_xf : " + str(acc_xf))
        acc_xf_lst = np.append(acc_xf_lst, acc_xf)
        idx = idx + 1
    return t, acc_x_lst, acc_xf_lst

def update(i):
    global acc_x_lst, acc_xf_lst
    acc = zumi.get_acc()
    acc_x = round(acc[0], 3)
    acc_x_lst = np.append(acc_x_lst, acc_x)
    acc_x_lst = np.delete(acc_x_lst, 0)


    acc_xf_lst = np.delete(acc_xf_lst, 0)
    mean_bf = ((mean_len - 1) / mean_len) * (acc_xf_lst[len(acc_xf_lst)-mean_len:len(acc_xf_lst)-1].sum()/(mean_len-1))
    acc_xf = round(mean_bf + 1/mean_len * acc_x, 3)
    acc_xf_lst = np.append(acc_xf_lst, acc_xf)
    #print("acc_x : " + str(acc_x) + ",  acc_xf : " + str(acc_xf))
    ln0.set_data(t, acc_x_lst)
    ln1.set_data(t, acc_xf_lst)
    return ln0, ln1



zumi = Zumi()
t, acc_x_lst, acc_xf_lst = init()
fig, ax = plt.subplots(2,1)


ln0, = ax[0].plot(t,acc_x_lst, 'r')
ax[0].grid(True)
ax[0].set_title("acc x")
ax[0].set_ylim((-0.5,0.5))
ln1, = ax[1].plot(t,acc_xf_lst, 'g')
ax[1].grid(True)
ax[1].set_title("acc x average filtered")
ax[1].set_ylim((-0.5,0.5))



ani = FuncAnimation(fig, update, frames=t, blit=True)
plt.show()