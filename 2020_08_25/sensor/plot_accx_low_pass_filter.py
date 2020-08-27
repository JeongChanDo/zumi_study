from zumi.zumi import Zumi
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

data_len = 100
sampling_len = 10
alpha = 0.5


def LPF(acc_xf_lst, sampling_len, alpha, acc_x):
    prevX = acc_xf_lst[len(acc_xf_lst)-sampling_len:len(acc_xf_lst)-1].sum()/sampling_len
    acc_xf = alpha * prevX + (1-alpha)*acc_x
    acc_xf = round(acc_xf, 3)
    return acc_xf


def data_insert(acc_x_lst, acc_x):
    acc_x_lst = np.append(acc_x_lst, acc_x)
    acc_x_lst = np.delete(acc_x_lst, 0)
    return acc_x_lst

def filter_data_insert(acc_xf_lst,  alpha, acc_x):
    acc_xf_lst = np.delete(acc_xf_lst, 0)
    acc_xf = LPF(acc_xf_lst, sampling_len, alpha, acc_x)
    acc_xf_lst = np.append(acc_xf_lst, acc_xf)
    return acc_xf_lst





def init():
    idx = 0
    acc_x_lst = np.zeros(data_len)
    acc_xf_lst = np.zeros(data_len)

    t = np.linspace(0, 1, data_len)

    while idx < data_len:
        acc = zumi.get_acc()
        acc_x = round(acc[0], 3)
        acc_x_lst = data_insert(acc_x_lst, acc_x)
        acc_xf_lst = filter_data_insert(acc_xf_lst, alpha, acc_x)
    
        idx = idx + 1
    return t, acc_x_lst, acc_xf_lst

def update(i):
    global acc_x_lst, acc_xf_lst
    acc = zumi.get_acc()
    acc_x = round(acc[0], 3)

    acc_x_lst = data_insert(acc_x_lst, acc_x)
    acc_xf_lst = filter_data_insert(acc_xf_lst, alpha, acc_x)

    ln0.set_data(t, acc_x_lst)
    ln1.set_data(t, acc_xf_lst)
    return ln0, ln1



zumi = Zumi()
t, acc_x_lst, acc_xf_lst = init()
fig, ax = plt.subplots(2,1)


ln0, = ax[0].plot(t,acc_x_lst, 'r')
ax[0].grid(True)
ax[0].set_title("acc x")
ax[0].set_ylim((-0.2,0.2))
ln1, = ax[1].plot(t,acc_xf_lst, 'g')
ax[1].grid(True)
ax[1].set_title("acc x LPF")
ax[1].set_ylim((-0.2,0.2))



ani = FuncAnimation(fig, update, frames=t, blit=True)
plt.show()