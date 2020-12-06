import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class Receiver(Node):

    def __init__(self):
        super().__init__('command_receiver')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.commands = []

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        self.get_commands(msg.data)
        self.get_logger().info('Command found: "%s"' % self.commands[0])
        self.get_logger().info('Parameter found: "%s"' % self.commands[1])

    def get_commands(self, data):
        com1 = 'go to'
        com2 = 'go forward'
        com3 = 'take picture'

        if data.find(com1) != -1:
            self.commands.append(com1)
            r1 = 'kitchen'
            r2 = 'bedroom'
            r3 = 'living room'
            if data.find(r1) != -1:
                self.commands.append(r1)
            elif data.find(r2) != -1:
                self.commands.append(r2)
            elif data.find(r3) != -1:
                self.commands.append(r3)
            else:
                print('No valid room mentioned')
        elif data.find(com2) != -1:
            self.commands.append(com2)
            distance = ''.join(filter(str.isdigit, data))
            self.commands.append(distance)
        elif data.find(com3) != -1:
            self.commands.append(com3)
        else:
            print('Command: ' + data + ' not found')


def main(args=None):
    rclpy.init(args=args)

    receiver = Receiver()

    rclpy.spin(receiver)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    receiver.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
