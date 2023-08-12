#!/usr/bin/env python3
from tkinter import*
import rospy
from std_msgs.msg import Int16

frame=Tk()
frame.geometry("200x200")

rospy.init_node('GUI')
rate = rospy.Rate(10) 
rate.sleep()

def read(num):
    sensor_read = num.data
    L1.config(text=str(sensor_read))

sub = rospy.Subscriber('Topic_Sensor', Int16, callback= read)
    
L1= Label(frame,font=('Arial',40), text = "0")
L1.pack()

frame.mainloop()
