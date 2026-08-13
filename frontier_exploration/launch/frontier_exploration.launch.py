from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 1. C++ Frontier Detector Node
        Node(
            package='frontier_exploration',
            executable='classical_frontier_detector',
            name='classical_frontier_detector',
            output='screen',
            parameters=[
                {"region_size_thresh_": 4},      # Minimum number of points on the frontier
                {"robot_width_": 0.4},             # Go2 Width (about 0.4m)
                {"occupancy_map_topic_": "map"}
            ]
        ),

        # 2. Python Frontier Exploration Node
        Node(
            package='frontier_exploration',
            executable='frontier_exploration_node.py',
            name='frontier_exploration_node',
            output='screen'
        )
    ])