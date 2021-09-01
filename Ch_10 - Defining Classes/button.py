# button.py
#   Defines a button object.
from graphics import *


class Button:
    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit')"""
        w, h = width / 2.0, height / 2.0
        x, y = center.getX(), center.getY()
        self.x_max, self.x_min = x + w, x - w
        self.y_max, self.y_min = y + h, y - h
        p1 = Point(self.x_min, self.y_min)
        p2 = Point(self.x_max, self.y_max)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgrey')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        """Returns true if button is active and p is inside"""
        return (self.active and
                self.x_min <= p.getX() <= self.x_max and
                self.y_min <= p.getY() <= self.y_max)

    def get_label(self):
        """Returns the label string of this button"""
        return self.label.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False
