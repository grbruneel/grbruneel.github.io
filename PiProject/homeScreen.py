import tkinter as tk
from resetScreen import resetScreen
from Cycles import Cycles
#import piOut as outputs
import lapOut as outputs
from timeScreen import timeSet

out = outputs.piControl(20, 21)
cycle_data = Cycles()
reset_data = resetScreen(cycle_data)
time_data = timeSet(cycle_data)
window = tk.Tk()
window.title("Cycles Home Screen")
window.geometry("400x300")
job = "0"
is_fullscreen = True
# This hides the cursor, Comment out when not using the touch screen
# window.config(cursor="none")

# Commands that go with Buttons
def start():
    global job
    if cycle_data.count >= cycle_data.max:
        stop()
        return
    out.off()
    out.rightOn()
    window.after(cycle_data.extend_time)
    out.off()
    out.leftOn()
    cycle_data.increment()
    update_count()
    job = window.after(cycle_data.retract_time, start)


def update_count():
    cycle_count_number.config(text=cycle_data.count)

def stop():
    global job
    out.off()
    window.after_cancel(job)


def reset_settings():
    global cycle_data
    stop()
    reset_data.show(cycle_data)
    cycle_limit_number.config(text=cycle_data.max)
    cycle_count_number.config(text=cycle_data.count)

def time_action():
    global cycle_data
    stop()
    time_data.show()
    # Not currently shown on main Screen

def close_fullscreen(Event):
    global is_fullscreen
    is_fullscreen = False
    window.attributes("-fullscreen", is_fullscreen)

def toggle_fullscreen(Event):
    global is_fullscreen
    if is_fullscreen:
        is_fullscreen = False
    else:
        is_fullscreen = True
    window.attributes("-fullscreen", is_fullscreen)

fontsize = 20
# Buttons on the Home Screen
start_Button = tk.Button(window, text="START", bg="Green", command=start, font=(None, fontsize))
start_Button.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
start_Button.config(height=12, width=36)

stop_Button = tk.Button(window, text="STOP", bg="Red", command=stop, font=(None, fontsize))
stop_Button.grid(row=0, column=2, padx=10, pady=10, columnspan=2)
stop_Button.config(height=12, width=36)

reset_Button = tk.Button(window, text="Cycle Settings", command=reset_settings, font=(None, fontsize))
reset_Button.grid(row=3, column=1, columnspan=2, ipadx=10, ipady=5)

time_Button = tk.Button(window, text="Time Settings", command=time_action, font=(None, fontsize))
time_Button.grid(row=4, column=1, columnspan=2, ipadx=10, ipady=5)

# Text on Home Screen
cycle_count_text = tk.Label(window, text="Current Cycle Count", font=(None, fontsize))
cycle_count_text.grid(row=1, column=0)

cycle_count_number = tk.Label(window, text=cycle_data.count, font=(None, fontsize))
cycle_count_number.grid(row=1, column=1)

cycle_limit_text = tk.Label(window, text="Cycle Limit", font=(None, fontsize))
cycle_limit_text.grid(row=2, column=0)

cycle_limit_number = tk.Label(window, text=cycle_data.max, font=(None, fontsize))
cycle_limit_number.grid(row=2, column=1)

# Full Screen
window.bind("<Escape>", close_fullscreen)
window.bind("<F11>", toggle_fullscreen)
window.attributes("-fullscreen", is_fullscreen)

window.mainloop()
