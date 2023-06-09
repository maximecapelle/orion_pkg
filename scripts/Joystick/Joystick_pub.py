#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
import pygame
from scripts import Init_Parameters as IP




class JoystickPubNode(Node):
    def __init__(self):
        super().__init__('JoystickPubNode')
        self.publisher_ = self.create_publisher(Joy, IP.JS_TopicName, IP.qos_profile)
        self.timer_ = self.create_timer(IP.JS_PublishRate, self.publish_controller_inputs)

        # Initialize pygame and the controller
        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def publish_controller_inputs(self):
        pygame.event.pump()

        axes = []
        for i in range(self.controller.get_numaxes()):
            axes.append(self.controller.get_axis(i))

        buttons = []
        for i in range(self.controller.get_numbuttons()):
            buttons.append(self.controller.get_button(i))

        joy_msg = Joy()
        joy_msg.header.stamp = self.get_clock().now().to_msg()
        joy_msg.axes = axes
        joy_msg.buttons = buttons
        self.publisher_.publish(joy_msg)

def main(args=None):
    if IP.EnableJoystick or IP.EnableAll:
        rclpy.init(args=args)
        node = JoystickPubNode()
        rclpy.spin(node)
        rclpy.shutdown()

if __name__ == '__main__':
    main()