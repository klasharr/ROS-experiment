# Experiment with ROS, Raspberry PI and Python

## Raspberry PI setup.

Put simple push switches on pins 18 and 24 on a breadboard.

![image](https://klausharris.files.wordpress.com/2019/05/img_20190504_081019052.jpg)

## ROS needs to be set up on the Raspberry PI

http://wiki.ros.org/ROS/Installation

If anything doesn't work, it's most likely to be an environment variables issue, e.g. for me this solved packages not being found.

`export ROS_PACKAGE_PATH=/home/pi/catkin_ws/src:$ROS_PACKAGE_PATH` 

Also, I only installed the shell version, not the full desktop version.

## The Python code

I created a new ROS package first as explained [here](http://wiki.ros.org/catkin/Tutorials/CreatingPackage), my test python scripts live in the [scripts](https://github.com/klasharr/auto_boat/tree/master/test/scripts) directory, and that's all you need to write. The code is based on this tutorial [code](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29).

## To Run

You can configure a [launch file](http://wiki.ros.org/roslaunch/XML#Example_.launch_XML_Config_Files) [#](http://wiki.ros.org/roslaunch), but the simplest way to test this is to run the following in three separate shells:

All from within catkin workspace directory:

`/home/pi/catkin_ws/`

Run the ROS OS.

`roscore`

Run the talker

`rosrun test talker.py`

Run the listener

`rosrun test listener.py`

## Test it

Press one one of the buttons and the output might look like:

```
pi@raspberrypi:~/catkin_ws/src/test/scripts $ rosrun test listener.py 
[INFO] [1556918461.361843]: heading 360
[INFO] [1556918461.964700]: heading 15
[INFO] [1556918462.867729]: heading 30
[INFO] [1556918463.667803]: heading 15
[INFO] [1556918464.167762]: heading 0
[INFO] [1556918464.372864]: heading 345
[INFO] [1556918464.778167]: heading 330
```

## What's next?

In this example, we see ROS decoupling sensor reading code from the action code. It would be possible to add more sensors and talkers or other listener (action code). See more on [publishers and subscribers](http://wiki.ros.org/roscpp/Overview/Publishers%20and%20Subscribers). 

e.g. instead of just outputting:

```
[INFO] [1556918464.372864]: heading 345
[INFO] [1556918464.778167]: heading 330
```

logic could be triggered to drive a motor. With a more complicated robot, this would be ideal to keep the application simple and all parts decoupled.

## Resources

- https://www.ros.org/ 
- http://wiki.ros.org/rospy - ROS Python client
- [Raspberry Pi cookbook](http://shop.oreilly.com/product/0636920045182.do)

