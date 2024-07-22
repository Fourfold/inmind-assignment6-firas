import rclpy
from rclpy.node import Node
from warehouse_interfaces.srv import CheckStock
import matplotlib.pyplot as plt
import time

class CheckStockClient(Node):
    def __init__(self):
        super().__init__('check_stock_client')
        self.client = self.create_client(CheckStock, 'check_stock')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')
        self.request = CheckStock.Request()

    def send_request(self, item_name):
        self.request.item_name = item_name
        self.future = self.client.call_async(self.request)
        rclpy.spin_until_future_complete(self, self.future)
        response = self.future.result()
        self.get_logger().info(f'Response from server: available stock for {item_name}: {response.stock_level}')
        return response.stock_level
    
    def plot_stock(self, items):
        stocks = []
        for item in items:
            stocks.append(self.send_request(item))
        plt.bar(items, stocks)
        plt.title("Stocks")
        plt.xlabel("Item")
        plt.ylabel("Quantity")
        plt.show()


def main(args=None):
    time.sleep(2)
    rclpy.init(args=args)
    client = CheckStockClient()
    client.plot_stock(['item 1', 'item 2', 'item 3', 'item 4', 'item 5', 'item 6', 'item 7', 'item 8', 'item 9', 'item 10'])
    client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()