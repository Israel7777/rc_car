#!/usr/bin/env python


import rospy
from std_msgs.msg import String
def callback_sonar(data):
	sonar = int(data.data)
	if sonar > 10:
	   
		pub.publish("d")
    else:
		pub.publish("f")

rospy.init_node('follow_me_node')
pub = rospy.Publisher('/command', String, queue_size = 2)
sub = rospy.Subscriber('/sonar', String, callback_sonar)
rospy.spin()

