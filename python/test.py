import guizero as gui
import RPi.GPIO as pin
import time
import Count


pin.setwarnings(False)
pin.setmode(pin.BCM)
pin.setup(18, pin.OUT)
total = Count.Count()

def light():
    pin.output(18, True)
    time.sleep(0.5)
    pin.output(18, False)


def push():
   light()
   total.increase()
   replace = total.count
   if replace % 2 == 1:
       number.text_color = "Red"
   else:
      number.text_color = "Black"
   number.value = replace

        
def stop():
    pin.output(18, False)

app = gui.App(title = "Hi")
button = gui.PushButton(app, text = "Start", command = push)
stopb = gui.PushButton(app, text = "STOP", command = stop)
button.bg = "green"
number = gui.Text(app, text = total.count)
stopb.when_clicked = stop



