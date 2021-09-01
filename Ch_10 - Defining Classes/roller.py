# roller.py
# Graphics program to roll a pair of dice. Uses custom widgets
# Button and DieView.

from random import randrange
from graphics import GraphWin, Point
from button import Button
from die_view import DieView


def main():
    # create the application window
    win = GraphWin("Dice Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    # Draw the interface widgets
    die_1 = DieView(win, Point(3, 7), 2)
    die_2 = DieView(win, Point(7, 7), 2)
    roll_button = Button(win, Point(5, 4.5), 6, 1, "Roll Dice")
    roll_button.activate()
    quit_button = Button(win, Point(5, 1), 2, 1, "Quit")

    # Event loop
    pt = win.getMouse()
    while not quit_button.clicked(pt):
        if roll_button.clicked(pt):
            for i in range(100):
                value_1 = randrange(1, 7)
                die_1.set_value(value_1)
                value_2 = randrange(1, 7)
                die_2.set_value(value_2)
            quit_button.activate()
        pt = win.getMouse()

    # close up shop
    win.close()


main()
