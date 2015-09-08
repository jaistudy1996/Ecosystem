__author__ = 'JayantArora'

from random import random, randint, choice
from time import time, sleep


def main():

    bear = []
    fish = []

    gender = ['male', 'female']

    for i in range(100):
        bear.append((choice(gender), 10*random()))
        fish.append((choice(gender), 10*random()))

    print(bear)
    print(fish)


    while True:
        index = randint(1, len(bear))
        will_change = randint(1, 4)

        if will_change == 1:        # if 1 then the bear stays where it is
            bear[index] = bear[index]
            sleep(3)
            print("slept 3 secs")

        if will_change == 2:
            # bear[index] = bear[index+1]
            if bear[index][0] != bear[index+1][0]:
                bear.append((choice(gender), 10*random()))
                print("Bear born")
                sleep(3)
                print("slept 3 secs")

            if bear[index][0] == bear[index][0]:
                if bear[index][1] > bear[index+1][1]:
                    del(bear[index+1])
                    print("2, bear died")
                    sleep(3)
                    print("slept 3 secs")
                if bear[index][1] < bear[index+1][1]:
                    del(bear[index])
                    print("2, bear died")
                    sleep(3)
                    print("slept 3 secs")

        if will_change == 3:
            if bear[index][0] != bear[index-1][0]:
                bear.append((choice(gender), 10*random()))
                print("Bear born")
                sleep(3)
                print("slept 3 secs")

            if bear[index][0] == bear[index][0]:
                if bear[index][1] > bear[index-1][1]:
                    del(bear[index-1])
                    print("3, bear died")
                    sleep(3)
                    print("slept 3 secs")

                if bear[index][1] < bear[index-1][1]:
                    del(bear[index])
                    print("3, bear died")
                    sleep(3)
                    print("slept 3 secs")

main()