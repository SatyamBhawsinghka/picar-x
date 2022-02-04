import sys
import atexit
sys.path.append(r'/home/satyam/picar-x/lib')
from picarx_improved import Picarx
import time
import numpy


class SensingU(Picarx):
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


class InterpretationU(object):
    def __init__(self, stopping_range=10):
        # Range in cm at which the car needs to be stopped
        self.stopping_range = stopping_range

    # Processing sensor data
    def processing(self, distance):
        if distance < 0:
            return 1
        elif distance > self.stopping_range:
            return 1
        else:
            return 0


class ControllerU(Picarx):
    def __init__(self):
        super().__init__()

    def control(self, go):
        if go == 1:
            self.forward(50)
            time.sleep(0.05)

        else:
            self.stop()
            time.sleep(0.05)




if __name__ == "__main__":
    time.sleep(3)
    sensor = SensingU()
    processor = InterpretationU() #Interpretation(range)
    controller = ControllerU()

    try:
        while True:
            distance = sensor.read()
            print(distance)
            go = processor.processing(distance)
            print(type(go), go)
            controller.control(go)

    except:
        print("Error in execution")
        atexit.register(controller.stop)

    finally:
        atexit.register(controller.stop)