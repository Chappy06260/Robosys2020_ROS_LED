#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool

if __name__ == "__main__":
    rospy.init_node( "led_pub" )
    pub1 = rospy.Publisher( "led1", Bool, queue_size = 10 )
    pub2 = rospy.Publisher( "led2", Bool, queue_size = 10 )
    pub3 = rospy.Publisher( "led3", Bool, queue_size = 10 )
    rate = rospy.Rate( 10 )

    pub1.publish( False )
    pub2.publish( False )
    pub3.publish( False )

    try:
        while not rospy.is_shutdown():
            direction = input('1:Led1, 2:Led2, 3:Led3, 4:Led1&2, 5:Led2&3, 6:Led1&3, a:All n: None, CTRL+C:Quit > ')
            if '1' in direction:
                pub1.publish( True )
                pub2.publish( False )
                pub3.publish( False )
            if '2' in direction:
                pub1.publish( False )
                pub2.publish( True )
                pub3.publish( False )
            if '3' in direction:
                pub1.publish( False )
                pub2.publish( False )
                pub3.publish( True )
            if '4' in direction:
                pub1.publish( True )
                pub2.publish( True )
                pub3.publish( False )
            if '5' in direction:
                pub1.publish( False )
                pub2.publish( True )
                pub3.publish( True )
            if '6' in direction:
                pub1.publish( True )
                pub2.publish( False )
                pub3.publish( True )
            if 'a' in direction:
                pub1.publish( True )
                pub2.publish( True )
                pub3.publish( True )
            if 'n' in direction:
                pub1.publish( False )
                pub2.publish( False )
                pub3.publish( False )

                rate.sleep()
    except rospy.KeybordInterrupt:
        pub1.publish( False )
        pub2.publish( False )
        pub3.publish( False )
        pass
