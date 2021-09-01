# rectangle_info.py
# This program displays information about a rectangle drawn by the user.

from graphics import *


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

    # input: two mouse clicks for the opposite corners of a rectangle.
    p1 = win.getMouse()
    p1.draw(win)
    print(p1)
    p2 = win.getMouse()
    p2.draw(win)
    print(p2)

    # extract coordinates of points
    x1 = round(p1.getX(), 2)
    x2 = round(p2.getX(), 2)
    y1 = round(p1.getY(), 2)
    y2 = round(p2.getY(), 2)

    # output: draw the rectangle
    rectangle = Rectangle(Point(x1, y1), Point(x2, y2))
    rectangle.draw(win)

    # length and width
    length = round((x2 - x1), 2)
    width = round((y2 - y1), 2)
    print("Length = ", length)
    print("Width = ", width)

    # output: print the perimeter and area of the rectangle.
    perimeter = round((2 * length + width), 2)
    area = round((length * width), 2)
    print("Perimeter = ", perimeter)
    print("Area = ", area)

    win.getMouse()
    win.close()


main()
