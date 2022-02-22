#!/usr/bin/env python
import rospy
from carla_msgs.msg import CarlaEgoVehicleControl
from std_msgs.msg import Float32


class RosNode:
    def __init__(self):
        rospy.init_node("carla_speed_control")
        rospy.loginfo("Starting Carla Speed Control.")
        self.TARGET_SPEED = 8.3  # 40 km/h
        self.KP = 0.5
        self.KD = 0.1
        self._prev_error = 0
        rospy.Subscriber("/carla/ego_vehicle/speedometer",
                         Float32, self._control)
        self._cmd_pub = rospy.Publisher(
            "/carla/ego_vehicle/vehicle_control_cmd", CarlaEgoVehicleControl, queue_size=1)

    def _control(self, current_speed):
        error = self.TARGET_SPEED - current_speed.data
        u = self.KP * error + self.KD*(error - self._prev_error)
        self._prev_error = error
        control_msg = CarlaEgoVehicleControl()
        control_msg.header.stamp = rospy.Time.now()
        control_msg.throttle = min(1.0, u)
        self._cmd_pub.publish(control_msg)


if __name__ == "__main__":
    ros_node = RosNode()
    rospy.spin()
