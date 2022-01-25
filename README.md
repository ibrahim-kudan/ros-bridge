# Changes 

- [x] Turning all ego vehicle traffic lights to green (It will be always driving and not wasting time in red traffic lights)
- [x] Added ROS argument to change the speed limit in the AutoPilot mode. check speed_limit_percent in [carla_ros_bridge_with_example_ego_vehicle.launch](https://github.com/ibrahim-kudan/ros-bridge/blob/aee83fcf0eea9aa07368c1c6d2b5909bf889717b/carla_ros_bridge/launch/carla_ros_bridge_with_example_ego_vehicle.launch#L7) 


## Run on Nausicaa

[1] Start CARLA server 

```console
$ cd /opt/carla-simulator && ./CarlaUE4.sh -prefernvidia -quality-level=Low -carla-server -RenderOffScreen
```
[2] Open CARLA ports 2000,20001

```console
$ sudo ufw allow 2000 && sudo ufw allow 2001

```
[3] Connect from client Laptop for example using ros_bridge 

```console
$ roslaunch carla_ros_bridge carla_ros_bridge_with_example_ego_vehicle.launch host:="Nausicaa_IP"
```

# ROS/ROS2 bridge for CARLA simulator

[![Actions Status](https://github.com/carla-simulator/ros-bridge/workflows/CI/badge.svg)](https://github.com/carla-simulator/ros-bridge)
[![Documentation](https://readthedocs.org/projects/carla/badge/?version=latest)](http://carla.readthedocs.io)
[![GitHub](https://img.shields.io/github/license/carla-simulator/ros-bridge)](https://github.com/carla-simulator/ros-bridge/blob/master/LICENSE)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/carla-simulator/ros-bridge)](https://github.com/carla-simulator/ros-bridge/releases/latest)

 This ROS package is a bridge that enables two-way communication between ROS and CARLA. The information from the CARLA server is translated to ROS topics. In the same way, the messages sent between nodes in ROS get translated to commands to be applied in CARLA.

![rviz setup](./docs/images/ad_demo.png "AD Demo")

**This version requires CARLA 0.9.12**

## Features

- Provide Sensor Data (Lidar, Semantic lidar, Cameras (depth, segmentation, rgb, dvs), GNSS, Radar, IMU)
- Provide Object Data (Transforms (via [tf](http://wiki.ros.org/tf)), Traffic light status, Visualization markers, Collision, Lane invasion)
- Control AD Agents (Steer/Throttle/Brake)
- Control CARLA (Play/pause simulation, Set simulation parameters)

## Getting started and documentation

Installation instructions and further documentation of the ROS bridge and additional packages are found [__here__](https://carla.readthedocs.io/projects/ros-bridge/en/latest/).
