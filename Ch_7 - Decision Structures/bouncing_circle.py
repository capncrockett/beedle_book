# bouncing_circle.py
#   A program that animates a circle bouncing around a window.
from graphics import *


def window_draw():
    win = GraphWin("Bouncing Circle", 400, 400)
    win.setCoords(-10, -10, 10, 10)
    win.setBackground("black")

    return win


def main():
    win = window_draw()

    radius = 1
    circle = Circle(Point(0, 0), radius)
    circle.setFill("green")
    circle.setOutline("gold")
    circle.draw(win)

    dx = 1
    dy = 1

    for i in range(10000):
        circle.move(dx, dy)
        center = circle.getCenter()
        print(center)
        center_x, center_y = center.getX(), center.getY()

        if 10 - abs(center_x) == radius:
            dx = -dx
        if 10 - abs(center_y) == radius:
            dy = -dy
        update(30)

    # click to quit
    win.getMouse()
    win.close()


main()
