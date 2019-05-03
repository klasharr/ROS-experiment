#!/usr/bin/env python

import rospy
from std_msgs.msg import String

import RPi.GPIO as GPIO
import time

def talker():
  
    # Publish to the direction topic 
    pub = rospy.Publisher('direction', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
    pub.publish( 'start' )

    # Set up the GPIO pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_UP)


    while not rospy.is_shutdown():

        # detect button presses on the two pins
        
        left = GPIO.input(18)
        right = GPIO.input(24)
        
        if left == False:
            
            rospy.loginfo( 'left' )
            
            # simple button debounce
            time.sleep(0.2)
            pub.publish( 'left' )
            
        if right == False:
            
            rospy.loginfo( 'right' )
            time.sleep(0.2)
            pub.publish( 'right' )
        
        rate.sleep();
                

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
