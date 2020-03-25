from RPi import GPIO as pi


class piControl:

    def __init__(self, x, y, xi, yi):
        self.right = x
        self.left = y
        self.righti = xi
        self.lefti = yi

        # Setup of the Pi to produce outputs
        pi.setwarnings(False)
        pi.setmode(pi.BCM)
        pi.setup([self.left, self.right], pi.OUT)
        pi.setup([self.lefti, self.righti], pi.IN)

    def leftOn(self):
        pi.output(self.left, True)

    def rightOn(self):
        pi.output(self.right, True)

    def off(self):
        pi.output([self.right, self.left], False)
        
    def leftIn(self):
        return (pi.input(self.lefti) == 1)
    
    def rightIn(self):
        return (pi.input(self.righti) == 1)

