__author__ = 'JayantArora'

from random import random, randint, choice
from time import sleep, time


def main():
    start = time()
    river = []

    gender = ['male', 'female']
    animal = ['bear', 'fish']

    for i in range(100):
        river.append((choice(animal), choice(gender), 10*random()))
        # 10*random() is the strength of the animal

    try:
        while True:
            index = randint(0, len(river)-1)
            will_change = randint(1, 4)     # possible chances where the object will mova
                                            # if 1: stay where it is
                                            # if 2: move to the next location in the list
                                            # if 3: will move to the previous location

            try:
                if will_change == 1:        # if 1 then the bear stays where it is
                    river[index] = river[index]
                    print("stay at same place")
                    sleep(1)
                ########
            except IndexError:
                pass

            if will_change == 2:
                # bear[index] = bear[index+1]
                if river[index][1] != river[index+1][1] and river[index][0] == river[index+1][0]:
                    ani = choice(animal)
                    gen = choice(gender)
                    river.append((ani, gen, 10*random()))
                    print(ani+" "+gen+" born")
                    sleep(1)
            ########
                if river[index][1] == river[index+1][1] and river[index][0] == river[index+1][0]:
                    if river[index][2] > river[index+1][2]:
                        print("2, "+river[index+1][0]+" "+river[index][1]+" died")
                        del(river[index+1])
                        sleep(1)
                    if river[index][2] < river[index+1][2]:
                        print("2, "+river[index][0]+" "+river[index][1]+" died")
                        del(river[index])
                        sleep(1)
            ########
                if river[index][0] != river[index+1][0]:
                    if river[index][0] == 'bear':
                        print("Bear killed fish")
                        del(river[index+1])
                        sleep(1)
                    else:
                        print("bear killed fish")
                        del(river[index])
                        sleep(1)
            ########

            if will_change == 3:
                if river[index][1] != river[index-1][1] and river[index][0] == river[index-1][0]:
                    ani = choice(animal)
                    gen = choice(gender)
                    river.append((ani, gen, 10*random()))
                    print(ani+" "+gen+" born")
                    sleep(1)
            ########
                if river[index][1] == river[index-1][1] and river[index][0] == river[index-1][0]:
                    if river[index][2] > river[index-1][2]:
                        print("3, "+river[index-1][0]+" "+river[index-1][1]+" died")
                        del(river[index-1])
                        sleep(1)
                    if river[index][2] < river[index-1][2]:
                        print("3, "+river[index][0]+" "+river[index-1][1]+" died")
                        del(river[index])
                        sleep(1)
            ########
                if river[index][0] != river[index-1][0]:
                    if river[index][0] == 'bear':
                        print("Bear killed fish")
                        del(river[index-1])
                        sleep(1)
                    else:
                        print("Bear killed fish")
                        del(river[index])
                        sleep(1)

    except KeyboardInterrupt:
        print("\nEcosystem's life stopped!")
        stop = time()
        time_run = stop-start
        log = ["The program ran for:", time_run, "Stopped at index: ", index, will_change]
        print(log)


main()