# Data class is where all the settings are stored. 
# Increment increases the count of cycles by one.
# Save writes a settings.txt file with all the current values
# Revert_default changes all the settings in the class back to a default state

class Data:

    def __init__(self):
        try:
            file = open("settings.txt", "r")
        except:
            self.revert_default()
            self.save()
            file = open("settings.txt", "r")
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
        self.max = 1000000
        self.count = 0
        self.retract_time = 500
        self.extend_time = 500
        self.mode = "Thump"
        self.runtime = "Continuous"
        self.stagger_on = 900000
        self.stagger_off = 2700000
