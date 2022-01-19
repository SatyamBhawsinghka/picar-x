import sys
sys.path.append(r'/home/satyam/picar-x/lib')
from picarx_improved import Picarx
import time


class Sensing(Picarx):
    def __init__(self, ref=1000):
        super().__init__()
        self.chn_0 = self.S0
        self.chn_1 = self.S1
        self.chn_2 = self.S2
        self.ref = ref



    def get_data(self):
        return self.get_adc_value()


    def get_line_status(self, fl_list):

        if fl_list[0] > self.ref and fl_list[1] > self.ref and fl_list[2] > self.ref:
            return 'stop'

        elif fl_list[1] <= self.ref:
            return 'forward'

        elif fl_list[0] <= self.ref:
            return 'right'

        elif fl_list[2] <= self.ref:
            return 'left'

if __name__ == "__main__":


    GM = Sensing(950)
    while True:
        print(GM.get_data())
        time.sleep(1)