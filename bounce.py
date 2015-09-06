#! /usr/bin/env python3

# Name: Jayant Arora
# Date: November 17, 2014
# This program make 30 balls bounce all over the screen without getting out of
# the screen

from random import *
from graphics import *

class Ball:
    def __init__(self, win):
        self.ball = Circle(Point(10 * random() - 1, 10 * random() - 1), 0.15)
        self.ball.draw(win)
        self.ball.setFill(self.gender())
        self.dx = 0.006
        self.dy = 0.030


    def gender(self):
        colors = {1: 'blue', 2: 'deep pink'}
        return colors[randrange(1, 3)]

    # in bool numbers evaluate to false


    def move(self):
        center = self.ball.getCenter()
        centerX = center.getX()
        centerY = center.getY()

        if (centerX + self.dx) >= 10 or (centerX + self.dx) <= 0:
            self.dx = - self.dx
        if (centerY + self.dy) >= 10 or (centerY + self.dy) <= 0:
            self.dy = - self.dy

        self.ball.move(self.dx, self.dy)

def main():
    win = GraphWin("Bounce", 500, 500)
    win.setCoords(0, 0, 10, 10)
    balls = []
    for i in range(150):
        balls.append(Ball(win))

    while True:
        for ball in balls:
            ball.move()
           


if __name__ == "__main__":
    main()
