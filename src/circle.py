#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import time

def automate():

	rospy.init_node('Automatic_Controller')

	pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

	move_cmd = Twist()

	move_cmd.linear.x = 0.0  	#	meter/second\
	move_cmd.angular.z = 0.0   	# 	radian/second
	pub.publish(move_cmd)
	time.sleep(2)

	i=0

	for i in range (12):

		move_cmd.linear.x = 2  	#	meter/second\
		move_cmd.angular.z = 1.6   	# 	radian/second
		pub.publish(move_cmd)
		time.sleep(5)

		"""move_cmd.linear.x = 2  	#	meter/second\
		move_cmd.angular.z = 1.6   	# 	radian/second
		pub.publish(move_cmd)
		time.sleep(3)

		move_cmd.linear.x = 0.0  	#	meter/second\
		move_cmd.angular.z = 0.0   	# 	radian/second
		pub.publish(move_cmd)
		time.sleep(1)

		move_cmd.linear.x = 2  	#	meter/second\
		move_cmd.angular.z = 1.6   	# 	radian/second
		pub.publish(move_cmd)
		time.sleep(3)

		move_cmd.linear.x = 0.0  	#	meter/second\
		move_cmd.angular.z = 0.0   	# 	radian/second
		pub.publish(move_cmd)
		time.sleep(1)"""
		
		
		i = i+1



if __name__ == '__main__' :
	
	try:
		automate()

	except rospy.ROSInterruptException:
		pass