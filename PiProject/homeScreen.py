import tkinter as tk

window = tk.Tk()
window.title("Cycles Home Screen")
window.geometry("400x300")
# This hides the cursor, Comment out when not using the touch screen
window.config(cursor="none")

# Commands that go with Buttons
def green():
    print("Green")


def red():
    print("Red")


def reset_settings():
    print("reset")


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

cycle_count_number = tk.Label(window, text="NUMBER")
cycle_count_number.grid(row=1, column=1)

cycle_limit_text = tk.Label(window, text="Cycle Limit")
cycle_limit_text.grid(row=2, column=0)

cycle_limit_number = tk.Label(window, text="NUMBER")
cycle_limit_number.grid(row=2, column=1)

#Find me!
window.mainloop()
