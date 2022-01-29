class Bus(object):
    def __init__(self):
        self.message = None

    def write(self, data):
        self.message = data

    def read(self):
        return self.message
