import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 0)
    rsz = cv2.resize(frame, dsize=(320,240))
   

    # generate Gaussian pyramid
    G = rsz.copy()
    gp = [G]
    for i in range(6):
        G = cv2.pyrDown(G)
        gp.append(G)

    # generate Laplacian Pyramid
    lp = [gp[5]]
    for i in range(5,0,-1):
        GE = cv2.pyrUp(gp[i])
        L = cv2.subtract(gp[i-1],GE)
        lp.append(L)


    cv2.imshow('res',gp)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()