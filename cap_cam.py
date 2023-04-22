#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

import cv2

import os
import datetime

cv_image = None

def image_callback(data):
    bridge = CvBridge()
    global cv_image
    try:
        cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError  as e:
        print(e)
    
def take_callback(data):
    if data.data == "cap":
        if cv_image is not None:
            time_stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            image_path = os.path.expanduser("~/Desktop")
            file_name = "Webcam "+ time_stamp + ".jpg"
            file_path = os.path.join(image_path, file_name)
            cv2.imwrite(file_path, cv_image)
            rospy.loginfo("Saved")
        else:
            rospy.loginfo("No image saved")



if __name__ == "__main__":
    rospy.init_node("capture_webcam")
    image_sub = rospy.Subscriber("/usb_cam/image_raw", Image, callback= image_callback)
    take_photo_sub = rospy.Subscriber("/take", String, callback= take_callback )
    rospy.spin()
