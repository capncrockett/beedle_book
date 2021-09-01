# triangle_3.py
# This program displays information about a triangle drawn by the user.
from graphics import *
import math


def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def square(x):
    return x ** 2


def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX())
                     + square(p2.getY() - p1.getY()))
    return dist


def main():
    win = GraphWin("Draw a Triangle", 640, 640)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    win.setBackground("gray")
    message = Text(Point(5, 1), "Click three points")
    message.draw(win)

    # Get and draw three vertices of triangle.
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use Polygon object to draw the triangle.
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Calculate the sides.
    side_1 = distance(p1, p2)
    side_2 = distance(p2, p3)
    side_3 = distance(p3, p1)

    perimeter = round(side_1 + side_2 + side_3, 2)
    area = round(triangle_area(side_1, side_2, side_3), 2)

    message.setText(f"Perimeter = {perimeter}\n "
                    f"Area = {area}\n"
                    "Click to exit.")

    # Wait for another mouse click to exit.
    win.getMouse()
    win.close()


main()
