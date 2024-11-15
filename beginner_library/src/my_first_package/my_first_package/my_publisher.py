import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TurtlesimPublisher(Node):
    def __init__(
        self,
        node_name: str = "turtlesim_publisher",
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
        self.pubisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)

        self.timer = self.create_timer(
            timer_period_sec=0.5, callback=self.timer_callback
        )

    def timer_callback(self):
        twist = Twist()
        twist.linear.x = 2.0
        twist.angular.z = 2.0
        self.pubisher.publish(msg=twist)


def main():
    rclpy.init()

    turtlesim_publisher = TurtlesimPublisher()
    rclpy.spin(turtlesim_publisher)

    turtlesim_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
