import message_filters
from sync_sub.msg import some_position

def callback(msg1, msg2):
  # do something
  position1 = msg1.position
  position2 = msg2.position
  out = [position1, position2]
  print(out)


if __name__ == '__main__':
    sub1 = message_filters.Subscriber('chatter1', some_position)
    sub2 = message_filters.Subscriber('chatter2', some_position)

    fps = 10.
    delay = 1/fps

    ts = message_filters.ApproximateTimeSynchronizer([sub1,sub2], 10, delay)
    ts.registerCallback(callback)
    rospy.spin()
