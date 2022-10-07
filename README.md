# refactored-pancake

This repository is for university project.

## 1. Run

This section shows the procedure of launching the code.

### 1.1. Lidar and Hector Slam

To run lidar and hector slam, run the following commands in seperate terminal:

1. Run `roscore`:

```bash
roscore
```

2. Launch lidar driver:

```bash
roslaunch refactored-pancake/catkin_ws/src/YDLiDAR/ydlidar_ws/src/ydlidar_ros_driver-master/launch/lidar.launch
```

3. Launch hector slam:

```bash
roslaunch refactored-pancake/catkin_ws/src/hector_slam/hector_slam_launch/launch/tutorial.launch
```

## 2. Issues

The issues should have the following sections if appropriate:

```md
# Description
# Screenshots
# To Reproduce
# Files
# Tasks
```

Not all the sections are required, but if the section better describe the issue, it must be included.