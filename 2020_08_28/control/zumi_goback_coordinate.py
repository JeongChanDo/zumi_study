from zumi.zumi import Zumi
import numpy as np

zumi =  Zumi()

zumi.reset_coordinate()
zumi.reset_drive()
zumi.move_to_coordinate(desired_x= 5, desired_y = 0)
zumi.move_to_coordinate(desired_x= 0, desired_y = 0)
