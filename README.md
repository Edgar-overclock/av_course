**1. Download the repository into your ROS 2 workspace**

Navigate to your ROS 2 workspace
cd ~/ros2_ws

Clone this repository
git clone https://github.com/Edgar-overclock/av_course

Go back to workspace root
cd ~/ros2_ws

Build all packages
colcon build --symlink-install

Source the overlay
source ~/.bashrc

**2. Running Mapping**

Launch the mapping node
ros2 launch my_robot_controller start_mapping.launch.py

**3. Running Navigation**

Launch the navigation node
ros2 launch my_robot_controller run_navigation.launch.py
