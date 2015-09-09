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

    bearscords = []
    bears = []
    moves = []

    for i in range(10):
        bearX = 10*random()
        bearY = 10*random()
        bearscords.append([bearX, bearY])
        moves.append([0.5 + randrange(1, 100, 1) /10, 1 + random()])
        #print(bears)
    print(moves)

    for j in range(len(bearscords)):
        x, y = bearscords[j]
        # print(x, y)
        # a, b = bears[j]
        # print(10*a, 10*b)
        # global bear
        bears.append(canvas.create_oval(50*x, 50*y, (50*x)+5, (50*y)+5))
        #bears.append(canvas.create_oval(100*x, 100*y, (100*x)+5, (100*y)+5))

    try:
        while 1:

            for i in range(len(bears)):
                a = canvas.coords(bears[i])
                print(a)

                a[0] += moves[i][0]
                a[1] += moves[i][1]
                a[2] += moves[i][0]
                a[3] += moves[i][1]

                canvas.coords(bears[i], a[0], a[2], a[1], a[3])

                if(a[1]>310):
                     canvas.coords(bears[i], randrange(40), -10, randrange(40), -10)
                window.update_idletasks() # redraw
                window.update() # process events

    except:
        pass


    window.mainloop()

main_window()