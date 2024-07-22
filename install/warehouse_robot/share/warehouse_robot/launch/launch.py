from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='warehouse_robot',
            executable='stock_server',
            name='stock_server'
        ),
        Node(
            package='warehouse_robot',
            executable='stock_client',
            name='stock_client'
        ),
    ])