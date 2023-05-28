#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from std_msgs.msg import Int16

color = "-"
previous_color = "-"

def Show_LED():
    global previous_color
    global color
    if color == "r" and previous_color != "r":
        pub_red.publish(1)
        pub_yellow.publish(0)
        pub_green.publish(0)
    elif color == "y" and previous_color != "y":
        pub_red.publish(0)
        pub_yellow.publish(1)
        pub_green.publish(0)
    elif color == "g" and previous_color != "g":
        pub_red.publish(0)
        pub_yellow.publish(0)
        pub_green.publish(1)
    previous_color = color

def LED_control(pose):
    global color
    x = pose.x
    y = pose.y
    if (x<1) or (x>10) or (y<1) or (y>10):
        rospy.loginfo("red-wall")
        color = "r"
    elif (x<3) or (x>8) or (y<3) or (y>8):
        rospy.loginfo("yellow-area")
        color = "y"
    else:
        rospy.loginfo("green-area")
        color = "g"
    Show_LED()

rospy.init_node("turtle_LED")
rospy.loginfo("Node started")
sub = rospy.Subscriber("/turtle1/pose", Pose, callback= LED_control)                
pub_red = rospy.Publisher("/red", Int16, queue_size=10)
pub_yellow = rospy.Publisher("/yellow", Int16, queue_size=10)
pub_green = rospy.Publisher("/green", Int16, queue_size=10)
rospy.spin()