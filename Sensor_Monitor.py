#!/usr/bin/env python
import rospy
from std_msgs.msg import Bool

# List of sensor topics and names to monitor
sensor_topics = [('/sensor1', 'Sensor 1'), ('/sensor2', 'Sensor 2'), ('/sensor3', 'Sensor 3')]

# Dictionary to store the status of sensors
sensor_status = {sensor_name: False for _, sensor_name in sensor_topics}

# Callback function to monitor the sensor status
def sensor_status_callback(msg, sensor_name):
    if msg.data:
        rospy.loginfo("{} is publishing data.".format(sensor_name))
        sensor_status[sensor_name] = True
    else:
        rospy.logwarn("{} is not publishing data.".format(sensor_name))
        sensor_status[sensor_name] = False

# ROS node initialization
rospy.init_node('sensor_monitor')

# Publisher to publish sensor status information
sensor_status_pub = rospy.Publisher('/sensor_status', Bool, queue_size=10)

# Create subscribers for each sensor topic
sensor_subscribers = []
for topic, sensor_name in sensor_topics:
    sensor_subscriber = rospy.Subscriber(topic, Bool, sensor_status_callback, callback_args=sensor_name)
    sensor_subscribers.append(sensor_subscriber)

# Timer callback function to periodically publish sensor statuses
def publish_sensor_status(event):
    overall_status = all(sensor_status.values())
    sensor_status_pub.publish(overall_status)

# Start a timer to periodically publish sensor statuses
status_timer = rospy.Timer(rospy.Duration(1), publish_sensor_status)  # Adjust the duration as needed

# Main loop
rospy.spin()
