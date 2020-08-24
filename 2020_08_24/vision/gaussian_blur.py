import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 0)
    rsz = cv2.resize(frame, dsize=(320,240))


    blur = cv2.GaussianBlur(rsz,(15,15),0)

    res = np.concatenate((rsz, blur), axis=1)
    cv2.imshow('res',res)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()