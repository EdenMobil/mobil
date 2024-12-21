from pybricks.parameters import Color
from pybricks.media.ev3dev import ImageFile, Image


class LineFollower:
    def __init__(self, drivebase, color_sensor, gyro_sensor, ev3):
        self.drivebase = drivebase
        self.color_sensor = color_sensor
        self.gyro_sensor = gyro_sensor
        self.ev3 = ev3
        self.forward = 100
        self.turn_rate = 10
        self.searched_color = Color.BLACK

        self.gyro_sensor.reset_angle(0)
        
    def on_line(self):
        print("Forward")
        while True:
            color = self.color_sensor.color()
            print(color)
            if color == self.searched_color:
                self.ev3.screen.load_image(ImageFile.FORWARD)
                self.drivebase.straight(self.forward)
            else:
                self.ev3.speaker.beep()
                self.search_line()
                
    def search_line(self):
        turn = "RIGHT"
        turned = 0
        turn_rate = self.turn_rate
        while self.searched_color != self.color_sensor.color():
            if turn == "RIGHT":
                self.drivebase.turn(-turn_rate)
                turn = "LEFT"
                turned += 1
            elif turn == "LEFT":
                self.drivebase.turn(2 * turn_rate)
                turn = "RIGHT"
                turned += 1
            if turned % 2 == 0 and turned >= 2:
                turn_rate += self.turn_rate