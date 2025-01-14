from pybricks.parameters import Color
from pybricks.media.ev3dev import ImageFile, Image

class GyroNavigation:
    def __init__(self, route, drivebase, color_sensor, gyro_sensor, ev3):
        self.route = route
        self.drivebase = drivebase
        self.color_sensor = color_sensor
        self.gyro_sensor = gyro_sensor
        self.ev3 = ev3

        self.event_counter = 0
        self.event_color = Color.YELLOW
        self.follow_angle = 0
        self.forward = 100

        self.gyro_sensor.reset_angle(0)
        
    def on_line(self):
        print("Forward")
        while True:
            angle = self.gyro_sensor.angle()
            print(angle)
            if angle == self.follow_angle:
                self.ev3.screen.load_image(ImageFile.FORWARD)
                self.drivebase.straight(self.forward)
            else:
                self.ev3.speaker.beep()
                self.correct_direction(angle)
            
            if self.event_color == self.color_sensor.color():
                self.event()
                #break
                
    def correct_direction(self, angle):
        """
        Adjusts the direction based on the current angle from the gyro sensor.

        :param angle: Current angle from the gyro sensor in degrees.
        """
        self.ev3.screen.load_image(ImageFile.QUESTION_MARK)
        self.drivebase.turn(-angle)

    def event(self):
        self.event_counter += 1