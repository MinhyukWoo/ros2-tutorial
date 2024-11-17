import rclpy
from rclpy.node import Node
from my_first_package_msgs.srv import MultiSpawn
from turtlesim.srv import Spawn
import math
import time


class MultiSpawning(Node):
    def __init__(
        self,
        node_name="multi_spawn",
        *,
        context=None,
        cli_args=None,
        namespace=None,
        use_global_arguments=True,
        enable_rosout=True,
        start_parameter_services=True,
        parameter_overrides=None,
        allow_undeclared_parameters=False,
        automatically_declare_parameters_from_overrides=False,
        enable_logger_service=False
    ):
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
        self.service = self.create_service(
            MultiSpawn, "multi_spawn", self.callback_service
        )
        self.spawn_client = self.create_client(Spawn, "/spawn")
        self.center_x = 5.54
        self.center_y = 5.54

    def callback_service(
        self, request: MultiSpawn.Request, response: MultiSpawn.Response
    ) -> MultiSpawn.Response:
        radius = 3
        response.theta = [
            2 * math.pi * (index / request.num) for index in range(request.num)
        ]

        response.x = [
            self.center_x + radius * math.cos(theta) for theta in response.theta
        ]
        response.y = [
            self.center_y + radius * math.sin(theta) for theta in response.theta
        ]

        for x, y, theta in zip(response.x, response.y, response.theta):
            spawn = Spawn.Request()
            spawn.x = x
            spawn.y = y
            spawn.theta = theta
            self.spawn_client.call_async(spawn)
            time.sleep(0.05)

        return response


def main():
    rclpy.init()
    multi_spawning = MultiSpawning()
    rclpy.spin(multi_spawning)
    multi_spawning.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
