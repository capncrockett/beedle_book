# shot_tracker.py
from graphics import *
from projectile import Projectile


class ShotTracker:

    def __init__(self, win, angle, velocity, height):
        """`win` is the GraphWin to display the shot. `angle`,
        `velocity`, and `height` are initial projectile parameters.
        """

        self.proj = Projectile(angle, velocity, height)
        self.marker = Circle(Point(0, height), 3)
        self.marker.setFill("red")
        self.marker.setOutline("red")
        self.marker.draw(win)

    def update(self, dt):
        """Move the shot `dt` seconds farther along its flight"""

        # update the projectile
        self.proj.update(dt)

        # move the circle to the new projectile location
        center = self.marker.getCenter()
        dx = self.proj.get_x() - center.getX()
        dy = self.proj.get_y() - center.getY()
        self.marker.move(dx, dy)

    def get_x(self):
        """return the current x coordinate of the shot's center"""
        return self.proj.get_x()

    def get_y(self):
        """return the current y coordinate of the shot's center"""
        return self.proj.get_y()

    def undraw(self):
        """undraw the shot"""
        self.marker.undraw()
