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
            out.append(avg[i]/s)
        return out

    # Processing sensor data
    def processing(self):
        direction = None
        degree = None
        data = self.read()
        print(data)
        print(data[0], data[1], data[2])
        print(self.polarity)
        if self.polarity == 0:
            r1 = data[1] / data[0]
            r2 = data[1] / data[2]
            if r1 > self.sensitivity and r2 > self.sensitivity:
                direction = 'center'
                degree = 0
            elif r1 > self.sensitivity > r2:
                direction = 'left'
                degree = r1-r2
            elif r2 > self.sensitivity > r1:
                direction = 'right'
                degree = r2-r1
            else:
                if (data[0] > self.sensitivity * data[1]) and (data[0] > self.sensitivity * data[2]):
                    direction = 'right'
                    degree = 2 * data[0]/(data[1]+data[2])
                if (data[2] > self.sensitivity * data[1]) and (data[2] > self.sensitivity * data[0]):
                    direction = 'left'
                    degree = 2 * data[2]/(data[1]+data[0])
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
                degree = r1-r2
            elif r2 > self.sensitivity > r1:
                direction = 'right'
                degree = r2-r1
            else:
                if data[1] > self.sensitivity * data[0] and data[2] > self.sensitivity * data[0]:
                    direction = 'right'
                    degree = 2 * data[0]/(data[1]+data[2])
                if data[1] > self.sensitivity * data[2] and data[0] > self.sensitivity * data[2]:
                    direction = 'left'
                    degree = 2 * data[2]/(data[1]+data[0])
                else:
                    direction = 'same'
                    degree = 0


        return direction, degree


if __name__ == "__main__":

    sample = Interpretation()
    while True:
        direction, degree = sample.processing()
        print(direction, degree)
        time.sleep(5)

