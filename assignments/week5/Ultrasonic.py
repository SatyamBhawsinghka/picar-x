import sys
import atexit
sys.path.append(r'/home/satyam/picar-x/lib')
from picarx_improved import Picarx
import time
import numpy


class Sensing(Picarx):
    def __init__(self):
        super().__init__()

    def get_data(self):
        return self.Get_distance()

    # Returns mean over 5 data values
    def read(self):
        values = []
        for i in range(5):
            values.append(self.get_data())
        avg = numpy.mean(values, axis=0)
        return avg


class Interpretation(object):
    def __init__(self, stopping_range=1):
        # Range in cm at which the car needs to be stopped
        self.stopping_range = stopping_range

    # Processing sensor data
    def processing(self, distance):
        if distance < self.stopping_range:
            return 1
        else:
            return 0


class Controller(Picarx):
    def __init__(self):
        super().__init__()

    def control(self, go):
        if go:
            self.forward(30)

        else:
            # self.stop()
            pass



if __name__ == "__main__":
    time.sleep(3)
    sensor = Sensing()
    processor = Interpretation() #Interpretation(range)
    controller = Controller()

    try:
        while True:
            distance = sensor.read()
            print("processed", distance)
            # controller.control(processor.processing(distance))
            time.sleep(0.05)
    except:
        print("Error in execution")
        atexit.register(controller.stop)

    finally:
        atexit.register(controller.stop)