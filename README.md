# Experiments with ROS and Raspberry PI and Python

## Raspberry PI setup.

Put simple push switches on pins 18 and 24 on a breadboard.

## ROS needs to be set up on the Raspberry PI

http://wiki.ros.org/ROS/Installation

## The Python code

See in the scripts directory. The code is based on tutorial [code](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29).

## To Run

Each in three shells:

Run the ROS OS.

`roscore`

Run the talker

`rosrun test talker.py`

Run the listener

`rosrun test listener.py`

Press one on of the buttons and the output might look like:

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

ROS decouples sensor reading code from other sensor code or motor driving code with the publisher, subscriber pattern. e.g. instead of just outputting:

```
[INFO] [1556918464.372864]: heading 345
[INFO] [1556918464.778167]: heading 330
```

logic could be triggerd to drive a motor. It gives a clue to the possibilities.
