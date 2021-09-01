# triangle_info.py
# This program displays information about a triangle drawn by the user.

from graphics import *
import math


def main():
    win = GraphWin("Rectangle Info", 600, 600)
    win.setCoords(-14, -14, 14, 14)
    win.setBackground("white")

    # draw grid lines
    x_lines = -10
    for i in range(21):
        vert_lines = Line(Point(x_lines, -10), Point(x_lines, 10))
        vert_lines.setFill(color_rgb(192, 192, 192))
        vert_lines.draw(win)
        x_lines = x_lines + 1

    y_lines = -10
    for i in range(21):
        horiz_lines = Line(Point(-10, y_lines), Point(10, y_lines))
        horiz_lines.setFill(color_rgb(192, 192, 192))
        horiz_lines.draw(win)
        y_lines = y_lines + 1

    x_axis = Line(Point(0, -10), Point(0, 10))
    x_axis.setWidth(2)
    x_axis.draw(win)
    y_axis = Line(Point(-10, 0), Point(10, 0))
    y_axis.setWidth(2)
    y_axis.draw(win)

    # input: three mouse clicks for the opposite corners of a triangle.
    p1 = win.getMouse()
    p1.draw(win)
    print(p1)
    p2 = win.getMouse()
    p2.draw(win)
    print(p2)
    p3 = win.getMouse()
    p3.draw(win)
    print(p3)

    # extract coordinates of points
    x1 = round(p1.getX(), 2)
    x2 = round(p2.getX(), 2)
    x3 = round(p3.getX(), 2)
    y1 = round(p1.getY(), 2)
    y2 = round(p2.getY(), 2)
    y3 = round(p3.getY(), 2)

    # output: draw the triangle
    triangle = Polygon(p1, p2, p3)
    triangle.draw(win)

    # output: print the perimeter and area of the triangle.
    dx_a = x2 - x1
    dy_a = y2 - y1
    length_a = math.sqrt(dx_a ** 2 + dy_a ** 2)
    print("A = ", length_a)

    dx_b = x3 - x2
    dy_b = y3 - y2
    length_b = math.sqrt(dx_b ** 2 + dy_b ** 2)
    print("B = ", length_b)

    dx_c = x1 - x3
    dy_c = y1 - y3
    length_c = math.sqrt(dx_c ** 2 + dy_c ** 2)
    print("C = ", length_c)

    perimeter = length_a + length_b + length_c
    print("Perimeter = ", perimeter)

    s = (length_a + length_b + length_c) / 2
    area = math.sqrt(s * (s - length_a) * (s - length_b) *
                     (s - length_c))
    print("Area = ", area)

    win.getMouse()
    win.close()


main()
