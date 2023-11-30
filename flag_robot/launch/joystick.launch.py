import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    ld = LaunchDescription()

    # Set the path to the params file
    joy_params_path = os.path.join(get_package_share_directory('flag_robot'),
                              'config', 'joystick_params.yaml')
    
    # Launch configuration variables specific to simulation
    use_sim_time = LaunchConfiguration('use_sim_time')
    joy_params = LaunchConfiguration('joy_params')

    
    # Declare launch configurations
    declare_use_sim_time_argument = DeclareLaunchArgument(
        name='use_sim_time',
        default_value='false',
        description='Use simulation clock')

    declare_params_cmd = DeclareLaunchArgument(
        name='joy_params',
        default_value=joy_params_path,
        description='Full path to the joystick parameters file')

    # Start the joy_node
    joy_node = Node(
            package='joy',
            executable='joy_node',
            parameters=[joy_params, {'use_sim_time': use_sim_time}],
         )

    # Start the teleop_node
    teleop_node = Node(
            package='teleop_twist_joy',
            executable='teleop_node',
            name='teleop_node',
            parameters=[joy_params, {'use_sim_time': use_sim_time}],
            remappings=[('/cmd_vel','/cmd_vel_joy')]
         )


    # Declare the launch options
    ld.add_action(declare_params_cmd)
    ld.add_action(declare_use_sim_time_argument)

    # Launch the packages
    ld.add_action(joy_node),
    ld.add_action(teleop_node)
    
    return ld