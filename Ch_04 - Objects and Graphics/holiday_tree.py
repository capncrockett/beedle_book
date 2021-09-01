from graphics import *


def main():
    win = GraphWin("Exercises", 400, 400)
    win.setCoords(0.0, 0.0, 10, 10)

    # draw tree
    tree = Polygon(Point(5, 8), Point(4, 3), Point(6, 3))
    tree.setFill("green")
    tree.draw(win)

    # draw trunk
    trunk = Rectangle(Point(4.8, 2.5), Point(5.2, 3))
    trunk.setFill("brown")
    trunk.draw(win)

    # draw snow man
    radius = 0.5
    y = 3
    for i in range(3):
        snow_man = Circle(Point(2, y), radius)
        y = y + (y * 0.2)
        radius = radius - 0.1
        snow_man.setFill("white")
        snow_man.setOutline("black")
        snow_man.draw(win)

    # click to quit
    win.getMouse()
    win.close()


main()
