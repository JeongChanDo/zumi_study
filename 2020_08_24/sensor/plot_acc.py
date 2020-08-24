from zumi.zumi import Zumi
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def init():
    idx = 0
    acc = np.zeros((100, 3))
    t = np.linspace(0, 1, 100)

    while idx < 100:
        accs = zumi.get_acc()
        acc_x = accs[0]
        acc_y = accs[1]
        acc_z = accs[2]
        acc_val = np.array([[acc_x, acc_y, acc_z]])

        #push
        acc = np.append(acc, acc_val, axis=0)
        #pop
        acc = np.delete(acc, 0, 0)
        idx = idx + 1

    return t, acc

def update(i):
    global acc
    accs = zumi.get_acc()
    acc_x = accs[0]
    acc_y = accs[1]
    acc_z = accs[2]
    acc_val = np.array([[acc_x, acc_y, acc_z]])

    #push
    acc = np.append(acc, acc_val, axis=0)
    #pop
    acc = np.delete(acc, 0, 0)

    #change y axis data
    ln0.set_data(t, acc[:,0])
    ln1.set_data(t, acc[:,1])
    ln2.set_data(t, acc[:,2])

    # change y limit dynamically
    ax[0].set_ylim(min(acc[:,0]), max(acc[:,0]))
    ax[1].set_ylim(min(acc[:,1]), max(acc[:,1]))
    ax[2].set_ylim(min(acc[:,2]), max(acc[:,2]))
    return ln0, ln1, ln2


#initialize
zumi = Zumi()
t, acc = init()

#plot
fig, ax = plt.subplots(3,1)
ln0, = ax[0].plot(t,acc[:,0], 'r')
ax[0].grid(True)
ax[0].set_title("acc x")
ln1, = ax[1].plot(t,acc[:,1], 'g')
ax[1].grid(True)
ax[1].set_title("acc y")
ln2, = ax[2].plot(t,acc[:,2], 'b')
ax[2].grid(True)
ax[2].set_title("acc z")

#animation
ani = FuncAnimation(fig, update, frames=t, blit=True)
plt.show()
