import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class TurtlebotMappingNode(Node):

    def __init__(self):
        super().__init__("mapping_node")
        self.get_logger().info("Mapping Node has started.")
        # Publisher to send movement commands
        self._pose_publisher = self.create_publisher(
        Twist, "/cmd_vel", 10
        )
        # Subscriber to receive LiDAR data
        self._scan_listener = self.create_subscription(
        LaserScan, "/scan", self.robot_controller, 10
        )
    def update_distance_variables(self, scan: LaserScan):
        """
        Update the directional distance variables from the scan message.
        """
        # Adjust these indices based on your LiDAR's configuration
        a = 5  # example width parameter for front detection
        b = 1  # example parameter for combining front slices
        self._front = min(scan.ranges[:b+1] + scan.ranges[-b:])
        self._left = min(scan.ranges[3:60])
        self._right = min(scan.ranges[359:300:-1])
        self._leftback = min(scan.ranges[60:179])
        self._rightback = min(scan.ranges[299:181:-1])
    def robot_controller(self, scan: LaserScan):
        cmd = Twist()
        # Define the width of the range for obstacle detection
        a = 5
        b = 1
        safe_dist = 0.5
        angl_speed = 3.0

        # Extract directional distances
        #self._front = min(scan.ranges[:b+1] + scan.ranges[-b:])
        self._left = min(scan.ranges[3:60])
        self._right = min(scan.ranges[359:300:-1])
        self._leftback = min(scan.ranges[60:179])
        self._rightback = min(scan.ranges[299:181:-1])
        # Navigation logic based on obstacle detection

        if self._left < safe_dist and self._right >= safe_dist:
            cmd.linear.x = 0.05
            cmd.angular.z = -angl_speed # Turn right
        
        elif self._right < safe_dist and self._left >= safe_dist:
            cmd.linear.x = 0.05
            cmd.angular.z = angl_speed # Turn left
        
        elif self._right < safe_dist and self._left < safe_dist:
            cmd.linear.x = 0.-5
            
            if self._leftback < self._rightback:
                cmd.linear.x = -0.05
                cmd.angular.z = -angl_speed # Turn right
            
            elif self._leftback > self._rightback:
                cmd.linear.x = -0.05
                cmd.angular.z = angl_speed # Turn left
        
        else:
            cmd.linear.x = 0.3
            cmd.angular.z = 0.0 # Move forward
        """
        
        
        if self._front < 1.3: # Obstacle ahead
            if self._right < self._left:
                cmd.linear.x = 0.00
                cmd.angular.z = 0.5 # Turn left
            else:
                cmd.linear.x = 0.00
                cmd.angular.z = -0.5 # Turn right
        """
        
        # Publish the command
        self._pose_publisher.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = TurtlebotMappingNode()
    rclpy.spin(node)
    rclpy.shutdown()