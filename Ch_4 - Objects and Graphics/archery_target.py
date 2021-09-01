from graphics import *


def main():
    win = GraphWin("Archery Target", 400, 400)
    win.setCoords(0.0, 0.0, 100, 100)

    # draw circles with radius' decreasing by 1/5
    x = 50
    colors = ["white", "black", "blue", "red", "yellow"]
    for i in colors:
        c1 = Circle(Point(50, 50), x)
        x = x - 10
        c1.setFill(i)
        c1.draw(win)

    # click to quit
    win.getMouse()
    win.close()


main()
