# In dieser Datei wird die Voraussetzung für
# ein gradliniges Fahren generell umgesetzt

# Importieren der wichtigsten Bibliotheken
from pybricks.parameters import Color
from pybricks.media.ev3dev import ImageFile, Image


class GyroNavigation:
    def __init__(self, route, drivebase, color_sensor, gyro_sensor, ev3):
        self.route = route
        self.drivebase = drivebase
        self.color_sensor = color_sensor
        self.gyro_sensor = gyro_sensor
        self.ev3 = ev3

        self.event_counter = 0 # Bitte die Aufgabe dieses Zählers benennen
        self.event_color = Color.YELLOW # Farbe des Kreppbandes
        self.follow_angle = 0
        self.forward = 100
        
        # Um den Gyrosensor korrekt zu nutzen muss er zu Beginn auf
        # den Wert 0 gesetzt werden
        
        self.gyro_sensor.reset_angle(0)
        
    def on_line(self):
        print("Vorwärts")
        while True:
            angle = self.gyro_sensor.angle()
            print('Winkel: ', angle, ' °')
            if angle == self.follow_angle:
                # Vorwärtspfeil wird angezeigt, wenn alles in Ordnung ist
                # Nach Programm muss dieser Winkel 0 Grad sein
                self.ev3.screen.load_image(ImageFile.FORWARD)
                self.drivebase.straight(self.forward)
            else:
                # Ansonsten wird ein kurzer Signalton wiedergegeben,
                # der anzeigt, dass vom Weg abgekommen wurde
                self.ev3.speaker.beep()
                self.correct_direction(angle)
            
            if self.event_color == self.color_sensor.color():
                self.event()
                #break
    
    # Die folgende Funktion korrigiert die Fahrt aufgrund einer Winkelabweichung
    
    def correct_direction(self, angle):
        
        # Korrigiert die Richtung basierend auf dem aktuellen Winkel, den der Gyrosensor angiebt
        # :param angle: Aktueller Winkel des Gyrosensors in Grad
        
        self.ev3.screen.load_image(ImageFile.QUESTION_MARK)
        self.drivebase.turn(-angle)

# Der Ereignis-Zähler 
    def event(self):
        self.event_counter += 1
        
        
        