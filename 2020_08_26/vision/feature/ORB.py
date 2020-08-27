import numpy as np
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
rsz = cv2.resize(frame, dsize=(320,240))
gray = cv2.cvtColor(rsz, cv2.COLOR_BGR2GRAY)
# Initiate ORB detector
orb = cv2.ORB_create()

# find the keypoints with ORB
kp = orb.detect(gray,None)
# compute the descriptors with ORB
kp, desc = orb.compute(gray, kp)
#print("orb kp.shape : " + str(len(kp)) + ", orb desc.shape : " + str(desc.shape))


while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 0)
    rsz = cv2.resize(frame,dsize=(320,240))
    gray = cv2.cvtColor(rsz, cv2.COLOR_BGR2GRAY)

    # find the keypoints with ORB
    kp = orb.detect(gray,None)
    # compute the descriptors with ORB
    kp, desc = orb.compute(gray, kp)

    # draw only keypoints location,not size and orientation
    res = cv2.drawKeypoints(gray,kp,None)

    cv2.imshow('res',res)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()