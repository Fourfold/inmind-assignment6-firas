import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from warehouse_interfaces.action import DeliverItem
import time

class DeliverItemServer(Node):
    def __init__(self):
        super().__init__('deliver_item_server')
        self.action_service = ActionServer(self, DeliverItem, 'deliver_item', self.execute_callback)
        self.get_logger().info('DeliverItem server started. Ready for requests.')

    def execute_callback(self, goal_handle):
        self.get_logger().info(f'Received delivery request: {goal_handle.request.quantity} of {goal_handle.request.item_name}')

        feedback_msg = DeliverItem.Feedback()
        feedback_msg.status = 'Loading items...'
        goal_handle.publish_feedback(feedback_msg)
        time.sleep(3)

        feedback_msg.status = 'Navigating...'
        goal_handle.publish_feedback(feedback_msg)
        time.sleep(5)

        feedback_msg.status = 'Unloading items...'
        goal_handle.publish_feedback(feedback_msg)
        time.sleep(3)

        goal_handle.succeed()

        result = DeliverItem.Result()
        result.success = True
        result.message = 'Delivery is completed successfully'
        return result

def main(args=None):
    rclpy.init(args=args)
    deliver_item_server = DeliverItemServer()
    rclpy.spin(deliver_item_server)
    deliver_item_server.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()