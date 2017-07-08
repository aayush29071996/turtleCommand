import turtle
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Tkinter import *


class mclass:

    def __init__(self,  window):
        self.window = window
        self.button = Button (window, text="CLICK ME", command=self.plot,height = 50, width = 50)


        self.button.pack()


window= Tk()
start= mclass (window)
window.mainloop()