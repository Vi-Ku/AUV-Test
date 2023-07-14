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


# Define a class to handle the subscription and publishing for each topic
class TopicSubscriber:
    def __init__(self, topic_name, data_id):
        self.topic_name = topic_name
        self.data_id = data_id
        self.pub = rospy.Publisher('acoustic_data', String, queue_size=10)
        rospy.Subscriber(self.topic_name, Float32, self.callback)

    def callback(self, data):
        converted_data = f"{self.data_id.value}, {data.data}"
        self.pub.publish(converted_data)


if __name__ == '__main__':
    try:
        rospy.init_node('data_converter')

        # Create topic subscribers
        subscribers = [
            TopicSubscriber('auv3/curr_latitude', DataID.LATITUDE),
            TopicSubscriber('auv3/curr_longitude', DataID.LONGITUDE),
            TopicSubscriber('auv3/depth', DataID.DEPTH),
            TopicSubscriber('auv3/velocity', DataID.VELOCITY_X),
            TopicSubscriber('auv3/yaw', DataID.YAW),
        ]

        rospy.spin()
    except rospy.ROSInterruptException:
        pass
