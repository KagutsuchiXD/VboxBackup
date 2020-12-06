import sys

import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class NetSpeaker(Node):

    def __init__(self):
        super().__init__('send_commands')
        self.commander = self.create_publisher(String, 'topic', 10)
        self.input = sys.argv[1]

    def command_drone(self):
        command = String()
        command.data = self.input
        self.commander.publish(command)
        self.get_logger().info('Sending: "%s"' % command.data)


def main(args=None):
    rclpy.init(args=args)

    commander = NetSpeaker()

    rclpy.spin_once(commander)

    commander.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
