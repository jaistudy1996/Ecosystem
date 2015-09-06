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
    fish = []

    for i in range(100):
        bearX = 10*random()
        bearY = 10*random()
        bears.append((bearX, bearY))
        #print(bears)


    for j in range(len(bears)):
        x, y = bears[j]
        print(x, y)
        # a, b = bears[j]
        # print(10*a, 10*b)
        global bear
        bear = canvas.create_oval(50*x, 50*y, (50*x)+10, (50*y)+10)
        bear2 = canvas.create_oval(100*x, 100*y, (100*x)+10, (100*y)+10)

    #for k in range(10000):



    window.mainloop()

main_window()