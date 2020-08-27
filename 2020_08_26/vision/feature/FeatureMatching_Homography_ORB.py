import numpy as np
import cv2
from matplotlib import pyplot as plt



# Initiate
MIN_MATCH_COUNT = 10
cap = cv2.VideoCapture(0)


#FLANN Feature Matcher & Param
index_params = dict(algorithm=6,
                    table_number=6,
                    key_size=12,
                    multi_probe_level=2)
search_params = {}
flann = cv2.FlannBasedMatcher(index_params, search_params)



# Initiate STAR detector
orb = cv2.ORB_create()

img1 = cv2.imread('./res/mpu6050.png',0)
# find the keypoints with ORB
kp1 = orb.detect(img1,None)
kp1, des1 = orb.compute(img1, kp1)





while(True):
    ret, frame = cap.read()
    #frame = cv2.flip(frame, 0)
    rsz = cv2.resize(frame, dsize=(320,240))
    gray = cv2.cvtColor(rsz, cv2.COLOR_BGR2GRAY)
    kp2 = orb.detect(gray,None)
    kp2, des2 = orb.compute(gray, kp2)





    matches = flann.knnMatch(des1, des2, k=2)


    good = []
    for i,(m,n) in enumerate(matches):
        if m.distance < 0.8*n.distance:
            good.append(m)


    if len(good)>MIN_MATCH_COUNT:
        src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
        matchesMask = mask.ravel().tolist()

        h,w = img1.shape
        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts,M)

        gray = cv2.polylines(gray,[np.int32(dst)],True,255,3, cv2.LINE_AA)

    else:
        #print("Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT))
        matchesMask = None



    draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                    singlePointColor = None,
                    matchesMask = matchesMask, # draw only inliers
                    flags = 2)

    res = cv2.drawMatches(img1,kp1,gray,kp2,good,None,**draw_params)



    cv2.imshow('res',res)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()