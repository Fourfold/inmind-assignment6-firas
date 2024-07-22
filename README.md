# Robotics Assignment - Session 6 - ROS2

To build the project, enter the following commands while in the directory of the repository:
```
source install/setup.bash
colcon build
```
---
Then, to run the project, enter:
```
ros2 launch src/temp_monitor/launch/launch.py
```
---
When the project is launched, the service and action servers are up and running, then the stock service client sends a request after 2 seconds, then the delivery action client sends a goal after 2 seconds.
