#!/bin/bash -eu

chmod +x myled.c
make
sudo insmod myled.ko
sudo chmod 666 /dev/myled0

chmod +x ~/catkin_ws/src/robosys2020_ROS_LED/scripts/led_sub.py
chmod +x ~/catkin_ws/src/robosys2020_ROS_LED/scripts/led_pub.py
