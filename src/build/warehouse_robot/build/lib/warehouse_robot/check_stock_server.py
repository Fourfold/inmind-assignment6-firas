import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_msgs.msg import String

class CheckStockServer(Node):
    def __init__(self):
        super().__init__('check_stock_server')