from Bus import Bus
import sys
sys.path.append(r'/home/satyam/picar-x/assignments/week3')
from lane_grayscale import Sensing, Interpretation, Controller
import time
import concurrent.futures
import atexit

def producer(delay, sensor_bus, sensor):
    while True:
        data = sensor.read()
        print("Sensor data", data)
        sensor_bus.write(data)
        time.sleep(delay)


def consumer_producer(delay, sensor_bus, processor_bus, processor):
    while True:
        data = sensor_bus.read()
        print("Sensor bus data", data)
        data = processor.processing(data)
        print("Processor data", data)
        processor_bus.write(data)
        time.sleep(delay)

def consumer(delay, processor_bus, controller):
    while True:
        data = processor_bus.read()
        print("Processor bus data", data)
        controller.control(data)
        time.sleep(delay)

if __name__ == "__main__":
    sensor = Sensing()
    processor = Interpretation()
    controller = Controller()
    sensor_bus = Bus([0, 0, 0])
    processor_bus = Bus([0])

    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            sense = executor.submit(producer, 0.2, sensor_bus, sensor)
            process = executor.submit(consumer_producer, 0.2, sensor_bus, processor_bus, processor)
            control = executor.submit(consumer, 0.2, processor_bus, controller)
        print(sense.result())
        print(process.result())
        print(control.result())
        # time.sleep(0.01)
    finally:
        atexit.register(controller.stop)






