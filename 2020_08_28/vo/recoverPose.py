import numpy as np 
import cv2
import pickle
from visual_odometry import PinholeCamera, VisualOdometry


def get_cameramat_dist(filename):
    
    f = open(filename, 'rb')
    mat, dist, rvecs, tvecs = pickle.load(f)
    f.close()

    print("camera matrix")
    print(mat)
    print("distortion coeff")
    print(dist)
    return mat,dist

#traj = np.zeros((600,600,3), dtype=np.uint8)


mat, dist = get_cameramat_dist("cam_calib.pkl")

img1 = cv2.imread('../../res/cap0.png',0)
img2 = cv2.imread('../../res/cap1.png',0)

print(img1.shape)
cam = PinholeCamera(img1.shape[1], img1.shape[0], fx=mat[0,0], fy=mat[1,1], cx=mat[0,2], cy=mat[1,2],
                k1=dist[0, 0], k2=dist[0, 1], p1=dist[0, 2], p2=dist[0, 3], k3=dist[0, 4])

vo = VisualOdometry(cam)

vo.update(img1, vo.frame_stage)
vo.update(img2, vo.frame_stage)
print("R matrix")
print(vo.cur_R)
print("T vector")
print(vo.cur_t)