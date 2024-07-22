from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'warehouse_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='fourfold',
    maintainer_email='fourfold164@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'stock_server = warehouse_robot.check_stock_server:main',
            'stock_client = warehouse_robot.check_stock_client:main',
            'delivery_server = warehouse_robot.deliver_item_server:main',
            'delivery_client = warehouse_robot.deliver_item_client:main',
        ],
    },
)
