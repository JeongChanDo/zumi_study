
import sys, select, termios, tty
from zumi.zumi import Zumi
import time

# https://github.com/turtlebot/turtlebot/blob/melodic/turtlebot_teleop/scripts/turtlebot_teleop_key

msg = """
Control
---------------------------
Moving around:
        i    
   j    k    l
        ,    
space key, k : force stop
anything else : stop smoothly
CTRL-C to quit
"""

moveBindings = ["i", "k", "j", "l"]

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

speed = .2
turn = 1

def vels(speed,turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)



if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    zumi = Zumi()

    x = 0
    count = 0
    try:
        while(1):
            key = getKey()
            print("key : " + str(key))
            if key in moveBindings:
                if (key == "i"):
                    zumi.forward(speed=5,duration=1)
                elif (key == "k"):
                    zumi.reverse(speed=5,duration=1)
                elif (key == "j"):
                    zumi.turn_left(desired_angle=30,duration=0.1)
                elif (key == "l"):
                    zumi.turn_right(desired_angle=30,duration=0.1)
                count = 0
            elif key == ' ' or key == 'k' :
                x = 0
                th = 0
                control_speed = 0
                control_turn = 0
            else:
                count = count + 1
                if count > 4:
                    x = 0
                    th = 0
                if (key == '\x03'):
                    break
    except Exception as e:
        print(e)

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)