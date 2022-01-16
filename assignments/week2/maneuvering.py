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
	time.sleep(0.75)
	px.backward(0)
	px.set_dir_servo_angle(-18)
	time.sleep(0.2)
	px.backward(30)
	time.sleep(0.5)
	px.backward(0)
	px.set_dir_servo_angle(-24)
	time.sleep(0.2)
	px.backward(30)
	time.sleep(0.5)
	px.backward(0)
	px.set_dir_servo_angle(9)
	px.forward(30)
	time.sleep(0.5)
	px.forward(0)
	px.set_dir_servo_angle(-24)
	time.sleep(0.2)
	px.forward(30)
	time.sleep(0.5)
	px.forward(0)
	px.set_dir_servo_angle(0)
	time.sleep(0.2)
	px.forward(10)
	time.sleep(0.25)
	px.forward(0)

	

def parallel_parking_left(px):
	px.set_dir_servo_angle(-18)
	time.sleep(0.2)
	px.backward(30)
	time.sleep(0.75)
	px.backward(0)
	px.set_dir_servo_angle(18)
	time.sleep(0.2)
	px.backward(30)
	time.sleep(0.5)
	px.backward(0)
	px.set_dir_servo_angle(24)
	time.sleep(0.2)
	px.backward(30)
	time.sleep(0.5)
	px.backward(0)
	px.set_dir_servo_angle(-9)
	px.forward(30)
	time.sleep(0.5)
	px.forward(0)
	px.set_dir_servo_angle(24)
	time.sleep(0.2)
	px.forward(30)
	time.sleep(0.5)
	px.forward(0)
	px.set_dir_servo_angle(0)
	time.sleep(0.2)
	px.forward(10)
	time.sleep(0.25)
	px.forward(0)

def three_point_turning(px):
	px.set_dir_servo_angle(-35)
	time.sleep(0.1)
	px.forward(30)
	time.sleep(0.75)
	px.forward(0)
	px.set_dir_servo_angle(35)
	time.sleep(0.1)
	px.backward(30)
	time.sleep(0.5)
	px.backward(0)
	px.set_dir_servo_angle(-35)
	time.sleep(0.1)
	px.forward(30)
	time.sleep(0.80)
	px.set_dir_servo_angle(0)
	time.sleep(0.1)
	px.forward(30)
	time.sleep(0.25)
	px.forward(0)


	

if __name__ == "__main__":
	px = Picarx()
	print("Enter 1 for Parallel Parking Right")
	print("Enter 2 for Parallel Parking Left")
	print("Enter 3 for Three Point Turning")
	print("Enter 4 for Forward and Backward")
	print("Enter 0 to exit")
	x = input()
	print(x)
	while(x != '0'):

		px.set_dir_servo_angle(0)
		if x=='1':
			parallel_parking_right(px)
		elif x=='2':
			parallel_parking_left(px)
		elif x=='3':
			three_point_turning(px)
		elif x=='4':
			forward_and_backward(px)
		else:
			print("Enter valid selection")
		print("Enter 1 for Parallel Parking Right")
		print("Enter 2 for Parallel Parking Left")
		print("Enter 3 for Three Point Turning")
		print("Enter 4 for Forward and Backward")
		print("Enter 0 to exit")
		x = input()
		print(x)
		time.sleep(2)

















