#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class Simple(Node):
    def __init__(self):
        super().__init__("simple")
        self.get_logger().info("hello ROS2")
        timer = self.create_timer(0.5, self.print_message)

    def print_message(self):
        self.get_logger().info("hello")

def main(args=None):
    rclpy.init(args=args)
    node = Simple()
   
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()