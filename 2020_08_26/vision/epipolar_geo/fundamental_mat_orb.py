import cv2
import numpy as np
from matplotlib import pyplot as plt

#https://blog.francium.tech/feature-detection-and-matching-with-opencv-5fd2394a590

img1 = cv2.imread('./res/myleft.jpg',0)  #queryimage # left image
img2 = cv2.imread('./res/myright.jpg',0) #trainimage # right image

# Initiate STAR detector
orb = cv2.ORB_create()

# find the keypoints with ORB
kp1 = orb.detect(img1,None)
kp1, des1 = orb.compute(img1, kp1)


kp2 = orb.detect(img2,None)
kp2, des2 = orb.compute(img2, kp2)



# FLANN parameters
index_params = dict(algorithm=6,
                    table_number=6,
                    key_size=12,
                    multi_probe_level=2)
search_params = {}
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)



good = []
pts1 = []
pts2 = []

# ratio test as per Lowe's paper
for i,(m,n) in enumerate(matches):
    if m.distance < 0.8*n.distance:
        good.append(m)
        pts2.append(kp2[m.trainIdx].pt)
        pts1.append(kp1[m.queryIdx].pt)

pts1 = np.int32(pts1)
pts2 = np.int32(pts2)
F, mask = cv2.findFundamentalMat(pts1,pts2,cv2.FM_LMEDS)


print(F)