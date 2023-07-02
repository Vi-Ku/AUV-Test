#!/usr/bin/env python
import rospy
import Jetson.GPIO as GPIO

# Pin Definitions
heartbeat_pin = 40  # BOARD pin 40
heartBeatTime = 0.5

def main():
    # Init Node
    rospy.init_node('heartbeat_node', anonymous=True)
    
    # Pin Setup:
    GPIO.setmode(GPIO.BOARD)  # use BOARD pin numbering
    GPIO.setup(heartbeat_pin, GPIO.OUT)  # set the heartbeat pin to be an output pin

    rospy.loginfo("Starting heartbeat...")
    try:
        while not rospy.is_shutdown():
            GPIO.output(heartbeat_pin, GPIO.HIGH)  # set the pin HIGH
            rospy.sleep(heartBeatTime)  # wait half a second
            GPIO.output(heartbeat_pin, GPIO.LOW)  # set the pin LOW
            rospy.sleep(heartBeatTime)  # wait half a second
    finally:
        GPIO.cleanup()  # cleanup all GPIOs

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        GPIO.cleanup()  # cleanup all GPIOs
        pass
