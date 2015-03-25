#############################################################################################
##Basic Clock application with a GUI, By Richard Jansen, HAN University of Applied Sciences##
##4-12-2014##################################################################################
#############################################################################################

######################
##Local Time Import###
######################

import tkinter as tk
import time

##########################
##Application Variables###
##########################

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="baah")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()
        
    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

app=App()
