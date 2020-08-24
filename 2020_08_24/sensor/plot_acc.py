from zumi.zumi import Zumi
import time
import numpy as np
import matplotlib.pyplot as plt

zumi = Zumi()
idx = 0

acc_x_lst = np.zeros(100)
acc_y_lst = np.zeros(100)
acc_z_lst = np.zeros(100)

t = np.linspace(0, 1, 100)


while idx < 100:
    acc = zumi.get_acc()
    acc_x = acc[0]
    acc_y = acc[1]
    acc_z = acc[2]

    acc_x_lst = np.append(acc_x_lst, acc_x)
    acc_x_lst = np.delete(acc_x_lst, 0)
    acc_y_lst = np.append(acc_y_lst, acc_y)
    acc_y_lst = np.delete(acc_y_lst, 0)
    acc_z_lst = np.append(acc_z_lst, acc_z)
    acc_z_lst = np.delete(acc_z_lst, 0)

    idx = idx + 1
    time.sleep(0.01)


plt.title("xyz accelerometer")
plt.subplot(211)
plt.plot(t, acc_x_lst, "r", label="x axis")
plt.plot(t, acc_y_lst, "g", label="y axis")
plt.legend(loc=2)
plt.subplot(212)
plt.plot(t, acc_z_lst, "b", label="z axis")
plt.legend(loc=2)
plt.show()