#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import time

def automate():

	rospy.init_node('Automatic_Controller')

	pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

	move_cmd = Twist()

	move_cmd.linear.x = 0.0  	
	move_cmd.angular.z = 0.0   	
	pub.publish(move_cmd)
	time.sleep(1)

	i = 1

	for i in range(2):
		
		move_cmd.linear.x = 0    	
	    move_cmd.angular.z = 0
		pub.publish(move_cmd)
		time.sleep(2)

		move_cmd.linear.x = 0.0  	
		move_cmd.angular.z = 0.0   	
		pub.publish(move_cmd)
		time.sleep(1)

    	move_cmd.linear.x = 2.0
    	move_cmd.angular.z = 0.0   		
		pub.publish(move_cmd)
		time.sleep(3)

		move_cmd.linear.x = 0.0  	
		move_cmd.angular.z = 0.0   	
		pub.publish(move_cmd)
		time.sleep(1)

		i = i + 1


if __name__ == '__main__' :
	
	try:
		automate()

	except rospy.ROSInterruptException:
		pass