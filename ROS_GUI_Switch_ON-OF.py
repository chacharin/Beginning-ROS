#!/usr/bin/env python3
from tkinter import*
import rospy
from std_msgs.msg import Int16

frame=Tk()
frame.geometry("200x200")

rospy.init_node('GUI_LED_Control')
rate = rospy.Rate(10) 
rate.sleep()
pub1 = rospy.Publisher('Topic_LED_13', Int16, queue_size=10)
   
def publish():
    talker()

def talker(val):
    cmd_value = Int16(val)
    rospy.loginfo(cmd_value)
    pub1.publish(cmd_value)
    
B1= Button(frame,text = "ON",command= lambda: talker(1))
B1.pack()
B2= Button(frame,text = "OFF",command= lambda: talker(0))
B2.pack()

frame.mainloop()
