#!/usr/bin/env python

import rospy
from std_msgs.msg import String

heading = 360

def callback(data):
    
    global heading
    
    if( data.data == 'left' ):
        
        if( heading == 0 ):
            heading = 360
        
        heading -= 15
     
    if( data.data == 'right' ): 
        
        if( heading == 360 ):
            heading = 0
        
        heading += 15
        
    rospy.loginfo( 'heading %d', heading )
    
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('direction', String, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
