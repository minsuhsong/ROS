import rospy
from beginner_tutorials.msg import first_msg

def callback(data):
    rospy.loginfo("talk1_int = %d", data.number)
    rospy.loginfo("talk1_string = %s", data.num_string)
    rospy.loginfo("talk1_list = " + data.num_list)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('chatter', first_msg, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()