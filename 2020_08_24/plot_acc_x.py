from zumi.zumi import Zumi
import time
import numpy as np

zumi = Zumi()
idx = 0

acc_x_lst = np.zeros(100)



while idx < 100:
    acc = zumi.get_acc()
    acc_x = acc[0]
    acc_x_lst = np.append(acc_x_lst, acc_x)
    acc_x_lst = np.delete(acc_x_lst, 0)
    idx = idx + 1
    time.sleep(0.01)


print(acc_x_lst)