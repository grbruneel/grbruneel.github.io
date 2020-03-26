class Data:

    def __init__(self):
        try:
            file = open("settings.txt", "r")
        except:
            file = open("defaultsettings.txt", "r")
        lines = file.readlines()
        self.max = int(lines[0])
        self.count = int(lines[1])
        self.retract_time = int(lines[2])
        self.extend_time = int(lines[3])
        self.mode = lines[4][:-1]
        self.runtime = lines[5][:-1]
        self.stagger_on = int(lines[6])
        self.stagger_off = int(lines[7])

    def increment(self):
        self.count = self.count + 1

    def save(self):
        file = open("settings.txt", "w")
        file.write(str(self.max) + "\n")
        file.write(str(self.count) + "\n")
        file.write(str(self.retract_time) + "\n")
        file.write(str(self.extend_time) + "\n")
        file.write(self.mode + "\n")
        file.write(self.runtime + "\n")
        file.write(str(self.stagger_on) + "\n")
        file.write(str(self.stagger_off) + "\n")
        file.close()

    def revert_default(self):
        file = open("defaultsettings.txt", "r")
        lines = file.readlines()
        self.max = int(lines[0])
        self.count = int(lines[1])
        self.retract_time = int(lines[2])
        self.extend_time = int(lines[3])
        self.mode = lines[4][:-1]
        self.runtime = lines[5][:-1]
        self.stagger_on = int(lines[6])
        self.stagger_off = int(lines[7])
