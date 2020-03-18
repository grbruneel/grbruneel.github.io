import tkinter as tk
import platform
if platform.system() == "Darwin" or platform.system() == "Windows":
    import lapOut as outputs
else:
    import piOut as outputs

class SettingLoad:

    def __init__(self):
        self.out = outputs.piControl(20, 21)
        self.right = True
        self.window = "0" #Becomes window object first time show() is done 
        
    def show(self):
        
        # Window
        self.window = tk.Tk()
        self.window.title("Setting the Load")
        self.window.config(bg="Blue")

        # Buttons
        switch_button = tk.Button(self.window, text="Switch Cylider", bg="Green", command=self.__switch)
        switch_button.grid(row=0, column=0, ipadx=10, ipady=10, padx=5, pady=5)

        stop_button = tk.Button(self.window, text="STOP", bg = "red", command=self.__stop)
        stop_button.grid(row=0, column=1, ipadx=10, ipady=10, padx=5, pady=5)

        self.out.rightOn()
        self.window.mainloop()

    def __switch(self):
        self.out.off()
        if self.right:
            self.right = False
            self.out.leftOn()
        else:
            self.right = True
            self.out.rightOn()
    
    def __stop(self):
        self.out.off()
        self.window.destroy()
        self.window.quit()
        