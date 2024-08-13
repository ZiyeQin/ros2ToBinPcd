# :zzz: ros2ToBinPcd

![Static Badge](https://img.shields.io/badge/Repo-ros2BinPcd-royalblue)
![GitHub watchers](https://img.shields.io/github/watchers/ZiyeQin/ros2ToBinPcd)

This repo is for converting ros2bag(.db3) Lidar data to .bin and .pcd data with UTC timestamps!

## Dependencies
- ROS2
- matplotlib
- numpy
- open3d

## Usage
1. Clone the repo
   
   `git clone https://github.com/ZiyeQin/ros2ToBinPcd.git`

3. Convert the ros2bag to .bin
   
   `python3 rosbag2bin.py`

*You can find the .csv file in the folder with UTC timestamp for each .bin file.*

3. .bin visualization (optional)
   
   `python3 binVisualization.py`

5. Convert the .bin to .pcd
   
   `python3 bin2pcd.py`

6. .pcd visualization (optional)
   
   `python3 pcdVisualization.py`

<!-- ## Contact

- Ziye Qin: ziyeq@ucr.edu -->