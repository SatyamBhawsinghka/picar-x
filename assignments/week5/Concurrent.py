import sys
sys.path.append(r'/home/satyam/picar-x/assignments/week3')
from lane_grayscale import Sensing, Interpretation, Controller
sys.path.append(r'/home/satyam/picar-x/lib')
import rossros as ros
sys.path.append(r'/home/satyam/picar-x/assignments/week5')
from Ultrasonic import SensingU, InterpretationU, ControllerU

if __name__ == "__main__":
    # Creating objects of Sensor, Interpretation and Controller classes of grayscale and ultrasonic
    ultra_sensor = SensingU()
    ultra_processor = InterpretationU()
    ultra_controller = ControllerU()
    gray_sensor = Sensing()
    gray_processor = Interpretation()
    gray_controller = Controller()
    # Creating sensor and processor buses
    gray_sensor_bus = ros.Bus(initial_message=[1, 1, 1], name="Grayscale sensor")
    gray_processor_bus = ros.Bus(initial_message=0, name="Grayscale processor")
    ultra_sensor_bus = ros.Bus(initial_message=-1, name="Ultrasonic sensor")
    ultra_processor_bus = ros.Bus(initial_message=1, name="Ultrasonic processor")
    #Creating termination bus
    term_bus = ros.Bus(name="Termination")
    #Creating objects of producer, consumer-producer and consumer classes
    ultra_p = ros.Producer(ultra_sensor.read(), ultra_sensor_bus, 0.05, term_bus, "Ultrasonic producer")
    gray_p = ros.Producer(gray_sensor.read(), gray_sensor_bus, 0.05, term_bus, "Grayscale producer")
    ultra_cp = ros.ConsumerProducer(ultra_processor.processing(), ultra_sensor_bus, ultra_processor_bus, 0.05, term_bus,
                                "Ultrasonic Consumer Producer")
    gray_cp = ros.ConsumerProducer(gray_processor.processing(), gray_sensor_bus, gray_processor_bus, 0.05, term_bus,
                                "Grayscale Consumer Producer")
    ultra_c = ros.Consumer(ultra_controller.control(), ultra_processor_bus, 0.05, term_bus, "Ultrasonic Consumer")
    gray_c = ros.Consumer(gray_controller.control(), gray_processor_bus, 0.05, term_bus, "Grayscale Consumer")
    #Creating object of Timer class
    timer = ros.Timer(term_bus, 5, 0.05, term_bus, "Timer")

    try:
        ros.runConcurrently([ultra_p, gray_p, ultra_cp, gray_cp, ultra_c, gray_c, timer.timer()])
    except:
        print("error in execution")



