from zumi.zumi import Zumi
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


zumi = Zumi()
idx = 0

acc_x_lst = np.zeros(100)
t = np.linspace(0, 1, 100)


while idx < 100:
    acc = zumi.get_acc()
    acc_x = acc[0]
    acc_x_lst = np.append(acc_x_lst, acc_x)
    acc_x_lst = np.delete(acc_x_lst, 0)
    idx = idx + 1


fig, ax = plt.subplots()
line = plt.plot(t, acc_x_lst)


def animate(i):
    global acc_x_lst

    acc = zumi.get_acc()
    acc_x = acc[0]
    acc_x_lst = np.append(acc_x_lst, acc_x)
    acc_x_lst = np.delete(acc_x_lst, 0)
    line.set_data(t, acc_x_lst)

    """
    plt.cla()
    plt.plot(t,acc_x_lst)
    """


myAnimation = animation.FuncAnimation(fig, animate, frames=t, interval=20, bilt=True)
plt.show()