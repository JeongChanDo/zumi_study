import numpy as np
import cv2

#queryImg
qImg = cv2.imread('./res/im100.png',1)
orb = cv2.ORB_create()

kp1 = orb.detect(qImg,None)
print(kp1)
res = cv2.drawKeypoints(qImg,kp1,None)

cv2.imshow('res',res)
cv2.waitKey(0)

