import rclpy
from rclpy.executors import MultiThreadedExecutor

from my_first_package.my_publisher import TurtlesimPublisher
from my_first_package.my_subscriber import TurtlesimSubscriber


def main(args=None):
    rclpy.init(args=args)
    publisher = TurtlesimPublisher()
    subscriber = TurtlesimSubscriber()

    executor = MultiThreadedExecutor()
    executor.add_node(publisher)
    executor.add_node(subscriber)
    try:
        executor.spin()
    finally:
        executor.shutdown()
        publisher.destroy_node()
        subscriber.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
