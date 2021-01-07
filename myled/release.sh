#!/bin/bash -eu

echo 0 > /dev/myled0
sudo rmmod myled
make clean

chmod -x myled.c
chmod -x ~/catkin_ws/src/Robosys2020_ROS_LED/scripts/led_sub.py
chmod -x ~/catkin_ws/src/Robosys2020_ROS_LED/scripts/led_pub.py


