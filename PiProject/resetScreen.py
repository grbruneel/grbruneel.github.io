import tkinter as tk

window = tk.Tk()
window.title("Reset Cycle Count")
number_entry = "0"

# Commands
def number(x):
    global number_entry

    if x == "DEL":
        if number_entry == "0":
            number_entry = "0"
        elif number_entry == number_entry[0]:
            number_entry = "0"
        else:
            number_entry = number_entry[:-1]
    
    elif x == "SET":
        print(number_entry)
        number_entry = "0"

    else: # Number Entry
        if number_entry == "0":
            number_entry = x
        else:
            number_entry = number_entry + x
    number_display.config(text=number_entry)
    

# Make set of 12 buttons to act as number pad
keys = [
    ['1', '2', '3'],    
    ['4', '5', '6'],    
    ['7', '8', '9'],    
    ['DEL', '0', 'SET'],    
]

number_display = tk.Label(window, fg="red", text=number_entry)
number_display.grid(row=0, column=0, columnspan=3)

for x in range(0, 4):
    for y in range(0,3):
        button = tk.Button(window, text=keys[x][y],  command=lambda num=keys[x][y] : number(num))
        button.grid(row = x + 1, column = y, ipadx=15, ipady=15)




window.mainloop()
