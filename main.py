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
        self.button = Button (window, text="CLICK ME TO START", command=self.plot,height = 100, width = 100)


        self.button.pack()

    def plot (self):
        self.button1 = Button(window, text="RUN TURTLE", command=self.runTurtle,height = 3, width = 20)
        self.box = Entry(window)

        self.box.pack()

        self.button1.pack()
        self.button.destroy()


        # obstacles are set here
        x=np.array ([ 2, 3, 4, 5, 6, 7, 8, 9, 10])
        y= np.array ([ 2, 3, 4, 5, 6, 7, 8, 9, 11])


        fig = Figure(figsize=(20,20))
        a = fig.add_subplot(111)
        a.scatter(y,x,color='red')

        a.set_title ("OBSTACLE PLOT", fontsize=20)
        a.set_ylabel("Y", fontsize=14)
        a.set_xlabel("X", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()

    def runTurtle(self):

        let =[]
        input1 = self.box.get()
        turtle.setup(width = 1400, height = 800)
        my_start = (1, 1)
        turtle.setx(my_start[0])
        turtle.sety(my_start[1])




        i=0

        for letter in input1:
            let.append(letter)
            i+=1

        for x in let:

            if x=='f'or x=='F':
               turtle.pendown()
               turtle.forward(1)
               turtle.penup()


            elif x=='l' or x=='L':
                turtle.pendown()
                turtle.left(90)
                turtle.penup()

            elif x=='r' or x=='R':
                turtle.pendown()
                turtle.right(90)
                turtle.penup()

            else:
                print "Command could not be executed because ",x," is an invalid command"


        if(turtle.heading()==0.0):
            print "Turtle is headed in EAST direction"
        elif(turtle.heading()==90.0):
            print "Turtle is headed in NORTH direction"
        elif (turtle.heading() == 180.0):
            print "Turtle is headed in WEST direction"
        else:
            print "Turtle is headed in SOUTH direction"

        print "The final position of the turtle is ",turtle.position(), " on XY plane"

window= Tk()
start= mclass (window)
window.mainloop()