import tkinter as tk
from resetScreen import resetScreen
from Cycles import Cycles
#import piOut as outputs
import lapOut as outputs

out = outputs.piControl(20, 21)
cycle_data = Cycles()
reset_data = resetScreen(cycle_data)
window = tk.Tk()
window.title("Cycles Home Screen")
window.geometry("400x300")
job = "0"
# This hides the cursor, Comment out when not using the touch screen
# window.config(cursor="none")

# Commands that go with Buttons
def green():
    global job
    if cycle_data.count >= cycle_data.max:
        red()
        return
    out.off()
    out.rightOn()
    window.after(cycle_data.time)
    out.off()
    out.leftOn()
    cycle_data.increment()
    update_count()
    job = window.after(cycle_data.time, green)


def update_count():
    cycle_count_number.config(text=cycle_data.count)

def red():
    global job
    out.off()
    window.after_cancel(job)


def reset_settings():
    global cycle_data
    red()
    reset_data.show(cycle_data)
    cycle_limit_number.config(text=cycle_data.max)
    cycle_count_number.config(text=cycle_data.count)



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
