# line_segment_info
# This program allows the user to draw a line segment and then displays
# some graphical and textual information about the line segment.

from graphics import *
import math


def main():
    win = GraphWin("Line Segment Info", 600, 600)
    win.setCoords(-14, -14, 14, 14)
    win.setBackground("white")

    # draw grid lines
    x_axis = -10
    for y_lines in range(21):
        vert_lines = Line(Point(x_axis, -10), Point(x_axis, 10))
        vert_lines.setFill(color_rgb(192, 192, 192))
        vert_lines.draw(win)
        x_axis = x_axis + 1

    y_axis = -10
    for x_lines in range(21):
        horiz_lines = Line(Point(-10, y_axis), Point(10, y_axis))
        horiz_lines.setFill(color_rgb(192, 192, 192))
        horiz_lines.draw(win)
        y_axis = y_axis + 1

    # input: two mouse clicks for the end points of a line segment.
    p1 = win.getMouse()
    p1.draw(win)
    print(p1)
    p2 = win.getMouse()
    p2.draw(win)
    print(p2)

    # output: draw the line.
    line = Line(p1, p2)
    line.draw(win)

    # draw the midpoint of the segment in cyan.
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()

    midpoint = Point(((x1 + x2) / 2), ((y1 + y2) / 2))
    midpoint.setFill("cyan")
    midpoint.draw(win)
    midpoint_x = round(midpoint.getX(), 2)
    midpoint_y = round(midpoint.getY(), 2)
    print("Midpoint is ~", midpoint_x, midpoint_y)

    # print the length and the slope of the line.
    dx = x2 - x1
    dy = y2 - y1
    length = round(math.sqrt(dx ** 2 + dy ** 2), 2)
    print("Length = ", length)

    try:
        slope = round(dy / dx, 2)
        print("Slope = ", slope)
        Text(Point(-6.5, 13), slope).draw(win)
        Text(Point(-9, 13), "Slope = ").draw(win)
    except ZeroDivisionError as zero_division:
        if str(zero_division) == "float division by zero":
            print("cannot divide 0 by 0 to find slope")
            Text(Point(-8, 13), "Slope = Error").draw(win)
            Text(Point(0, 0), "cannot divide 0 by 0 to find slope").draw(win)

    # draw relevant info.
    Text(Point(-9, 11), "Length = ").draw(win)
    Text(Point(-6.5, 11), length).draw(win)
    Text(Point(0, 13), "Midpoint X = ").draw(win)
    Text(Point(0, 11), "Midpoint Y = ").draw(win)
    Text(Point(3, 13), midpoint_x).draw(win)
    Text(Point(3, 11), midpoint_y).draw(win)

    win.getMouse()
    win.close()


for i in range(10):
    main()
