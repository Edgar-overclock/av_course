**Mapping Robot Simulation Launching Guide**

**Before running the mapping process, ensure you have the following installed:**

Ubuntu 20.04 (or compatible version)
ROS 2 (Foxy, Galactic, or Humble recommended) 3 .Gazebo simulator
TurtleBot3 packages
Navigation and SLAM tools (if needed for mapping visualization)

**Clone the repository**

paste following lines in the terminal (one at a time)

cd ~/ros2_ws/src

git clone https://github.com/Edgar-overclock/av_course

colcon build --packages-select my_robot_controller

source ~/.bashrc

**Launch the simulation**

ros2 launch my_robot_controller start_mapping.launch.py
