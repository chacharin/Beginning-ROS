#!/usr/bin/env python3
from tkinter import*
import rospy
from std_msgs.msg import Int16

frame=Tk()
frame.geometry("200x200")


def publish():
    talker()

def talker(val):
    pub1 = rospy.Publisher('LED_Control_Topic', Int16, queue_size=10)
    rospy.init_node('GUI_LED_Control', anonymous=True)
    rate = rospy.Rate(10) 
    cmd_value = Int16(val)
    rospy.loginfo(cmd_value)
    pub1.publish(cmd_value)
    rate.sleep()

B1= Button(frame,text = "ON",command= lambda: talker(1))
B1.pack()
B2= Button(frame,text = "OFF",command= lambda: talker(0))
B2.pack()

frame.mainloop()
