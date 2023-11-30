import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, EmitEvent, RegisterEventHandler
from launch.conditions import IfCondition, UnlessCondition
from launch.event_handlers import OnProcessExit
from launch.events import Shutdown
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from nav2_common.launch import ReplaceString
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Get the launch directory
    bringup_dir = get_package_share_directory('flag_robot')

    # Create the launch configuration variables
    rviz_config_file = LaunchConfiguration('rviz_config')

    # Declare rviz parameter file to be used. We are using 'view_robot.rviz' as a default 
    declare_rviz_config_file_cmd = DeclareLaunchArgument(
        'rviz_config',
        default_value=os.path.join(bringup_dir, 'rviz', 'view_robot.rviz'),
        description='Full path to the RVIZ config file to use')

    # Start the rviz2 node
    start_rviz_cmd = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_file],
        output='screen')

    # Create the launch description and populate
    ld = LaunchDescription()

    # Declare the launch options
    ld.add_action(declare_rviz_config_file_cmd)

    # Launch rviz node with config file loaded up
    ld.add_action(start_rviz_cmd)

    return ld
