#!/bin/bash -eu

sudo rmmod myled
make clean

chmod -x myled.c
chmod -x ~/catkin_ws/src/robosys2020_ros_led/scripts/led_sub.py
chmod -x ~/catkin_ws/src/robosys2020_ros_led/scripts/led_pub.py


