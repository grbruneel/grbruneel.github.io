import tkinter as tk
import RPi.GPIO as pin
import time
import Count


pin.setwarnings(False)
pin.setmode(pin.BCM)
pin.setup(18, pin.OUT)
total = Count.Count()
num = 10

def lighton():
    pin.output(18, True)

def lightoff():
    pin.output(18, False)

def push():
    global job
    total.increase()
    lighton()   
    replace = total.count
    number.config(text=replace)
    window.after(500)
    lightoff()
    if replace == num:
        stopb()
        return
    job = window.after(500, push)

def stopb():
    global job
    window.after_cancel(job)

def endscreen(event=None):
    window.attributes("-fullscreen", False)
    
window = tk.Tk()
window.title("Continue")
window.geometry("350x300")
number = tk.Label(window, text = total.count)
number.grid(column = 1, row = 0)
start = tk.Button(window, text = "START", bg="Green", command = push)
start.grid(column = 0, row = 0)
stop = tk.Button(window, text = "STOP", bg="Red", command = stopb)
stop.grid(column=0, row=1)
cyclesStop = tk.Label(window, text = num)
cyclesStop.grid(column=1, row=1)
window.bind("<Escape>", endscreen)
window.attributes("-fullscreen", True)


window.mainloop()
