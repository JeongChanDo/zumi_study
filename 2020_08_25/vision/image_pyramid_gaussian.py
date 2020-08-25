import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 0)
    rsz = cv2.resize(frame, dsize=(320,240))
    gray = cv2.cvtColor(rsz, cv2.COLOR_BGR2GRAY)


    # generate Gaussian pyramid
    G = gray.copy()
    gp = [G]
    for i in range(2):
        G = cv2.pyrDown(G)
        gp.append(G)
    
    #without dtype = int -> dtype initialized float
    #mat shows only white
    #dtype=np.int8
    zero = np.zeros(gp[1].shape, dtype=np.int8)
    zero[0:gp[2].shape[0], 0:gp[2].shape[1]] = gp[2]

    #himg = np.hstack((gp[1], zero))
    #himg = np.hstack((gray, zero))

    #print(himg)
    #res = np.vstack((gp[0], himg))

    cv2.imshow('res',zero)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()