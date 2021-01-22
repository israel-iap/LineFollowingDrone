#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool
from std_msgs.msg import Empty
# to do:
# agregar y crear topico, para determinar si se debe aterrizar

def listen():
    rospy.init_node("land",anonymous=True)
    rospy.Subscriber("status",Bool,callback)
    while not rospy.is_shutdown():
      pub.publish(Empty())
      rate.sleep()


def land():
    pub = rospy.Publisher("ardrone/land", Empty, queue_size=10 )
    rospy.init_node('land', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
      pub.publish(Empty())
      rate.sleep()


if __name__ == '__main__':
  try:
   listen()
   land()
  except rospy.ROSInterruptException:
   pass