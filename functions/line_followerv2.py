from pybricks.parameters import Color
from pybricks.media.ev3dev import ImageFile, Image
from time import sleep

class LineFollower:
    def __init__(self, route, drivebase, color_sensor, gyro_sensor, ev3):
        self.route = route
        self.drivebase = drivebase
        self.color_sensor = color_sensor
        self.gyro_sensor = gyro_sensor
        self.ev3 = ev3

        self.route = route
        self.follow_colors = [Color.WHITE, Color.YELLOW]
        self.turn_right_color = Color.GREEN
        self.turn_left_color = Color.RED
        self.crossing_color = Color.BLUE

        self.forward = 100
        self.crossing_forward = 50
        self.follow_angle = 0
        self.retry_value = 0
        self.retry_turn = 15
        self.event_counter = 0

        self.gyro_sensor.reset_angle(0)
        
    def on_line(self):
        print("Forward")
        while True:
            angle = self.gyro_sensor.angle()
            color = self.color_sensor.color()
            print(angle, color)

            if color in self.follow_colors:
                self.ev3.screen.load_image(ImageFile.FORWARD)
                self.drivebase.straight(self.forward)
                self.retry_value = 0
            if color == self.crossing_color:
                if self.confirm_color(color):
                    self.crossing()
            else:
                # self.ev3.speaker.beep()
                self.correct_direction(angle)
                
    def correct_direction(self, angle):
        self.ev3.screen.load_image(ImageFile.QUESTION_MARK)
        if angle >= 2:
            self.drivebase.turn(-angle)
        elif angle == 0:
            print("Angle is 0 retry:", self.retry_value)
            if self.retry_value < 2:
                self.drivebase.turn(-10)
                self.retry_value += 1
            elif self.retry_value < 4:
                self.drivebase.turn(-15)
                self.retry_value += 1
            else:
                self.retry_turn += 5
                self.drivebase.turn(-self.retry_turn)
        elif angle <= 2:
            self.drivebase.turn(abs(angle))

    def confirm_color(self, color):
        self.drivebase.turn(3)
        self.drivebase.turn(-3)
        print("Confirming color")
        if self.color_sensor.color() == color:
            print("Confirmed")
            return True
        else:
            print("Not confirmed")
            return False
    
    def event(self):
        self.event_counter += 1
        turn_crossing = self.route[0]
        turn_direction = self.route[1]
        if self.event_counter == turn_crossing:
            self.drivebase.straight(self.crossing_forward)
            if turn_direction == "right":
                turn = 90
                self.follow_colors.append(self.turn_right_color)
                self.follow_colors.remove(self.turn_left_color)
            elif turn_direction == "left":
                turn = -90
                self.follow_colors.append(self.turn_left_color)
                self.follow_colors.remove(self.turn_right_color)
            self.drivebase.turn(turn)
            # make sure the robot is facing the right direction
            self.drivebase.turn(abs(self.gyro_sensor.angle() - turn))
            self.gyro_sensor.reset_angle(0)

    def crossing(self):
        while self.color_sensor.color() == self.crossing_color:
            self.drivebase.straight(10)
            print("Searching stop")
        if self.color_sensor.color() in self.follow_colors:
            self.drivebase.stop()
            print("Crossing")
            self.event()