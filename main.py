#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from functions.line_followerv2 import LineFollower


# Initialisieren des Bricks

ev3 = EV3Brick()




# Sensors
Farbsensor = ColorSensor(Port.S3)
Gyrosensor = GyroSensor(Port.S2)

# Motors
MotorRechts = Motor(Port.B)
MotorLinks = Motor(Port.C)

Fahrgestell = DriveBase(MotorRechts, MotorLinks, wheel_diameter=56, axle_track=152)



# Hauptprogramm

ev3.speaker.beep()


# Im Hauptprogramm sollte eingebaut werden, dass man entscheiden kann,
# wohin der Roboter fährt

 while True:
    raumwahl = int(input('In welchen Raum soll der Roboter ?\n
    Werkraum      (1)\n
    Kunstraum U07 (2)\n
    Kunstraum U06 (3)\n'))
    if raumwahl == 1:
        gyna = LineFollower([], Fahrgestell, Farbsensor, Gyrosensor, ev3)
        gyna.AufLinie()