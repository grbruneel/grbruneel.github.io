# This is how the program recieves inputs and prints outputs when not on the Raspberry Pi

class piControl:

    def __init__(self, x, y, xi, yi):
        self.x = x
        self.y = y
        self.xi = xi
        self.yi = yi

    def rightOn(self):
        print(self.x)
    
    def leftOn(self):
        print(self.y)
    
    def off(self):
        print("OFF")

    def leftIn(self):
        return bool(input("left True or False: "))
    
    def rightIn(self):
        return bool(input("Right True or False: "))

