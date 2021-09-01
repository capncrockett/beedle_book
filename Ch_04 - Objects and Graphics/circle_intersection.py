# circle_intersection.py

from graphics import *
import math


def main():
    win = GraphWin("Circle Intersection", 600, 600)
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

    # get input radius and y-intercept
    Text(Point(-9, 13), "Circle Radius:").draw(win)
    Text(Point(-9, 11), "     y-intercept:").draw(win)
    y_int = Entry(Point(-4, 11), 3)
    y_int.setText("0")
    y_int.draw(win)
    radius = Entry(Point(-4, 13), 3)
    radius.setText("0")
    radius.draw(win)

    # wait for a click
    button = Text(Point(6, 12), "Click to calculate")
    button.draw(win)
    Rectangle(Point(1, 11), Point(11, 13)).draw(win)
    win.getMouse()

    # radius = 3    FOR TESTING
    # y_int = 2     FOR TESTING
    radius = float(radius.getText())
    y_int = float(y_int.getText())

    # output circle centered at 0,0.
    circle = Circle(Point(0, 0), radius)
    circle.setOutline("blue")
    circle.draw(win)

    # draw horizontal line at y-int
    y_int_line = Line(Point(-10, y_int),
                      Point(10, y_int))
    y_int_line.setFill("green")
    y_int_line.setWidth(2)
    y_int_line.draw(win)

    try:
        # draw the two points of interception in red
        intercept_x_1 = abs(math.sqrt(radius ** 2 - y_int ** 2))
        intercept_x_2 = abs(math.sqrt(radius ** 2 - y_int ** 2)) * -1

        intercept_point_1 = Point(intercept_x_1, y_int)
        intercept_point_1.setFill("red")
        intercept_point_1.draw(win)
        intercept_point_2 = Point(intercept_x_2, y_int)
        intercept_point_2.setFill("red")
        intercept_point_2.draw(win)

        # print x values of intercept
        Text(Point(intercept_x_1 + 1, y_int + 1),
             round(intercept_x_1, 2)).draw(win)
        Text(Point(intercept_x_2 - 1, y_int + 1),
             round(intercept_x_2, 2)).draw(win)

    except ValueError as y_int_out_of_range:
        if str(y_int_out_of_range) == "math domain error":
            print("Y-intercept is out of range")
            Text(Point(0, y_int + 1), "Y-intercept out of range").draw(win)

    # wait for click and then quit
    button.setText("Quit")
    win.getMouse()
    win.close()


main()
