import rospy
from beginner_tutorials.msg import first_msg

def talker():
    pub = rospy.Publisher('chatter', first_msg, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    msg = first_msg()
    msg.number = 1
    msg.num_string = "ONE"
    msg.num_list = [1, 2, 3]

    while not rospy.is_shutdown():
        rospy.loginfo("Integer sent: %d", msg.number)
        rospy.loginfo("Sting sent: %s", msg.num_string)
        rospy.loginfo("List sent: " + msg.num_list)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
