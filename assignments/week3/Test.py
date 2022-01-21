import sys

sys.path.append(r'/home/satyam/picar-x/lib')
from picarx_improved import Picarx
import time
import numpy


class Sensing(Picarx):
    def __init__(self):
        super().__init__()

    def get_data(self):
        return self.get_adc_value()


class Interpretation(Sensing):
    def __init__(self, sensitivity=1.5, polarity=0):
        super().__init__()
        self.sensitivity = sensitivity
        # Dark surface has lower readings and light surface has higher readings
        # Sensitivity is the ratio of sensor value returned for light to dark readings
        self.polarity = polarity
        # Polarity of 0 means the line to be followed is light and has higher sensor readings
        # Polarity of 1 means the line to be followed is dark and has lower sensor readings

    # Returns normalized mean over 5 data values
    def read(self):
        values = []
        out = []
        for i in range(5):
            values.append(self.get_data())
        avg = numpy.mean(values, axis=0)
        s = numpy.sum(avg)
        for i in range(3):
            out.append(avg[i] / s)
        return out

    # Processing sensor data
    def processing(self):
        direction = None
        degree = None
        data = self.read()

        if self.polarity == 0:
            r1 = data[1] / data[0]
            r2 = data[1] / data[2]
            if r1 > self.sensitivity and r2 > self.sensitivity:
                direction = 'center'
                degree = 0
            elif r1 > self.sensitivity > r2:
                direction = 'left'
                degree = r1 - r2
            elif r2 > self.sensitivity > r1:
                direction = 'right'
                degree = r2 - r1
            elif (data[0] > self.sensitivity * data[1]) and (data[0] > self.sensitivity * data[2]):
                direction = 'right'
                degree = 2 * data[0] / (data[1] + data[2])
            elif (data[2] > self.sensitivity * data[1]) and (data[2] > self.sensitivity * data[0]):
                direction = 'left'
                degree = 2 * data[2] / (data[1] + data[0])
            else:
                direction = 'same'
                degree = 0

        if self.polarity == 1:
            r1 = data[0] / data[1]
            r2 = data[2] / data[1]
            if r1 > self.sensitivity and r2 > self.sensitivity:
                direction = 'center'
                degree = 0
            elif r1 > self.sensitivity > r2:
                direction = 'left'
                degree = r1 - r2
            elif r2 > self.sensitivity > r1:
                direction = 'right'
                degree = r2 - r1
            else:
                if data[1] > self.sensitivity * data[0] and data[2] > self.sensitivity * data[0]:
                    direction = 'right'
                    degree = 2 * data[0] / (data[1] + data[2])
                if data[1] > self.sensitivity * data[2] and data[0] > self.sensitivity * data[2]:
                    direction = 'left'
                    degree = 2 * data[2] / (data[1] + data[0])
                else:
                    direction = 'same'
                    degree = 0

        return direction, degree


class Controller(Interpretation):
    def __init__(self, scaling_factor=5):
        super().__init__()
        self.scaling_factor = scaling_factor

    def control(self):
        direction, degree = self.processing()
        turn = int(self.scaling_factor * degree)

        if direction == 'right':
            turn = -1 * turn

        if direction == 'same':
            self.stop()
            self.set_dir_servo_angle(0)
            time.sleep(0.01)
            return 100
        else:
            self.set_dir_servo_angle(turn)
            time.sleep(0.01)
            return turn






if __name__ == "__main__":

    car = Controller()
    angle = car.control(10)
    while angle != 100:
        angle = car.control(10)
        car.forward(20)
        time.sleep(0.1)
