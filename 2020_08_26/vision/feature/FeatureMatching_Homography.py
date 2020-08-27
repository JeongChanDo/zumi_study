import numpy as np
import cv2
from matplotlib import pyplot as plt



# Initiate
MIN_MATCH_COUNT = 10
cap = cv2.VideoCapture(0)


#FLANN Feature Matcher & Param
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)
flann = cv2.FlannBasedMatcher(index_params, search_params)





qImg = cv2.imread('./res/mpu6050.png',0)
sift = cv2.SIFT_create()
kp1, desc1 = sift.detectAndCompute(qImg,None)







while(True):
    ret, frame = cap.read()
    #frame = cv2.flip(frame, 0)
    rsz = cv2.resize(frame, dsize=(320,240))
    gray = cv2.cvtColor(rsz, cv2.COLOR_BGR2GRAY)
    kp2, desc2 = sift.detectAndCompute(gray,None)






    matches = flann.knnMatch(desc1,desc2,k=2)
    good = []
    for m,n in matches:
        if m.distance < 0.7*n.distance:
            good.append(m)



    if len(good)>MIN_MATCH_COUNT:
        src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
        matchesMask = mask.ravel().tolist()

        h,w = qImg.shape
        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts,M)

        gray = cv2.polylines(gray,[np.int32(dst)],True,255,3, cv2.LINE_AA)

    else:
        print("Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT))
        matchesMask = None



    draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                    singlePointColor = None,
                    matchesMask = matchesMask, # draw only inliers
                    flags = 2)

    res = cv2.drawMatches(qImg,kp1,gray,kp2,good,None,**draw_params)



    cv2.imshow('res',res)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()