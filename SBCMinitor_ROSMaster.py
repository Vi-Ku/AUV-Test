#!/usr/bin/env python
import rospy
import RPi.GPIO as GPIO

# Pin Definitions
heartbeat_pin = 18  # BOARD pin 40
heartBeatTime = 0.5

def if_roscore_running():
  try:
    rospy.get_master().getPid()
    return True
  except roslaunch.core.RLException:
    return False

def main():
    # Init Node
    rospy.init_node('heartbeat_node', anonymous=True)

    # Pin Setup:
    GPIO.setmode(GPIO.BCM)  # BCM pin-numbering scheme from Raspberry Pi
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)
    # Pin Setup:


    rospy.loginfo("Starting heartbeat...")
    try:
        while not rospy.is_shutdown() and if_roscore_running():
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
