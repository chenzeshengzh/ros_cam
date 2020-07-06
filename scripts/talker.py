#!/usr/bin/env python
# coding: utf-8

import time

import rospy
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


def talker():
    pub = rospy.Publisher('cam_img', Image, queue_size=10)
    rospy.init_node('talker_img', anonymous=True)
    rate = rospy.Rate(10)
    capture = cv2.VideoCapture(0)
    br = CvBridge()
    while not rospy.is_shutdown():
        [status, img] = capture.read()
        if status == True:
            rospy.loginfo('publish image')
            pub.publish(br.cv2_to_imgmsg(img))
            rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

