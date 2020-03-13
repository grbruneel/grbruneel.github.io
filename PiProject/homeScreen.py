# Outputs are on pin 20 and 21
# Inputs are on pins 5 and 6
import tkinter as tk
from resetScreen import resetScreen
from Cycles import Cycles
from timeScreen import timeSet
import platform
if platform.system() == "Darwin":
    import lapOut as outputs
else:
    import piOut as outputs
import LoadSet

class home:
    def __init__ (self):
        self.out = outputs.piControl(20, 21)
        self.cycle_data = Cycles()
        self.reset_data = resetScreen(self.cycle_data)
        self.time_data = timeSet(self.cycle_data)
        self.cycle_side = True
        self.previous_cycle_side = False
        self.window = tk.Tk()
        self.window.title("Cycles Home Screen")
        self.window.geometry("400x300")
        self.job = "0"
        self.load = LoadSet.SettingLoad()
        self.fontsize = 18
        self.is_fullscreen = True
        if platform.system() != "Darwin":
            self.window.config(cursor="none") #Hides the mouse when not on a mac
        self.cycle_limit_number = tk.Label(self.window, text=self.cycle_data.max, font=(None, self.fontsize))
        self.cycle_limit_number.grid(row=2, column=1)
        self.cycle_count_number = tk.Label(self.window, text=self.cycle_data.count, font=(None, self.fontsize))
        self.cycle_count_number.grid(row=1, column=1, pady=3)
                # Buttons on the Home Screen
        start_Button = tk.Button(self.window, text="START", bg="Green", command=self.__start, font=(None, self.fontsize))
        start_Button.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        start_Button.config(height=7, width=21)

        stop_Button = tk.Button(self.window, text="STOP", bg="Red", command=self.__stop, font=(None, self.fontsize))
        stop_Button.grid(row=0, column=2, padx=10, pady=10, columnspan=2)
        stop_Button.config(height=7, width=21)

        reset_Button = tk.Button(self.window, text="Cycle Settings", command=self.__reset_settings, font=(None, self.fontsize))
        reset_Button.grid(row=3, column=1, columnspan=2, ipadx=10, ipady=5)

        time_Button = tk.Button(self.window, text="Time Settings", command=self.__time_action, font=(None, self.fontsize))
        time_Button.grid(row=4, column=1, columnspan=2, ipadx=10, ipady=5)

        set_load_button = tk.Button(self.window, text="To Set Load", command=self.__load, font=(None, self.fontsize))
        set_load_button.grid(row=2, column=4)

        end_fullscreen_button = tk.Button(self.window, text="ESC", command=self.__close_fullscreen, font=(None, self.fontsize))
        end_fullscreen_button.grid(row=5, column=5)

        # Text on Home Screen
        cycle_count_text = tk.Label(self.window, text="Current Cycle Count", font=(None, self.fontsize))
        cycle_count_text.grid(row=1, column=0)

        cycle_limit_text = tk.Label(self.window, text="Cycle Limit", font=(None, self.fontsize))
        cycle_limit_text.grid(row=2, column=0, pady=3)

        # Full Screen
        self.window.bind("<Escape>", self.__close_fullscreen)
        self.window.bind("<F11>", self.__toggle_fullscreen)
        self.window.attributes("-fullscreen", self.is_fullscreen)
        
        self.__cycle_inputs()
        self.window.mainloop()

# Commands that go with Buttons
    def __start(self):
        if self.cycle_data.count >= self.cycle_data.max:
            self.__stop()
            return
        self.out.off()
        self.out.rightOn()
        self.window.after(self.cycle_data.extend_time)
        self.out.off()
        self.out.leftOn()
        self.cycle_data.increment()
        self.__update_count()
        self.job = self.window.after(self.cycle_data.retract_time, self.__start)
        

    def __cycleStart(self):
        if self.cycle_data.count >= self.cycle_data.max:
            self.__stop()
            return
        if self.cycle_side:
            if not self.previous_cycle_side:
                self.previous_cycle_side = self.cycle_side
                self.cycle_data.increment()
                self.__update_count()
                self.out.off()
                self.out.rightOn()
        elif not self.cycle_side:
            if self.previous_cycle_side:
                self.out.off()
                self.out.leftOn()
                self.previous_cycle_side = self.cycle_side
        
        self.job = self.window.after(1, self.__cycleStart)

    def __update_count(self):
        self.cycle_count_number.config(text=self.cycle_data.count)

    def __stop(self):
        self.out.off()
        self.window.after_cancel(self.job)


    def __reset_settings(self):
        self.__stop()
        self.reset_data.show(self.cycle_data)
        self.cycle_limit_number.config(text=self.cycle_data.max)
        self.cycle_count_number.config(text=self.cycle_data.count)

    def __time_action(self):
        self.__stop()
        self.time_data.show()
        # Not currently shown on main Screen

    def __close_fullscreen(self, Event=None):
        self.is_fullscreen = False
        self.window.attributes("-fullscreen", self.is_fullscreen)

    def __toggle_fullscreen(self, Event):
        if self.is_fullscreen:
            self.is_fullscreen = False
        else:
            self.is_fullscreen = True
        self.window.attributes("-fullscreen", self.is_fullscreen)

    def __load(self):
        self.__stop()
        self.load.show()

    def __cycle_inputs(self):
        if self.out.rightIn():
            self.cycle_side = True
        if self.out.leftIn():
            self.cycle_side = False
        self.window.after(1, self.__cycle_inputs)
        
    


test = home()

