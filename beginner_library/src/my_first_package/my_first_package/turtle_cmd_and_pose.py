import rclpy
from rclpy.node import Node
from my_first_package_msgs.msg import CmdAndPoseVel
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


class CmdAndPose(Node):
    def __init__(
        self,
        node_name: str = "turtle_cmd_pose",
        *,
        context: rclpy.Context | None = None,
        cli_args: rclpy.List[str] | None = None,
        namespace: str | None = None,
        use_global_arguments: bool = True,
        enable_rosout: bool = True,
        start_parameter_services: bool = True,
        parameter_overrides: rclpy.List[rclpy.Parameter] | None = None,
        allow_undeclared_parameters: bool = False,
        automatically_declare_parameters_from_overrides: bool = False,
        enable_logger_service: bool = False
    ) -> None:
        super().__init__(
            node_name,
            context=context,
            cli_args=cli_args,
            namespace=namespace,
            use_global_arguments=use_global_arguments,
            enable_rosout=enable_rosout,
            start_parameter_services=start_parameter_services,
            parameter_overrides=parameter_overrides,
            allow_undeclared_parameters=allow_undeclared_parameters,
            automatically_declare_parameters_from_overrides=automatically_declare_parameters_from_overrides,
            enable_logger_service=enable_logger_service,
        )
        self.pose_subscription = self.create_subscription(
            Pose, "/turtle1/pose", self.callback_pose, 10
        )
        self.cm_vel_subscription = self.create_subscription(
            Twist, "/turtle1/cmd_vel", self.callback_cmd_vel, 10
        )
        self.publisher = self.create_publisher(CmdAndPoseVel, "/cmd_and_pose", 10)
        self.timer = self.create_timer(1.0, self.callback_timer)
        self.cmd_pose = CmdAndPoseVel()

    def callback_pose(self, pose: Pose):
        self.cmd_pose.pose_x = pose.x
        self.cmd_pose.pose_y = pose.y
        self.cmd_pose.linear_vel = pose.linear_velocity
        self.cmd_pose.angular_vel = pose.angular_velocity

    def callback_cmd_vel(self, twist: Twist):
        self.cmd_pose.cmd_vel_angular = twist.angular.z
        self.cmd_pose.cmd_vel_linear = twist.linear.x

    def callback_timer(self):
        self.publisher.publish(self.cmd_pose)


def main():
    rclpy.init()

    cmd_and_pose = CmdAndPose()
    rclpy.spin(cmd_and_pose)

    cmd_and_pose.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
