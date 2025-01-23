#!/usr/bin/env pybricks-micropython


# PROJEKT "EDENMOBIL 2025"
# In diesem Projekt planen wir einen Roboter, der in verschiedene Räume fahren kann
# Der Weg soll mit farbigen Markierungen eindeutig vorprogrammierbar sein.


# Importieren der wichtigsten Bibliotheken

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Eigene Unterprogramme/ Module
from functions.line_followerv2 import LineFollower


# Initialisieren des EV3-Steins

ev3 = EV3Brick()



# Sensoren

color_sensor = ColorSensor(Port.S3)
gyro_sensor = GyroSensor(Port.S2)

# Motoren

right_motor = Motor(Port.B)
left_motor = Motor(Port.C)

# Mit Hilfer der Drivebase (Fahrgestell), wird ein einheitliches
# Fahrwerk erstellt und die Motoren arbeiten zusammen
Drive = DriveBase(right_motor, left_motor, wheel_diameter=56, axle_track=152)



# Hauptprogramm des Edenmobils
ev3.speaker.beep()

gyna = LineFollower([], Drive, color_sensor, gyro_sensor, ev3)
gyna.on_line()


