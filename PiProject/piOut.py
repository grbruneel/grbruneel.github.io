from RPi import GPIO as pi


class piControl:

    def __init__(self, x, y):
        self.right = x
        self.left = y

        # Setup of the Pi to produce outputs
        pi.setwarnings(False)
        pi.setmode(pi.BCM)
        pi.setup([self.left, self.right], pi.OUT)
        pi.setup([23, 24], pi.IN)

    def leftOn(self):
        pi.output(self.left, True)

    def rightOn(self):
        pi.output(self.right, True)

    def off(self):
        pi.output([self.right, self.left], False)
        
    def leftIn(self):
        return pi.input(5)
    
    def rightIn(self):
        return pi.input(6)

