import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    ld = LaunchDescription()

    # Start the Gazebo Simulation
    sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('flag_robot'),
                         'launch/sim.launch.py')
        )
    )

    # Start rviz2
    rviz2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('flag_robot'),
                         'launch/rviz.launch.py')
        )
    )

    # Start the SLAM code
    bringup = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('flag_robot'),
                             'launch/bringup.launch.py')
            ), launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Launch the packages
    ld.add_action(bringup)
    ld.add_action(sim)
    ld.add_action(rviz2)
    return ld