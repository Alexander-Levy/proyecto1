import os

from launch import LaunchDescription

from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource 
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    # Declarte Launch Arguments
    use_sim_time = LaunchConfiguration('use_sim_time')
    
    declare_use_sim_time_cmd = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false',
        description='Use simulation (Gazebo) clock if true')
    
    # Start Simultaneous Localization And Mapping
    slam = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('flag_robot'),
                             'launch/slam.launch.py')
            ), launch_arguments={'use_sim_time': use_sim_time}.items()
    )
        
    # Start nan2 controller, planner, and lifecylce manager
    nav2_stack = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('flag_robot'),
                             'launch/nav2.launch.py')
            ), launch_arguments={'use_sim_time': use_sim_time}.items()
    )

    ld = LaunchDescription()
    # Declare the launch options
    ld.add_action(declare_use_sim_time_cmd)

    # Start running SLAM
    ld.add_action(slam)

    # Start Nav2 Stack
    ld.add_action(nav2_stack)

    return ld