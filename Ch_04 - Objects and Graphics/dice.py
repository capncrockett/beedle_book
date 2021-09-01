from graphics import *


def main():
    win = GraphWin("dice", 400, 400)
    win.setCoords(0.0, 0.0, 130, 130)

    # draw dice
    dice_1 = Rectangle(Point(5, 40), Point(25, 60))
    dice_1.setFill("white")
    dice_1.draw(win)
    dot_1 = Point(15, 50)
    dot_1.draw(win)

    dice_2 = Rectangle(Point(30, 40), Point(50, 60))
    dice_2.setFill("white")
    dice_2.draw(win)
    dot_2 = Point(35, 45)
    dot_2.draw(win)
    dot_2 = Point(15, 50)
    dot_2.draw(win)

    dice_3 = Rectangle(Point(55, 40), Point(75, 60))
    dice_3.setFill("white")
    dice_3.draw(win)
    dot_1 = Circle

    dice_4 = Rectangle(Point(80, 40), Point(100, 60))
    dice_4.setFill("white")
    dice_4.draw(win)
    dot_1 = Circle

    dice_5 = Rectangle(Point(105, 40), Point(125, 60))
    dice_5.setFill("white")
    dice_5.draw(win)
    dot_1 = Circle

    win.getMouse()
    win.close()


main()
