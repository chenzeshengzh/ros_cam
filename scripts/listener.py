#!/usr/bin/env python
# coding: utf-8

import time

import rospy
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from std_msgs.msg import String
from std_msgs.msg import Int32


def callback(data):
    br = CvBridge()
    rospy.loginfo('receiving image')
    dx = br.imgmsg_to_cv2(data)

    cv2.imshow("camera", dx)
    cv2.waitKey(1)


def listener():
    rospy.init_node('listener_img', anonymous=True)
    rospy.Subscriber('cam_image', Image, callback)
    rospy.spin()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    listener()
