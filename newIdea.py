__author__ = 'JayantArora'

from random import random, randint, choice
from time import sleep


def main():

    river = []

    gender = ['male', 'female']
    animal = ['bear', 'fish']

    for i in range(100):
        river.append((choice(animal), choice(gender), 10*random()))
        # 10*random() is the strength of the animal

    print(river)

    while True:
        index = randint(1, len(river))
        will_change = randint(1, 4)

        if will_change == 1:        # if 1 then the bear stays where it is
            river[index] = river[index]
            print("stay at same place")
            sleep(3)
            print("slept 3 secs")

        if will_change == 2:
            # bear[index] = bear[index+1]
            if river[index][1] != river[index+1][1] and river[index][0] == river[index+1][0]:
                river.append((choice(gender), 10*random()))
                print("Bear born")
                sleep(3)
                print("slept 3 secs")

            if river[index][1] == river[index+1][1] or river[index][0] != river[index+1][0]:
                if river[index][2] > river[index+1][2]:
                    del(river[index+1])
                    print("2, bear died")
                    sleep(3)
                    print("slept 3 secs")
                if river[index][1] < river[index+1][1]:
                    del(river[index])
                    print("2, bear died")
                    sleep(3)
                    print("slept 3 secs")

        if will_change == 3:
            if river[index][0] != river[index-1][0]:
                river.append((choice(gender), 10*random()))
                print("Bear born")
                sleep(3)
                print("slept 3 secs")

            if river[index][0] == river[index][0]:
                if river[index][1] > river[index-1][1]:
                    del(river[index-1])
                    print("3, bear died")
                    sleep(3)
                    print("slept 3 secs")

                if river[index][1] < river[index-1][1]:
                    del(river[index])
                    print("3, bear died")
                    sleep(3)
                    print("slept 3 secs")

main()