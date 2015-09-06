__author__ = 'JayantArora'


from tkinter import *
from random import *


def main_window():
    window = Tk()
    window.geometry("1000x1000")
    window.config(background="light green")
    #window.
    # water = Frame(window, height=100, width=500)
    # water.config(background="light blue", highlightbackground="black")
    # water.pack(padx=50, pady=50)

    canvas = Canvas(window, height="500p", width="500p", bg="white")

    canvas.pack()

    bears = []
    moves = []

    for i in range(100):
        bearX = 10*random()
        bearY = 10*random()
        bears.append([bearX, bearY])
        moves.append([0.04 + random()/10,0.7 + random()])
        #print(bears)


    for j in range(len(bears)):
        x, y = bears[j]
        print(x, y)
        # a, b = bears[j]
        # print(10*a, 10*b)
        global bear
        bear = canvas.create_oval(50*x, 50*y, (50*x)+10, (50*y)+10)
        bear2 = canvas.create_oval(100*x, 100*y, (100*x)+10, (100*y)+10)

    for i in range(len(bears)):
        z = canvas.coords(bears[i])
        print(z)

        a[0] += moves[i][0]
        a[1] += moves[i][1]
        b[0] += moves[i][0]
        b[1] += moves[i][1]
        canvas.coords(bears[i],a[0],a[1])

    if(p[1]>310):
        window.coords(bear[i],randrange(400),-10)
        window.update_idletasks() # redraw
        window.update() # process events


    window.mainloop()

main_window()