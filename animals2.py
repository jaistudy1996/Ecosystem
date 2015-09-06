__author__ = 'JayantArora'


from graphics import *
from random import *
from bounce import *



def move(bear):
    center = bear.getCenter()
    centerX = center.getX()
    centerY = center.getY()
    dx = 0.29
    dy = 0.165

    if (centerX + dx) >= 10 or (centerX + dx) <= 10:
        dx = - dx

    if (centerY + dy) >= 10 or (centerY + dy) <= 10:
        dy = - dy

    bear.move(dx, dy)



def window():
    win = GraphWin("Ecosystem", 500, 500)
    win.setCoords(-2, -2, 10, 10)

    bears = []
    for i in range(100):
        bears.append(Circle(Point(10*random()-1, 10*random()-1), 0.15))

    dx = 0.8
    dy = 0.665
    # try:
    for i in range(len(bears)):
        bears[i].draw(win)


    for bear in bears:
        center = bear.getCenter()
        centerX = center.getX()
        centerY = center.getY()

        if (centerX + dx) >= 10 or (centerX + dx) <= 0:
            dx = - dx

        if (centerY + dy) >= 10 or (centerY + dy) <= 0:
            dy = - dy
        print(centerX+dx, centerY+dy)
        a = bool
        print(a)
        bear.move(dx, dy)


window()
