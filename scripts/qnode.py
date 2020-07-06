#!/usr/bin/env python
# coding: utf-8

import sys

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
from PyQt5.QtCore import QThread, QStringListModel, QModelIndex, pyqtSignal
from PyQt5.QtWidgets import QListView


class QNode(QThread):
    # updateLog = pyqtSignal()
    # rosShutdown = pyqtSignal()

    def __init__(self, queue_view):
        QThread.__init__(self)
        rospy.init_node('listener_img', anonymous=True)
        self.queue = queue_view

    def __del__(self):
        if not rospy.is_shutdown():
            # rospy.shutdown('shutdown reason')
            self.wait()

    def callback(self, data):
        br = CvBridge()
        rospy.loginfo('receiving image')
        dx = br.imgmsg_to_cv2(data)
        frame = {}
        frame["img"] = dx
        self.queue.put(frame)

    def run(self):
        rospy.Subscriber('cam_img', Image, self.callback) 
        rospy.spin()
        # self.rosShutdown.emit()  # emit signal for shutdown

