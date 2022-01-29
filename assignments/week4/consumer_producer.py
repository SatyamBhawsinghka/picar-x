from Bus import Bus
import sys
sys.path.append(r'/home/satyam/picar-x/assignments/week3')
from lane_grayscale import Sensing, Interpretation, Controller
import time
import concurrent.futures
import atexit

def producer(delay, sensor_bus, sensor):
    while True:
        sensor_bus.write(sensor.read())
        time.sleep(delay)


def consumer_producer(delay, sensor_bus, processor_bus, processor):
    while True:
        processor_bus.write(processor.processing(sensor_bus.read()))
        time.sleep(delay)

def consumer(delay, processor_bus, controller):
    while True:
        controller.control(processor_bus.read())
        time.sleep(delay)

if __name__ == "__main__":
    sensor = Sensing()
    processor = Interpretation()
    controller = Controller()
    sensor_bus = Bus()
    processor_bus = Bus()

    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            sense = executor.submit(producer, 0.05, sensor_bus, sensor)
            process = executor.submit(consumer_producer, 0.05, sensor_bus, processor_bus, processor)
            control = executor.submit(consumer, 0.05, processor_bus, controller)
        print(sense.result())
        print(process.result())
        print(control.result())
        # time.sleep(0.01)
    finally:
        atexit.register(controller.stop)






