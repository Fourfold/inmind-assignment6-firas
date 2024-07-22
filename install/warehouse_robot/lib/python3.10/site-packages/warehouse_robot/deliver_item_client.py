import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from warehouse_interfaces.action import DeliverItem
import time

class DeliverItemServer(Node):
    def __init__(self):
        super().__init__('deliver_item_client')
        self.action_client = ActionClient(self, DeliverItem, 'deliver_item')

    def send_goal(self, item_name, quantity):
        goal_msg = DeliverItem.Goal()
        goal_msg.item_name = item_name
        goal_msg.quantity = quantity

        self.action_client.wait_for_server()
        self.send_goal_future = self.action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
        self.send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Delivery goal rejected')
            return

        self.get_logger().info('Delivery goal accepted')

        self.get_result_future = goal_handle.get_result_async()
        self.get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        if result.success:
            self.get_logger().info('Delivery successful.')
        else:
            self.get_logger().info('Delivery unsuccessful.')
        self.get_logger().info(f'Delivery result message: {result.message}')
        self.destroy_node()
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(f'Received delivery feedback, status: {feedback.status}')


def main(args=None):
    time.sleep(4)
    rclpy.init(args=args)
    deliver_item_client = DeliverItemServer()

    future = deliver_item_client.send_goal('item 1', 5)
    rclpy.spin(deliver_item_client)


if __name__ == '__main__':
    main()