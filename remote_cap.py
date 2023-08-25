#!/usr/bin/env python3
from tkinter import*

frame=Tk()
frame.geometry("200x100")

import rospy
from std_msgs.msg import String

rospy.init_node("GUI")
pub = rospy.Publisher("/take", String, queue_size=10)

def cap():
    pub.publish("cap")

B1 = Button(text = "Capture", command=cap)
B1.pack()

frame.mainloop()
