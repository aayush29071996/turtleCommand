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

    def plot (self):
        self.button1 = Button(window, text="RUN TURTLE", command=self.runTurtle,height = 3, width = 20)
        self.box = Entry(window)

        self.box.pack()

        self.button1.pack()
        self.button.destroy()


        # obstacles are set here
        x=np.array ([ 2, 3, 4, 5, 6, 7, 8, 9, 10])
        v= np.array ([ 2, 3, 4, 5, 6, 7, 8, 9, 11])
        p= np.array ([0.23697,     2.31653,     6.22094,     6.68631,     6.73641 ,    8.6368,
            8.32125,     8.31756 ,    10.20247  ,   10.41444   ,  10.11718  ,   10.12453])

        fig = Figure(figsize=(20,20))
        a = fig.add_subplot(111)
        a.scatter(v,x,color='red')
        a.plot(p, range(2 +max(x)),color='white')

        a.set_title ("TURTLE COMMAND", fontsize=20)
        a.set_ylabel("Y", fontsize=14)
        a.set_xlabel("X", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()



window= Tk()
start= mclass (window)
window.mainloop()