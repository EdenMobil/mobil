from pybricks.parameters import Color
from pybricks.media.ev3dev import ImageFile
from pybricks.tools import wait

class LineFollower:
    def __init__(self, drivebase, color_sensor, gyro_sensor, ev3):
        self.drivebase = drivebase
        self.color_sensor = color_sensor
        self.gyro_sensor = gyro_sensor
        self.ev3 = ev3
        self.forward_speed = 100  # Speed in mm/s
        self.turn_rate = 10      # Turn rate in deg/s
        self.searched_color = Color.BLACK
        self.running = True
        
        # Reset gyro angle to 0
        self.gyro_sensor.reset_angle(0)