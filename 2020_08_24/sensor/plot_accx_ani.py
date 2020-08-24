from zumi.zumi import Zumi
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def init():
    idx = 0
    acc_x_lst = np.zeros(100)
    t = np.linspace(0, 1, 100)

    while idx < 100:
        acc = zumi.get_acc()
        acc_x = acc[0]
        acc_x_lst = np.append(acc_x_lst, acc_x)
        acc_x_lst = np.delete(acc_x_lst, 0)
        idx = idx + 1

    return t, acc_x_lst

def update(i):
    global acc_x_lst
    acc = zumi.get_acc()
    acc_x = acc[0]
    acc_x_lst = np.append(acc_x_lst, acc_x)
    acc_x_lst = np.delete(acc_x_lst, 0)
    ln.set_data(t, acc_x_lst)
    return ln,



zumi = Zumi()

t, acc_x_lst = init()


fig, ax = plt.subplots()
ln, = plt.plot(t,acc_x_lst, 'r')
#ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-0.3, 0.3)

ani = FuncAnimation(fig, update, frames=t, blit=True)
plt.show()