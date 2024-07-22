import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_msgs.msg import String
from warehouse_interfaces.srv import CheckStock
from random import randint

class CheckStockServer(Node):
    stocks = {
        'item 1': 86,
        'item 2': 75,
        'item 3': 98,
        'item 4': 27,
        'item 5': 79,
        'item 6': 6,
        'item 7': 23,
        'item 8': 2,
        'item 9': 14,
        'item 10': 4,
    }

    def __init__(self):
        super().__init__('check_stock_server')
        self.service = self.create_service(CheckStock, 'check_stock', self.check_stock_callback)
        self.get_logger().info('CheckStock server started. Ready for requests.')

    def check_stock_callback(self, request, response):
        item_name = request.item_name
        self.get_logger().info(f'Incoming check stock request for item: {item_name}')
        response.stock_level = randint(0, 100)
        return response

    
def main(args=None):
    rclpy.init(args=args)
    check_stock_server = CheckStockServer()
    rclpy.spin(check_stock_server)
    check_stock_server.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()