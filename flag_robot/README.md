# Autonomous Flag Capturing Differential Drive Robot 

## Introduction
This is a template for a simple capture the flag differential drive robot. This proyect is built to be easy to modify, expand and apdat it to your needs. This is a ROS2 based proyect that is built to work on: 

    Linux distro: Ubuntu 20.04 LTS
    ROS2 distro: Foxy Fitzroy

The proyect includes two packages, one name "flag_robot" consist of an autonomous robot that can map its working area, locate itself within that area and plan the best path to its objective. Please make sure to change all instances of "flag_robot" to whatever you choose to name your pacakge.

## File Organization
This pacakage consist of 4 main folders:

- config: This is where all of the parameters files are saved. This is done so that we don't need to re-parametrize our nodes each time we run them

- description: This is where all our files referring to the robot description are saved. This could be done in only one file, but for readability and versatility, we are using xacro to make development quicker.

- launch: This is where we store our launch files.

- rviz: Parameter files for common and useful views, topics and remapping for rviz will be stored here for automation purposes.

- worlds: Here i store worlds used to testing our robot in our simulated enviroment.

## Dependencies
This proyect depends on these general packages: 

    joystick 
    jstest-gtk evtest
    python3-argcomplete
    software-properties-common
    python3-colcon-common-extensions

This proyect depends on the following ROS2 packages:

    ros-foxy-desktop

    ros-foxy-xacro
    ros-foxy-joint-state-publisher-gui
    ros-foxy-gazebo-ros-pkgs

    ros-foxy-rplidar-ros

    v4l-utils 
    ros-foxy-v4l2-camera 
    ros-foxy-image-transport-plugins

    ros-foxy-ros2-control 
    ros-foxy-ros2-controllers 
    ros-foxy-gazebo-ros2-control

    ros-foxy-slam-toolbox
    ros-foxy-navigation2
    ros-foxy-nav2-bringup
    ros-foxy-turtlebot3

    ros-foxy-twist-mux

Rasberry Pi dependency only: 

    libraspberrypi-bin
