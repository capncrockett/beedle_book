# random_walk_angle.py
import math
from math import sin, cos
from random import random
from graphics import *


# These two "constants" are defined here so they can be used in multiple
#    functions to draw the done button and check to see if it is clicked in.


def draw_win():
    win = GraphWin("Random Walk", 600, 600)
    win.setCoords(-100, -100, 100, 100)

    return win


def walking(x, y):
    print(x, y)     # FOR TESTING
    angle = random() * 2 * math.pi
    print(angle)       # FOR TESTING
    x = x + cos(angle)
    y = y + sin(angle)

    print(x, y)        # FOR TESTING
    return x, y


def walk_around(n):
    win = draw_win()
    # n = 2500

    p1_x = 0
    p1_y = 0

    for i in range(n):
        p2_x, p2_y = walking(p1_x, p1_y)
        # print((p2_x, p2_y))       # FOR TESTING

        walk_line = Line(Point(p1_x, p1_y), Point(p2_x, p2_y))
        walk_line.draw(win)

        p1_x = p2_x
        p1_y = p2_y

    # click to quit
    win.getMouse()
    win.close()


def main():
    print("This program draws you walking around with random angles. \n"
          "Click for additional walks.")
    walks = int(input("How many walks would you like to take? "))
    steps = int(input("How many steps do you plan to take? "))

    for i in range(walks):
        walk_around(steps)


if __name__ == '__main__':
    main()
