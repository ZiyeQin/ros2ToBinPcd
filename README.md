# ros2ToBinPcd
This repo is for converting ros2bag Lidar data to .bin and .pcd data with UTC timestamps!

## Dependencies
- ROS2
- matplotlib
- numpy
- open3d

## Usage
1. Clone the repo
`git clone https://github.com/ZiyeQin/ros2ToBinPcd.git`

2. Convert the ros2bag to .bin
`python3 rosbag2bin.py`

*You can find the .csv file in the folder with UTC timestamp for each .bin file.*

3. .bin visualization (optional)
`python3 binVisualization.py`

4. Convert the .bin to .pcd
`python3 bin2pcdVisualization.py`