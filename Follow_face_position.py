#!/usr/bin/env python3
import rospy
from opencv_apps.msg import FaceArrayStamped
from std_msgs.msg import Int16

servo9_postion = 90
servo10_postion = 90

def callback(data):
    global servo9_postion
    global servo10_postion
    if len(data.faces) > 0:
        face = data.faces[0]
        x = face.face.x
        y = face.face.y
        width = face.face.width
        if width>90 and width<120:
            rospy.loginfo("x: "+str(x) + " , "+ " y: "+str(y) + " width: "+ str(width))
            if x <= 250:
                if servo9_postion >= 60:
                    left_pan = servo9_postion + 1
                    pub_servo_9.publish(left_pan)
                    servo9_postion = left_pan
            if x >= 450:
                if servo9_postion <= 140:
                    right_pan = servo9_postion - 1
                    pub_servo_9.publish(right_pan)
                    servo9_postion = right_pan

            if y<= 150:
                if servo10_postion <= 120:
                    lift_up = servo10_postion + 1
                    pub_servo_10.publish(lift_up)
                    servo10_postion = lift_up
            if y>= 300:
                if servo10_postion >= 40:
                    lift_down = servo10_postion - 1
                    pub_servo_10.publish(lift_down)
                    servo10_postion = lift_down
            

rospy.init_node('control_follow_face')
    
pub_servo_9 = rospy.Publisher("/Topic_servo_9", Int16, queue_size=10)
pub_servo_10 = rospy.Publisher("/Topic_servo_10", Int16, queue_size=10)
pub_servo_9.publish(90)
pub_servo_10.publish(90)
rospy.loginfo("set-motor")

rospy.Subscriber("/face_detection/faces", FaceArrayStamped, callback)
rospy.spin()

    
