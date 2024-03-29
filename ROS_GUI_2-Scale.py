#!/usr/bin/env python3
from tkinter import*
import rospy
from std_msgs.msg import Int16

frame=Tk()
frame.geometry("200x200")

S1_value = 0
S2_value = 0

rospy.init_node('GUI')
pub1 = rospy.Publisher('Topic_servo_9', Int16, queue_size=10)
pub2 = rospy.Publisher('Topic_servo_10', Int16, queue_size=10)
rate = rospy.Rate(100)
rate.sleep()

def talker(val):
    global S1_value
    global S2_value

    S1_value = Int16(S1.get())
    S2_value = Int16(S2.get())
    
    pub1.publish(S1_value)
    pub2.publish(S2_value)

S1= Scale(frame, from_=0, to=180, label= "SV-9", command=talker)
S1.place(x=5, y=10)
S1.set(90)

S2= Scale(frame, from_=0, to=180, label= "SV-10", command=talker)
S2.place(x=100, y=10)
S2.set(90)

frame.mainloop()
