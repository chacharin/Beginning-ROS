#!/usr/bin/env python3
import rospy

if __name__ == "__main__":
    rospy.init_node("node_one")

    rospy.loginfo("Start Hello from node one")
    rospy.logwarn("This is a warning is YELLOW")
    rospy.logerr("This is an error is RED")
    rospy.sleep(1.0)
    
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        rospy.loginfo("Hello")
        rate.sleep()
