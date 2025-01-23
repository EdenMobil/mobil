from pybricks.parameters import Color
from pybricks.media.ev3dev import ImageFile, Image

class LineFollower:
    def __init__(self, route, drivebase, color_sensor, gyro_sensor, ev3):
        self.route = route
        self.drivebase = drivebase
        self.color_sensor = color_sensor
        self.gyro_sensor = gyro_sensor
        self.ev3 = ev3

        self.event_counter = 0
        self.follow_color = [Color.YELLOW, Color.WHITE]
        self.crossing_color = COLOR.BLUE
        self.follow_angle = 0
        self.forward = 100
        self.retry_value = 0

        self.gyro_sensor.reset_angle(0)
        
    def on_line(self):
        print("Vorwärts")
        while True:
            angle = self.gyro_sensor.angle()
            color = self.color_sensor.color()
            print(angle, color)

            if color in self.follow_color:
                self.ev3.screen.load_image(ImageFile.FORWARD)
                self.drivebase.straight(self.forward)
                self.retry_value = 0
            if color == self.crossing_color:
                if self.confirm_color(color):
                    print("Found Crossing")
            else:
                self.ev3.speaker.beep()
                self.correct_direction(angle)
                
    def correct_direction(self, angle):
        """
        Adjusts the direction based on the current angle from the gyro sensor.

        :param angle: Current angle from the gyro sensor in degrees.
        """
        self.ev3.screen.load_image(ImageFile.QUESTION_MARK)
        if angle >= 2:
            self.drivebase.turn(-angle)
        elif angle == 0:
            if self.retry_value < 5:
                self.drivebase.turn(5)
                self.retry_value += 1
            else:
                self.drivebase.turn(10)
        elif angle <= 2:
            self.drivebase.turn(abs(angle))

    def confirm_color(self, color):
        self.drivebase.turn(2)
        self.drivebase.turn(-2)
        if self.color_sensor.color() == color:
            return True
        else:
            return False
    
    def event(self):
        self.event_counter += 1