import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/fourfold/dev/inmind sessions/inmind-session-6/assignment_6/src/install/warehouse_robot'
