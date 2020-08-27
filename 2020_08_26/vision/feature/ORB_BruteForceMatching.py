import numpy as np
import cv2

cap = cv2.VideoCapture(0)


#queryImg
#qImg = cv2.imread('./res/mpu6050_2.png',0)
qImg = cv2.imread('../../../res/mpu6050_2.png',0)

# Initiate STAR detector
orb = cv2.ORB_create()
# find the keypoints with ORB
kp1 = orb.detect(qImg,None)
# compute the descriptors with ORB
kp1, desc1 = orb.compute(qImg, kp1)

# create BFMatcher object
bf = cv2.BFMatcher()
print(len(desc1))

while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 0)
    rsz = cv2.resize(frame, dsize=(320,240))
    gray = cv2.cvtColor(rsz, cv2.COLOR_BGR2GRAY)

    # find the keypoints with ORB
    kp2 = orb.detect(gray,None)
    # compute the descriptors with ORB
    kp2, desc2 = orb.compute(gray, kp2)

    # Match descriptors.
    matches = bf.knnMatch(desc1,desc2, k=2)
    # Apply ratio test
    good = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])


    gray = cv2.drawMatchesKnn(qImg,kp1,gray,kp2,good, None, flags=2)


    cv2.imshow('res',gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()