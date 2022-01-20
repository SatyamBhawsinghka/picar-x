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
        data = self.read()
        r1 = data[1]/data[0]
        r2 = data[1]/data[2]

        # if self.polarity == 0:
        #     if
















if __name__ == "__main__":

    sample = Interpretation()
    out = sample.read()

