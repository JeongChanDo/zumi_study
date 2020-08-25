import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 0)
    rsz = cv2.resize(frame, dsize=(320,240))
    gray = cv2.cvtColor(rsz, cv2.COLOR_BGR2GRAY)

    laplacian = cv2.Laplacian(gray,cv2.CV_64F)
    sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)

    res = np.concatenate((laplacian, sobelx, sobely), axis=1)
    cv2.imshow('res',res)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()