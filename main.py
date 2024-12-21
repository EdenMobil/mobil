#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from functions.line_follower import LineFollower
import uasyncio as asyncio

ev3 = EV3Brick()

# Sensors
color_sensor = ColorSensor(Port.S3)
gyro_sensor = GyroSensor(Port.S2)

# Motors
right_motor = Motor(Port.B)
left_motor = Motor(Port.C)

Drive = DriveBase(right_motor, left_motor, wheel_diameter=56, axle_track=152)

# Write your program here.
ev3.speaker.beep()

linefollower = LineFollower(Drive, color_sensor, gyro_sensor, ev3)
linefollower.on_line()