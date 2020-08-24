import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()


    # Display the resulting frame
    frame = cv2.flip(frame, 0)
    dst = cv2.resize(frame, dsize=(320,240))
    cv2.imshow('dst',dst)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()