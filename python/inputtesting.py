import RPi.GPIO as pins

pins.setwarnings(False)
pins.setmode(pins.BCM)
pins.setup(20, pins.OUT)
pins.setup(6, pins.IN)

while True:
    if pins.input(6) == 1:
        pins.output(20, False)
    else:
        pins.output(20, True)

