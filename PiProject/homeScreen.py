import tkinter as tk
from resetScreen import resetScreen
from Cycles import Cycles
import RPi.GPIO as pi

# Setup of the Pi to produce outputs
# Outputs occur on 20 and 21
pi.setwarnings(False)
pi.setmode(pi.BCM)
pi.setup([20,21], pi.OUT)


cycle_data = Cycles()
reset_data = resetScreen(cycle_data)
window = tk.Tk()
window.title("Cycles Home Screen")
window.geometry("400x300")
# This hides the cursor, Comment out when not using the touch screen
# window.config(cursor="none")

# Commands that go with Buttons
def green():
    global job
    pi.output(20, True)
    window.after(cycle_data.time)
    pi.output(20, False)
    pi.output(21, True)
    window.after(cycle_data.time)
    pi.output(21, False)
    cycle_data.increment()
    cycle_count_number.config(text=cycle_data.count)
    job = window.after(0, green)


def red():
    global job
    window.after_cancel(job)


def reset_settings():
    red()
    global cycle_data
    reset_data.show(cycle_data)
    cycle_limit_number.config(text=cycle_data.max)



# Buttons on the Home Screen
start_Button = tk.Button(window, text="START", bg="Green", command=green)
start_Button.grid(row=0, column=0)
start_Button.config(height=5, width=15)

stop_Button = tk.Button(window, text="STOP", bg="Red", command=red)
stop_Button.grid(row=0, column=2)
stop_Button.config(height=5, width=15)

reset_Button = tk.Button(window, text="Cycle Settings", command=reset_settings)
reset_Button.grid(row=3, column=1)

# Text on Home Screen
cycle_count_text = tk.Label(window, text="Current Cycle Count")
cycle_count_text.grid(row=1, column=0)

cycle_count_number = tk.Label(window, text=cycle_data.count)
cycle_count_number.grid(row=1, column=1)

cycle_limit_text = tk.Label(window, text="Cycle Limit")
cycle_limit_text.grid(row=2, column=0)

cycle_limit_number = tk.Label(window, text=cycle_data.max)
cycle_limit_number.grid(row=2, column=1)


window.mainloop()
