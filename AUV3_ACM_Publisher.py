#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from std_msgs.msg import String
from enum import Enum

# Define enums for data IDs
class DataID(Enum):
    LATITUDE = 10
    LONGITUDE = 20
    DEPTH = 30
    VELOCITY_X = 40
    YAW = 50
    BATTERY_STATE = 60
    SBC_STATUS = 70

# Define a class to handle the subscription and publishing
class DataConverter:
    def __init__(self):
        rospy.init_node('acm_communication')

        # Create publishers for the converted data
        self.pub = rospy.Publisher('acoustic_data', String, queue_size=10)

        # Subscribe to the rostopics
        rospy.Subscriber('auv3/curr_latitude', Float32, self.latitude_callback)
        rospy.Subscriber('auv3/curr_longitude', Float32, self.longitude_callback)
        rospy.Subscriber('auv3/depth', Float32, self.depth_callback)
        rospy.Subscriber('auv3/velocity', Float32, self.velocity_callback)
        rospy.Subscriber('auv3/yaw', Float32, self.yaw_callback)

    def latitude_callback(self, data):
        self.publish_data(DataID.LATITUDE, data.data)

    def longitude_callback(self, data):
        self.publish_data(DataID.LONGITUDE, data.data)

    def depth_callback(self, data):
        self.publish_data(DataID.DEPTH, data.data)

    def velocity_callback(self, data):
        self.publish_data(DataID.VELOCITY_X, data.data)

    def yaw_callback(self, data):
        self.publish_data(DataID.YAW, data.data)

    def publish_data(self, data_id, value):
        # Create a string in the format of 'data_id, value'
        converted_data = f"{data_id.value}, {value}"

        # Publish the converted data
        self.pub.publish(converted_data)

if __name__ == '__main__':
    try:
        converter = DataConverter()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
