class Data:

    def __init__(self):
        self.max = 1000000
        self.count = 0
        self.retract_time = 500
        self.extend_time = 500
        self.mode = "Thump"
        self.runtime = "Continuous"
        self.stagger_on = 45
        self.stagger_off = 15

    def increment(self):
        self.count = self.count + 1

    