class Data:

    def __init__(self):
        self.max = 1000000
        self.count = 0
        self.retract_time = 500
        self.extend_time = 400
        self.mode = "Thump"

    def increment(self):
        self.count = self.count + 1

    