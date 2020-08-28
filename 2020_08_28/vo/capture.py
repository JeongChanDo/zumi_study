import numpy as np
import cv2

cap = cv2.VideoCapture(0)
idx = 0

while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, -1)
    rsz = cv2.resize(frame, dsize=(320,240))

    res = cv2.cvtColor(rsz, cv2.COLOR_BGR2GRAY)
    cv2.imshow('res',res)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(20) & 0xFF == ord('c'):
        print("image captured")
        name = "./cap/cap" + str(idx) + ".png"
        cv2.imwrite(name, res)
        idx = idx + 1

cap.release()
cv2.destroyAllWindows()