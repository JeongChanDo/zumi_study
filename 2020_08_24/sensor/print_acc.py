from zumi.zumi import Zumi

zumi = Zumi()

acc = zumi.get_acc()
acc_x = acc[0]
acc_y = acc[1]
acc_z = acc[2]

msg = "acc x : "+str(acc_x) +", acc y : " + str(acc_y) + ", acc z : " + str(acc_z)
print(msg)
