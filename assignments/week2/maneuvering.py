import sys
sys.path.append(r'/home/pi/picar-x/lib')
from utils import reset_mcu
reset_mcu()

from picarx import Picarx
import time

def forward_and_backward(px):
	px.forward(30)
	time.sleep(1)
	px.set_dir_servo_angle(10)
	time.sleep(1)
	px.forward(0)
	time.sleep(0.01)
	px.backward(30)
	time.sleep(1)
	px.set_dir_servo_angle(0)
	time.sleep(1)
	px.backward(0)


def parallel_parking_right(px):
	px.set_dir_servo_angle(18)
	time.sleep(0.2)
	px.backward(30)
	time.sleep(0.5)
	px.backward(0)
	px.set_dir_servo_angle(-18)
	time.sleep(0.2)
	px.backward(30)
	time.sleep(0.25)
	px.backward(0)
	px.set_dir_servo_angle(-24)
	time.sleep(0.2)
	px.backward(30)
	time.sleep(0.5)
	px.backward(0)
	px.set_dir_servo_angle(18)
	px.forward(30)
	time.sleep(0.75)
	px.forward(0)
	px.set_dir_servo_angle(0)
	time.sleep(0.2)
	px.forward(30)
	time.sleep(0.25)
	px.forward(0)
	

def parallel_parking_left(px):
	px.set_dir_servo_angle(-18)
	time.sleep(0.1)
	px.backward(30)
	time.sleep(0.5)
	px.backward(0)
	px.set_dir_servo_angle(18)
	time.sleep(0.1)
	px.backward(30)
	time.sleep(0.5)
	px.backward(0)
	px.set_dir_servo_angle(36)
	time.sleep(0.1)
	px.backward(30)
	time.sleep(0.5)
	px.backward(0)
	px.set_dir_servo_angle(-18)
	px.forward(30)
	time.sleep(0.25)
	px.forward(0)
	px.set_dir_servo_angle(0)
	time.sleep(0.1)
	px.forward(30)
	time.sleep(0.25)
	px.forward(0)


def three_point_turning(px):
	px.set_dir_servo_angle(-35)
	time.sleep(0.1)
	px.forward(30)
	time.sleep(0.5)
	px.forward(0)
	px.set_dir_servo_angle(35)
	time.sleep(0.1)
	px.backward(30)
	time.sleep(0.5)
	px.backward(0)
	px.set_dir_servo_angle(-35)
	time.sleep(0.1)
	px.forward(30)
	time.sleep(0.5)
	px.forward(0)
	

if __name__ == "__main__":
	px = Picarx()
	# print("starting first")
	# time.sleep(1)
	# forward_and_backward(px)
	# print("first done")
	time.sleep(3)
	print("starting second")
	time.sleep(1)
	parallel_parking_right(px)
	print("second done")
	# time.sleep(3)
	# print("starting third")
	# time.sleep(1)
	# parallel_parking_left(px)
	# print("third done")
	# time.sleep(3)
	# print("starting fourth")
	# time.sleep(1)
	# three_point_turning(px)
	# print("fourth done")


