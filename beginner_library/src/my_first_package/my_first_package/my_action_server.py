import time
import rclpy
from rclpy.node import Node
from rclpy.action.server import ActionServer, ServerGoalHandle
from my_first_package_msgs.action import DistTurtle


class DistTurtleServer(Node):
    def __init__(
        self,
        node_name: str = "dist_turtle_action_server",
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
        self.action_server = ActionServer(
            self, DistTurtle, "dist_turtle", self.execute_callback
        )

    def execute_callback(self, goal_handle: ServerGoalHandle) -> DistTurtle.Result:
        result_msg = DistTurtle.Result()
        feedback_msg = DistTurtle.Feedback()

        result_msg.result_dist = 0.0
        for index in range(10):
            feedback_msg.remained_dist = float(index)
            result_msg.result_dist += feedback_msg.remained_dist
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(0.5)

        goal_handle.succeed()
        return result_msg


def main():
    rclpy.init()
    dist_turtle_server = DistTurtleServer()
    rclpy.spin(dist_turtle_server)
    dist_turtle_server.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
