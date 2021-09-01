# moving_circle.py
from graphics import *


def move_to(shape, new_point):
    center = shape.getCenter()
    dx = new_point.getX() - center.getX()
    dy = new_point.getY() - center.getY()
    shape.move(dx, dy)


def main():
    # Draw window.
    win = GraphWin("Circle Mover", 500, 500)
    win.setCoords(0, 0, 20, 20)
    message = Text(Point(10, 1), "")
    message.draw(win)

    # Draw initial circle.
    item = Circle(Point(10, 10), 2)
    item.setOutline("blue")
    item.draw(win)

    # move the circle
    message.setText("Click to move circle.")
    for i in range(10):
        init_point = win.getMouse()
        move_to(item, init_point)

    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()


main()
