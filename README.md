# Description
Use ROS with Raspberry Pi 3 model B+ <br>
Operate three LEDs using Raspberry Pi with linux. <br>
写真 <br>
Used lecture materials of Robosys and iidayuki's github as a reference. <br>
https://github.com/ryuichiueda/robosys2020.git <br>
https://github.com/iidayuki/robosys_ros

# Requirements

|No.|Item Name|Quantity|
|:---:|:---:|:---:|
|1|Raspberry Pi 3 model B+ <br> (installed ROS)|1|
|2|Bread board|1|
|3|LED|3|
|4|Cable|7|
|5|150Ω Resistor|3|

# Circuit diagram
![キャプチャ](https://user-images.githubusercontent.com/50652151/101168661-19692600-367f-11eb-98eb-d5c2cc75d4ee.PNG)

# How to use
**Install**
```python
$ cd ~/catkin_ws/src
$ git clone https://github.com/Chappy06260/robosys2020_ros_led.git
$ cd ~/catkin_ws
$ catkin_make
$ cd ~/catkin_ws/src/robosys2020_ros_led/myled
$ chmod +x setup.sh
$ ./setup.sh
```

**Run** <br>
Terminal1
```python
$ roscore
```
Terminal2
``` python
$ rosrun robosys2020_ros_led led_sub.py
```
Terminal3
``` python
$ rosrun robosys2020_ros_led led_pub.py
```

**Commnad list** <br>
```python
1: Turn on only Led1
2: Turn on only Led2
3: Turn on only Led3
4: Turn on Led1 & Led2
5: Turn on Led2 & Led3
6: Turn on Led1 & Led3
a: Turn on all Led
n: Turn off all Led
CTRL + C: Quit
```

**Uninstall**
```python
$ cd ~/catkin_ws/src/robosys2020_ros_led/myled
$ chmod +x release.sh
$ ./release.sh
```

**Video**
