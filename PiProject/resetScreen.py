import tkinter as tk

window = tk.Tk()
window.title("Reset Cycle Count")

# Make set of 12 buttons to act as number pad

keys = [
    ['1', '2', '3'],    
    ['4', '5', '6'],    
    ['7', '8', '9'],    
    ['DEL', '9', 'SET'],    
]

entry_box = tk.Entry(window)
entry_box.grid(row=0, column=0, columnspan=3)

for x in range(0, 4):
    for y in range(0,3):
        button = tk.Button(window, text=keys[x][y])
        button.grid()


window.mainloop()
