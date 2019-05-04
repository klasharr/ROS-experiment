# Experiments with ROS and Raspberry PI and Python

## Raspberry PI setup.

Put simple push switches on pins 18 and 24 on a breadboard.

![image](https://klausharris.files.wordpress.com/2019/05/img_20190504_081019052.jpg)

## ROS needs to be set up on the Raspberry PI

http://wiki.ros.org/ROS/Installation

## The Python code

I created a new ROS package first as explained [here](http://wiki.ros.org/catkin/Tutorials/CreatingPackage), the added the python scripts which live in the [scripts](https://github.com/klasharr/auto_boat/tree/master/test/scripts) directory. The code is based on this tutorial [code](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29).

## To Run

ROS has a mechanism for making launch files to simplify this but the absolute simplest way to test this is to run the following in three separate shells:

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
