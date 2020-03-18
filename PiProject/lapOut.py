class piControl:

    def __init__(self, x, y):
        self.x = x
        self.y = y

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

