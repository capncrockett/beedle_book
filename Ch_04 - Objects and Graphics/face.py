from graphics import *


def main():
    win = GraphWin("Exercises", 400, 400)
    win.setCoords(0.0, 0.0, 10, 10)

    # draw main face
    base_face = Oval(Point(10, 1), Point(0, 9))
    base_face.setFill("orange")
    base_face.draw(win)

    # draw two eyes
    eye_1 = Polygon(Point(8, 6), Point(7, 5), Point(6, 6))
    eye_2 = Polygon(Point(4, 6), Point(3, 5), Point(2, 6))
    eye_1.setFill("black")
    eye_2.setFill("black")
    eye_1.draw(win)
    eye_2.draw(win)

    # draw nose
    nose = Rectangle(Point(4.9, 4.5), Point(5.1, 4.9))
    nose.setFill("black")
    nose.draw(win)

    # draw mouth
    upper_teeth = Text(Point(5, 3.5), "VVVVVVVVV")
    upper_teeth.setSize(24)
    upper_teeth.setStyle("bold")
    upper_teeth.draw(win)
    lower_teeth = Text(Point(5, 2.5), "^^^^^^^")
    lower_teeth.setSize(32)
    lower_teeth.setStyle("bold")
    lower_teeth.draw(win)

    # click to quit
    win.getMouse()
    win.close()


main()
