import tkinter as tk
from Cycles import Cycles

class resetScreen:

    def __init__(self, cycle=Cycles()):
        self.cycle_data = cycle
        self.number_entry = "0"
        self.number_display = 0

    def show(self, cycle):
        self.cycle_data = cycle
        window = tk.Tk()
        window.title("Reset Cycle Count")
        self.number_display = tk.Label(window, fg="red", text=self.number_entry)
        self.number_display.grid(row=0, column=0, columnspan=3)


#number_entry = "0"
#cycle_data = Cycles()



        keys = [
            ['1', '2', '3'],    
            ['4', '5', '6'],    
            ['7', '8', '9'],    
           ['DEL', '0', '   '],    
        ]

# Commands
        def number(x):
            if x == "DEL":
                if self.number_entry == "0":
                    self.number_entry = "0"
                elif self.number_entry == self.number_entry[0]:
                    self.number_entry = "0"
                else:
                    self.number_entry = self.number_entry[:-1]
    
            elif x == " ":
               self.number_display = "0"

            else: # Number Entry
                   if self.number_entry == "0":
                        self.number_entry = x
                   else:
                        self.number_entry = self.number_entry + x
            self.number_display.config(text=self.number_entry)
    
        def limit():
            if self.number_entry.isdigit():
                self.cycle_data.max = int(self.number_entry)
            cycle_limit_number.config(text=self.cycle_data.max)

        def done_action():
            window.destroy()
            window.quit()

        def count_to_zero():
            self.cycle_data.count = 0
            cycle_count_number.config(text=self.cycle_data.count)
        

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

        cycle_limit_number = tk.Label(window, text=self.cycle_data.max)
        cycle_limit_number.grid(row=2, column=3)

        cycle_count_text = tk.Label(window, text="Cycle Count")
        cycle_count_text.grid(row=1, column=4)

        cycle_count_number = tk.Label(window, text=self.cycle_data.count)
        cycle_count_number.grid(row=2, column=4)

# Buttons to reset the Cycle Count and Cycle Limit
        reset_limit = tk.Button(window, text="Reset Limit", command=limit)
        reset_limit.grid(row=3, column=3)

        done_button = tk.Button(window, text="Done", command=done_action)
        done_button.grid(row=0, column=3, columnspan=2)

        reset_count = tk.Button(window, text="Set Count 0", command=count_to_zero)
        reset_count.grid(row=3, column=4)

        window.mainloop()
