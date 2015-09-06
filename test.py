__author__ = 'akshaysingh'
from tkinter import *
from random import randint

#Return random color #RRGGBB
def getRandomColor():
    color = '#'
    for j in range(6):
        color+= toHexChar(randint(0, 15))
    return color

#Convert an integer to a single hex digit in a character
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue+ord('0'))
    else:
        return chr(hexValue - 10 + ord('A'))

#Define ball class
class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 2
        self.dy = 2
        self.radius = 9
        self.color = getRandomColor()


class BounceBalls():
    def __init__(self):
        self.ballList = []
        window = Tk()
        window.title("Bouncing Balls")
        self.width = 350
        self.height = 150
        self.canvas = Canvas(window, bg = "white", width = self.width, height = self.height)
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()

        buttonStop = Button(frame, text = "Stop", command = self.stop)
        buttonStop.pack(side = LEFT)

        buttonFaster = Button(frame, text = "Faster", command = self.increaseBallSpeed)
        buttonFaster.pack(side = LEFT)

        buttonSlower = Button(frame, text = "Slower", command = self.decreaseBallSpeed)
        buttonSlower.pack(side = LEFT)

        buttonResume = Button(frame, text = "Resume", command = self.resume)
        buttonResume.pack(side = LEFT)

        buttonAdd = Button(frame, text = "Add", command = self.add)
        buttonAdd.pack(side = LEFT)

        buttonRemove = Button(frame, text = "Remove", command = self.remove)
        buttonRemove.pack(side = LEFT)


        self.sleepTime = 50
        self.isStopped = False
        self.animate()
        window.mainloop()


    def stop(self): #Stop animation
        self.isStopped = True

    def resume(self): #Resume animation
        self.isStopped = False
        self.animate()

    def add(self): #Add a new ball
        self.ballList.append(Ball())

    def remove(self): #Remove the last ball
        self.ballList.pop()

    def animate(self): #Animate ball movements
        while not self.isStopped:
            self.canvas.after(self.sleepTime)
            self.canvas.update()
            self.canvas.delete("ball")
            for ball in self.ballList:
                self.redisplayBall(ball)


    def increaseBallSpeed(self):
        if self.sleepTime <= 10:
            self.sleepTime = 10
        else:
            self.sleepTime-=10

    def decreaseBallSpeed(self):
        self.sleepTime+=10


    def redisplayBall(self, ball):
        if ball.x > self.width or ball.x < 0:
            ball.dx = -ball.dx
        if ball.y > self.height or ball.y < 0:
            ball.dy = -ball.dy


        ball.x += ball.dx
        ball.y += ball.dy
        self.canvas.create_oval(ball.x - ball.radius, ball.y - ball.radius,
                                ball.x + ball.radius, ball.y + ball.radius,
                                fill = ball.color, tags = "ball")


BounceBalls()