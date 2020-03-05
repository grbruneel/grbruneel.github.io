import tkinter as tk
from Cycles import Cycles

window = tk.Tk()
window.title("Reset Cycle Count")
number_entry = "0"
cycle_data = Cycles()

number_display = tk.Label(window, fg="red", text=number_entry)
number_display.grid(row=0, column=0, columnspan=3)

keys = [
    ['1', '2', '3'],    
    ['4', '5', '6'],    
    ['7', '8', '9'],    
    ['DEL', '0', '   '],    
]

# Commands
def number(x):
    global number_display
    global number_entry

    if x == "DEL":
        if number_entry == "0":
            number_entry = "0"
        elif number_entry == number_entry[0]:
            number_entry = "0"
        else:
            number_entry = number_entry[:-1]
    
    elif x == " ":
        number_display = number_display

    else: # Number Entry
        if number_entry == "0":
            number_entry = x
        else:
            number_entry = number_entry + x
    number_display.config(text=number_entry)
    
def limit():
    global number_entry
    if number_entry.isdigit():
        cycle_data.max = int(number_entry)
    cycle_limit_number.config(text=cycle_data.max)

# Make set of 12 buttons to act as number pad

for x in range(0, 4):
    for y in range(0,3):
        button = tk.Button(window, text=keys[x][y],  command=lambda num=keys[x][y] : number(num))
        button.grid(row = x + 1, column = y, ipadx=15, ipady=15)
        if keys[x][y] == "DEL":
            button.grid(ipadx=8)

# Labels that display current Cycle Values
cycle_limit_text = tk.Label(window, text="Cycle Limit")
cycle_limit_text.grid(row=1, column=3)

cycle_limit_number = tk.Label(window, text=cycle_data.max)
cycle_limit_number.grid(row=2, column=3)

cycle_count_text = tk.Label(window, text="Cycle Count")
cycle_count_text.grid(row=1, column=4)

cycle_count_number = tk.Label(window, text=cycle_data.count)
cycle_count_number.grid(row=2, column=4)

# Buttons to reset the Cycle Count and Cycle Limit
reset_limit = tk.Button(window, text="Reset Limit", command=limit)
reset_limit.grid(row=3, column=3)



window.mainloop()
