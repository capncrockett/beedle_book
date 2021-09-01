from graphics import *


def main():
    win = GraphWin("Exercises", 400, 400)
    win.setCoords(0.0, 0.0, 200, 200)

    # a) creates a point
    p1 = Point(130, 130)
    p1.draw(win)

    # b)
    c = Circle(Point(30, 40), 25)
    c.setFill("blue")
    c.setOutline("red")
    c.draw(win)

    # c)
    r = Rectangle(Point(20, 20), Point(40, 40))
    r.setFill(color_rgb(0, 255, 150))
    r.setWidth(3)
    r.draw(win)

    # d)
    l = Line(Point(100, 100), Point(100, 200))
    l.setOutline("red4")
    l.setArrow("first")
    l.draw(win)

    # e)
    o = Oval(Point(50, 50), Point(60, 100))
    o.draw(win)

    # f)
    shape = Polygon(Point(50, 50), Point(100, 100),
                    Point(50, 100), Point(100,50))
    shape.setFill("orange")
    shape.draw(win)

    # g)
    t = Text(Point(100, 100), "Hello World!")
    t.setFace("courier")
    t.setSize(16)
    t.setStyle("italic")
    t.draw(win)

    # wait for click and then quit
    win.getMouse()
    win.close()


main()
