import numpy as np
import cv2
import glob
import pickle

def get_cameramat_dist(filename):

    f = open(filename, 'rb')
    mat, dist = pickle.load(f)
    f.close()

    print("camera matrix")
    print(mat)
    print("distortion coeff")
    print(dist)
    return mat,dist





def main():

    mat, dist = get_cameramat_dist("cam_calib.pkl")

    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()
    #frame = cv2.flip(frame, 0)
    rsz = cv2.resize(frame, dsize=(320,240))
    gray = cv2.cvtColor(rsz, cv2.COLOR_BGR2GRAY)


    h,  w = gray.shape[:2]
    newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mat,dist,(w,h),1,(w,h))




    cap = cv2.VideoCapture(0)

    while(True):
        ret, frame = cap.read()
        #frame = cv2.flip(frame, 0)
        rsz = cv2.resize(frame, dsize=(320,240))
        gray = cv2.cvtColor(rsz, cv2.COLOR_BGR2GRAY)

        # undistort
        mapx,mapy = cv2.initUndistortRectifyMap(mat,dist,None,newcameramtx,(w,h),5)
        res = cv2.remap(gray,mapx,mapy,cv2.INTER_LINEAR)

        # crop the image
        x,y,w,h = roi
        res = res[y:y+h, x:x+w]

        cv2.imshow('res',res)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()