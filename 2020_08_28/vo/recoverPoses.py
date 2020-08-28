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

img = cv2.imread('../../res/cap0.png',0)
mat, dist = get_cameramat_dist("cam_calib.pkl")

cam = PinholeCamera(img.shape[1], img.shape[0], fx=mat[0,0], fy=mat[1,1], cx=mat[0,2], cy=mat[1,2],
                k1=dist[0, 0], k2=dist[0, 1], p1=dist[0, 2], p2=dist[0, 3], k3=dist[0, 4])

vo = VisualOdometry(cam)



for img_id in range(0, 10):
    img = cv2.imread('../../res/cap'+str(img_id)+'.png',0)
    vo.update(img, img_id)
    cur_t = vo.cur_t
    if (img_id > 2):
        x, y, z = cur_t[0], cur_t[1], cur_t[2]
    else:
        x, y, z = 0., 0., 0.
    
    print("R matrix")
    print(vo.cur_R)
    print("curr pose x : "+str(x)+", y : " +str(y) + ", z : "+str(z))