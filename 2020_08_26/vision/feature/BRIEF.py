import numpy as np
import cv2

cap = cv2.VideoCapture(0)
sift = cv2.SIFT_create()
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()


ret, frame = cap.read()
rsz = cv2.resize(frame, dsize=(320,240))
gray = cv2.cvtColor(rsz, cv2.COLOR_BGR2GRAY)
kp, desc = sift.detectAndCompute(gray, None)
brief_kp, brief_desc = brief.compute(gray, kp)
print("surf kp.shape : " + str(len(kp)) + ", surf desc.shape : " + str(desc.shape))
print("brief kp.shape : " + str(len(brief_kp)) + ", brief desc.shape : " + str(brief_desc.shape) )


while(True):
    ret, frame = cap.read()
    #frame = cv2.flip(frame, 0)
    rsz = cv2.resize(frame, dsize=(320,240))
    gray = cv2.cvtColor(rsz, cv2.COLOR_BGR2GRAY)


    #find keypoints and descriptors directly
    kp, desc = sift.detectAndCompute(gray, None)

    # compute the descriptors with BRIEF
    brief_kp, brief_desc = brief.compute(gray, kp)
    res = cv2.drawKeypoints(gray, brief_kp, None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imshow('res',res)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()