import rclpy as rp
from rclpy.node import Node
from turtlesim.msg import Pose


class TurtlesimSubscriber(Node):
    def __init__(
        self,
        node_name: str = "turtlesim_subscriber",
        *,
        context: rp.Context | None = None,
        cli_args: rp.List[str] | None = None,
        namespace: str | None = None,
        use_global_arguments: bool = True,
        enable_rosout: bool = True,
        start_parameter_services: bool = True,
        parameter_overrides: rp.List[rp.Parameter] | None = None,
        allow_undeclared_parameters: bool = False,
        automatically_declare_parameters_from_overrides: bool = False,
        enable_logger_service: bool = False,
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
        self.subscription = self.create_subscription(
            Pose, "turtle1/pose", self.callback, 10
        )

    def callback(self, msg: Pose):
        print(f"X: {msg.x}, Y: {msg.y}, theta: {msg.theta}")


def main():
    rp.init()

    turtlesim_subscriber = TurtlesimSubscriber()
    rp.spin(turtlesim_subscriber)

    turtlesim_subscriber.destroy_node()
    rp.shutdown()


if __name__ == "__main__":
    main()
