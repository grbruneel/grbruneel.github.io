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
