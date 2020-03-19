import tkinter as tk
from Cycles import Data

class Other:

    def __init__(self):
        self.data = Data()
        self.window = "0" # Becomes the main window
        self.cycle_thump_label = "0" # Becomes a label
    
    def show(self, data=Data()):
        self.data = data

        # Set up the window
        self.window = tk.Tk()
        self.window.title("Other Settings")

        # Display the current setttings on the left
        self.cycle_thump_label = tk.Label(self.window, text=self.data.mode)
        self.cycle_thump_label.grid(row=0, column=0)

        # Toggle buttons to the right of the Labels
        cycle_thump_button = tk.Button(self.window, text="Cycle/Thump Toggle", command=self.__toggle_thump_cycle)
        cycle_thump_button.grid(row=0, column=1)

        self.window.mainloop()
    
    def __toggle_thump_cycle(self):
        if self.data.mode == "Thump":
            self.data.mode = "Cycle"
        elif self.data.mode == "Cycle":
            self.data.mode = "Thump"
        self.cycle_thump_label.config(text=self.data.mode)
